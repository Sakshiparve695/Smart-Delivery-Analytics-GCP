<<<<<<< HEAD
# 🚚 Smart Delivery Data Pipeline (GCP + Airflow + ETL)

## 🚀 Overview

This project implements an end-to-end **data engineering pipeline** for optimizing delivery operations. It ingests delivery data via APIs, processes it using a Python-based ETL pipeline, and enables analytics using **Google BigQuery**.

The entire workflow is orchestrated using **Apache Airflow (Dockerized)**, making the pipeline automated and production-ready.
=======
# 🚚 Smart Delivery Data Pipeline (GCP + ETL + Analytics)

## 🚀 Overview

This project implements an end-to-end **data engineering pipeline** for optimizing delivery operations. It ingests delivery data via REST APIs, processes it through ETL pipelines, and enables analytics using SQL and Google BigQuery.
>>>>>>> 230b9a6 (final clean data pipeline)

---

## 🎯 Problem Statement

<<<<<<< HEAD
Logistics systems generate large volumes of delivery data, but most systems lack structured pipelines for analysis.

This project solves that by:

* Building a **layered data pipeline (raw → processed → fact)**
* Enabling **analytical insights on delivery performance**
* Automating workflows using **Airflow scheduling**
=======
Logistics systems generate large volumes of delivery data (orders, routes, timings), but this data is often underutilized.

This system solves that by:

* Building a structured data pipeline (raw → processed → fact)
* Enabling analytics on delivery performance
* Supporting route optimization using algorithms
>>>>>>> 230b9a6 (final clean data pipeline)

---

## 🏗️ Architecture

```
<<<<<<< HEAD
Client / API
     │
     ▼
FastAPI (Data Ingestion)
     │
     ▼
MySQL (Raw Layer - raw_deliveries)
     │
     ▼
Python ETL Pipeline
     │
     ├── Processed Layer (processed_deliveries)
     └── Fact Table (fact_deliveries)
     │
     ▼
Google BigQuery (Analytics Layer)
     │
     ▼
Airflow (Scheduling & Orchestration via Docker)
```

=======
Client / API Testing Tool
        │
        ▼
Flask API (Data Ingestion Layer)
        │
        ▼
MySQL - Raw Layer (raw_deliveries)
        │
        ▼
ETL Pipeline (Python / PySpark)
        │
        ▼
Processed Layer (processed_deliveries)
        │
        ▼
Fact Table (fact_deliveries)
        │
        ▼
Google BigQuery (Analytics Layer)
```


>>>>>>> 230b9a6 (final clean data pipeline)
---

## ⚙️ Tech Stack

<<<<<<< HEAD
* Python
* FastAPI
* MySQL
* Google BigQuery
* Apache Airflow (Docker)
* SQL
* Pandas

---

## 🔄 Data Pipeline

1. API ingests delivery data into **raw_deliveries**
2. ETL pipeline performs:

   * Incremental load (`processed_flag`)
   * Transformation (`delivery_duration`, `is_delayed`)
   * Lookup joins (location enrichment)
3. Data stored in:

   * `processed_deliveries` (clean layer)
   * `fact_deliveries` (analytics layer)
4. Data loaded into **BigQuery**
5. Airflow schedules and automates the pipeline

---

## ⚡ Key Features

* Incremental ETL processing
* Data transformation & enrichment
* Cloud data warehouse integration (BigQuery)
* Workflow orchestration using Airflow
* Docker-based deployment

---

## 📊 Analytics & Insights

* Average delivery time
* Delay percentage
* Agent performance
* Delivery trends

---

## ☁️ Cloud Integration

* Integrated with **Google BigQuery**
* Enabled SQL-based analytical queries on delivery data

---

## 🔄 Workflow Orchestration

* Implemented DAG using **Apache Airflow**
* Scheduled ETL jobs automatically
* Managed pipeline using Docker containerization

---

## 📸 Screenshots


```
![Airflow](screenshots/airflow.png)
![ETL Output](screenshots/etl.png)
```

---

## 🚀 Future Improvements

* Real-time streaming (Kafka)
* Dashboard (Power BI / Looker Studio)
* CI/CD integration
* Data validation layer
=======
* Python (Flask)
* MySQL (Data Storage)
* SQL (Data Processing)
* Google BigQuery (Analytics)
* PySpark (ETL experimentation)
* Render (Deployment)

---

## 🔌 API Endpoints

* `POST /add-delivery` → Ingest delivery data into raw layer
* `POST /optimize-route` → Compute shortest route using Dijkstra’s Algorithm
* `GET /deliveries` → Fetch delivery records
* `POST /update-status` → Update delivery status
* `GET /analytics/*` → Analytical insights

---

## 🔄 Data Pipeline

1. API ingests delivery data into **raw layer**
2. ETL script processes and cleans data
3. Data is stored in **processed and fact tables**
4. Fact data is analyzed using **BigQuery**
5. Implemented batch ETL processing to transform and load delivery data into analytical tables.

---

## 🚀 Advanced Feature

* Implemented **Dijkstra’s Algorithm** for route optimization
* Cost function considers **distance + traffic weight**

---

## 📊 Analytics & Insights

* Delivery delay percentage
* Agent performance tracking
* Average delivery duration
* Route efficiency insights
* Enabled analysis of delivery performance and delay patterns

---

## ☁️ GCP Integration

* Loaded processed data into **BigQuery**
* Performed SQL-based analytics on delivery performance

---

## 🌐 Deployment

API deployed on Render

---

## 📈 Future Improvements

* Pipeline orchestration (Airflow)
* Real-time streaming (Kafka)
* Dashboard (Streamlit / React)
* Automated scheduling for ETL jobs
>>>>>>> 230b9a6 (final clean data pipeline)

---

## 🎯 Why This Project Stands Out

<<<<<<< HEAD
* End-to-end pipeline (API → DB → ETL → Cloud → Orchestration)
* Real-world architecture used in data engineering
* Demonstrates both backend + data engineering skills
* Includes Airflow + Docker integration
=======
* End-to-end data pipeline implementation
* Combines backend + data engineering + analytics
* Includes algorithmic optimization (Dijkstra)
* Demonstrates real-world system design
>>>>>>> 230b9a6 (final clean data pipeline)

---

## 👩‍💻 Author

Sakshi Parve
<<<<<<< HEAD
Aspiring Data Engineer 
=======
Aspiring Data Engineer | Backend Developer

>>>>>>> 230b9a6 (final clean data pipeline)
