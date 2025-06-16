import cryptocompare
import numpy as np
import pandas as pd
import datetime

cryptocompare.cryptocompare._set_api_key_parameter("5c5ef1da79a49d4ba3c4d14b62ac811646759e02a8d491ca848102a82dc6f9fb")
btcdata = cryptocompare.get_historical_price_day("BTC", currency="USD", limit=59, toTs=datetime.datetime(year=2023, month=4, day=29))


price = [entry['close'] for entry in btcdata]
arr = np.arange(1, 61)
myList = arr.tolist()

data = {'timeStamp': myList,
        'btc prices': price}

mydata = pd.DataFrame(data)
mydata.to_csv('output.csv', index=False)