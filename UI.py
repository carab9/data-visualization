from tkinter import ttk
import tkinter as tk
from Graph import Graph

class UI:
    blackboard = None

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Data Visualization")
        self.root.geometry('600x400')
        self.tabControl = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text ='XY Plot')
        self.tabControl.add(self.tab2, text ='Bar Chart')
        self.tabControl.add(self.tab3, text ='Linear Regression')
        self.tabControl.pack(expand = 1, fill ="both")

    def run(self, df, intercept, slope):
        g = Graph(df)
        g.display_xy_plot(self.tab1)
        g.display_bar_char(self.tab2)
        g.display_lin_reg(self.tab3, intercept, slope)
        self.root.mainloop()