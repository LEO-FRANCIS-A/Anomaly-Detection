# ====== STEP 1: Install & Import ======
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from google.colab import files

# ====== STEP 2: Upload Your CSV ======
uploaded = files.upload()  # Choose your CSV file
filename = list(uploaded.keys())[0]  # Auto-get filename

# ====== STEP 3: Load Dataset ======
df = pd.read_csv(filename)

# ====== STEP 4: Feature Engineering ======
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.dayofweek

X = df.drop(columns=['timestamp', 'user_id'])

categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
numeric_cols = X.select_dtypes(exclude=['object']).columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols),
        ('num', StandardScaler(), numeric_cols)
    ]
)

# ====== STEP 5: Automatic Contamination Search ======
best_contamination = None
best_separation = -np.inf  # Higher is better

for contamination in np.linspace(0.01, 0.1, 10):  # Try 1% to 10%
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('isoforest', IsolationForest(
            n_estimators=100,
            contamination=contamination,
            random_state=42
        ))
    ])
    model.fit(X)
    scores = -model.named_steps['isoforest'].decision_function(
        model.named_steps['preprocessor'].transform(X)
    )
    # Separation metric: difference between top 5% and bottom 5% scores
    sep = np.percentile(scores, 95) - np.percentile(scores, 5)
    if sep > best_separation:
        best_separation = sep
        best_contamination = contamination
        best_model = model
        best_scores = scores

print(f"✅ Best contamination found: {best_contamination:.2%}")

# ====== STEP 6: Final Model & Output ======
preds = best_model.named_steps['isoforest'].predict(
    best_model.named_steps['preprocessor'].transform(X)
)
df['anomaly_flag'] = np.where(preds == -1, 1, 0)
df['anomaly_score'] = best_scores

# ====== STEP 7: Save & Download ======
output_filename = "dataset_with_anomalies.csv"
df.to_csv(output_filename, index=False)
files.download(output_filename)

# ====== STEP 8: Preview ======
df[['user_id', 'activity_type', 'anomaly_score', 'anomaly_flag']].head(10)
