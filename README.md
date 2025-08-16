# Anomaly-Detection
This machine learning model detects and notifies the security team whenever a login activity significantly deviates from the user’s historical behavior. Unlike the risk score model, this system does not block access — it only sends alerts, ensuring that legitimate but unusual actions (e.g., emergencies, travel) are still permitted.

The system is built with:

    --> Backend (ML model) → Isolation Forest (unsupervised anomaly detection).
    --> Frontend (Streamlit app) → Visualizes anomalies interactively.
    --> Email Notifications → Sends alerts + CSV reports of anomalies.
    --> Database (Postgres) → Stores anomalies for historical tracking.
