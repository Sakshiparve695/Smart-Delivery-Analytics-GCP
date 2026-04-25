# 🚚 Smart Delivery Data Pipeline (GCP + ETL + Analytics)

## 🚀 Overview

This project implements an end-to-end **data engineering pipeline** for optimizing delivery operations. It ingests delivery data via REST APIs, processes it through ETL pipelines, and enables analytics using SQL and Google BigQuery.

---

## 🎯 Problem Statement

Logistics systems generate large volumes of delivery data (orders, routes, timings), but this data is often underutilized.

This system solves that by:

* Building a structured data pipeline (raw → processed → fact)
* Enabling analytics on delivery performance
* Supporting route optimization using algorithms

---

## 🏗️ Architecture

Client → Flask API → MySQL (raw_deliveries)
               ↓
              ETL Pipeline
               ↓
processed_deliveries → fact_deliveries
               ↓
            BigQuery (Analytics)

---

## ⚙️ Tech Stack

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

---

## ☁️ GCP Integration

* Loaded processed data into **BigQuery**
* Performed SQL-based analytics on delivery performance

---

## 🌐 Deployment

API deployed on Render: <ADD YOUR LINK HERE>

---

## 📈 Future Improvements

* Pipeline orchestration (Airflow)
* Real-time streaming (Kafka)
* Dashboard (Streamlit / React)
* Automated scheduling for ETL jobs

---

## 🎯 Why This Project Stands Out

* End-to-end data pipeline implementation
* Combines backend + data engineering + analytics
* Includes algorithmic optimization (Dijkstra)
* Demonstrates real-world system design

---

## 👩‍💻 Author

Sakshi Parve
Aspiring Data Engineer | Backend Developer

