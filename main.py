from src.data_preprocessing import load_and_prepare_datasets
from src.model_training import train_all_models
from src.feature_analysis import run_feature_analysis

def main():
    print("Running pipeline...")
    dfA, dfB = load_and_prepare_datasets()
    train_all_models(dfA, label="Dataset A")
    train_all_models(dfB, label="Dataset B")
    run_feature_analysis(dfA)

if __name__ == "__main__":
    main()
