from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
import numpy as np

x, y = make_classification(n_samples=1000, n_features=5, random_state=42)
x_labeled, x_unlabeled, y_labeled, y_unlabeled = train_test_split(
    x, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(x_labeled, y_labeled)

# perform self-training on unlabeled data
for _ in range(5):
    probs = model.predict_proba(x_unlabeled)[:, 1]
    high_confidence_indices = np.where((probs > 0.9) | (probs < 0.1))[0]

    x_labeled=np.vstack((x_labeled, x_unlabeled[high_confidence_indices]))
    y_labeled=np.hstack((y_labeled, (probs[high_confidence_indices] > 0.5).astype(int)))
    x_unlabeled = np.delete(x_unlabeled, high_confidence_indices, axis=0)

x_train, x_test, y_train, y_test = train_test_split(
    x_labeled, y_labeled, test_size=0.2, random_state=42
)

model.fit(x_train, y_train)
y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy after self-training: {accuracy:.4f}")