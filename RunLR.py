class RunLR:
    def __init__(self):
        self.slope = 0.0
        self.intercept = 0.0

    def run(self, df):
        sumx = 0.0
        sumy = 0.0
        sumxy = 0.0
        sumx2 = 0.0
        sumy2 = 0.0
        for index, row in df.iterrows():
            x = row['Co2']
            y = row['SeaLevel']
            sumx += x
            sumy += y
            sumxy += x * y
            sumx2 += x * x
            sumy2 += y * y

        n = len(df)
        a = (sumy * sumx2 - sumx * sumxy) / (n * sumx2 - sumx * sumx)
        b = (n * sumxy - sumx * sumy) / (n * sumx2 - sumx * sumx)

        self.intercept = a
        self.slope = b

        print("Calculated LR results:")
        print('intercept:', self.intercept)
        print('slope:', self.slope)

    def get_slope(self):
        return self.slope

    def get_intercept(self):
        return self.intercept