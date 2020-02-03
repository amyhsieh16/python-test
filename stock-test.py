import requests
from io import StringIO
import pandas as pd
import numpy as np

def main():
    date = '20200203'
    data = getStackInfo(date)
    df = sortOutData(data)
    print(df)

def getStackInfo(date):
    # 下載股價
    stockInfo_All = requests.get('https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + date + '&type=ALL')
    return stockInfo_All
def sortOutData(data):
    #設定column顯示的數量
    pd.set_option("display.max_columns", None)
    #讓資料對齊
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd.set_option('display.unicode.east_asian_width', True)

    # 整理資料，變成表格
    df = pd.read_csv(StringIO(data.text.replace("=", "")), 
            header=["證券代號" in l for l in data.text.split("\n")].index(True)-1)
    return df.head()


if __name__ == "__main__":
    main()
