import numpy as np

class Loading():
    def __init__(self):
        self.path: str
    
    def read_csv(self, file:str):
        """Return the data from the csv file"""
        self.file:str = file
        return np.loadtxt(self.file, skiprows=4, delimiter=",", encoding="utf-8")[:, 1:]
    