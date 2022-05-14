# -- coding: utf-8 --
"""
    author:michael

    project:matplotlib_pro

    date:2020/2/4

"""
from matplotlib import pyplot as plt,font_manager
from test01 import get_sql_result as get_result
import matplotlib

font = {'family': 'STFangsong',
        'weight': 'bold',
        'size': 60}
matplotlib.rc('font', **font)
plt.figure(figsize=(80, 40), dpi=50)
sql_group = """select DISTINCT pub_date,total_cure_count,total_dead_count from  new_pneumonia_count where pub_date in (select max(pub_date) from new_pneumonia_count where pub_date between "2020-01-01" and NOW()  GROUP BY DATE_FORMAT(pub_date,'%Y-%m-%d'))  ORDER BY pub_date"""
result_list = get_result.get_select(sql_group)
x_date = []
y_cure_count = []
y_dead_count = []
y_cure_add_count = []
y_dead_add_count = []
for index in range(len(result_list)):
    if index + 1 == len(result_list):
        break
    cure_add_count = result_list[index + 1][1] - result_list[index][1]
    dead_add_count = result_list[index + 1][2] - result_list[index][2]
    if index == len(result_list) - 1:
        xdate = str(result_list[index][0]).split('20-')[-1]
    else:
        xdate = str(result_list[index][0]).split(' ')[0].split('20-')[-1]
    ycure = result_list[index][1]
    ydead = result_list[index][2]
    x_date.append(xdate)
    y_cure_count.append(ycure)
    y_dead_count.append(ydead)
    y_cure_add_count.append(cure_add_count)
    y_dead_add_count.append(dead_add_count)
plt.plot(x_date, y_cure_count, label='总共治愈人数', linewidth=10)
plt.plot(x_date, y_dead_count, color='red',  label='总共死亡人数', linewidth=10)
plt.plot(x_date, y_cure_add_count, label='每天治愈人数', linewidth=10)
plt.plot(x_date, y_dead_add_count, color='red',  label='每天死亡人数', linewidth=10)
for a, b in zip(x_date, y_cure_count):
    plt.text(a, b, b, ha='center', va='top', fontsize=50)
for a, b in zip(x_date, y_dead_count):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=50)
for a, b in zip(x_date, y_cure_add_count):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=50)
for a, b in zip(x_date, y_dead_add_count):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=50)
plt.legend(loc='upper left')
# plt.xticks(rotation=0)
# plt.xlabel('每日增长统计时间')
plt.ylabel('每日增长人数')
# plt.legend(loc='best', shadow=False, fontsize=60)
# plt.grid(alpha=1, linestyle='--')
plt.savefig('各省疫情波形图/治愈和死亡每日增长人数1.svg')
