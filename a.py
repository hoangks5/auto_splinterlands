from os import name
import threading
import time
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
import main
import tes
import timct
import random
import main1





def chay(acc):
    thres = []
    for acc1 in acc:
        thres.append(threading.Thread(target=main.hay,args={acc1},))
    for thre in thres:
        thre.start()
        time.sleep(5)
    for thre in thres:
        thre.join()

def chay1(acc):
    ct = acc[(len(acc)-1)]
    acc = acc[:len(acc)-1]
    thres = []
    for i in acc:
        list = i+';'+ct
        thres.append(threading.Thread(target=main1.hay,args={list},))
    for thre in thres:
        thre.start()
        time.sleep(5)
    for thre in thres:
        thre.join()

def card(acc):
    ct = acc[(len(acc)-1)]
    acc = acc[:len(acc)-1]
    thres = []
    for i in acc:
        list = i+';'+ct
        thres.append(threading.Thread(target=main1.chuyencard,args={list},))
    for thre in thres:
        thre.start()
        time.sleep(5)
    for thre in thres:
        thre.join()
        
    
    
    

