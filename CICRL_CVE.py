#! /usr/bin/env python

# Headers
import os,sys,json,csv,re,requests,sys,cowsay
from tabulate import tabulate
import pandas as pd,numpy as np,pathlib
import urllib.parse,urllib.error,urllib3
from pandas.io.json import json_normalize

# Browse
def browse():
    resp = requests.get('http://cve.circl.lu/api/browse')
    t = json.loads(resp.text)
    result = pd.DataFrame(t['vendor'],columns=['vendors'])  
    p= print(tabulate(result, headers='keys', tablefmt='psql'))
    csv_Input = int(input("Please, enter the 'CSV' as options to get csv :\n [1].YES\n [2].NO\n"))
    if csv_Input == '1':
        result.to_csv('./Browse_CSV.csv')
    else:
        cowsay.tux("Adois Amigo !")
    return p

# Vendors
def browse_vendors(data):
    print("The vendor is "+data)
    resp = requests.get('http://cve.circl.lu/api/browse/'+data)
    t = json.loads(resp.text)
    result = pd.DataFrame(t['product'],columns=['product'])
    p= print(tabulate(result, headers='keys', tablefmt='psql'))
    return result

# CVE_ID Search
def cve_ID(data):
    resp = requests.get('https://cve.circl.lu/api/cve/'+data)
    t = json.loads(resp.text)
    result = json_normalize(t)
    Fin_res = result.to_csv('./cve.csv')
    print('CSV is generated!')
    return Fin_res

# CVE 
def Last_CVE():
    limit_cve = input("Enter the search limit to fetch records: \n{Click enter if no value (or) Enter the value}")
    if len(limit_cve) == 0:
        resp = requests.get('http://cve.circl.lu/api/last')
    else:
        resp = requests.get('http://cve.circl.lu/api/last/'+limit_cve)
    t = json.loads(resp.text)
    result = json_normalize(t)
    csv = result.to_csv('./Last_CVE.csv')
    Curr_Path = pathlib.Path().absolute()
    print('\n')
    print("Last_CVE.csv generated at ",Curr_Path)
    return result

# dbinfo
def db_info():
    resp = requests.get('http://cve.circl.lu/api/dbInfo')
    t = json.loads(resp.text)
    p= (json.dumps(t, indent=4, sort_keys=True))
    print(p)

try:
    if sys.argv[1] == '-b' or sys.argv[1] == '--browse':
        browse()
    elif sys.argv[1] == '-v' or sys.argv[1] == '--vendor':
        data = input("Enter the keyword, to search for vendor :")
        browse_vendors(data)
    elif sys.argv[1] == '-c' or sys.argv[1] == '--CVE':
        data = input("Enter the CVE id :")
        cve_ID(data)
    elif sys.argv[1] == '-lc' or sys.argv[1] == '--lastcve':
        Last_CVE()
    elif sys.argv[1] == '-db' or sys.argv[1] == '--dbinfo':
        db_info()
    elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
        cowsay.tux("Use any following options\n [1]. Browse [or] -b\n [2]. Vendor [or] -v\n [3]. CVE [or] -c\n [4]. LastCVE [or] -lc\n [5]. DBinfo [or] -db\n kindly follow the format\n python CIRCL_CVE.py [OPTIONS] eg:--db ")
    else:
        cowsay.tux("Use any following options\n [1]. Browse [or] -b\n [2]. Vendor [or] -v\n [3]. CVE [or] -c\n [4]. LastCVE [or] -lc\n [5]. DBinfo [or] -db\n kindly follow the format\n python CIRCL_CVE.py [OPTIONS] eg:--db ")
except:
    cowsay.tux("Use any following options\n [1]. Browse [or] -b\n [2]. Vendor [or] -v\n [3]. CVE [or] -c\n [4]. LastCVE [or] -lc\n [5]. DBinfo [or] -db\n kindly follow the format\n python CIRCL_CVE.py [OPTIONS] eg:--db ")