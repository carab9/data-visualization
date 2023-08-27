from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graph:
    def __init__(self, df):
        self.data = df

    def display_xy_plot(self, tab):
        x = self.data['Co2'].to_numpy()
        y = self.data['SeaLevel'].to_numpy()

        fig = Figure(figsize=(8, 6), dpi=100)
        plot = fig.add_subplot()
        canvas = FigureCanvasTkAgg(fig, master=tab)

        # Plot the actual points as scatter plot
        plot.scatter(x, y, color="blue")

        # Plot the regression line
        plot.plot(x, y, '--', color="red")

        # Plot the labels
        plot.set_xlabel('CO2/Year')
        plot.set_ylabel('Rise/Year')
        plot.set_title('SeaLevel vs CO2')

        # Show plot
        canvas.draw()
        canvas.get_tk_widget().pack()

    def display_bar_char(self, tab):
        x = self.data['Co2'].to_numpy()
        y = self.data['SeaLevel'].to_numpy()

        fig = Figure(figsize=(8, 6), dpi=100)
        plot = fig.add_subplot()
        canvas = FigureCanvasTkAgg(fig, master=tab)
        plot.bar(x, y, color='blue', width=0.8)
        plot.grid(color='lightgrey', linestyle='--', linewidth=0.5, axis='y')

        plot.set_xlabel('CO2/Year')
        plot.set_ylabel('Rise/Year')
        plot.set_title('SeaLevel vs CO2')

        canvas.draw()
        canvas.get_tk_widget().pack()

    def display_lin_reg(self, tab, intercept, slope):
        print('Linear Regression result:')

        print('intercept:', intercept)
        print('slope:', slope)

        x = self.data['Co2'].to_numpy()
        y = self.data['SeaLevel'].to_numpy()

        fig = Figure(figsize=(8, 6), dpi=100)
        plot = fig.add_subplot()
        canvas = FigureCanvasTkAgg(fig, master=tab)

        plot.scatter(x, y, color="blue")
        y_pred = intercept + slope * x
        plot.plot(x, y_pred, color="green")

        plot.set_xlabel('CO2/Year')
        plot.set_ylabel('Rise/Year')
        plot.set_title('SeaLevel vs CO2')

        # Show plot
        canvas.draw()
        canvas.get_tk_widget().pack()