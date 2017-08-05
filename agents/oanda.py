#! /usr/bin/python
# -*- coding: utf-8 -*-

import oandapy
import sys
import mydata
import json
import zipfile
from datetime import datetime, timedelta


class MyStreamer(oandapy.Streamer):

    def __init__(self, count=10, *args, **kwargs):
        super(MyStreamer, self).__init__(*args, **kwargs)
        self.count = count
        self.reccnt = 0

    def on_success(self, data):
        print(data, "\n")
        self.reccnt += 1
        if(self.reccnt == self.count):
            self.disconnect()

    def on_error(self, data):
        self.disconnect()


def doTEST(data):
    open = data["openMid"]
    close = data["closeMid"]
    high = data["highMid"]
    low = data["lowMid"]

    print(data["openMid"])

def TEST(**data):
    open = data["openMid"]
    close = data["closeMid"]
    high = data["highMid"]
    low = data["lowMid"]

    print(data["openMid"])



def main():
    my_data = mydata.readAccountinfo("mydata.json")
    oanda = oandapy.API(environment=my_data["jp"]["environment"],
                        access_token=my_data["jp"]["token"])

    response = oanda.get_prices(instruments="USD_JPY")
    # response2 = oanda.get_history(instrument="USD_JPY", count="5", granularity="D")
    # response2 = oanda.get_history(instrument="USD_JPY", count="5", granularity="D",
    #             dailyAlignment="12", candleFormat="midpoint", start="2014-06-19T15:47:45.000000Z")
    # response2 = oanda.get_history(instrument="USD_JPY", count="5", granularity="D",
    #            dailyAlignment="12", candleFormat="midpoint")


    # with zipfile.ZipFile('candle_test.zip', 'w', zipfile.ZIP_DEFLATED) as myzip:
    #      myzip.writestr("candle-USD_JPY_5.json", json.dumps(response2, sort_keys=True, indent=2))

    # print(response)
    # prices = response.get("prices")
    # asking_price = prices[0].get("ask")
    # print(prices)
    #
    # print(json.dumps(response2, indent=4))

    with zipfile.ZipFile('candle_test.zip') as myzip:
        for each in myzip.namelist():
            print("File name = ", each)
            with myzip.open(each) as myfile:
                data = json.loads(myfile.read().decode('utf-8'))

    print(data)
    candle=data.get("candles")

    print(candle[0]["openMid"])

    doTEST(candle[0])
    TEST(**candle[0])

    # stream = MyStreamer(environment=my_data["jp"]["environment"],
    #                     access_token=my_data["jp"]["token"])
    # stream.events(ignore_heartbeat=False)


if __name__ == '__main__':
    main()
