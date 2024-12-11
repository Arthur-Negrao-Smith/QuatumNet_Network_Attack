from .datacollector import DataCollector
import matplotlib.pyplot as plt
import numpy as np

class GraphicGenerator:
    """
    A graphic render to plot data

    Args:
        dataCollectors (required): Is a tuple with all DataCollector to be analyzed
    """
    def __init__(self) -> None:
        self.dataCollectors: DataCollector = None

    def add_on_plot(self, plot_label: str, x_column: tuple[float, float], y_column_name: str, y_standard_deviation: bool, dc: tuple[DataCollector] = None) -> None:
        """
        Will add data on plot selected

        Args:
            plot_label (required): Name of plot
            x_column (required): Tuple with initial value of x, step
            y_column_name (required): Name of y column on DataCollector
            dataCollectors (required): Is a tuple with all DataCollector to be analyzed
        """
        y_points = []
        if dc:
            self.dataCollectors = dc

        for dataCollector in self.dataCollectors:
            dataCollector.standard_Deviation(y_column_name)
            if y_standard_deviation:
                y_points.append(dataCollector.standard_deviations[y_column_name])
            else:
                y_points.append(dataCollector.arithmetic_Mean(y_column_name)[y_column_name])

        x_points = []
        temp_x = x_column[0]
        for i in range(0, len(y_points)):
            x_points.append(temp_x)
            temp_x += x_column[1]

        x_points = np.array(x_points)
        y_points = np.array(y_points)

        plt.plot(x_points, y_points, label=plot_label)

    def show_plot(self, title: str, x_label: str, y_label: str) -> None:
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

        plt.legend()
        
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        plt.show()