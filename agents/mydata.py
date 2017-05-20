# -*- coding: utf-8 -*-

import json
import sys
import os


def readAccountinfo(filename):
    if not os.path.exists(filename):
        filename = 'agents/' + filename

    with open(filename, 'r') as f:
        mydata = json.load(f)

    return mydata


def main():

    data = readAccountinfo('mydata.json')
    print(data)


if __name__ == '__main__':

    # print("Called by main")
    # print("__file__ :%s" %  __file__)
    # print("sys.argv[0] :%s" %  sys.argv[0])
    # print("os.path.dirname(__file__) : %s" % os.path.dirname(__file__))
    # print("os.path.basename(__file__) :%s" % os.path.basename(__file__))
    # print("os.path.abspath(__file__) :%s" % os.path.abspath(__file__))
    # print("os.path.abspath(os.path.dirname(__file__)) :%s" % os.path.abspath(os.path.dirname(__file__)))
    # print("os.getcwd() : %s \n" % os.getcwd())

    main()
