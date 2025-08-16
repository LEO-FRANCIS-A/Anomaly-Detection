# Anomaly-Detection
This project uses machine learning to detect unusual login activities based on user behavior patterns. Instead of blocking access, the system sends real-time alerts to the security team — ensuring legitimate but uncommon actions (e.g., travel, emergencies) are still permitted while being closely monitored.

The system is built with:

    --> Backend (ML model) → Isolation Forest (unsupervised anomaly detection).
    --> Frontend (Streamlit app) → Visualizes anomalies interactively.
    --> Email Notifications → Sends alerts + CSV reports of anomalies.
    --> Database (Postgres) → Stores anomalies for historical tracking.
