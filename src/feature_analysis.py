import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier

def run_feature_analysis(dataset):
    X, y = dataset
    model = GradientBoostingClassifier().fit(X,y)
    explainer = shap.Explainer(model)
    sv = explainer(X)
    shap.summary_plot(sv, X, show=False)
    plt.savefig("shap_summary.png")
