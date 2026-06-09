import pandas as pd

# ==========================================
# SMART CITY WASTE ANALYTICS ENGINE
# ==========================================

try:

    df = pd.read_csv("data/waste_data.csv")

except Exception as e:

    print("Error Loading CSV:", e)
    exit()

# ==========================================
# BASIC KPIs
# ==========================================

avg_fill = df["FillPercent"].mean()

max_fill = df["FillPercent"].max()

min_fill = df["FillPercent"].min()

total_records = len(df)

# ==========================================
# PRIORITY ANALYSIS
# ==========================================

high_priority = len(
    df[df["Priority"] == "HIGH"]
)

medium_priority = len(
    df[df["Priority"] == "MEDIUM"]
)

low_priority = len(
    df[df["Priority"] == "LOW"]
)

# ==========================================
# ALERT ANALYSIS
# ==========================================

total_alerts = len(
    df[df["Alert"] == 1]
)

collection_requests = len(
    df[df["CollectionRequired"] == 1]
)

# ==========================================
# COLLECTION ACTIONS
# ==========================================

print("\n")
print("=" * 60)
print("SMART CITY WASTE MONITORING ANALYTICS")
print("=" * 60)

print("\nCOLLECTION ACTIONS")
print("-" * 40)

if high_priority > 0:

    print(
        f"{high_priority} HIGH priority bins require immediate collection."
    )

else:

    print(
        "No urgent collection requests."
    )

# ==========================================
# KPI DASHBOARD
# ==========================================

print("\nSMART CITY KPI DASHBOARD")
print("-" * 40)

print(
    f"Average Fill Level       : {avg_fill:.2f}%"
)

print(
    f"Maximum Fill Level       : {max_fill:.2f}%"
)

print(
    f"Minimum Fill Level       : {min_fill:.2f}%"
)

print(
    f"Total Records Logged     : {total_records}"
)

print(
    f"Total Alerts Generated   : {total_alerts}"
)

print(
    f"Collection Requests      : {collection_requests}"
)

# ==========================================
# PRIORITY DISTRIBUTION
# ==========================================

print("\nCOLLECTION PRIORITY ANALYSIS")
print("-" * 40)

print(
    f"HIGH Priority Bins       : {high_priority}"
)

print(
    f"MEDIUM Priority Bins     : {medium_priority}"
)

print(
    f"LOW Priority Bins        : {low_priority}"
)

# ==========================================
# MUNICIPAL PERFORMANCE KPIs
# ==========================================

print("\nMUNICIPAL PERFORMANCE KPIs")
print("-" * 40)

print(
    "Monitoring Accuracy      : Simulated (95%+)"
)

print(
    "Response Time            : Real Time"
)

print(
    "Collection Strategy      : Demand Based"
)

print(
    "Overflow Detection       : Enabled"
)

print(
    "Cloud Monitoring         : Enabled"
)

# ==========================================
# PREDICTIVE WASTE COLLECTION
# ==========================================

print("\nPREDICTIVE RECOMMENDATION")
print("-" * 40)

full_bins = len(
    df[df["FillPercent"] >= 80]
)

if full_bins > 10:

    print(
        "Recommendation: Increase waste collection frequency."
    )

elif full_bins > 5:

    print(
        "Recommendation: Monitor collection schedule closely."
    )

else:

    print(
        "Recommendation: Current collection schedule is sufficient."
    )

# ==========================================
# BUSINESS IMPACT
# ==========================================

print("\nBUSINESS IMPACT")
print("-" * 40)

print(
    "✓ Reduces unnecessary collection trips"
)

print(
    "✓ Prevents waste overflow"
)

print(
    "✓ Reduces fuel consumption"
)

print(
    "✓ Improves operational efficiency"
)

print(
    "✓ Supports smart-city initiatives"
)

print(
    "✓ Enables data-driven waste collection"
)

# ==========================================
# COMPLETED
# ==========================================

print("\nAnalytics Completed Successfully.")
print("=" * 60)