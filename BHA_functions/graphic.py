from datacollector import DataCollector
import matplotlib.pyplot as plt
import numpy as np

class Graphic:
    def __init__(self, dataCollectors: list[DataCollector]) -> None:
        self.dataCollectors = dataCollectors

    def show(self, title: str, plot_labels: list[str], x_label: str, x_column: str, y_label: str, y_column: str):
        fig, ax = plt.subplots()
        for i, dataCollector in enumerate(self.dataCollectors):
            x_points = np.array(dataCollector.standard_deviations[x_column])
            y_points = np.array(dataCollector.standard_deviations[y_column])
            ax.plot(x_points, y_points, label=plot_labels[i])

        if title != None:
            ax.set_title(title)
        
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)

        plt.show()