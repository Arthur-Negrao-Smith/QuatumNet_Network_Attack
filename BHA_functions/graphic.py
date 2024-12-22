from .datacollector import DataCollector
import matplotlib.pyplot as plt
import numpy as np

class GraphicGenerator:
    """
    A graphic render to plot data
    """
    def __init__(self) -> None:
        self.dataCollectors: tuple[DataCollector]

    def add_on_plot(
        self, plot_label: str, 
        x_column: tuple[float, float], 
        y_column_name: str, 
        y_standard_deviation: bool, 
        dc: tuple[DataCollector], 
        default_diff: DataCollector | None = None) -> None:
        """
        Will add data on plot selected

        Args:
            plot_label (required): Name of plot
            x_column (required): Tuple with initial value of x, step
            y_column_name (required): Name of y column on DataCollector
            dataCollectors (required): Is a tuple with all DataCollector to be analyzed
            y_standard_deviation (optional): If True, the standard deviation will be used
            dc (required): Tuple with all DataCollectors
            default_diff (optional): Pass the network without black holes to compare, if None don't affect the result
        """
        y_points = []
        if dc:
            self.dataCollectors = dc

        default_arithmetic_mean = 0 if default_diff == None else default_diff.arithmetic_Mean(y_column_name)[y_column_name]
        for dataCollector in self.dataCollectors:
            dataCollector.standard_Deviation(y_column_name)
            if not y_standard_deviation:
                arithmetic_mean = dataCollector.arithmetic_Mean(y_column_name)[y_column_name]
                y_points.append(default_arithmetic_mean - arithmetic_mean)
                continue

            y_points.append(dataCollector.standard_deviations[y_column_name])

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