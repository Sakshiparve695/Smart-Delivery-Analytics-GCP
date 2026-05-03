# 🚚 Smart Delivery Data Pipeline (GCP + Airflow + ETL)

## 🚀 Overview

This project implements an end-to-end **data engineering pipeline** for optimizing delivery operations. It ingests delivery data via APIs, processes it using a Python-based ETL pipeline, and enables analytics using **Google BigQuery**.

The entire workflow is orchestrated using **Apache Airflow (Dockerized)**, making the pipeline automated and production-ready.

---

## 🎯 Problem Statement

Logistics systems generate large volumes of delivery data, but most systems lack structured pipelines for analysis.

This project solves that by:

* Building a **layered data pipeline (raw → processed → fact)**
* Enabling **analytical insights on delivery performance**
* Automating workflows using **Airflow scheduling**

---

## 🏗️ Architecture

```
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

---

## ⚙️ Tech Stack

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

(Add your screenshots here)

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

---

## 🎯 Why This Project Stands Out

* End-to-end pipeline (API → DB → ETL → Cloud → Orchestration)
* Real-world architecture used in data engineering
* Demonstrates both backend + data engineering skills
* Includes Airflow + Docker integration

---

## 👩‍💻 Author

Sakshi Parve
Aspiring Data Engineer 
