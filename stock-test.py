import requests
from io import StringIO
import pandas as pd
import numpy as np

def main():
    date = '20200203'
    data = getStackInfo(date)
    df = sortOutData(data)
    #選出本益比 > 15
    df = df[pd.to_numeric(df['本益比'], errors='coerce')>15] 
    print(df)

def getStackInfo(date):
    # 下載股價
    stockInfo_All = requests.get('https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + date + '&type=ALL')
    return stockInfo_All

def sortOutData(data):
    #設定column顯示的數量
    pd.set_option("display.max_columns", None)
    #pd.set_option('max_colwidth', 800)
    #讓資料對齊
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd.set_option('display.unicode.east_asian_width', True)

    #整理資料，變成表格
    #read_csv("檔案位置或 file-like object(因此需要StringIO)"
    #         ,找到allStockInfo的起始(由)證劵代號在data.text中
    #         ,如果想要完整資料則需加入 delimiter="\n"
            

    df = pd.read_csv(StringIO(data.text.replace("=", "")),
                     header=["證券代號" in L for L in data.text.split("\n")].index(True)-1)
    # remote all NaN columns
    df = df.dropna(axis = 1, how = 'all')

    return df


#呼叫main function
main()
