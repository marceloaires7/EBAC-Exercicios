# %%

import pandas as pd
import streamlit as st
from pycaret.classification import *

# %%

df = pd.read_feather('.\input\credit_scoring.ftr')
df.drop(columns=['index', 'data_ref'], inplace=True)
data = df.sample(50000, random_state=123)
data_unseen = df.drop(data.index)
data
# %%

clf = setup(data=data,
            target='mau',
            session_id=123,
            numeric_imputation=-1,
            pca=True,
            pca_method='linear',
            normalize=True,
            normalize_method='robust',
            remove_outliers=True,
            fix_imbalance=True,
            fix_imbalance_method='TomekLinks')
# %%

lightgbm = create_model(estimator='lightgbm', fold=5)

# %%

tuned_lightgbm = tune_model(estimator=lightgbm, fold=5, optimize='MCC')

# %%

plot_model(tuned_lightgbm, plot='auc')

# %%

plot_model(estimator=tuned_lightgbm, plot='confusion_matrix')

# %%

final_lightgbm = finalize_model(tuned_lightgbm)

# %%

evaluate_model(final_lightgbm)

# %%

new_prediction = predict_model(final_lightgbm, data=data_unseen)
new_prediction

# %%

pd.crosstab(new_prediction['mau'], new_prediction['prediction_label'])
# %%
