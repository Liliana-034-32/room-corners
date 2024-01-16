import pandas as pd
import matplotlib.pyplot as plt
import os

class PlotDrawer():
    def draw_plots(self, data):
        if isinstance(data, str):
            data_frame = pd.read_json(data)
        elif isinstance(data, pd.DataFrame):
            data_frame = data
        else:
            raise ValueError("Invalid input. Provide either a JSON file path or a pandas DataFrame.")

        return [plot_path]

    def draw_comparison_plot(self, data):
        if isinstance(data, str):
            data_frame = pd.read_json(data)
        elif isinstance(data, pd.DataFrame):
            data_frame = data
        else:
            raise ValueError("Invalid input. Provide either a JSON file path or a pandas DataFrame.")

        plt.figure(figsize=(12, 6))
        plt.bar(data_frame.index, data_frame['gt_corners'], label='Ground Truth', color='blue')
        plt.bar(data_frame.index, data_frame['rb_corners'], label='Predicted Corners', alpha=0.7, color='orange')
        plt.xlabel('Room Index')
        plt.ylabel('Number of Corners')
        plt.title('Comparison of Ground Truth and Predicted Corners')
        plt.legend()

        os.makedirs("plots", exist_ok=True)
        plot_path = f"plots/comparison_plot.png"
        plt.savefig(plot_path)

        plt.show()

        return [plot_path]

    def draw_deviation_plot(self, data):
        if isinstance(data, str):
            data_frame = pd.read_json(data)
        elif isinstance(data, pd.DataFrame):
            data_frame = data
        else:
            raise ValueError("Invalid input. Provide either a JSON file path or a pandas DataFrame.")

        plt.figure(figsize=(12, 6))
        plt.plot(data_frame.index, data_frame['mean'], label='Mean Deviation', marker='o')
        plt.plot(data_frame.index, data_frame['max'], label='Max Deviation', marker='o')
        plt.plot(data_frame.index, data_frame['min'], label='Min Deviation', marker='o')
        plt.xlabel('Room Index')
        plt.ylabel('Deviation (degrees)')
        plt.title('Deviation Statistics')
        plt.legend()

        os.makedirs("plots", exist_ok=True)
        plot_path = f"plots/deviation_plot.png"
        plt.savefig(plot_path)

        plt.show()

        return [plot_path]
    
    
    def calculate_and_draw_statistics(self, data):
        if isinstance(data, str):
            data_frame = pd.read_json(data)
        elif isinstance(data, pd.DataFrame):
            data_frame = data
        else:
            raise ValueError("Invalid input. Provide either a JSON file path or a pandas DataFrame.")

        plt.figure(figsize=(12, 6))
        plt.bar(data_frame.index, data_frame['gt_corners'], label='Ground Truth', alpha=0.9, color='blue')
        plt.bar(data_frame.index, data_frame['rb_corners'], label='Predicted Corners', alpha=0.7, color='orange') 
        plt.xlabel('Room Index')
        plt.ylabel('Number of Corners')
        plt.title('Comparison of Ground Truth and Predicted Corners')
        plt.legend()

        os.makedirs("plots", exist_ok=True)
        plot_path = f"plots/comparison_plot.png"
        plt.savefig(plot_path)

        gt_mean = data_frame['gt_corners'].mean()
        gt_max = data_frame['gt_corners'].max()
        rb_mean = data_frame['rb_corners'].mean()
        rb_max = data_frame['rb_corners'].max()

        print(f"Ground Truth Mean: {gt_mean}")
        print(f"Ground Truth Max: {gt_max}")
        print(f"Predicted Corners Mean: {rb_mean}")
        print(f"Predicted Corners Max: {rb_max}")

        plt.show()

        return [plot_path]


    
if __name__ == "__main__":
    pass