# -- coding: utf-8 --
"""

    author:michael

    project:matplotlib

    date:2020/1/31

"""
from matplotlib import pyplot as plt,font_manager
import test01.get_sql_result as get_select
import test01.get_new_pneumonia_DB as get_np_DB
import matplotlib
font = {'family': 'STFangsong',
        'weight': 'bold',
        'size': 25}
matplotlib.rc('font', **font)
# 显示的所有字体
# a= sorted([f.name for f in font_manager.fontManager.ttflist])
# for i in a:
#     print(i)

# 解决中文显示
# plt.rcParams['font.sans-serif'] = ['STFangsong']
# 解决符号无法显示
# plt.rcParams['axes.unicode_minus'] = False
# 设置图片大小
fig = plt.figure(figsize=(80, 30), dpi=100)

# province = '安徽'
# province_sql = "select DISTINCT city from new_pneumonia_count where province = '"+province+"' and city is not null"
# get_np_DB.cursor.execute(province_sql)
# citys_list = get_np_DB.cursor.fetchall()
# city_list = [city[0] for city in citys_list ]
city_list = [
    '武汉',
    '黄冈',
    '合肥',
    '芜湖',
      '阜阳'
]
c_confirm_sql_start = "select DISTINCT pub_date,c_confirm_count from  new_pneumonia_count where city ='"
c_sql_end = "' and c_confirm_count is not null ORDER BY pub_date"
result_list = []
sql = ''
for result_index in range(len(city_list)):
    sql = c_confirm_sql_start + city_list[result_index] + c_sql_end
    # sql = c_confirm_sql_start + city_list[result_index] + "' and province = '" + province + c_sql_end
    print(sql)
    result_list.append(get_select.get_select(sql))
x_date=[]
y_confirm_count = []

subplot_index = 1
# for result in result_list:
#     for index in range(len(result)):
#         # x_date.append(result[index][0])
#         x_date.append(str(result[index][0]))
#         y_confirm_count.append(result[index][1])
#         print(result[index][0])
#         print(result[index][1])
#     plt.plot(x_date, y_confirm_count)
#     x_date.clear()
#     y_confirm_count.clear()
city_index = 0
for results in result_list:
    for result_index in range(len(results)):
        a = results[result_index]
        if result_index != 0:
            b = results[result_index - 1]
            if a[1] != b[1]:
                x_date.append(str(a[0]))
                y_confirm_count.append(a[1])
            else:
                # print(a[1])
                # print(b[1])
                # print(type(b[1]))
                # print('-' * 200)
                continue
        elif result_index == 0:
            x_date.append(str(a[0]))
            y_confirm_count.append(a[1])
        # if result_index != 0:
        #     b = results[result_index - 1][0]
        #     if a[0].hour != b.hour:
        #         x_date.append(str(a[0]))
        #         y_confirm_count.append(a[1])
        #     else:
        #         continue
        # elif result_index == 0:
        #     x_date.append(str(a[0]))
        #     y_confirm_count.append(a[1])
    print(x_date)
    print(y_confirm_count)
    # a_date = [result for result in x_date]
    plt.subplot(len(result_list), 1, subplot_index)
    subplot_index += 1
    plt.plot(x_date, y_confirm_count, label=city_list[city_index])
    plt.legend(loc='upper left')
    city_index +=1
    x_date.clear()
    y_confirm_count.clear()


# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# 设置坐标轴label的大小，背景色等信息
# for label in ax.get_xticklabels() + ax.get_yticklabels():
#     label.set_fontsize(30)
#     label.set_bbox(dict(facecolor = 'green', edgecolor = 'None', alpha = 0.7))

plt.grid(alpha=1,linestyle='--')
# 绘制X轴刻度
plt.xticks(rotation=45)
plt.xlabel('疫情发布日期')
plt.ylabel('人数')
plt.title('确诊波形图')
plt.savefig('a2.svg')


plt.show()

