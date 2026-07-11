# 🚚 Smart Delivery Analytics Platform
### End-to-End Cloud Data Engineering Solution using Flask REST API, Azure MySQL, Apache Airflow, Google BigQuery, PySpark & Power BI


---

## 🚀 Project Overview

Smart Delivery Analytics Platform is an end-to-end cloud-based Data Engineering project that simulates a modern logistics analytics platform. It automates the journey of delivery data from ingestion to reporting by combining REST APIs, cloud databases, ETL, workflow orchestration, cloud warehousing, scalable analytics and interactive dashboards.

---

# 🎯 Business Problem

Logistics companies generate thousands of delivery transactions every day. Running reports directly on operational databases results in slow analytical queries, repetitive manual data preparation and limited business visibility. There was no automated pipeline to validate incoming data, transform it into analytics-ready datasets or provide centralized dashboards for decision makers.
---

# 🎯 Solution

The platform was designed using a layered data architecture. Delivery requests are captured through FastAPI, stored in Azure MySQL, transformed using a Python ETL pipeline, automatically orchestrated with Apache Airflow, published to Google BigQuery for analytics, processed using PySpark and visualized through Power BI dashboards.
---
# 🏗️Smart Delivery Analytics Platform
End-to-End Cloud Data Engineering Architecture

```text
                                      ┌──────────────────────┐
                                      │      Client/User     │
                                      └──────────┬───────────┘
                                                 │
                                                 ▼
                                   ┌─────────────────────────┐
                                   │     Flask REST APIs     │
                                   │  (Delivery Management)  │
                                   └──────────┬──────────────┘
                                              │
                               Add / Update / Fetch Deliveries
                                              │
                                              ▼
                              ┌────────────────────────────────┐
                              │      Azure MySQL Database      │
                              │      Raw Delivery Records      │
                              └──────────┬─────────────────────┘
                                         │
                                         ▼
                         ┌──────────────────────────────────────┐
                         │        Python ETL Pipeline           │
                         │--------------------------------------│
                         │ • Extract Raw Data                   │
                         │ • Data Validation                    │
                         │ • Handle Invalid Records             │
                         │ • Data Cleaning                      │
                         │ • Data Transformation                │
                         │ • Generate Processed Dataset         │
                         └──────────┬───────────────────────────┘
                                    │
                                    ▼
                     ┌──────────────────────────────────────────┐
                     │     Apache Airflow (Workflow Engine)     │
                     │------------------------------------------│
                     │ • Schedule ETL Jobs                      │
                     │ • Automate Pipeline Execution            │
                     │ • Monitor DAG Runs                       │
                     │ • Retry Failed Tasks                     │
                     └──────────┬───────────────────────────────┘
                                │
                 ┌──────────────┴──────────────┐
                 ▼                             ▼
      ┌──────────────────────┐       ┌────────────────────────┐
      │ Processed Deliveries │       │  Fact Deliveries Table │
      └──────────┬───────────┘       └──────────┬─────────────┘
                 │                              │
                 └──────────────┬───────────────┘
                                ▼
                    ┌────────────────────────────┐
                    │ Google BigQuery Warehouse  │
                    │ Analytics Ready Datasets   │
                    └──────────┬─────────────────┘
                               │
                               ▼
                   ┌─────────────────────────────┐
                   │      PySpark Analytics      │
                   │-----------------------------│
                   │ • Aggregations              │
                   │ • Agent Performance         │
                   │ • Delivery Insights         │
                   │ • DataFrame Transformations │
                   └──────────┬──────────────────┘
                              │
                              ▼
                    ┌────────────────────────────┐
                    │     Power BI Dashboard     │
                    │----------------------------│
                    │ • Total Deliveries         │
                    │ • Delayed Deliveries       │
                    │ • Avg Delivery Time        │
                    │ • Total Distance           │
                    │ • Agent Performance        │
                    │ • Business KPIs            │
                    └────────────────────────────┘
```
## Data Flow

1. Delivery requests are received through Flask REST APIs.
2. Delivery records are stored in Azure MySQL as operational data.
3. A Python ETL pipeline extracts, validates, cleans and transforms raw delivery records.
4. Apache Airflow schedules and automates ETL execution.
5. Processed and fact tables are created for analytical workloads.
6. Curated datasets are loaded into Google BigQuery.
7. PySpark performs scalable analytical transformations and aggregations.
8. Power BI connects to the analytical dataset and provides interactive business dashboards for decision-making.
---

#  ⚙️ Technology Stack

| Category | Technologies |
|-----------|--------------|
| **Programming Language** | Python 3.11 |
| **Backend Framework** | Flask REST API |
| **Cloud Platform** | Microsoft Azure |
| **Application Hosting** | Azure App Service |
| **Operational Database (OLTP)** | Azure MySQL Flexible Server |
| **Data Ingestion** | REST APIs, JSON |
| **ETL Pipeline** | Python, Pandas |
| **Workflow Orchestration** | Apache Airflow |
| **Containerization** | Docker, Docker Compose |
| **Cloud Data Warehouse (OLAP)** | Google BigQuery |
| **Big Data Processing** | PySpark |
| **Data Modeling** | Raw Layer, Processed Layer, Fact Layer |
| **Data Transformation** | Pandas, PySpark DataFrames |
| **Analytics** | SQL, Window Functions, Aggregations |
| **Business Intelligence** | Microsoft Power BI |
| **Development Tools** | VS Code, Postman |
| **Version Control** | Git, GitHub |
| **Deployment** | Azure App Service, GitHub Actions |
---

# 🔄 End-to-End Cloud Data Engineering Pipeline

The Smart Delivery Analytics Platform follows a modern layered data engineering architecture that transforms operational delivery data into analytics-ready datasets for reporting and business intelligence.

---

## 📥 Step 1 — Data Ingestion Layer

Delivery requests are submitted through REST APIs and act as the entry point of the platform.

Each request contains delivery details such as:

- Order Information
- Source Location
- Destination Location
- Agent Details
- Delivery Status

Example Request

```json
{
  "order_name": "Order_1001",
  "source": 3,
  "destination": 8
}
```

Once validated, every request is stored inside the operational database.

📷 **Screenshot:** Running API / Postman

---

## ☁️ Step 2 — Operational Database (Azure MySQL)

The application stores incoming delivery records in the **Raw Layer** of Azure MySQL.

```sql
raw_deliveries
```

This layer preserves the original transactional data exactly as received from the application.

### Stored Information

- Delivery ID
- Order Name
- Source
- Destination
- Agent Name
- Status
- Timestamp

📷 **Screenshot:** ![Raw Deliveries Table](Smart_route_System_Process_DElivery) 

---

## 🔄 Step 3 — ETL Processing

A Python-based ETL pipeline extracts raw delivery records and prepares them for analytical processing.

### ETL Operations

- Extract Raw Records
- Data Validation
- Handle Invalid Records
- Data Cleaning
- Delivery Time Calculation
- Delay Detection
- Data Transformation
- Logging & Error Handling

Only validated records move to downstream analytical layers.

📷 **Screenshot:** ![ETL Execution Log](Smart_Delivery_ETL) 


---

## 📂 Step 4 — Processed Data Layer

Validated records are stored in the Processed Layer.

```sql
processed_deliveries
```

The processed dataset contains standardized delivery information ready for reporting and analytics.


---

## 📊 Step 5 — Fact Layer

The ETL pipeline generates a centralized fact table that serves as the primary analytical dataset.

```sql
fact_deliveries
```

### Business Metrics

- Delivery Duration
- Distance Covered
- Delay Status
- Delivery Date
- Agent Information

The fact layer acts as the single source of truth for analytical workloads.

📷 **Screenshot:** ![Fact Deliveries Table](Smart_route_system_Fact_deliveries)

---

## ⏰ Step 6 — Workflow Orchestration (Apache Airflow)

Apache Airflow automates the complete ETL workflow.

### Responsibilities

- Schedule ETL Jobs
- Trigger Pipeline Execution
- Monitor DAG Runs
- Retry Failed Tasks
- Centralized Workflow Monitoring

Running the ETL through Airflow removes the need for manual execution and ensures consistent pipeline automation.

📷 **Screenshot:** ![Airflow DAG & Graph](ETL_Pipeline_Graph)

---

## ☁️ Step 7 — Cloud Data Warehouse (Google BigQuery)

Curated analytical datasets are published to Google BigQuery.

BigQuery separates analytical workloads from transactional workloads and enables fast cloud-based reporting.

### Advantages

- High Performance SQL Queries
- Cloud Scalability
- Analytics-Optimized Storage
- Integration with Business Intelligence Tools

📷 **Screenshot:** 1[BigQuery Tables](PySpark_And_BigQuerypng)

---

## ⚡ Step 8 — PySpark Analytics Layer

PySpark performs scalable analytical transformations on the curated delivery dataset.

### Implemented Features

- DataFrame Transformations
- Aggregations using groupBy()
- Window Functions
- Agent Performance Analysis
- Ranking Reports

### Generated Dataset

```sql
agent_performance
```

### KPIs Generated

- Total Deliveries
- Average Delivery Time
- Total Distance Covered
- Delay Percentage
- Agent Performance Ranking

The resulting analytics dataset is published to Google BigQuery for reporting.


---

## 📈 Step 9 — Business Intelligence (Power BI)

Power BI connects to the analytics-ready datasets stored in Google BigQuery and provides interactive dashboards for business users.

### Dashboard KPIs

- Total Deliveries
- Delayed Deliveries
- Average Delivery Time
- Total Distance Covered
- Delivery Success Rate
- Active Delivery Agents

### Interactive Visualizations

- Deliveries by Agent
- Delivery Status Distribution
- Average Delivery Time by Agent
- Agent Performance Ranking
- Daily Delivery Trends
- Distance Analysis

### Business Insights

- Monitor Delivery Operations
- Track Agent Productivity
- Identify Delayed Deliveries
- Analyze Operational Efficiency
- Support Data-Driven Decision Making

📷 **Screenshot:** ![Power BI Dashboard](PowerBI_Dashboard_Final)

---

# 🛣 Route Optimization

The platform includes an intelligent route optimization module based on **Dijkstra's Algorithm**.

### Features

- Shortest Path Computation
- Distance Optimization
- Efficient Route Selection
- Reduced Travel Distance

---

# 🔌 REST API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/add-delivery` | Add a new delivery record |
| POST | `/optimize-route` | Calculate the shortest delivery route |
| GET | `/deliveries` | Retrieve delivery records |
| POST | `/update-status` | Update delivery status |

---

# 📊 Analytics Delivered

The platform provides insights into:

- Delivery Volume
- Delivery Trends
- Agent Performance
- Delivery Delay Percentage
- Average Delivery Duration
- Distance Travelled
- Agent Ranking
- Operational KPIs
- Performance Leaderboards

---

# ☁️ Cloud Deployment on Microsoft Azure

To simulate a production-ready environment, the Smart Delivery Analytics Platform was deployed on Microsoft Azure.

The application is hosted on **Azure App Service**, while **Azure MySQL Flexible Server** serves as the operational database. This cloud deployment enables centralized data storage, remote accessibility, and an architecture similar to enterprise-grade applications.

The screenshots below demonstrate the successful deployment and cloud infrastructure used in the project.
![Web Services](App_Services_Azure)
![Azure Mysql](Azure_MYSQL)
![Resource Group](Azure_Resource_Group)
![Deployment](Deployment_Center)
![Status](Azure_Running_Website)
---

# ⭐ Key Features

The Smart Delivery Analytics Platform demonstrates an end-to-end cloud data engineering workflow, covering data ingestion, transformation, orchestration, warehousing, scalable analytics, and business intelligence.

### Core Features

- 🚚 REST API-based Delivery Management System
- ☁️ Cloud Deployment using Microsoft Azure App Service
- 🗄 Azure MySQL Operational Database
- 🔄 Automated ETL Pipeline for Data Validation & Transformation
- 📂 Layered Data Architecture (Raw → Processed → Fact)
- ⏰ Workflow Automation using Apache Airflow
- ☁️ Google BigQuery Cloud Data Warehouse
- ⚡ PySpark Analytics Layer for Scalable Processing
- 📊 Interactive Power BI Business Dashboard
- 🛣 Intelligent Route Optimization using Dijkstra's Algorithm
- 📈 Agent Performance Analytics
- 📉 Delivery Performance & Delay Analysis
- 📦 Dockerized Deployment Environment
- 🔐 Secure Configuration using Environment Variables

---

# 🧩 Engineering Challenges Solved

Throughout the project, several real-world engineering challenges were addressed while integrating multiple cloud and analytics technologies into a unified data pipeline.

### Data Engineering

- Designed a layered data architecture (Raw → Processed → Fact)
- Built an incremental ETL pipeline using processed flags
- Implemented data validation, transformation and cleansing
- Separated transactional and analytical workloads

### Cloud Integration

- Integrated Azure MySQL with Google BigQuery
- Deployed the application on Microsoft Azure App Service
- Configured secure cloud authentication using service accounts
- Automated cloud data publishing

### Workflow Automation

- Scheduled recurring ETL workflows using Apache Airflow
- Configured Docker-based Airflow deployment
- Managed workflow retries and execution monitoring

### Analytics Engineering

- Built PySpark analytics pipelines using DataFrames
- Implemented GroupBy Aggregations
- Applied Window Functions (RANK, ROW_NUMBER)
- Generated Agent Performance Analytics Mart
- Published analytics-ready datasets to Google BigQuery

### Business Intelligence

- Connected Power BI directly to BigQuery
- Designed KPI dashboards for operational reporting
- Developed interactive analytics for delivery performance

---

# 📁 Project Structure

```text
Smart_Delivery_Analytics/
│
├── API_Server.py                  # REST API
├── etl.py                         # ETL Pipeline
├── generate_data.py               # Sample Data Generator
├── requirements.txt
├── docker-compose.yml
├── Smart_Delivery_PySpark_Analytics.ipynb
│
├── airflow-docker/
│   └── dags/
│       └── etl_dag.py
│
├── Power_BI/
│   └── Smart_Delivery_Dashboard.pbix
│
├── screenshots/
│
├── etl.log
└── README.md
```

---

# 🚀 Getting Started

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Sakshiparve695/Smart-Delivery-Analytics-GCP.git
cd Smart-Delivery-Analytics-GCP
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Configure Environment Variables

Create a `.env` file and configure the following:

```env
DB_HOST=<your_host>
DB_USER=<your_username>
DB_PASSWORD=<your_password>
DB_NAME=smart_delivery_system

BIGQUERY_PROJECT=<your_project_id>
GOOGLE_APPLICATION_CREDENTIALS=<service_account.json>
```

---

## 4️⃣ Start the REST API

```bash
python API_Server.py
```

---

## 5️⃣ Execute ETL Pipeline

```bash
python etl.py
```

---

## 6️⃣ Launch Apache Airflow

```bash
docker-compose up -d
```

Open:

```
http://localhost:8080
```

and trigger the ETL DAG.

---

## 7️⃣ Open Power BI Dashboard

Connect Power BI to the curated analytical dataset stored in Google BigQuery to explore delivery analytics and business KPIs.

---

# 🚀 Future Roadmap

The architecture has been designed to support future scalability and enterprise-grade enhancements.

Planned improvements include:

- 📡 Real-Time Data Streaming using Apache Kafka
- 🔄 CI/CD Pipeline using GitHub Actions & Azure
- 📊 Data Quality Monitoring Framework
- 📩 Email Notifications & Alerting
- 🏗 Microsoft Fabric / Lakehouse Integration
- 📈 Real-Time Streaming Dashboards
- 🤖 Predictive Delivery Analytics using Machine Learning
- ☁️ Kubernetes-based Deployment
- 📦 Data Versioning & Lineage Tracking

---

# 👩‍💻 Author

## Sakshi Parve

**Aspiring Data Engineer**

**Tech Stack**

Python • SQL • Azure • Apache Airflow • Google BigQuery • PySpark • Power BI • Docker • Git • GitHub

---

⭐ If you found this project useful, consider giving it a Star.
