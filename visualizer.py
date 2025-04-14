import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

class Visualizer:
    def __init__(self, grid):
        self.grid = grid
        self.rows, self.cols = grid.shape
        self.cmap = mcolors.ListedColormap(["white", "black", "yellow", "purple", "red", "green", "blue"])
        self.bounds = [-1.5, -0.5, 0.5, 2.5, 3.5, 4.5, 5.5, 6.5]
        self.norm = mcolors.BoundaryNorm(self.bounds, self.cmap.N)

    def plot_path(self, path, algorithm_name):
        if not path:
            print(f"No path found for {algorithm_name}")
            return

        fig, ax = plt.subplots(figsize=(6, 6))
        ax.imshow(self.grid, cmap=self.cmap, norm=self.norm, interpolation="nearest")

        # Add grid lines and labels
        ax.set_xticks(np.arange(self.cols + 1) - 0.5, minor=True)
        ax.set_yticks(np.arange(self.rows + 1) - 0.5, minor=True)
        ax.grid(which="minor", color="gray", linestyle='-', linewidth=1)
        ax.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False)

        # Plot the path
        if path:
            path_y, path_x = zip(*path)
            plt.plot(path_x, path_y, 'o-', color='cyan', linewidth=2, markersize=8)

        # Add legend
        legend_patches = [
            plt.Line2D([0], [0], marker='s', color='w', markerfacecolor="green", markersize=10, label="Start (S)"),
            plt.Line2D([0], [0], marker='s', color='w', markerfacecolor="blue", markersize=10, label="Goal (G)"),
            plt.Line2D([0], [0], marker='s', color='w', markerfacecolor="white", markersize=10, label="Walls (W)"),
            plt.Line2D([0], [0], marker='s', color='w', markerfacecolor="yellow", markersize=10, label="Quicksand (QS)"),
            plt.Line2D([0], [0], marker='s', color='w', markerfacecolor="purple", markersize=10, label="Portal (P)"),
            plt.Line2D([0], [0], marker='s', color='w', markerfacecolor="red", markersize=10, label="Wild Beasts (WB)"),
            plt.Line2D([0], [0], marker='o', color='cyan', label="Path")
        ]

        fig.legend(handles=legend_patches, loc="center left", fontsize="small", bbox_to_anchor=(1, 0.5))
        plt.title(f"Magical Forest Maze\n{algorithm_name} Path", pad=20)
        plt.tight_layout()
        plt.show()

    def plot_performance_comparison(self, results):
        metrics = ['time', 'memory', 'nodes_expanded']
        algorithms = list(results.keys())
        
        fig, axes = plt.subplots(3, 1, figsize=(10, 12))
        
        for idx, metric in enumerate(metrics):
            values = [results[alg][metric] for alg in algorithms]
            axes[idx].bar(algorithms, values, color='skyblue')
            axes[idx].set_title(f'{metric.replace("_", " ").title()}')
            axes[idx].tick_params(axis='x', rotation=45)
            axes[idx].grid(True, linestyle='--', alpha=0.7)
        
        plt.tight_layout()
        plt.show()
