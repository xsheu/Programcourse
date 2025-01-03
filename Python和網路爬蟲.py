# 請不要動
import subprocess
import sys
subprocess.check_call([sys.executable, "-m","pip", "install", "requests"])
subprocess.check_call([sys.executable, "-m","pip", "install", "pprint"])
subprocess.check_call([sys.executable, "-m","pip", "install", "webbrowser"])
subprocess.check_call([sys.executable, "-m","pip", "install", "time"])
subprocess.check_call([sys.executable, "-m","pip", "install", "matplotlib"])

# 請不要動


import requests

response = requests.get('https://stats.moe.gov.tw/files/detail/109/109_student.csv')

print(response.text)


# In[4]:


response = requests.get('https://media.taiwan.net.tw/XMLReleaseALL_public/Activity_C_f.json')

print(response.text)


# ## 10-1 以 requests 取得網路服務

# ### *簡單的網路服務範例*

# In[5]:


import requests
url = 'https://random.dog/woof.json'

response = requests.get(url)
print(response.text)


# ### *解讀 JSON 格式資料*

# In[6]:


response.json()


# In[7]:


type(response.json())


# In[8]:


data = response.json()

print(data['url'])


# In[9]:


import webbrowser

webbrowser.open(data['url'])


# ## 10-2 解析網路服務的資料內容

# ### *從回應的 JSON 文字取出所需資料*
# 
# Foreign exchange rates API 網站：https://exchangeratesapi.io/

# In[13]:


import requests, pprint

url = 'https://api.exchangeratesapi.io/latest?access_key=a27e49d6643267b2122f24b194b9cce9'

response = requests.get(url)
data = response.json()
pprint.pprint(data)


# In[14]:


print(data)
data['rates']


# In[15]:


data['rates']['IDR']


# ### *在程式重複查詢服務並取回資料*
# 
# World Time API 網站: http://worldtimeapi.org/

# In[16]:


import requests, pprint

url = 'http://worldtimeapi.org/api/ip'

data = requests.get(url).json()
pprint.pprint(data)


# In[19]:


# 此程式不會停止, 執行後按停止鈕來中止它

import requests, time

url = 'http://worldtimeapi.org/api/ip'

data = requests.get(url).json()
print(data['datetime'])


# ### *確保網路服務有正確回應*

# In[21]:


# 沿用上一小節的模組及 url

response = requests.get(url)

if response.status_code == requests.codes.ok:
    data = response.json()
    print(data['datetime'])
else:
    print('網路服務查詢失敗')


# ### *在查詢服務時使用參數*
# 
# Sunset and sunrise times API 網站：https://sunrise-sunset.org/api

# In[22]:


import requests, pprint

url = 'https://api.sunrise-sunset.org/json?lat=22.753773&lng=121.166549'
data = requests.get(url).json()
pprint.pprint(data)


# In[23]:


latitude = 52.286998
longitude = 104.286992

url = f'https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}'
data = requests.get(url).json()
pprint.pprint(data)


# ## 10-3 網路服務實用範例：中央氣象局 36 小時天氣預報
# 
# 資料擷取 API 線上說明文件：https://opendata.cwb.gov.tw/dist/opendata-swagger.html

# ### *了解服務傳回的 JSON 資料之結構*

# In[25]:


import requests, pprint

url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=rdec-key-123-45678-011121314&locationName=連江縣'

data = requests.get(url).json()
pprint.pprint(data)


# In[26]:


data['records']['location'][0]['weatherElement'][1]['time']


# ### *走訪資料*

# In[27]:


# 沿用上一小節的模組及 data

pop = data['records']['location'][0]['weatherElement'][1]['time']

for p in pop:
    print('預報區間', p['startTime'], '~', p['endTime'])
    print('降雨機率:', p['parameter']['parameterName'] + '%')
    print()


# ## 10-4 網路資料圖形化：以地震震度統計為例
# 
# GeoJSON API 網站：https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

# ### *取出地震震度*

# In[28]:


import requests, pprint

url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson'

data = requests.get(url).json()
pprint.pprint(data)


# In[29]:


quakes = data['features']
mag = quakes[0]['properties']['mag']

print(mag)


# ### *統計各種地震規模的數量*

# In[30]:


# 沿用上一小節的模組及 data

quakes = data['features']
mag_label = ['未滿3級', '3~4級', '4~5級', '5~6級', '6級以上']
mag_list = [0, 0, 0, 0, 0]

for q in quakes:
    mag = q['properties']['mag']
    if mag >= 6:
        mag_list[4] += 1
    elif mag >= 5:
        mag_list[3] += 1
    elif mag >= 4:
        mag_list[2] += 1
    elif mag >= 3:
        mag_list[1] += 1
    else:
        mag_list[0] += 1

print(mag_list)


# ### *繪製長條圖與圓餅圖*

# In[31]:


# 沿用上一小節的模組及 mag_label/mag_list

import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['Microsoft JhengHei']   # 參閱第 8 章

plt.bar(mag_label, mag_list)
plt.show()

plt.pie(mag_list, labels=mag_label, autopct='%1.1f%%')
plt.show()


# In[ ]:




