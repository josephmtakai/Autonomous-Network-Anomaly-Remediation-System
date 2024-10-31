import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load the data
data = pd.read_csv("network_traffic.csv")
X = data[['bytes_sent', 'packets']]
y = data['label']  # 1 for anomaly, 0 for normal

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train an Isolation Forest model
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
model.fit(X_train)

# Predict on test data
y_pred = model.predict(X_test)
y_pred = [1 if i == -1 else 0 for i in y_pred]  # Convert output to binary

# Evaluate model performance
print(classification_report(y_test, y_pred))
