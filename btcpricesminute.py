import cryptocompare
import numpy as np
import pandas as pd
import datetime

cryptocompare.cryptocompare._set_api_key_parameter("5c5ef1da79a49d4ba3c4d14b62ac811646759e02a8d491ca848102a82dc6f9fb")
btcdata = cryptocompare.get_historical_price_minute("BTC", currency="USD", limit=1799, toTs=datetime.datetime(year=2023, month=3, day=2, hour=6, minute=0))


price = [entry['close'] for entry in btcdata['Data']['Data']]
arr = np.arrange(1, 1801)
myList = arr.tolist()

data = {'timeStamp': myList,
        'btc prices': price}

mydata = pd.DataFrame(data)
mydata.to_csv('output.csv', index=False)