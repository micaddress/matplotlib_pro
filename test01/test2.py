# -- coding: utf-8 --
"""
    author:michael

    project:matplotlib_pro

    date:2020/3/4

"""
import time, requests, json

print('开始更换IP')
start_time = time.time()
restart_senconds = 10
requestPayload = json.dumps({"method": "do", "login": {"password": "ypZ6l6409TefbwK"}})
response = requests.post('http://192.168.1.1', data=requestPayload)
response = response.content.decode('utf-8')
session = json.loads(response)
# 断开网络
disconnectdata = json.dumps(
    {"network": {"change_wan_status": {"proto": "pppoe", "operate": "disconnect"}}, "method": "do"})
code = requests.post(url='http://192.168.1.1/stok=' + session['stok'] + '/ds', data=disconnectdata)
for i in range(5):
    print('更换IP倒计时: ', restart_senconds - i, ' 秒')
    time.sleep(1)
# 连接网络
connectdata = json.dumps(
    {"network": {"change_wan_status": {"proto": "pppoe", "operate": "connect"}}, "method": "do"})
code = requests.post(url='http://192.168.1.1/stok=' + session['stok'] + '/ds', data=connectdata)
for i in range(5):
    print('更换IP倒计时: ', restart_senconds - i - 5, ' 秒')
    time.sleep(1)

print('更换IP结束')
print('耗时: ', round(time.time() - start_time), ' 秒')






