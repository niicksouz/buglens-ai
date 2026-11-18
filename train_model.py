import csv
import joblib
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


csv_path = Path(__file__).parent / "data" / "bug_reports.csv"

with csv_path.open(encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))

descriptions = [row["description"] for row in rows]
categories = [row["category"] for row in rows]

x_train, x_test, y_train, y_test = train_test_split(
    descriptions,
    categories,
    test_size=0.25,
    random_state=42,
    stratify=categories,
)

model = Pipeline(
    steps=[
        ("text_to_numbers", TfidfVectorizer()),
        ("classifier", LogisticRegression(max_iter=1000)),
    ]
)

model.fit(x_train, y_train)

predictions = model.predict(x_test)

print(f"Total de relatos: {len(descriptions)}")
print(f"Acurácia: {accuracy_score(y_test, predictions):.2f}")
print(classification_report(y_test, predictions, zero_division=0))

# Reajusta o modelo com todos os relatos para usá-lo na API
model.fit(descriptions, categories)

model_path = Path(__file__).parent / "buglens_model.joblib"
joblib.dump(model, model_path)

print(f"Modelo salvo em: {model_path.name}")