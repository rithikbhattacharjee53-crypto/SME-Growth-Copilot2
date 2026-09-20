import pandas as pd
df = pd.read_csv("../data/processed/cleaned_business_data.csv")
summary = df.groupby("Channel", as_index=False).agg(
    Customers=("Customers_Acquired","sum"),
    Repeat_Customers=("Repeat_Customers","sum")
)
summary["Repeat_Customer_Rate"] = summary["Repeat_Customers"]/summary["Customers"]
print(summary.round(3).to_string(index=False))
summary.to_csv("../data/processed/customer_summary.csv", index=False)
