import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def load_and_prepare_datasets():
    path = "data/HLA_data.xlsx"
    df = pd.read_excel(path)
    df.columns = df.columns.str.strip().str.replace("\n", "")
    df["status"] = df["status"].replace({2:0})
    df["sex"] = df["sex"].replace({"male":1,"female":0})
    df = df.drop(columns=["ID","SAL"], errors="ignore")
    dfA = df.dropna()
    dfB = df.drop(columns=["C1","C2","DQB11","DQB12"], errors="ignore").dropna()
    def encode(df_):
        categorical = [c for c in df_.columns if c not in ["age","sex","status"]]
        enc = OneHotEncoder(sparse=False)
        Xc = enc.fit_transform(df_[categorical])
        import pandas as pd
        Xc = pd.DataFrame(Xc, columns=enc.get_feature_names_out(categorical))
        X = pd.concat([df_[["age","sex"]].reset_index(drop=True), Xc], axis=1)
        y = df_["status"].values
        return X, y
    return encode(dfA), encode(dfB)
