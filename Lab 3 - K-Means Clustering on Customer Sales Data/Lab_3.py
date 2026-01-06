import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os

# Step 1: Load Data
print("Reading Lab_3_Data.txt...")
df = pd.read_csv('Lab_3_Data.txt')  # comma-separated
print("Data loaded:")
print(df.head())

# Step 2: Preprocessing
X = df[['Sales', 'Profit']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Elbow Method
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot Elbow and Save
print("Saving elbow plot...")
fig1, ax1 = plt.subplots(figsize=(8, 5))
ax1.plot(range(1, 11), wcss, marker='o', linestyle='--')
ax1.set_xlabel('Number of Clusters (k)')
ax1.set_ylabel('WCSS')
ax1.set_title('Elbow Method for Optimal K')
fig1.savefig('elbow_plot.png')  # save the specific figure object
plt.show()
plt.close(fig1)
print("Elbow plot saved as elbow_plot.png")

# Step 4: KMeans with k=3
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)
print("Cluster counts:\n", df['Cluster'].value_counts())

# Plot Clusters and Save
print("Saving cluster plot...")
fig2, ax2 = plt.subplots(figsize=(10, 6))
colors = ['red', 'blue', 'green']
for i in range(3):
    ax2.scatter(df[df['Cluster'] == i]['Sales'],
                df[df['Cluster'] == i]['Profit'],
                label=f'Cluster {i}',
                color=colors[i],
                edgecolors='k',
                alpha=0.6)

# Inverse scale the cluster centers
centroids = scaler.inverse_transform(kmeans.cluster_centers_)
ax2.scatter(centroids[:, 0], centroids[:, 1],
            s=300, c='yellow', marker='X', label='Centroids')

ax2.set_xlabel('Sales')
ax2.set_ylabel('Profit')
ax2.set_title('Customer Segmentation based on Sales and Profit')
ax2.legend()
fig2.savefig('cluster_plot.png')  # <-- Save this figure
plt.show()
plt.close(fig2)

print("Cluster plot saved as cluster_plot.png")

# Step 5: Save CSV
df.to_csv('Lab_3_output.txt', sep=',', index=False)
print("Clustered data saved to Lab_3_output.txt")

# Show where it's saved
print("All done. Current directory:", os.getcwd())
