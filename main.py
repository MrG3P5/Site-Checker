#!/usr/bin/env python3
import requests
import os
import sys
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, init

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Color
green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
white = Fore.WHITE
cyan = Fore.LIGHTCYAN_EX
yellow = Fore.LIGHTYELLOW_EX

init(autoreset=True)

try:
    open("res-200.txt", "a")
except:
    pass

def domainFixer(domain):
    try:
        domain = domain.split("://")[1].split("/")[0]
        if ":" in domain:
            domain = domain.split(":")[0]
        return "https://" + domain
    except:
        return domain

def banner():
    os.system("cls||clear")
    __banner__ = f""" 	
  {red}------------.        .-----------
    ------     \  __  /    ------
      -----     \(  )/    -----      {cyan}[ {white}X - SiteChecker Status Code {cyan}]
          {red}---   ' \/ `   ---             {cyan}[ {white}Created By X-MrG3P5 {cyan}]
            {red}--- :    : ---                   {cyan}[ {white}Version 1.0 {cyan}]
              {red}--'    '--
                //..\\\\
           ====UU====UU====
               '//||\\\\'
                 ''''"""
    os.system("cls||clear")
    print(__banner__)
    
def SiteCheck(domain):
    domain = domainFixer(domain.strip("\r\n"))
    try:
        req = requests.get(domain, verify=False, timeout=10)
        
        if req.status_code == 200:
            sys.stdout.write(f"\n{white}---> {green}{domain} 200 OK")
            open("res-200.txt", "a").write(domain + "\n")
        else:
            sys.stdout.write(f"\n{white}---> {yellow}{domain} {req.status_code}")
    except:
        sys.stdout.write(f"\n{white}---> {red}{domain} DIE SITE!")
    
if __name__=="__main__":
    banner()
    list_domain = open(input(f"{red}[{white}?{red}] {white}Domain List : "), "r").readlines()
    Thread = input(f"{red}[{white}?{red}] {white}Thread : ")
    pool = ThreadPool(int(Thread))
    banner()
    pool.map(SiteCheck, list_domain)
    pool.close()
    pool.join()
    sys.stdout.write(f"\n{white}----> {green}DONE")
