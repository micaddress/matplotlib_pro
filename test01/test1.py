# -- coding: utf-8 --
'''
    author:michael

    project:matplotlib

    date:2020/1/31

'''
import pymysql
import matplotlib
params = {
            'host' : '192.168.1.106',
            'user' : 'root',
            'password' : 'zh850113',
            'database' : 'michael_newpneumonia',
            'port' : 3306,
            'charset' : 'utf8'
        }
conn = pymysql.connect(**params)
cursor = conn.cursor()

def get_select(sql):

    cursor.execute(sql)
    result = cursor.fetchall()
    result_list = list(result)

    return result_list

sql_group = """select id from  new_pneumonia_count where pub_date in (select max(pub_date) from new_pneumonia_count where pub_date between "2020-01-01" and NOW() GROUP BY DATE_FORMAT(pub_date,'%Y-%m-%d')) and city!='' and city is not null and city not in ('待确认', '地区待确认', '待确定区域', '待确定', '待确认地区', '区域待定', '地区待确定') ORDER BY city,pub_date"""
print(sql_group)
city_result_list_sql = get_select(sql_group)
str1 = ''
for index in range(len(city_result_list_sql)):
    if index == len(city_result_list_sql) - 1:
        str1 = str1 + str(city_result_list_sql[index][0])
    else:
        str1 = str1 + str(city_result_list_sql[index][0]) + ','
print(str1)
del_sql = '''delete from new_pneumonia_count where id not in ('''+str1+''');'''
print(del_sql)