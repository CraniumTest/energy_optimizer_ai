import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

class EnergyDataSimulator:
    def __init__(self, num_devices=5, days=30):
        self.num_devices = num_devices
        self.days = days

    def generate_data(self):
        np.random.seed(42)
        data = np.random.randint(50, 500, size=(self.days, self.num_devices))
        dates = pd.date_range(end=pd.Timestamp.today(), periods=self.days)
        df = pd.DataFrame(data, columns=[f'Device_{i+1}' for i in range(self.num_devices)], index=dates)
        return df

class EnergyOptimizerAI:
    def __init__(self, data):
        self.data = data

    def analyze_energy_usage(self):
        self.daily_totals = self.data.sum(axis=1)
        print("Daily Energy Usage (kWh):")
        print(self.daily_totals)
        return self.daily_totals

    def cluster_energy_data(self):
        model = KMeans(n_clusters=3)
        self.data['Cluster'] = model.fit_predict(self.data)
        print("\nClustered Energy Data:")
        print(self.data)
        self.plot_clusters()
        
    def plot_clusters(self):
        plt.figure(figsize=(10, 6))
        for cluster in sorted(self.data['Cluster'].unique()):
            cluster_data = self.data[self.data['Cluster'] == cluster]
            plt.plot(cluster_data.index, cluster_data.drop(columns='Cluster').sum(axis=1), label=f'Cluster {cluster}')
        plt.xlabel('Date')
        plt.ylabel('Total Energy Usage (kWh)')
        plt.title('Energy Usage Clustering')
        plt.legend()
        plt.show()

    def generate_recommendations(self):
        recommendations = []
        large_consumption_days = self.daily_totals.nlargest(5).index
        recommendations.append(f"Consider reducing usage on these high consumption days: {large_consumption_days}")

        # Further analysis and recommendations can be expanded here.
        print("\nRecommendations:")
        for rec in recommendations:
            print(rec)
        return recommendations


if __name__ == "__main__":
    # Simulating IoT Data
    simulator = EnergyDataSimulator()
    energy_data = simulator.generate_data()

    # Energy Optimizer AI
    optimizer = EnergyOptimizerAI(energy_data)
    optimizer.analyze_energy_usage()
    optimizer.cluster_energy_data()
    optimizer.generate_recommendations()
