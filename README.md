# 🚚 Smart Delivery Data Pipeline & Analytics System (GCP + BigQuery)

## 📌 Overview
This project is an end-to-end Data Engineering pipeline that simulates a real-world delivery system. It processes raw delivery data using Python, applies ETL transformations, and loads structured data into Google BigQuery for analytics.

The system demonstrates complete data flow from ingestion to insights.

---

## ⚙️ Tech Stack
- Python  
- Flask (REST API)  
- MySQL  
- Google BigQuery  
- PySpark (simulation)  
- Git & GitHub  

---

## 🔄 Workflow

1. API generates delivery data  
2. Data is stored in MySQL (raw layer)  
3. ETL pipeline extracts and processes data  
4. Data is transformed (duration, delay detection, cleaning)  
5. Processed data is stored in structured tables  
6. Data is loaded into BigQuery (analytics layer)  
7. Analytical queries generate insights  

---

## 🧠 Data Architecture

- Raw Layer → MySQL (incoming data)  
- Processed Layer → cleaned and structured data  
- Analytics Layer → BigQuery fact tables  

---

## 🔄 ETL Pipeline

- Extract: Delivery data from database and API  
- Transform: Calculate delivery duration, detect delays, clean data  
- Load: Store data into processed tables and BigQuery  

---

## 📊 Features

- End-to-end ETL pipeline  
- Delivery time calculation  
- Delay detection system  
- Data warehouse design using fact tables  
- Cloud-based analytics with BigQuery  
- PySpark pipeline simulation for scalability  

---

## 📁 Project Structure

smart_delivery/  
│── API_Server.py  
│── etl.py  
│── test_api.py  
│── requirements.txt  

---

## 🚀 Sample BigQuery Query

```sql
SELECT agent_id,
AVG(delivery_duration) AS avg_delivery_time
FROM `delivery-analytics-gcp.delivery_dataset.fact_deliveries`
GROUP BY agent_id;
```
---

💡 Key Learnings
Built a real-world ETL pipeline
Integrated local database with cloud warehouse
Understood data flow from ingestion to analytics
Gained hands-on experience with BigQuery and data processing

👩‍💻 Author
Sakshi Parve
Aspiring Data Engineer | Python | SQL | ETL | GCP
