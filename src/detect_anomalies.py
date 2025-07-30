import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Load data
df = pd.read_csv("data/simulated_network_logs.csv")

# Train model
clf = IsolationForest(contamination=0.05, random_state=42)
clf.fit(df[["bytes_sent", "duration"]])

# Predict anomalies
df["anomaly_score"] = clf.decision_function(df[["bytes_sent", "duration"]])
df["is_anomaly"] = clf.predict(df[["bytes_sent", "duration"]])
df["is_anomaly"] = df["is_anomaly"].map({1: 0, -1: 1})

# Save plot
plt.figure()
normal = df[df["is_anomaly"] == 0]
anomalies = df[df["is_anomaly"] == 1]
plt.scatter(normal["bytes_sent"], normal["duration"], c="blue", label="Normal")
plt.scatter(anomalies["bytes_sent"], anomalies["duration"], c="red", label="Anomalies")
plt.xlabel("Bytes sent")
plt.ylabel("Duration")
plt.title("Détection d’anomalies réseau avec Isolation Forest")
plt.legend()
plt.savefig("images/anomaly_detection_plot.png")
print("✅ Graphe enregistré dans images/anomaly_detection_plot.png")