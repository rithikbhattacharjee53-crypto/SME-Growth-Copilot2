import pandas as pd

df = pd.read_csv("../data/processed/cleaned_business_data.csv")

channel = df.groupby("Channel", as_index=False).agg(
    Marketing_Spend=("Marketing_Spend","sum"),
    Leads=("Leads","sum"),
    Customers=("Customers_Acquired","sum"),
    Revenue=("Revenue","sum")
)
channel["Conversion_Rate"] = channel["Customers"] / channel["Leads"]
channel["CPL"] = channel["Marketing_Spend"] / channel["Leads"]
channel["CAC"] = channel["Marketing_Spend"] / channel["Customers"]
channel["ROMI"] = (channel["Revenue"] - channel["Marketing_Spend"]) / channel["Marketing_Spend"]

print("\nCHANNEL PERFORMANCE\n")
print(channel.round(3).sort_values("ROMI", ascending=False).to_string(index=False))

monthly = df.groupby("Month", as_index=False).agg(
    Revenue=("Revenue","sum"),
    Marketing_Spend=("Marketing_Spend","sum"),
    Leads=("Leads","sum"),
    Customers=("Customers_Acquired","sum")
)
monthly["Conversion_Rate"] = monthly["Customers"]/monthly["Leads"]
monthly["CAC"] = monthly["Marketing_Spend"]/monthly["Customers"]
monthly["Revenue_Growth"] = monthly["Revenue"].pct_change()

print("\nMONTHLY PERFORMANCE\n")
print(monthly.round(3).to_string(index=False))

channel.to_csv("../data/processed/channel_summary.csv", index=False)
monthly.to_csv("../data/processed/monthly_summary.csv", index=False)
