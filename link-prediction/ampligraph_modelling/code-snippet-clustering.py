import requests
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from adjustText import adjust_text
from ampligraph.datasets import load_from_csv
from ampligraph.latent_features import ComplEx
from ampligraph.discovery import find_clusters

model.fit(X)

df = pd.DataFrame(X, columns=["s", "p", "o"])
actors = np.unique(np.concatenate((df.s,
                                    df.o)))
actors

actor_embeddings = model.get_embeddings(actors, embedding_type='entity')

embeddings_2d = PCA(n_components=2).fit_transform(np.array([i for i in actor_embeddings]))

# Find clusters of embeddings using KMeans
kmeans = KMeans(n_clusters=10, n_init=100, max_iter=500)
clusters = find_clusters(actors, model, kmeans, mode='entity')

 # Plot results
df = pd.DataFrame({"actors": actors, "clusters": "cluster" + pd.Series(clusters).astype(str),
                  "embedding1": embeddings_2d[:, 0], "embedding2": embeddings_2d[:, 1]})

plt.figure(figsize=(20, 20))
plt.title("Cluster embeddings")

ax = sns.scatterplot(data=df, x="embedding1", y="embedding2", hue="clusters")

texts = []
for i, point in df.iterrows():
     if np.random.uniform() < 0.1:
         texts.append(plt.text(point['embedding1']+.02, point['embedding2'], str(point['actors'])))
adjust_text(texts)
