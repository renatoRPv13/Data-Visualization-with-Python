import pandas as pd

from common.paths import EXPERIMENT_DATASET_PATH

pd.options.mode.copy_on_write = True


def read() -> pd.DataFrame:
    return pd.read_csv(EXPERIMENT_DATASET_PATH)


def preprocess(data=None):
    # 1. Cria uma cópia para evitar o aviso SettingWithCopyWarning
    df = data.copy()

    # 2. Remove rows where 'x', 'approximated_y', or 'y' are missing
    df = df.dropna(subset=["x", "approximated_y", "y"])

    return df
