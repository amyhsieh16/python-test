import requests
from io import StringIO
import pandas as pd
import numpy as np

datestr = '20200203'

# 下載股價
r = requests.get('https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')
#設定column顯示的數量
pd.set_option("display.max_columns", None)
#讓資料對齊
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
# 整理資料，變成表格
df = pd.read_csv(StringIO(r.text.replace("=", "")), 
            header=["證券代號" in l for l in r.text.split("\n")].index(True)-1)

df.style.apply(_color_if_even, subset=['本益比'])
(df.style
 .hide_index()
 .highlight_null()
 .background_gradient('Greens', subset='本益比')
 .highlight_max('成交股數')
 )
# 整理一些字串：
#df = df.apply(lambda s: pd.to_numeric(s.astype(str).str.replace(",", "").replace("+", "1").replace("-", "-1"), errors='coerce'))

# 顯示出來
df.head()
print(df.head())
