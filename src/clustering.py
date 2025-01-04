from sklearn.cluster import KMeans

def perform_kmeans(scaled_features, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(scaled_features)
    return kmeans, labels
