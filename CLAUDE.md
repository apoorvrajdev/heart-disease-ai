# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Heart Disease AI is a cardiovascular risk prediction system. It consists of a reproducible training pipeline (Jupyter notebook) and a lightweight Streamlit inference app. The serving boundary loads a serialized XGBoost artifact and never executes training code paths.

## Common commands

```bash
# Setup
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

# Run the Streamlit inference app
streamlit run app.py
```

There is no test suite, linting configuration, or build system in this repository.

## Architecture

### Training / serving separation

- `heart_disease_training.ipynb` — Training, evaluation, and model serialization. This is exploratory and notebook-driven.
- `app.py` — Inference-only Streamlit entrypoint. It loads `heart_disease_model.pkl` via joblib and runs `predict` / `predict_proba`. It must not import training code.
- `heart_disease_model.pkl` — Immutable serialized artifact produced by the notebook. To update the model, rerun the notebook and commit the new `.pkl`.

### Feature schema contract

The model was trained on 12 features, explicitly dropping the `thal` column that exists in `data/heart.csv`:

```python
# From the notebook
x = df.iloc[:, :-2]   # drops last two columns: thal, target
```

`app.py` assembles the feature vector in this exact order:

```python
features = np.array(
    [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca]]
)
```

**If you modify feature engineering in the notebook, you must update the fixed feature order in `app.py` to match.** Using a dict-to-DataFrame coercion is discouraged because it introduces silent schema drift.

### Output design

The app surfaces `predict_proba` rather than binary labels. Risk is tiered as:
- `< 30%` — low risk (green)
- `30–60%` — moderate risk (yellow/orange)
- `> 60%` — high risk (red)

## File guide

- `app.py` — Streamlit UI, input validation, feature assembly, inference, Plotly visualizations.
- `heart_disease_training.ipynb` — Full ML pipeline: ingestion, cleaning, model comparison, tuning, cross-validation, serialization.
- `data/heart.csv` — Source UCI Heart Disease dataset (1025 rows, 14 columns).
- `requirements.txt` — Minimal dependency set: streamlit, scikit-learn, pandas, numpy, xgboost, joblib, plotly, matplotlib.

## Modeling context

- Algorithm: XGBoost gradient-boosted ensemble
- Best observed accuracy: 89.42%
- Training split: 65/35 (random_state=0)
- The notebook also evaluates KNN, SVM, Random Forest, and a Voting Ensemble for comparison.
