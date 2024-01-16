import pandas as pd
from plot_drawer import PlotDrawer

json_file = "file.json"
data_frame = pd.read_json(json_file)

drawer = PlotDrawer()

comparison_paths = drawer.draw_comparison_plot(data_frame)
print("Comparison Plot saved at:", comparison_paths)

statistics_paths = drawer.calculate_and_draw_statistics(data_frame)
print("Statistics and Comparison Plot saved at:", statistics_paths)

deviation_paths = drawer.draw_deviation_plot(data_frame)
print("Deviation Plot saved at:", deviation_paths)




if __name__ == '__main__':
    pass


