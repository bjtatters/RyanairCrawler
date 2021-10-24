import datetime
from dateutil.relativedelta import relativedelta
import requests
import pandas as pd

today = datetime.datetime.today()
flight_dict = {'LGW':'ALC','STN':'ALC'} 
master_df = pd.DataFrame(columns = ['Origin','Destination','Period','Date','Time','Price','Published Price'])

for keys, values in flight_dict.items():
    two_week = today + relativedelta(days=+14)
    one_month = today + relativedelta(months=+1)
    four_month = today + relativedelta(months=+4)
    date_dict = {'Two Weeks':two_week,'One Month':one_month,'Four Months':four_month}
    for keys2, values2  in date_dict.items():
        date_in = values2.strftime('%Y-%m-%d')
        date_out = values2 + relativedelta(days=+7)
        date_out = date_out.strftime('%Y-%m-%d')
        url = 'https://www.ryanair.com/api/booking/v4/en-gb/availability?ADT=1&CHD=0&DateIn={}&DateOut={}&Destination={}&Disc=0&INF=0&Origin={}&TEEN=0&promoCode=&IncludeConnectingFlights=false&FlexDaysBeforeIn=2&FlexDaysIn=2&RoundTrip=true&FlexDaysBeforeOut=2&FlexDaysOut=2&ToUs=AGREED'.format(date_in, date_out, values, keys)
        content = str(requests.get(url).content)
        flight_keys, prices, published_prices = ([] for i in range(3)) 
        for i, _ in enumerate(content):
            needle1 = '"flightKey":"'
            needle2 = '"amount":'
            needle3 = '"publishedFare":'
            if content[i:i + len(needle1)] == needle1:
                flight_keys.append(content[i+13:i+200].split('~~","',1)[0])
            if content[i:i + len(needle2)] == needle2:
                prices.append(content[i+9:i+18].split(',',1)[0])
            if content[i:i + len(needle3)] == needle3:
                published_prices.append(content[i+16:i+25].split(',',1)[0])
        if len(flight_keys) == len(published_prices) == len(prices):
            for i in range(0, len(flight_keys)):
                time = flight_keys[i][-5:]
                date  = flight_keys[i][-16:-6]
                if flight_keys[i][-20:-17] == values:
                    origin = keys
                    destination = values
                else:
                    origin = values
                    destination = keys
                price = prices[i]
                published_price = published_prices[i]
                row = [origin,destination,keys2,date,time,price,published_price]
                master_df.loc[len(master_df)] = row
print(master_df)