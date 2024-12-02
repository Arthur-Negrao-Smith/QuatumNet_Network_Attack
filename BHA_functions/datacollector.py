import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class DataCollector:
    """
    Data collector to calculate simulations results

    Args:
        dataFrame (optional): DataFrame with all simulation data
    """
    def __init__(self, dataFrame: pd.DataFrame = None) -> None:
        self.df: pd.DataFrame = dataFrame

    def is_DataFrame(
            self, 
            dataFrame: pd.DataFrame
            ) -> Exception:
        """
        Find out if it is a DataFrame

        Args:
            dataFrame (required): DataFrame to be analyzed

        Returns:
            Exception: If isn't DataFrame return a Exception, else, return None
        """
        if type(dataFrame) != pd.DataFrame:
            raise Exception("O valor dado não é um DataFrame")

    def get_DataFrame(
            self, 
            dataFrame: pd.DataFrame = None, 
            convert: bool = None
            ) -> None:
        """
        Get a DataFrame to DataCollector

        Args:
            dataFrame (required): DataFrame or Dict to add on DataCollector
            convert (optional): If is True convert dict to DataFrame
        """
        if convert:
            dataFrame = pd.DataFrame(dataFrame)
        
        # Checks for a DataFrame
        self.is_DataFrame(dataFrame)
        # Save DataFrame
        self.df = dataFrame

    def get_DataFrame_csv(self, path: str) -> None:
        """
        Get a DataFrame from a csv file

        Args:
            path (required): Path to csv file
        """
        # Checks if is a valid path
        if type(path) == str:
            self.df = pd.read_csv(self.file, encoding='utf-8')
            return
        raise Exception("Não é um caminho válido")
    
    def arithmetic_Mean(self, *columns) -> dict:
        """
        Will calculate the arithmetic mean from columns of DataFrame

        Args:
            *columns (required): Columns of DataFrame

        Returns:
            dict: Dict with all arithmetic means
        """
        # Checks for a DataFrame
        self.is_DataFrame(self.df)

        averages = {}
        for column in columns:
            averages[column] = self.df[column].sum() / len(self.df[column])
        return averages
    
    def standard_Deviation(self, *columns) -> dict:
        """
        Will calculate standard deviations from columns of DataFrame

        Args:
            *columns (required): Columns of DataFrame

        Returns:
            dict: Dict with all standard deviatons
        """
        # Checks for a DataFrame
        self.is_DataFrame(self.df)

        avareges = self.arithmetic_Mean(*columns)
        standard_deviations = {}
        for column in columns:
            variance = 0
            # Used to divide
            number_items = len(self.df[column])

            # Sum all (Xi - u)^2
            for item in self.df[column]:
                variance += (item - avareges[column]) ** 2
            
            variance /= number_items
            # Square root of variance
            standard_deviations[column] = variance ** 0.5

        return standard_deviations

    def save(
            self, 
            file_name: str, 
            save_standard_deviation: bool = None, 
            standard_columns: list = None
            ) -> None:
        """
        Will save all data from DataCollector on files

        Args:
            file_name (required): Name of the file to be saved
            save_standard_deviation (optional): If True, save the standard deviations
            standard_columns (optional): Columns of DataFrame to be save
        """
        # Checks for a DataFrame
        self.is_DataFrame(self.df)

        # Save DataFrame on csv file
        self.df.to_csv(F'{file_name}.csv', encoding='utf-8', header=True, index=True)

        if save_standard_deviation:
            standard_deviations = self.standard_Deviation(*standard_columns)
            with open(f"{file_name}_standard_deviations.txt", mode='+w', encoding='utf-8') as file:
                for column, standard_deviation in standard_deviations.items():
                    file.write(f"{column}:{standard_deviation}\n")


if __name__ == "__main__":
    a = {
        1:[1, 1],
        2:[2, 1]
    }

    dataCollector = DataCollector()
    dataCollector.get_DataFrame(a, convert=True)
    dataCollector.save('test.csv', save_standard_deviation=True, standard_columns=[1, 2])