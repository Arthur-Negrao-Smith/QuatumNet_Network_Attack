import pandas as pd

class DataCollector:
    """
    Data collector to calculate simulations results

    Args:
        dataFrame (optional): DataFrame with all simulation data
    """
    def __init__(self, dataFrame: pd.DataFrame = None) -> None:
        self.df: pd.DataFrame = dataFrame
        self.standard_deviations: dict = {}

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
            self.df = pd.read_csv(path, encoding='utf-8')
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
            standard_deviations[column] = [variance ** 0.5]

        self.standard_deviations = standard_deviations

        return self.standard_deviations

    def save(
            self, 
            file_name: str, 
            save_standard_deviation: bool = None, 
            standard_columns: tuple = None
            ) -> None:
        """
        Will save all data from DataCollector on files

        Args:
            file_name (required): Name of the file to be saved (without .extension)
            save_standard_deviation (optional): If True, save the standard deviations
            standard_columns (optional): Columns of DataFrame to be save
        """
        # Checks for a DataFrame
        self.is_DataFrame(self.df)

        # Save DataFrame on csv file
        self.df.to_csv(f'{file_name}.csv', encoding='utf-8', header=True, index=True)

        if save_standard_deviation:
            standard_deviations = pd.DataFrame(self.standard_Deviation(*standard_columns))
            standard_deviations.to_csv(f'{file_name}_standard_deviations.csv', encoding='utf-8', header=True, index=False)
            
if __name__ == "__main__":
    a = {
        1:[1, 1],
        2:[2, 1]
    }

    dataCollector = DataCollector()
    dataCollector.get_DataFrame(a, convert=True)
    dataCollector.save('test', save_standard_deviation=True, standard_columns=(1, 2))


class DataGroup:
    def __init__(self):
        self._group: dict = dict()

    def __getitem__(self, key) -> tuple:
        return self._group[key]
    
    def __setitem__(self, key, value):
        self._group[key] = value
    
    def __len__(self) -> int:
        return len(self._group)

    def __str__(self) -> str:
        return f'{self._group}'
    
    def _isTuple(self, value) -> TypeError:
        if type(value) != tuple:
            raise TypeError("The given value is not a Tuple")
        
    def _isDataCollector(self, value) -> TypeError:
        if type(value) != DataCollector:
            raise TypeError("The given value is not a DataCollector")

    def add_Group(self, value: tuple, keygroup) -> dict:
        """
        The safest way to add a Tuple of DataCollectors
        """
        self._isTuple(value)
        
        self._group[keygroup] = value
        return self._group

    def add_Data(self, value: DataCollector, keygroup) -> dict:
        """
        The safest way to add a DataCollector
        """
        self._isDataCollector(value)

        if keygroup not in self._group.keys():
            self._group[keygroup] = (value,)
            return self._group
        
        self._group[keygroup] += (value,)
        return self._group

if __name__ == '__main__':
    a = DataGroup()
    a.add_Group((1, 2, 3), 1)
    print(a, a[1])
    a[1] = (1, 2, 4)
    print(a[1])
    dc = DataCollector(pd.DataFrame({1:[1, 2], 2:['a', 'b']}))
    a.add_Data(dc, 2)
    print(a)