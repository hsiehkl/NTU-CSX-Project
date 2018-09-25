
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import time


# ## 讀取 climate1_getStationInfo 所取得觀測站資料

# In[49]:


station_info = pd.read_csv('station_info.csv')


# In[50]:


station_info.head(5)


# In[51]:


# remove Unnammed colums
# delete the column without reassigning station_info
station_info.drop('Unnamed: 0', axis=1, inplace=True)


# In[52]:


station_info.head(5)


# In[53]:


# get the column labels of the station_info
stationIndexList = station_info.columns


# In[104]:


def getClimate(site, date):
    precpAvgList = list()
    tempAvgList = list()
    
    #if site[0] == "台":
        #site = "臺" + site[1:] #字串無法直接指定, ex: site[k] = "臺"
    for i in range(len(stationIndexList)):
        
        #此地區每個測站
        if station_info[stationIndexList[i]][2] == site:
            time.sleep(0.11)
            
            #去指定網址爬取資料
            #print(station_info[stationIndexList[i]][0])
            temp = pd.read_html(station_info[stationIndexList[i]][4] + date)
            
            #此測站的24小時資料
            for hour in range(len(temp[1][3][2:])):
                #單一觀測站資料list
                precpList = list()
                tempList = list()
                
                #讀取，若是x則跳過
                try:
                    precpList.append(np.float(temp[1][10][hour+2]))
                    tempList.append(np.float(temp[1][3][hour+2]))
                except:
                    continue
                    
                #求得此測站平均
                precpAvg = np.average(precpList)
                tempAvg = np.average(tempList)
            
            #此地區所有測站平均
            if precpAvg == precpAvg:
                precpAvgList.append(precpAvg)
            if tempAvg == tempAvg:
                    tempAvgList.append(tempAvg)
        
    #所有測站平均值四捨五入至小數點第二位
    finalPrecpAvg = round(np.average(precpAvgList), 2)
    finalTempAvg = round(np.average(tempAvgList), 2)
    
    #回傳區域平均降水量以及平均溫度
    return finalPrecpAvg, finalTempAvg


# ## Test getClimate()

# In[106]:


getClimate('臺北市', '2018-09-20')


# In[107]:


getClimate('新北市', '2018-09-20')

