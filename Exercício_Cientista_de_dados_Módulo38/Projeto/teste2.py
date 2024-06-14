# %%

import pandas as pd
import streamlit as st
from pycaret.classification import *

# %%

df = pd.read_feather('.\input\credit_scoring.ftr')
df.drop(columns=['index', 'data_ref'], inplace=True)
data = df.sample(50000, random_state=123)
data_unseen = df.drop(data.index)

# %%

clf = setup(data=data,
            target='mau',
            session_id=123,
            numeric_imputation=-1)
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

plot_model(final_lightgbm, plot='auc')

# %%

save_model(final_lightgbm, 'Saved_LIGHTGBM')

# %%

plot_model(estimator=final_lightgbm, plot='confusion_matrix')

# %%

new_prediction = predict_model(final_lightgbm, data=data_unseen)
new_prediction

# %%

pred = pd.crosstab(new_prediction['mau'], new_prediction['prediction_label'])
pred['Diff'] = pred.diff(axis=1).iloc[:,1]
pred = pd.concat([pred, pred.diff().dropna().rename({True: 'Diff'})])
pred
# %%

pred_proba = pd.crosstab(new_prediction['mau'], new_prediction['prediction_label'], normalize=True)
pred_proba['Diff'] = pred_proba.diff(axis=1).iloc[:,1]
pred_proba = pd.concat([pred_proba, pred_proba.diff().dropna().rename({True: 'Diff'})]).style.format('{:.2%}')
pred_proba

# %%

final_lightgbm