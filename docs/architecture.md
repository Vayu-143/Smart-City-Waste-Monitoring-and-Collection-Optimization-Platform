# System Architecture

## Smart City Waste Monitoring and Collection Optimization Platform

### Overview

The Smart City Waste Monitoring and Collection Optimization Platform is an IoT-based solution designed to monitor waste bin levels in real time and provide intelligent collection recommendations. The system integrates embedded hardware, cloud computing, data analytics, and web-based visualization to improve municipal waste management efficiency.

---

## Architecture Diagram

```text
+--------------------+
| Ultrasonic Sensor  |
| (HC-SR04)          |
+---------+----------+
          |
          v
+--------------------+
| ESP32 Controller   |
| Data Acquisition   |
+---------+----------+
          |
          v
+--------------------+
| ThingSpeak Cloud   |
| Data Storage       |
| Real-Time Feed     |
+---------+----------+
          |
          v
+--------------------+
| Python Analytics   |
| Data Processing    |
| KPI Generation     |
+---------+----------+
          |
          v
+--------------------+
| Streamlit Dashboard|
| Visualization      |
| Monitoring         |
+---------+----------+
          |
          v
+--------------------+
| Municipal Decision |
| Support System     |
+--------------------+
```

---

## System Components

### 1. Ultrasonic Sensor (HC-SR04)

The ultrasonic sensor measures the distance between the sensor and the waste surface inside the bin.

Responsibilities:

- Waste level detection
- Distance measurement
- Fill percentage calculation input

---

### 2. ESP32 Microcontroller

The ESP32 serves as the primary data acquisition and communication unit.

Responsibilities:

- Read ultrasonic sensor data
- Process sensor measurements
- Connect to Wi-Fi network
- Transmit data to ThingSpeak Cloud

---

### 3. ThingSpeak Cloud Platform

ThingSpeak acts as the cloud-based IoT platform for storing and visualizing sensor data.

Responsibilities:

- Receive sensor readings
- Store historical records
- Provide REST API access
- Enable remote monitoring

Data Fields:

| Field | Description |
|---------|-------------|
| Field 1 | Distance (cm) |
| Field 2 | Fill Percentage (%) |
| Field 3 | Bin Status |
| Field 4 | Alert Status |
| Field 5 | Collection Required |

---

### 4. Python Analytics Engine

The analytics module processes collected data and generates operational insights.

Responsibilities:

- Fill level calculation
- Priority classification
- Alert generation
- Collection recommendation
- KPI computation
- Report generation

Priority Classification:

| Fill Percentage | Priority |
|----------------|----------|
| 0–39% | LOW |
| 40–79% | MEDIUM |
| 80–100% | HIGH |

---

### 5. Streamlit Dashboard

The Streamlit dashboard provides a user-friendly interface for monitoring and decision-making.

Features:

- Live waste bin monitoring
- KPI cards
- Trend analysis
- Priority distribution
- Collection recommendations
- Historical records
- Report downloads

---

### 6. Municipal Decision Support Layer

This layer assists waste management authorities in planning collection schedules efficiently.

Benefits:

- Reduced operational costs
- Reduced fuel consumption
- Overflow prevention
- Improved collection efficiency
- Data-driven decision making

---

## Data Flow

1. Ultrasonic sensor measures bin level.
2. ESP32 collects sensor data.
3. Data is transmitted to ThingSpeak Cloud.
4. Python retrieves and processes cloud data.
5. Analytics engine generates KPIs and recommendations.
6. Streamlit dashboard visualizes information.
7. Municipal operators monitor system status and take action.

---

## Functional Workflow

```text
Sensor Reading
      ↓
ESP32 Processing
      ↓
Cloud Upload
      ↓
Data Storage
      ↓
Analytics Engine
      ↓
Priority Detection
      ↓
Dashboard Visualization
      ↓
Collection Recommendation
```

---

## Expected Outcomes

- Real-time waste monitoring
- Intelligent collection planning
- Improved operational efficiency
- Reduced waste overflow incidents
- Enhanced smart-city waste management

---

## Conclusion

The Smart City Waste Monitoring and Collection Optimization Platform demonstrates the integration of IoT devices, cloud computing, analytics, and visualization technologies to create an efficient and scalable waste management solution. The system supports modern smart-city initiatives by enabling real-time monitoring, predictive insights, and optimized collection operations.