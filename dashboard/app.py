import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from streamlit_autorefresh import st_autorefresh

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Smart City Waste Dashboard",
    layout="wide"
)

# Auto refresh every 10 seconds
st_autorefresh(
    interval=10000,
    key="dashboardrefresh"
)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("Navigation")

st.sidebar.info(
    """
    Smart City Waste Monitoring Platform

    Technologies Used:

    • ESP32
    • Ultrasonic Sensor
    • ThingSpeak Cloud
    • Python
    • Pandas
    • Matplotlib
    • Streamlit
    """
)

# ==========================================
# THINGSPEAK CONFIG
# ==========================================

CHANNEL_ID = "3404107"
READ_API_KEY = "PFZ0QLNIVZ20YM3Q"

# ==========================================
# LOAD DATA FROM THINGSPEAK
# ==========================================

@st.cache_data(ttl=10)
def load_data():

    url = (
        f"https://api.thingspeak.com/channels/"
        f"{CHANNEL_ID}/feeds.csv"
        f"?api_key={READ_API_KEY}"
        f"&results=100"
    )

    df = pd.read_csv(url)

    df = df.rename(
        columns={
            "created_at": "Timestamp",
            "field1": "Distance",
            "field2": "FillPercent",
            "field3": "Status",
            "field4": "Alert",
            "field5": "CollectionRequired"
        }
    )

    df["Distance"] = pd.to_numeric(
        df["Distance"],
        errors="coerce"
    )

    df["FillPercent"] = pd.to_numeric(
        df["FillPercent"],
        errors="coerce"
    )

    df["Alert"] = pd.to_numeric(
        df["Alert"],
        errors="coerce"
    )

    df["CollectionRequired"] = pd.to_numeric(
        df["CollectionRequired"],
        errors="coerce"
    )

    def get_priority(fill):

        if fill >= 80:
            return "HIGH"
        elif fill >= 40:
            return "MEDIUM"
        else:
            return "LOW"

    df["Priority"] = df["FillPercent"].apply(
        get_priority
    )

    return df.dropna()


df = load_data()
latest = df.iloc[-1]

# ==========================================
# TITLE
# ==========================================

st.title(
    "🗑️ IoT-Based Smart City Waste Monitoring and Collection Optimization Platform"
)

st.markdown("---")

# ==========================================
# LIVE STATUS BANNER
# ==========================================

if latest["Priority"] == "HIGH":

    st.error(
        "🚨 HIGH PRIORITY BIN DETECTED"
    )

elif latest["Priority"] == "MEDIUM":

    st.warning(
        "⚠️ MEDIUM PRIORITY BIN"
    )

else:

    st.success(
        "✅ LOW PRIORITY BIN"
    )

# ==========================================
# KPI CARDS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Fill Level %",
    f"{latest['FillPercent']:.2f}"
)

col2.metric(
    "Distance (cm)",
    f"{latest['Distance']:.2f}"
)

col3.metric(
    "Collection Required",
    "YES"
    if latest["CollectionRequired"] == 1
    else "NO"
)

col4.metric(
    "Priority",
    latest["Priority"]
)

# ==========================================
# BIN STATUS
# ==========================================

st.subheader("Current Bin Status")

st.write(
    f"**Status:** {latest['Status']}"
)

st.write(
    f"**Alert:** {latest['Alert']}"
)

# ==========================================
# FILL LEVEL TREND
# ==========================================

st.subheader("Fill Percentage Trend")

st.line_chart(
    df["FillPercent"]
)

# ==========================================
# COLLECTION REQUEST TREND
# ==========================================

st.subheader("Collection Requests Trend")

st.line_chart(
    df["CollectionRequired"]
)

# ==========================================
# PRIORITY DISTRIBUTION
# ==========================================

st.subheader("Priority Distribution")

priority_counts = (
    df["Priority"]
    .value_counts()
)

fig, ax = plt.subplots()

ax.pie(
    priority_counts,
    labels=priority_counts.index,
    autopct="%1.1f%%"
)

st.pyplot(fig)

# ==========================================
# MUNICIPAL KPI DASHBOARD
# ==========================================

st.subheader("Municipal KPI Dashboard")

avg_fill = df["FillPercent"].mean()

max_fill = df["FillPercent"].max()

total_alerts = len(
    df[df["Alert"] == 1]
)

collection_requests = len(
    df[df["CollectionRequired"] == 1]
)

k1, k2, k3, k4 = st.columns(4)

k1.metric(
    "Average Fill",
    f"{avg_fill:.2f}%"
)

k2.metric(
    "Maximum Fill",
    f"{max_fill:.2f}%"
)

k3.metric(
    "Alerts Generated",
    total_alerts
)

k4.metric(
    "Collection Requests",
    collection_requests
)

# ==========================================
# COLLECTION RECOMMENDATION
# ==========================================

st.subheader(
    "Collection Recommendation"
)

high_bins = len(
    df[df["Priority"] == "HIGH"]
)

medium_bins = len(
    df[df["Priority"] == "MEDIUM"]
)

if high_bins >= 5:

    st.error(
        "Immediate waste collection recommended."
    )

elif medium_bins >= 10:

    st.warning(
        "Schedule collection within next cycle."
    )

else:

    st.success(
        "Collection schedule is currently optimal."
    )

# ==========================================
# PRIORITY QUEUE
# ==========================================

st.subheader(
    "Collection Priority Queue"
)

priority_df = df[
    [
        "Timestamp",
        "FillPercent",
        "Priority",
        "CollectionRequired"
    ]
].tail(20)

st.dataframe(
    priority_df,
    use_container_width=True
)

# ==========================================
# SYSTEM ARCHITECTURE
# ==========================================

st.subheader(
    "System Architecture"
)

try:

    st.image(
        "images/architecture_diagram.png",
        use_container_width=True
    )

except:

    st.info(
        "Add architecture_diagram.png inside images folder."
    )

# ==========================================
# BUSINESS IMPACT
# ==========================================

st.subheader(
    "Business Impact"
)

st.markdown(
    """
    ✅ Reduces unnecessary collection trips

    ✅ Prevents waste overflow

    ✅ Improves operational efficiency

    ✅ Supports smart-city initiatives

    ✅ Enables predictive waste collection

    ✅ Reduces fuel consumption

    ✅ Provides data-driven decision making
    """
)

# ==========================================
# HISTORICAL DATA
# ==========================================

st.subheader(
    "Historical Records"
)

st.dataframe(
    df.tail(100),
    use_container_width=True
)

# ==========================================
# PDF DOWNLOAD
# ==========================================

st.subheader(
    "Download Report"
)

try:

    with open(
        "outputs/smart_city_waste_report.pdf",
        "rb"
    ) as pdf:

        st.download_button(
            label="📄 Download PDF Report",
            data=pdf,
            file_name="Smart_City_Waste_Report.pdf",
            mime="application/pdf"
        )

except:

    st.warning(
        "Generate PDF report first."
    )

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Smart City Waste Monitoring & Collection Optimization Platform | ESP32 + ThingSpeak + Python + Streamlit"
)