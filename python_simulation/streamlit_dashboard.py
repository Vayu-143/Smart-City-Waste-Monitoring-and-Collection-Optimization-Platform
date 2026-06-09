import pandas as pd
import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Smart City Waste Dashboard",
    page_icon="🗑️",
    layout="wide"
)

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv("data/waste_data.csv")

# Latest Record
latest = df.iloc[-1]

# =====================================
# HEADER
# =====================================

st.title(
    "🗑️ IoT-Based Smart City Waste Monitoring and Collection Optimization Platform"
)

st.markdown("---")

# =====================================
# KPI CARDS
# =====================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Fill Level (%)",
        f"{latest['FillPercent']:.2f}"
    )

with col2:
    st.metric(
        "Distance (cm)",
        f"{latest['Distance']:.2f}"
    )

with col3:
    st.metric(
        "Collection Required",
        int(latest["CollectionRequired"])
    )

with col4:
    st.metric(
        "Priority",
        latest["Priority"]
    )

# =====================================
# STATUS
# =====================================

st.subheader("Current Bin Status")

st.write(
    f"Status: **{latest['Status']}**"
)

st.write(
    f"Alert: **{latest['Alert']}**"
)

# =====================================
# FILL TREND
# =====================================

st.subheader("Fill Percentage Trend")

st.line_chart(
    df["FillPercent"]
)

# =====================================
# COLLECTION TREND
# =====================================

st.subheader("Collection Requests Trend")

st.line_chart(
    df["CollectionRequired"]
)

# =====================================
# PRIORITY DISTRIBUTION
# =====================================

st.subheader("Priority Distribution")

priority_counts = (
    df["Priority"]
    .value_counts()
)

st.bar_chart(priority_counts)

# =====================================
# KPI ANALYTICS
# =====================================

st.subheader("Municipal KPIs")

avg_fill = df["FillPercent"].mean()

max_fill = df["FillPercent"].max()

alerts = len(
    df[df["Alert"] == 1]
)

st.write(
    f"Average Fill Level: {avg_fill:.2f}%"
)

st.write(
    f"Maximum Fill Level: {max_fill:.2f}%"
)

st.write(
    f"Total Alerts: {alerts}"
)

# =====================================
# PREDICTIVE RECOMMENDATION
# =====================================

st.subheader("Predictive Recommendation")

full_bins = len(
    df[df["FillPercent"] >= 80]
)

if full_bins > 10:

    st.error(
        "Increase waste collection frequency."
    )

else:

    st.success(
        "Current collection schedule is sufficient."
    )

# =====================================
# DATA TABLE
# =====================================

st.subheader("Historical Records")

st.dataframe(df.tail(50))