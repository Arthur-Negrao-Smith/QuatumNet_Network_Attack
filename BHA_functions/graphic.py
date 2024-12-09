from .datacollector import DataCollector
import matplotlib.pyplot as plt
import numpy as np

class GraphicGenerator:
    """
    A graphic render to plot data

    Args:
        dataCollectors (required): Is a tuple with all DataCollector to be analyzed
    """
    def __init__(self, dataCollectors: tuple[DataCollector]) -> None:
        self.dataCollectors = dataCollectors

    def add_on_plot(self, plot_name: str, plot_label: str, x_column: tuple[float, float], y_column_name: str) -> None:
        """
        Will add data on plot selected

        Args:
            plot_name (required): Keyname of axis
            plot_label (required): Name of plot
            x_column (required): Tuple with initial value of x, step
            y_column_name (required): Name of y column on DataCollector
        """
        y_points = []
        for dataCollector in self.dataCollectors:
            dataCollector.standard_Deviation(y_column_name)
            y_points.append(dataCollector.standard_deviations[y_column_name])
        
        x_points = []
        temp_x = x_column[0]
        for i in range(0, len(y_points)):
            x_points.append(temp_x)
            temp_x += x_column[1]

        x_points = np.array(x_points)
        
        y_points = np.array(y_points)
        print('AQUI ESTÁ O PRINT', len(x_points), len(y_points))

        plt.plot(x_points, y_points, label=plot_label)

    def show_plot(self, plot_name: str, title: str, x_label: str, y_label: str) -> None:
        """
        Will show especific plot selected

        Args:
            plot_name (required): Keyname of axis
            title (required): Title of plot, if None will don't have title
            x_label (required): Label of x axis
            y_label (required): Label of y axis
        """
        if title != None:
            plt.title(title)
        
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        plt.show()