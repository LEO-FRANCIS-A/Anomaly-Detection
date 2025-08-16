# Anomaly-Detection
This project uses machine learning to detect unusual login activities based on user behavior patterns. Instead of blocking access, the system sends real-time alerts to the security team — ensuring legitimate but uncommon actions (e.g., travel, emergencies) are still permitted while being closely monitored.

The system is built with:

    --> Backend (ML model) → Isolation Forest (unsupervised anomaly detection).
    --> Frontend (Streamlit app) → Visualizes anomalies interactively.
    --> Email Notifications → Sends alerts + CSV reports of anomalies.
    --> Database (Postgres) → Stores anomalies for historical tracking.

# Workflow

User Login Events
           
    CSV input contains login records (IP address, timestamp, location, etc.).

Anomaly Detection

    The ML model (IsolationForest) learns normal login patterns.
    Assigns each login an anomaly score and an anomaly flag (0 = normal, 1 = anomaly).

Detected Anomalies are:

    Stored in PostgreSQL for persistence
    Emailed to security team (HTML + CSV report)
    Displayed in Streamlit with filtering & anomaly highlighting

# Tech Stack

    Python (Pandas, Scikit-learn, SQLAlchemy)
    Streamlit (frontend dashboard)
    PostgreSQL (cloud-hosted on Render)
    SMTP (Gmail for email alerts)
    Altair (visualizations)
