import pandas as pd

df = pd.read_csv("data/notifications.csv")
for i in range(len(df.columns)):
    print("----------------------------")
    print(df.columns[i])
    print(df.iloc[:, i].unique())
    print(df.iloc[:, i].value_counts())
    # print(df.iloc[:, i].isna().sum())


    plan = {'AED' : 1, 'SEK' : 1, 'AUD' : 1, 'GBP' : 1, 'ETH' : 0, 'RUB' : 1, 'CHF' : 1, 'HRK' : 1, 'LTC' : 0, 'MAD' : 1, 'BTC' : 0, 'NZD' : 1, 'JPY' : 1, 'ILS' : 1, 'QAR' : 1, 'MXN' : 1, 'DKK' : 1, 'SGD' : 1, 'ZAR' : 1, 'BGN' : 1, 'USD' : 1, 'INR' : 1, 'THB' : 1, 'RON' : 1, 'HUF' : 1, 'TRY' : 1, 'XRP' : 1, 'PLN' : 1, 'EUR' : 1, 'BCH' : 0, 'CZK' : 1, 'CAD' : 1, 'NOK' : 1, 'HKD' : 1, 'SAR' : 1}
