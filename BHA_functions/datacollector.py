import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class DataCollector:
    def __init__(self) -> None:
        self.df: pd.DataFrame = None

    def is_DataFrame(self, dataFrame: pd.DataFrame) -> bool:
        if type(dataFrame) == pd.DataFrame:
            return True
        return False

    def get_DataFrame(self, dataFrame: pd.DataFrame = None) -> None:
        if self.is_DataFrame(dataFrame):
            self.df = dataFrame
            return
        raise Exception("Não é um DataFrame")

    def get_DataFrame_csv(self, path: str) -> None:
        if type(path) == str:
            self.df = pd.read_csv(self.file, encoding='utf-8')
            return
        raise Exception("Não é um caminho válido")
    
    def arithmetic_Mean(self, *columns) -> dict:
        averages = {}
        for column in columns:
            averages[column] = self.df[column].sum() / len(self.df[column])
        return averages
    
    def standard_Deviation(self, *columns) -> dict:
        avareges = self.arithmetic_Mean(*columns)
        standard_deviations = {}
        for column in columns:
            variance = 0
            number_items = len(self.df[column])

            for item in self.df[column]:
                variance += (item - avareges[column])
            
            variance /= number_items
            standard_deviations[column] = variance ** 0.5

        return standard_deviations

    def save(self, file_name: str, save_standard_deviation: bool = None, columns: list = None) -> None:
        self.df.to_csv(F'{file_name}.csv', encoding='utf-8', header=True, index=True)

        if save_standard_deviation:
            standard_deviations = self.standard_Deviation(*columns)
            with open(f"{file_name}.txt", mode='+w', encoding='utf-8') as file:
                for column, standard_deviation in standard_deviations:
                    file.write(f"{column}:{standard_deviation}\n")





a = {
    1:['a'],
    2:['b']
}

df = pd.DataFrame(a)
graphic = DataCollector()
graphic.get_DataFrame(df)
graphic.save('test.csv')