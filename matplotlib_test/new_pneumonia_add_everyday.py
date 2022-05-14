# -- coding: utf-8 --
"""
    author:michael

    project:matplotlib_pro

    date:2020/2/4

"""
from matplotlib import pyplot as plt
from test01 import get_sql_result as get_result
import matplotlib

def takeSecond(elem):
    return elem[-1][1]

provinces_sql = "select DISTINCT province from new_pneumonia_count"
province_list = get_result.get_select(provinces_sql)
# province_list = [
#     ('湖北',),
#     ('安徽',),
#     ('上海',),
#     ]


for province in province_list:
    # province = '安徽'
    province = province[0]
    font = {'family': 'STFangsong',
            'weight': 'bold',
            'size': 30}
    matplotlib.rc('font', **font)
    plt.figure(figsize=(100, 200), dpi=50)
    province_sql = "select DISTINCT city from new_pneumonia_count where province = '"+province+"' and city is not null and city not in ('待确认', '地区待确认', '待确定区域', '待确定', '待确认地区', '区域待定', '地区待确定')"
    citys_list = get_result.get_select(province_sql)
    city_list = [city[0] for city in citys_list ]
    # city_list = [
    #     '武汉',
    #     '黄冈',
    #     '合肥',
    #     '芜湖',
    #     '阜阳'
    # ]

    result_list = []
    for city_index in range(len(city_list)):
        sql_group = """select DISTINCT pub_date,c_confirm_count from  new_pneumonia_count where pub_date in (select max(pub_date) from new_pneumonia_count where pub_date between "2020-01-01" and NOW() and city in ('"""+city_list[city_index]+"""') and province = '"""+province+"""' GROUP BY DATE_FORMAT(pub_date,'%Y-%m-%d')) and province = '"""+province+"""' and city='"""+city_list[city_index]+"""'ORDER BY pub_date """
        print(sql_group)
        mid = []
        mid.append(city_list[city_index])
        result_list.append(mid+get_result.get_select(sql_group))
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
        plt.subplot(len(city_list), 2, subplot_index)
        subplot_index += 1
        plt.plot(x, y, label=city_list[city_index], linewidth=10, markersize=60)
        # plt.xticks(rotation=45)
        # plt.xlabel('每日增长统计时间')
        plt.ylabel('每日增长人数')
        plt.title(city+' 截止到今日'+title_time+' 确诊:'+str(city_count_result[-1][-1])+'例', fontsize=60)
        for a, b in zip(x, y):
            plt.text(a, b, b, ha='center', va='baseline', fontsize=50)
        # plt.legend(loc='best', shadow=False, fontsize=60)
        plt.grid(alpha=1, linestyle='--')
        print(city)
        city_index += 1
        x.clear()
        y.clear()
    plt.savefig('各省疫情波形图/每日增长人数/'+province+'.svg')
