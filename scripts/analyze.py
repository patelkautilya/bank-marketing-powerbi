"""Prepare and validate the UCI Bank Marketing portfolio case study."""
from pathlib import Path
from urllib.request import urlopen
import io, zipfile, hashlib, json, sqlite3
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'; REPORTS=ROOT/'reports'
DATA.mkdir(exist_ok=True); REPORTS.mkdir(exist_ok=True)
URL='https://archive.ics.uci.edu/static/public/222/bank+marketing.zip'
archive=DATA/'bank-marketing.zip'
if not archive.exists():archive.write_bytes(urlopen(URL,timeout=45).read())
with zipfile.ZipFile(archive) as outer, zipfile.ZipFile(io.BytesIO(outer.read('bank.zip'))) as inner:
    source=inner.read('bank-full.csv')
    (DATA/'bank-full.csv').write_bytes(source)
    (DATA/'bank-names.txt').write_bytes(inner.read('bank-names.txt'))
df=pd.read_csv(io.BytesIO(source),sep=';',keep_default_na=False)
assert df.shape==(45211,17)
assert not df.isna().any().any()
assert df['y'].isin(['yes','no']).all()
assert df['campaign'].ge(1).all()
assert df['pdays'].ge(-1).all()
assert (df['previous'].eq(0)&df['pdays'].eq(-1)).sum()>0
month_order=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
bands=pd.cut(df['campaign'],[0,1,2,3,5,10,float('inf')],labels=['01 1 contact','02 2 contacts','03 3 contacts','04 4–5 contacts','05 6–10 contacts','06 11+ contacts'])
out=pd.DataFrame({
 'RecordID':range(1,len(df)+1),
 'ContactChannel':df.contact.str.replace('cellular','Cellular').str.replace('telephone','Telephone').str.replace('unknown','Unknown'),
 'ContactMonth':[f'{x+1:02d} {month_order[x].title()}' for x in pd.Categorical(df.month,categories=month_order,ordered=True).codes],
 'ContactDayOfMonth':df.day,
 'CampaignContacts':df.campaign,
 'ContactBand':bands.astype(str),
 'PreviousOutcome':df.poutcome.str.title(),
 'PriorContacts':df.previous,
 'HousingLoan':df.housing.str.title(),
 'PersonalLoan':df.loan.str.title(),
 'Job':df.job.str.title(),
 'Education':df.education.str.title(),
 'Subscribed':df.y.eq('yes').astype(int),
 'Records':1,
})
assert out.isna().sum().sum()==0
assert out['Subscribed'].sum()==5289
out.to_csv(DATA/'campaigns.csv',index=False)
con=sqlite3.connect(':memory:')
out.to_sql('campaigns',con,index=False)
sql=con.execute('select count(*),sum(Subscribed),sum(CampaignContacts) from campaigns').fetchone()
assert sql==(len(df),int(out.Subscribed.sum()),int(out.CampaignContacts.sum()))
def segment(field):
    g=out.groupby(field,observed=True).agg(Records=('Records','sum'),Subscriptions=('Subscribed','sum'),CampaignContacts=('CampaignContacts','sum')).reset_index()
    g['SubscriptionRate']=g.Subscriptions/g.Records
    g.to_csv(REPORTS/(field.lower()+'-summary.csv'),index=False)
    return g
summaries={field:segment(field) for field in ['ContactChannel','ContactBand','PreviousOutcome','ContactMonth','HousingLoan','Job']}
metrics={'records':len(out),'subscriptions':int(out.Subscribed.sum()),'subscription_rate':float(out.Subscribed.mean()),'campaign_contacts':int(out.CampaignContacts.sum()),'source_sha256':hashlib.sha256(source).hexdigest(),'source_zip_sha256':hashlib.sha256(archive.read_bytes()).hexdigest()}
(REPORTS/'metrics.json').write_text(json.dumps(metrics,indent=2)+'\n',encoding='utf-8')
print(json.dumps(metrics,indent=2))
for key in ['ContactChannel','ContactBand','PreviousOutcome','ContactMonth','HousingLoan']:
    print('\n'+key+'\n'+summaries[key].to_string(index=False))
