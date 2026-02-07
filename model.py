import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

MODEL_FILE = "model.pkl"

df = pd.read_csv("WineQuality.csv")
features = df.drop("quality", axis=1)
labels = df["quality"].copy()

x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

if not os.path.exists(MODEL_FILE):
    model = DecisionTreeRegressor(random_state=42)
    model.fit(x_train, y_train)

    joblib.dump(model, MODEL_FILE)
    print("Model trained and saved.")

else:
    model = joblib.load(MODEL_FILE)

    predictions = model.predict(x_test)

    x_test = x_test.copy()
    x_test["predicted_quality"] = predictions
    x_test["actual_quality"] = y_test.values
    x_test.to_csv("predictions.csv", index=False)

    print("Model loaded and predictions saved to predictions.csv.")