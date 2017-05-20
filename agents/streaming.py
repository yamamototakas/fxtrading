"""
Demonstrates streaming feature in OANDA open api

To execute, run the following command:

python streaming.py [options]

To show heartbeat, replace [options] by -b or --displayHeartBeat
"""

import requests
import json

from optparse import OptionParser
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def connect_to_stream():
    """

    Environment           <Domain>
    fxTrade               stream-fxtrade.oanda.com
    fxTrade Practice      stream-fxpractice.oanda.com
    sandbox               stream-sandbox.oanda.com
    """

    # Replace the following variables with your personal ones
    domain = 'stream-fxpractice.oanda.com'
    access_token = 'a12ba83f1e8d9c4e309076966ed82166-cacf1b3b295a705ab7cf53c7cdbf2f48'
    account_id = '3954876'
    instruments = "EUR_USD"


    try:
        s = requests.Session()
        url = "https://" + domain + "/v1/prices"
        headers = {'Authorization' : 'Bearer ' + access_token,
                   # 'X-Accept-Datetime-Format' : 'unix'
                }
        params = {'instruments' : instruments, 'accountId' : account_id}
        req = requests.Request('GET', url, headers = headers, params = params)
        pre = req.prepare()
        resp = s.send(pre, stream = True, verify = False)
        return resp
    except Exception as e:
        s.close()
        print "Caught exception when connecting to stream\n" + str(e)

def demo(displayHeartbeat):
    response = connect_to_stream()
    if response.status_code != 200:
        print response.text
        return
    for line in response.iter_lines(1):
        if line:
            try:
                msg = json.loads(line)
            except Exception as e:
                print "Caught exception when converting message into json\n" + str(e)
                return

            if displayHeartbeat:
                print line
            else:
                if msg.has_key("instrument") or msg.has_key("tick"):
                    print line

def main():
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("-b", "--displayHeartBeat", dest = "verbose", action = "store_true",
                        help = "Display HeartBeat in streaming data")
    displayHeartbeat = False

    (options, args) = parser.parse_args()
    if len(args) > 1:
        parser.error("incorrect number of arguments")
    if options.verbose:
        displayHeartbeat = True
    demo(displayHeartbeat)


if __name__ == "__main__":
    main()
