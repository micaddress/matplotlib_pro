# -- coding: utf-8 --
"""
    author:michael

    project:matplotlib_pro

    date:2020/2/4

"""
from matplotlib import pyplot as plt,font_manager
import matplotlib, pymysql, time
params = {
            'host' : '127.0.0.1',
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


# while True:
country_list = ['挪威', '美国', '意大利', '瑞典']
subplot_index = 0
font = {'family': 'STFangsong',
                'weight': 'bold',
                'size': 80}
matplotlib.rc('font', **font)
plt.figure(figsize=(80, 60), dpi=50)
plt.subplots_adjust(wspace=2, hspace=0.5)
for country in country_list:
    result_list = []
    sql_group = """select DISTINCT pub_date,country_confirm_count from  new_pneumonia_foreign_count 
                    where pub_date in (select max(pub_date) from new_pneumonia_foreign_count 
                    where pub_date between "2020-01-01" and NOW() 
                    and country = '"""+country+"""'
                    and country = '"""+country+"""' 
                    GROUP BY DATE_FORMAT(pub_date,'%Y-%m-%d')
                    ) 
                    and country = '"""+country+"""' and country='"""+country+"""'ORDER BY pub_date """
    print(sql_group)
    mid = []
    mid.append(country)
    mid = mid+get_select(sql_group)
    result_list.append(mid)
    x_date=[]
    y_confirm_count = []

    this_count = -1
    last_count = -1
    x = []
    y = []
    city_index = 0
    title_time = ''
    for city_count_result in result_list:
        city = city_count_result[0]
        print(city)
        city_count_result.remove(city)
        # title_time = str(city_count_result[0][0])
        for index in range(len(city_count_result)):
            if index+1 == len(city_count_result):
                break
            if city_count_result[index + 1][1] == '-':
                city_count_result[index + 1][1] = 0
            if city_count_result[index][1] == '-':
                city_count_result[index][1] = 0
            add_count = int(city_count_result[index + 1][1]) - int(city_count_result[index][1])
            if index == len(city_count_result) - 2:
                title_time = str(city_count_result[index + 1][0])
            result = str(city_count_result[index + 1][0]).split(' ')[0].split('20-0')[-1]
            a = str(int(result.split('-')[0]))
            b = str(int(result.split('-')[1]))
            # if int(b) % 3 == 0 or len(city_count_result) - 2:
            #     x.append(a + '-' + b)
            #     y.append(add_count)
            x.append(a + '-' + b)
            y.append(add_count)

    subplot_index += 1
    plt.subplot(len(country_list), 1, subplot_index)
    plt.text(0, 0, 'as', rotation=90)
    plt.plot(x, y, label=country, linewidth=10, markersize=60)
    plt.xticks(rotation=315)
    # plt.xlabel('每日增长统计时间')
    # plt.ylabel('每日增长人数')
    print(city_count_result[-1][-1])
    plt.title(city+' 截止到'+title_time+' 确诊:'+str(city_count_result[-1][-1])+'例', fontsize=100)
    for a, b in zip(x, y):
        plt.text(a, b, b, ha='center', va='baseline', fontsize=50)
    # plt.legend(loc='best', shadow=False, fontsize=60)
    plt.grid(alpha=1, linestyle='--')
    city_index += 1
plt.savefig('各省疫情波形图/国外.svg')
# time.sleep(60)