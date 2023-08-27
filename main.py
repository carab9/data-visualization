import sys
import os
from Database import Database
from RunLR import RunLR
from UI import UI



def main():

    db = Database()
    db.build("Co2.html", "SeaLevel.csv")
    df = db.get_Co2_sealevel_db()

    lr = RunLR()
    lr.run(df)

    ui = UI()
    ui.run(df, lr.get_intercept(), lr.get_slope())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
