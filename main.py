import warnings
warnings.filterwarnings("ignore")


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5.QtWidgets import *

import numpy as np
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.left = 50
        self.top = 50
        self.width = 1080
        self.height = 640
        self.title = "Clustering"

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

class PlowCanvas(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 100):
        self.fig = Figure(figsize=(width,height),dpi = dpi)

        FigureCanvas.__init__(self,self.fig)

    def plot(self, x,y,c,s, m = "."):

        self.ax = self.figure.add_subplot(111)
        self.ax.scatter(x,y,c= c, s = s, marker = m)
        self.ax.set_title("K-Means Clustering")
        self.ax.set_xlabel("Income")
        self.ax.set_ylabel("Number of Transaction")
        self.draw()

    def clear(self):
        self.fig.clf()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())