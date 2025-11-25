from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

def train_all_models(dataset, label="Dataset"):
    X, y = dataset
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    models = {
        "GaussianNB": GaussianNB(),
        "BernoulliNB": BernoulliNB(),
        "GradientBoosting": GradientBoostingClassifier(),
        "RandomForest": RandomForestClassifier()
    }
    print(f"=== Results for {label} ===")
    for name, clf in models.items():
        print(f"--- {name} ---")
        clf.fit(Xtr, ytr)
        preds = clf.predict(Xte)
        print(classification_report(yte, preds))
        print(confusion_matrix(yte, preds))
