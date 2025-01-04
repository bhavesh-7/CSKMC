import matplotlib.pyplot as plt
import seaborn as sns

def plot_elbow_method(inertia):
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, 11), inertia, marker='o')
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.show()

def plot_clusters(df, x_col, y_col, cluster_col):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x=df[x_col],
        y=df[y_col],
        hue=df[cluster_col],
        palette='viridis',
        s=100
    )
    plt.title('Customer Segmentation')
    plt.show()
