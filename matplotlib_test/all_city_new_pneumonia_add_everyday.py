# -- coding: utf-8 --
"""
    author:michael

    project:matplotlib_pro

    date:2020/2/4

"""
from matplotlib import pyplot as plt
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

def takeSecond(elem):
    return elem[-1][1]

font = {'family': 'STFangsong',
            'weight': 'bold',
            'size': 30}
matplotlib.rc('font', **font)
plt.figure(figsize=(100, 5000), dpi=50)
r_list = []
sql_group = """select DISTINCT city,pub_date,c_confirm_count from  new_pneumonia_count where pub_date in (select max(pub_date) from new_pneumonia_count where pub_date between "2020-01-01" and NOW() GROUP BY DATE_FORMAT(pub_date,'%Y-%m-%d')) and city!='' and city is not null and city not in ('待确认', '地区待确认', '待确定区域', '待确定', '待确认地区', '区域待定', '地区待确定') ORDER BY city,pub_date"""
print(sql_group)
city_result_list_sql = get_select(sql_group)
city_name = ''
last_city_name = ''
this_city_name = ''
result_list = []
c_r_list = []
flag = 1
for city_result in city_result_list_sql:
    c_list = []
    this_city_name = city_result[0]
    if this_city_name == last_city_name:
        c_list.append(city_result[1])
        c_list.append(city_result[2])
    elif this_city_name != last_city_name:
        if flag != 1:
            c_r_list = []
            result_list.append(c_r_list)
        c_r_list.append(city_result[0])
        c_list.append(city_result[1])
        c_list.append(city_result[2])
        flag = 2
    c_r_list.append(c_list)
    last_city_name = this_city_name

# mid = []
# mid.append(city)
# result_list.append(mid + city)
x_date=[]
y_confirm_count = []

this_count = -1
last_count = -1
x = []
y = []
city_index = 0
subplot_index = 1
result_list.sort(key=takeSecond, reverse=True)
# for result in result_list:
#     print(result)
for city_count_result in result_list:
    title_time = ''
    city = city_count_result[0]
    city_count_result.remove(city)
    for index in range(len(city_count_result)):
        if index+1 == len(city_count_result):
            break
        add_count = city_count_result[index + 1][1] - city_count_result[index][1]
        if index == len(city_count_result) - 2:
            title_time = str(city_count_result[index + 1][0]).split(' ')[-1]
            result = str(city_count_result[index + 1][0]).split(' ')[0].split('20-0')[-1]
            a = str(int(result.split('-')[0]))
            b = str(int(result.split('-')[1]))
            x.append(a + '-' + b)
        else:
            result = str(city_count_result[index + 1][0]).split(' ')[0].split('20-0')[-1]
            a = str(int(result.split('-')[0]))
            b = str(int(result.split('-')[1]))
            x.append(a + '-' + b)
        y.append(add_count)
    plt.subplot(len(result_list), 2, subplot_index)
    subplot_index += 1
    plt.plot(x, y, label=city, linewidth=10, markersize=60)
    # plt.xticks(rotation=45)
    # plt.xlabel('每日增长统计时间')
    plt.ylabel('每日增长人数')
    plt.title(city+' 截止到今日'+title_time+' 确诊:'+str(city_count_result[-1][-1])+'例', fontsize=60)
    for a, b in zip(x, y):
        plt.text(a, b, b, ha='center', va='baseline', fontsize=50)
    # plt.legend(loc='best', shadow=False, fontsize=60)
    plt.grid(alpha=1, linestyle='--')
    print(city, city_index)
    city_index += 1
    x.clear()
    y.clear()
plt.savefig('全国.svg')
print('结束...')