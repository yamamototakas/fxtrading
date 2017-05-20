#! /usr/bin/python
# -*- coding: utf-8 -*-

import oandapy
import sys
import mydata
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


def main():
    my_data = mydata.readAccountinfo("mydata.json")
    oanda = oandapy.API(environment=my_data["jp"]["environment"],
                        access_token=my_data["jp"]["token"])

    response = oanda.get_prices(instruments="USD_JPY")
    prices = response.get("prices")
    asking_price = prices[0].get("ask")
    print(asking_price)

    stream = MyStreamer(environment="practice",
                        access_token="a12ba83f1e8d9c4e309076966ed82166-cacf1b3b295a705ab7cf53c7cdbf2f48")
    stream.events(ignore_heartbeat=False)


if __name__ == '__main__':
    main()
