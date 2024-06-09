# %%

import pandas as pd
import streamlit as st
from pycaret.classification import *

# %%

df = pd.read_feather('.\EBAC-Exercicios\Exercício_Cientista_de_dados_Módulo38\Projeto\input\credit_scoring.ftr')
data = df
# %%

clf = setup(data=data,
            target='mau',
            session_id=123,
            numeric_imputation=-1,
            normalize=True,
            normalize_method='maxabs',
            remove_outliers=True,
            fix_imbalance=True)
# %%

lightgbm = create_model(estimator='lightgbm', fold=5)

# %%

tuned_lightgbm = tune_model(estimator=lightgbm, fold=5, optimize='Precision')

# %%

plot_model(tuned_lightgbm, plot='auc')

# %%

final_lightgbm = finalize_model(tuned_lightgbm)

# %%

evaluate_model(final_lightgbm)
# %%

plot_model(estimator=tuned_lightgbm, plot='confusion_matrix')
# %%
