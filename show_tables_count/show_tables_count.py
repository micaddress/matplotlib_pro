# -- coding: utf-8 --
"""
    author:michael

    project:matplotlib_pro

    date:2020/2/24

"""
import pymysql
params = {
            'host' : '192.168.1.106',
            'user' : 'root',
            'password' : 'zh850113',
            'database' : 'michael_lianjia',
            'port' : 3306,
            'charset' : 'utf8'
        }
db = pymysql.connect(**params)
cursor = db.cursor()
cursor.execute("show tables")
table_name_tuple = cursor.fetchall()
all_name_list = []
esf_list = []
cj_list = []
for tb in table_name_tuple:
    table_name = tb[0]
    if table_name.startswith('lianjia_esf'):
        esf_list.append(table_name)
    elif table_name.startswith('lianjia_cj'):
        cj_list.append(table_name)
all_name_list.append(max(esf_list))
all_name_list.append(max(cj_list))
for tb in all_name_list:
    sql = '''select 1 from ''' + tb
    result = cursor.execute(sql)
    print(tb, result)









