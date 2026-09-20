import pandas as pd
df = pd.read_csv("../data/processed/cleaned_business_data.csv")
monthly = df.groupby("Month", as_index=False)["Revenue"].sum()
monthly["Revenue_Growth"] = monthly["Revenue"].pct_change()
print(monthly.round(2).to_string(index=False))
monthly.to_csv("../data/processed/sales_summary.csv", index=False)
