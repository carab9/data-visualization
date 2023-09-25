# Data Visualization

This project is a data processing, analysis, and visualization program. The purpose of this project is to analyze the correlation between sea level rise and CO2 levels by year, between 1992 and 2019. Two data files are provided to the program, a CSV file containing sea level data and an HTML file containing CO2 data. The program parses and processes the data, stores it into the database, and then retrieves the data from the database and analyzes it. The output of the program is three graphs. The relationship between sea level rise and CO2 levels is analyzed via linear regression, as well as an xy-plot and a bar chart. These graphs can be accessed via different tabs in the user interface.

## Architecture

My code has an architecture with 3 layers: a UI layer that contains components required to enable user interaction with the application; a Business Layer that processes the input data; and a Data Layer that controls access logic components to access the data.

![image](https://github.com/carab9/data-visualization/blob/main/architecture.png?raw=true)


The UI layer consists of the UI and Graph classes. The Graph Class creates and displays three different graphs. The UI class creates the interface that the user interacts with: the main window and the tabs.

The Business layer consists of the FileIO, Database, and RunLR classes. The FileIO class extracts the necessary data from the csv and html files. The Database class processes the data, including consolidating the data into annual values. The processed CO2 and sea level data are then joined by common year, and this consolidated data is stored into the database. The RunLR class performs a linear regression between the sea level data and the CO2 data, and calculates the intercept and slope required to draw the linear regression line.

The Data layer consists of the SqliteDB class, which provides the SQL APIs to create, store and access the SQLite database 

## Requirements

Python
Python Libraries: numpy, pandas, re, sqlite3, matplotlib.figure, matplotlib.backends.backend_tkagg, tkinter.
Run the program: python main.py

## Technical Skills

Regular expression and pandas dataframe for data processing, SQLite for database, matplotlib Figure and FigureCanvasTkAgg for plotting graphs. Tkinter for GUIs.

## Results


This chart shows a scatterplot displaying sea level rise vs CO2 levels based on yearly data.

![image](https://github.com/carab9/data-visualization/blob/main/sealevel_co2_scatterplot.png?raw=true)

This barchart shows sea level rise vs CO2 levels. Each bar is one year.

![image](https://github.com/carab9/data-visualization/blob/main/sealevel_co2_barchart.png)

This chart shows the linear regression between sea level rise and CO2 levels, displayed alongside a scatter plot.

![image](https://github.com/carab9/data-visualization/blob/main/sealevel_co2_linreg.png?raw=true)

