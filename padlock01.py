#!/usr/bin/env python3


def padlock (d1, d2, d3, d4):
    if d1*17 + d2*79 + d3*941 + d4*1259 == 18556:
        print("🔓 congratulations! 🥳")
    else:
        print("🔒 wrong 😔 try again!")



padlock(1, 2, 3, 4)