import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# --- Settings ---
CAMINHO_PLANILHA = "data/escolas.xlsx"          # Place your spreadsheet in the data/ folder
CAMINHO_SAIDA = "data/escolas_clusterizadas.xlsx"
N_CLUSTERS = 5
RANDOM_STATE = 42

# Load data
df = pd.read_excel(CAMINHO_PLANILHA)

# Select columns for clustering
COLUNAS_CATEGORICAS = ['porte']
COLUNAS_NUMERICAS = ['desempenho', 'IEF', 'media_mensalidade']
colunas_para_clusterizar = COLUNAS_CATEGORICAS + COLUNAS_NUMERICAS

X = df[colunas_para_clusterizar]

# Preprocessing:
# - One-Hot Encoding for the categorical variable 'porte'
# - Passthrough for already normalized numerical variables
preprocessador = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), COLUNAS_CATEGORICAS),
        ('num', 'passthrough', COLUNAS_NUMERICAS)
    ]
)

# Pipeline: preprocessing + K-Means
pipeline = Pipeline([
    ('preprocessador', preprocessador),
    ('kmeans', KMeans(n_clusters=N_CLUSTERS, random_state=RANDOM_STATE, n_init='auto'))
])

# Fit the model
pipeline.fit(X)

# Add cluster column to the original DataFrame
df['cluster'] = pipeline.named_steps['kmeans'].labels_

# Save spreadsheet with clusters
df.to_excel(CAMINHO_SAIDA, index=False)
print(f"Spreadsheet with clusters saved at: {CAMINHO_SAIDA}")

# --- Cluster interpretation ---
# Numerical variables: mean | Categorical variable: mode
cluster_summary = df.groupby('cluster').agg(
    porte=('porte', lambda x: x.mode().iloc[0]),   # Mode for categorical
    desempenho=('desempenho', 'mean'),
    IEF=('IEF', 'mean'),
    media_mensalidade=('media_mensalidade', 'mean')
).round(2)

print("\nCluster summary (k=5):")
print(cluster_summary)