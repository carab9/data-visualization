import re
import numpy as np
import pandas as pd


class FileIO():
    def __init__(self):
        pass

    @staticmethod
    def read_html(html_file):
        df = None
        count = 0
        try:
            infile = open(html_file, "r")
            for line in infile:
                line = line.strip()
                # Skip empty line
                if line:
                    # Skip Table header/footer
                    # Skip comments
                    if re.search(r'<TBODY><TR><TD># ', line):
                        count +=1
                        continue
                    elif count:
                        # First non-comment line (a header line)
                        break
            # Strip out HTML syntax
            print(count)
            ds = pd.read_html(html_file, header=count)
            df = ds[0]
        except IOError as err:
            print("Error:", str(err))
            raise RuntimeError from err
        else:
            infile.close()
        return df

    @staticmethod
    def read_csv(csv_file):
        df = None
        # Use try/except to catch file open failure
        try:
            df = pd.read_csv(csv_file, delimiter=',', comment='#',
                             skip_blank_lines=True)
        except IOError as exc:
            print("Error:", str(exc))
            raise RuntimeError from exc
        return df