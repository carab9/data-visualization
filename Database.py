import re
import numpy as np
import pandas as pd
from SqliteDB import SqliteDB
from FileIO import FileIO

class Database():
    def __init__(self):
        self.db = SqliteDB()
        self.db.connect("CIS41b")
        self.db.createTable()

    def _create_co2_df(self, co2_data):
        co2_dict = {}
        try:
            # Store monthly Co2 data for the same year in a list
            for index, row in co2_data.iterrows():
                year = int(row['year'])
                avg = float(row['average'])
                if not (year in co2_dict.keys()):
                    co2_dict[year] = []
                co2_dict[year].append(avg)
        except ValueError as exc:
            print("Error:", str(exc))
            raise RuntimeError from exc

        co2_df = pd.DataFrame(columns=['Year', 'Co2'])
        for key, value in co2_dict.items():
            avg = 0.0
            if len(value):
                avg = sum(value) / len(value)
            co2_df.loc[len(co2_df.index)] = [key, avg]

        return co2_df

    def _create_sealevel_df(self, sealevel_data):
        sea_dict = {}
        keys = list(sealevel_data.keys())
        keys.remove('year')

        # Use try/except to catch list access error
        # or int or float conversion errors
        try:
            for index, row in sealevel_data.iterrows():
                year = row['year']
                m = re.search(r'(\d+)\.(\d*)', str(year))
                if m:
                    found = int(m.group(1))
                    if not (found in sea_dict.keys()):
                        sea_dict[found] = []
                    for k in keys:
                        v = row[k]
                        if not np.isnan(v):
                            sea_dict[found].append(v)
        except ValueError as exc:
            print("Error:", str(exc))
            raise RuntimeError from exc

        sea_df = pd.DataFrame(columns=['Year', 'SeaLevel'])
        for key, value in sea_dict.items():
            avg = 0.0
            if len(value):
                # Compute the average of Sea Level values for a year
                avg = sum(value) / len(value)
            # Add a new row to the end of DataFrame
            sea_df.loc[len(sea_df.index)] = [key, avg]

        return sea_df

    def build(self, co2_file, sealevel_file):
        co2_data = FileIO.read_html(co2_file)
        html = co2_data.to_html(index=False)
        data_t = (1, "CO2", html)
        self.db.insert(data_t)
        co2_df = self._create_co2_df(co2_data)
        print(co2_df)

        sealevel_data = FileIO.read_csv(sealevel_file)
        html = sealevel_data.to_html(index=False)
        data_t = (2, "SeaLevel", html)
        self.db.insert(data_t)
        sealevel_df = self._create_sealevel_df(sealevel_data)
        print(sealevel_df)

        new_df = sealevel_df.join(co2_df.set_index('Year'), how = 'inner', on = 'Year')
        html = new_df.to_html(index=False)
        data_t = (3, "SeaLevel vs CO2", html)
        self.db.insert(data_t)
        print(new_df)



    def get_Co2_db(self):
        rec = self.db.search("CO2")
        df = pd.read_html(rec[0][2])[0]
        return df

    # Get Sea Level data
    def get_sealevel_db(self):
        rec = self.db.search("SeaLevel")
        df = pd.read_html(rec[0][2])[0]
        return df

    # Get Co2 vs Sea Level data
    def get_Co2_sealevel_db(self):
        rec = self.db.search("SeaLevel vs CO2")
        print(rec)
        df = pd.read_html(rec[0][2])[0]
        return df