let
    Source = Csv.Document(
        Web.Contents("https://raw.githubusercontent.com/patelkautilya/bank-marketing-powerbi/main/data/campaigns.csv"),
        [Delimiter=",", Columns=14, Encoding=65001, QuoteStyle=QuoteStyle.Csv]
    ),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {
        {"RecordID", Int64.Type}, {"ContactChannel", type text},
        {"ContactMonth", type text}, {"ContactDayOfMonth", Int64.Type},
        {"CampaignContacts", Int64.Type}, {"ContactBand", type text},
        {"PreviousOutcome", type text}, {"PriorContacts", Int64.Type},
        {"HousingLoan", type text}, {"PersonalLoan", type text},
        {"Job", type text}, {"Education", type text},
        {"Subscribed", Int64.Type}, {"Records", Int64.Type}
    })
in
    Typed
