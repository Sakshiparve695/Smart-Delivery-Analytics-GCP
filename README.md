# 🚚 Smart Delivery Analytics System (GCP + BigQuery)

## 📌 Overview
This project is an end-to-end data pipeline that processes delivery data using Python, stores it in MySQL, and performs analytics using Google BigQuery.

---

## ⚙️ Tech Stack
- Python
- MySQL
- Google BigQuery
- REST API (Flask)
- Git & GitHub

---

## 🔄 Workflow
1. API generates delivery data
2. Data stored in MySQL database
3. ETL pipeline processes data
4. Transformed data loaded into BigQuery
5. Analytical queries performed for insights

---

## 📊 Features
- Delivery time calculation
- Delay detection system
- Average delivery time analysis
- Cloud-based data warehousing

---

## 📁 Project Structure
smart_delivery/
│── API_Server.py
│── etl.py
│── test_api.py
│── requirements.txt

---

## 🚀 Sample Query (BigQuery)
```sql
SELECT agent_id,
AVG(delivery_duration) AS avg_delivery_time
FROM `delivery-analytics-gcp.delivery_dataset.fact_deliveries`
GROUP BY agent_id;
```

---

💡 Key Learnings
Built real-world ETL pipeline
Integrated local DB with cloud warehouse
Hands-on with BigQuery analytics

---

