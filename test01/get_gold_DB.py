# encoding='utf-8'
import pymysql
params = {
            'host' : '192.168.1.106',
            'user' : 'root',
            'password' : 'zh850113',
            'database' : 'michael_gold_price',
            'port' : 3306,
            'charset' : 'utf8'
        }
conn = pymysql.connect(**params)
cursor = conn.cursor()





