import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import argparse
plt.style.use("seaborn-muted")
from utils.input_pipeline import load_data
from sklearn.manifold import TSNE
from sklearn.decomposition import IncrementalPCA
from sklearn.preprocessing import StandardScaler


parser = argparse.ArgumentParser()
parser.add_argument("--i",type=str,help="input file path to the data")
parser.add_argument("--f",type=str,help="input file path to the feature set")


args = parser.parse_args()

feature_set = pd.read_csv(args.f)
# hacked solution
feature_set = feature_set['0']

X,y = load_data(args.i,features_list=feature_set)

X = StandardScaler().fit_transform(X)

# preprocess the data using PCA, reduce by an order of magnitude
#X_pca = IncrementalPCA(n_components=int(np.floor(X.shape[1]/10))).fit_transform(X)

# Now run the TSNE algorithm

X_tsne = TSNE(n_components=2,perplexity=50, n_iter=250, init='pca', n_iter_without_progress=50).fit_transform(X)

# Visualize the results

plt.scatter(X_tsne[:,0],X_tsne[:,1],c=y.flatten())

plt.savefig("test_tsne.png")