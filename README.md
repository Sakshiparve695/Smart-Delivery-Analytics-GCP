# 🚚 Smart Delivery Analytics Pipeline (GCP + Airflow + ETL)

## 🚀 Overview

This project implements an end-to-end delivery analytics pipeline using Python, MySQL, Google BigQuery, and Apache Airflow.

The system ingests delivery data through REST APIs, processes it using automated ETL workflows, and enables analytical insights on delivery performance, operational efficiency, and route optimization.

The pipeline follows a layered architecture (Raw → Processed → Fact) and is orchestrated using Dockerized Apache Airflow workflows.

---

# 🎯 Problem Statement

Logistics systems generate large volumes of delivery data, but most systems lack structured pipelines for analytics and operational monitoring.

This project solves that by:

- Building a layered ETL pipeline
- Automating delivery data processing
- Enabling cloud-based analytics using BigQuery
- Supporting route optimization workflows
- Creating production-style orchestration using Airflow

---

# 🏗️ System Architecture

```text
Client / API Requests
        │
        ▼
Flask REST API Layer
        │
        ▼
MySQL Raw Layer
(raw_deliveries)
        │
        ▼
Python ETL Pipeline
        │
 ┌───────────────┐
 ▼               ▼
Processed Layer  Fact Layer
(processed_      (fact_
deliveries)      deliveries)
        │
        ▼
Google BigQuery
(Analytics Warehouse)
        │
        ▼
Apache Airflow
(Dockerized Scheduling & Orchestration)
```

---

# ⚙️ Tech Stack

| Category | Technologies |
|---|---|
| Backend | Python, Flask |
| Database | MySQL |
| ETL | Python, Pandas |
| Cloud | Google BigQuery |
| Orchestration | Apache Airflow, Docker |
| APIs | REST APIs |
| Analytics | SQL |
| DevOps | Git, GitHub |

---

# 🔄 ETL Workflow

1. Delivery data is ingested through REST APIs
2. Data is stored in the raw layer (`raw_deliveries`)
3. ETL pipeline extracts and transforms records
4. Processed data is loaded into:
   - `processed_deliveries`
   - `fact_deliveries`
5. Analytical data is pushed into Google BigQuery
6. Airflow DAG automates scheduled execution

---

# ⚡ Key Features

- REST API-based data ingestion
- Automated ETL processing using Python
- Incremental batch processing using processed flags
- Delivery data transformation and enrichment
- Google BigQuery cloud analytics integration
- Apache Airflow DAG orchestration using Docker
- Delivery route optimization using Dijkstra’s Algorithm
- Logging and monitoring support
- Layered data architecture (Raw → Processed → Fact)

---

# 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/add-delivery` | Add delivery into raw layer |
| POST | `/optimize-route` | Compute optimal delivery route |
| GET | `/deliveries` | Fetch delivery records |
| POST | `/update-status` | Update delivery status |

---

# 📊 Analytics & Insights

The system enables analysis of:

- Average delivery duration
- Delay percentage
- Delivery performance trends
- Agent performance tracking
- Route optimization efficiency
- Delivery status monitoring

---

# ☁️ BigQuery Integration

- Integrated Google BigQuery for cloud analytics
- Loaded processed delivery data into analytical warehouse tables
- Used partitioned tables for optimized analytical querying
- Enabled SQL-based analysis on delivery datasets

---

# 🔄 Airflow Orchestration

- Implemented Apache Airflow DAG for ETL scheduling
- Automated pipeline execution using Dockerized Airflow containers
- Managed recurring ETL workflows and monitoring

---

# 📸 Project Screenshots

## 🔄 Airflow DAG Orchestration

![Airflow DAG](screenshots/Docker-Airflow.png)

---

## ⚙️ ETL Pipeline Execution

![ETL Execution](screenshots/ETL_status.png)

---

## ☁️ BigQuery Analytics Layer

![BigQuery](screenshots/bigquery-fact-deliveries.png)

---

## 🗄️ Processed Deliveries Table

![Processed Layer](screenshots/Smart_route_system_Processed_DEliveries.png)

---

## 📊 Fact Deliveries Analytics Table

![Fact Table](screenshots/Smart_route_system_Fact_deliveries.png)

---

# ⚠️ Engineering Challenges Solved

- Implemented incremental ETL processing using processed flags
- Debugged schema mismatch and BigQuery loading issues
- Added ETL logging and monitoring support
- Optimized batch loading into analytical tables
- Integrated cloud warehouse partitioned tables using BigQuery
- Automated DAG scheduling using Airflow Docker containers

---

# 📁 Project Structure

```text
Smart_route_system/
│
├── API_Server.py
├── etl.py
├── requirements.txt
├── docker-compose.yml
├── dags/
├── screenshots/
├── etl.log
└── README.md
```

---

# 🚀 Setup Instructions

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

Create a `.env` file:

```env
DB_HOST=localhost
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=your_database
```

---

## 4️⃣ Run Flask API

```bash
python API_Server.py
```

---

## 5️⃣ Run ETL Pipeline

```bash
python etl.py
```

---

## 6️⃣ Start Airflow (Docker)

```bash
docker-compose up
```

---

# 🚀 Future Improvements

- Real-time streaming using Kafka
- CI/CD pipeline integration
- Dashboard visualization using Power BI / Looker Studio
- Data validation framework
- Real-time monitoring and alerting

---

# 👩‍💻 Author

Sakshi Parve

```
