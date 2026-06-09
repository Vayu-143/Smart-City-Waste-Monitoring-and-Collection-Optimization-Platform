from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv("data/waste_data.csv")

avg_fill = df["FillPercent"].mean()
max_fill = df["FillPercent"].max()
min_fill = df["FillPercent"].min()

alerts = len(df[df["Alert"] == 1])

collection_requests = len(
    df[df["CollectionRequired"] == 1]
)

high_priority = len(
    df[df["Priority"] == "HIGH"]
)

medium_priority = len(
    df[df["Priority"] == "MEDIUM"]
)

low_priority = len(
    df[df["Priority"] == "LOW"]
)

# =====================================
# PDF SETTINGS
# =====================================

pdf = SimpleDocTemplate(
    "outputs/smart_city_waste_report.pdf"
)

styles = getSampleStyleSheet()

content = []

# =====================================
# TITLE PAGE
# =====================================

title = """
IoT-Based Smart City Waste Monitoring
and Collection Optimization Platform
"""

content.append(
    Paragraph(title, styles["Title"])
)

content.append(Spacer(1, 20))

content.append(
    Paragraph(
        "Project Report",
        styles["Heading2"]
    )
)

content.append(
    Paragraph(
        "Smart City Waste Management using IoT, ESP32, Ultrasonic Sensors, Python Analytics and ThingSpeak Cloud",
        styles["Normal"]
    )
)

content.append(PageBreak())

# =====================================
# EXECUTIVE SUMMARY
# =====================================

content.append(
    Paragraph(
        "1. Executive Summary",
        styles["Heading1"]
    )
)

content.append(
    Paragraph(
        """
        This project presents an IoT-based Smart City Waste Monitoring
        and Collection Optimization Platform. The system continuously
        monitors waste-bin fill levels using ultrasonic sensing,
        analyzes collection requirements, generates alerts, and
        visualizes data on the ThingSpeak cloud dashboard.
        The platform helps municipalities optimize collection
        schedules and reduce operational costs.
        """,
        styles["BodyText"]
    )
)

# =====================================
# PROBLEM STATEMENT
# =====================================

content.append(
    Paragraph(
        "2. Problem Statement",
        styles["Heading1"]
    )
)

content.append(
    Paragraph(
        """
        Traditional waste collection systems follow fixed schedules,
        resulting in unnecessary collection trips, fuel wastage,
        and overflowing bins. This project provides a real-time
        monitoring solution that enables data-driven waste
        collection decisions.
        """,
        styles["BodyText"]
    )
)

# =====================================
# SYSTEM ARCHITECTURE
# =====================================

content.append(
    Paragraph(
        "3. System Architecture",
        styles["Heading1"]
    )
)

content.append(
    Paragraph(
        """
        Ultrasonic Sensor → ESP32/Simulation →
        Fill-Level Calculation → Priority Engine →
        ThingSpeak Cloud → Dashboard →
        Analytics & Reporting
        """,
        styles["BodyText"]
    )
)

# =====================================
# TECHNOLOGIES USED
# =====================================

content.append(
    Paragraph(
        "4. Technologies Used",
        styles["Heading1"]
    )
)

content.append(
    Paragraph(
        """
        • ESP32 Microcontroller<br/>
        • Ultrasonic Sensor (HC-SR04)<br/>
        • Python Programming<br/>
        • Pandas Analytics<br/>
        • ThingSpeak Cloud Platform<br/>
        • ReportLab PDF Generation<br/>
        • CSV Data Logging
        """,
        styles["BodyText"]
    )
)

# =====================================
# DASHBOARD
# =====================================

content.append(
    Paragraph(
        "5. ThingSpeak Dashboard",
        styles["Heading1"]
    )
)

content.append(
    Paragraph(
        """
        The dashboard provides real-time visualization
        of waste-bin status through:
        <br/><br/>
        • Fill Percentage Gauge
        <br/>
        • Distance Monitoring
        <br/>
        • Overflow Alert Indicator
        <br/>
        • Collection Required Indicator
        <br/>
        • Historical Fill-Level Trends
        <br/>
        • Collection Request Trends
        """,
        styles["BodyText"]
    )
)

# =====================================
# KPI ANALYSIS
# =====================================

content.append(
    Paragraph(
        "6. KPI Analysis",
        styles["Heading1"]
    )
)

content.append(
    Paragraph(
        f"""
        Average Fill Level : {avg_fill:.2f}%<br/>
        Maximum Fill Level : {max_fill:.2f}%<br/>
        Minimum Fill Level : {min_fill:.2f}%<br/>
        Total Alerts : {alerts}<br/>
        Collection Requests : {collection_requests}<br/>
        Total Records Logged : {len(df)}
        """,
        styles["BodyText"]
    )
)

# =====================================
# PRIORITY SYSTEM
# =====================================

content.append(
    Paragraph(
        "7. Collection Priority System",
        styles["Heading1"]
    )
)

content.append(
    Paragraph(
        f"""
        HIGH Priority Bins : {high_priority}<br/>
        MEDIUM Priority Bins : {medium_priority}<br/>
        LOW Priority Bins : {low_priority}
        """,
        styles["BodyText"]
    )
)

content.append(
    Paragraph(
        """
        The priority engine automatically categorizes
        waste bins and assists municipal authorities
        in scheduling waste collection operations.
        """,
        styles["BodyText"]
    )
)

# =====================================
# PREDICTIVE COLLECTION
# =====================================

content.append(
    Paragraph(
        "8. Predictive Waste Collection",
        styles["Heading1"]
    )
)

if high_priority > 10:

    recommendation = (
        "Increase waste collection frequency."
    )

else:

    recommendation = (
        "Current collection schedule is sufficient."
    )

content.append(
    Paragraph(
        recommendation,
        styles["BodyText"]
    )
)

# =====================================
# BUSINESS BENEFITS
# =====================================

content.append(
    Paragraph(
        "9. Business Benefits",
        styles["Heading1"]
    )
)

content.append(
    Paragraph(
        """
        • Reduces unnecessary collection trips<br/>
        • Prevents waste overflow<br/>
        • Reduces fuel consumption<br/>
        • Improves operational efficiency<br/>
        • Supports smart-city initiatives<br/>
        • Enables data-driven decision making
        """,
        styles["BodyText"]
    )
)

# =====================================
# FUTURE SCOPE
# =====================================

content.append(
    Paragraph(
        "10. Future Scope",
        styles["Heading1"]
    )
)

content.append(
    Paragraph(
        """
        • Integration with real ESP32 hardware<br/>
        • GPS-enabled smart bins<br/>
        • Route optimization using AI<br/>
        • Mobile application for operators<br/>
        • Machine Learning based waste prediction<br/>
        • Integration with municipal smart-city platforms
        """,
        styles["BodyText"]
    )
)

# =====================================
# COMPLETION
# =====================================

content.append(Spacer(1, 20))

content.append(
    Paragraph(
        "Report Generated Automatically",
        styles["Heading2"]
    )
)

pdf.build(content)

print(
    "Professional Smart City Report Generated Successfully."
)