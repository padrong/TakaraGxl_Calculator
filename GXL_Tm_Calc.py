#!/usr/bin/python3

import sys
import argparse
import gzip

primer1 = input("Please input your forward primer: ")
primer2 = input("Please input your reverse primer: ")

primer1 = primer1.upper()
primer2 = primer2.upper()

def tm_calc(primer):
    ccount = 0
    tcount = 0
    acount = 0
    gcount = 0
    for base in primer:
        if base == "C":
            ccount += 1
        elif base == "G":
            gcount += 1 
        elif base == "A":
            acount += 1
        elif base == "T":
            tcount += 1
    tm = (((acount + tcount) *2) + ((gcount+ccount)*4)) - 5
    if tm > 55:
        tm = 60
    else:
        tm = 55
    return(tm)

print("Your forward Tm is: ", tm_calc(primer1), "\n" "Your reverse Tm is: ", tm_calc(primer2))
