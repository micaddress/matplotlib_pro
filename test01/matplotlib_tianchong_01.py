# encoding='utf-8'
import test.get_gold_DB as gold_DB
import test.get_huilv_DB as huilv_DB
import numpy as np
import matplotlib.pyplot as plt

huilv_sql = 'select xianchao_In from meiyuan where pull_date = (select max(pull_date) from meiyuan)'
huilv_DB.cursor.execute(huilv_sql)
meiyuan = huilv_DB.cursor.fetchone()
meiyuan = meiyuan[0]/100
print(meiyuan)

cny_sql = 'select ke from gold_price where money_code = "CNY" order by pub_time'
gold_DB.cursor.execute(cny_sql)
gold_tuples_cny = gold_DB.cursor.fetchall()
cny_gold_list = []
for gold_tuple in gold_tuples_cny:
    cny_gold_list.append(gold_tuple[0]/meiyuan)

# plt.figure()
# plt.plot(np.arange(len(gold_list)),gold_list,c='red')
# plt.show()

usd_sql = 'select ke from gold_price where money_code = "USD" order by pub_time'
gold_DB.cursor.execute(usd_sql)
gold_tuples_usd = gold_DB.cursor.fetchall()
usd_gold_list = []
for gold_tuple in gold_tuples_usd:
    usd_gold_list.append(gold_tuple[0])

plt.figure()
# plt.plot(np.arange(len(cny_gold_list)),cny_gold_list,c='red')
a = np.arange(len(cny_gold_list))
plt.plot(a,cny_gold_list,c='red')
# plt.xlim([0,30000])
ax = plt.gca()
ax.locator_params(nbins=3000)
plt.show()
print(type(a))
# plt.savefig('saving4.png')

# plt.figure()
# plt.plot(np.arange(len(usd_gold_list)),usd_gold_list,c='blue')
# plt.show()
#
# plt.figure()
# plt.plot(np.arange(len(cny_gold_list)),cny_gold_list,c='red')
# plt.plot(np.arange(len(usd_gold_list)),usd_gold_list,c='blue')
# plt.show()
# meiyuan_zhesuanjia_numpy = np.array(meiyuan_zhesuanjia_list)
# meiyuan_pullDate_numpy = np.array(meiyuan_pullDate_list)
# print(meiyuan_zhesuanjia_numpy)
# print(meiyuan_pullDate_numpy)

# a = np.arange(len(meiyuan_zhesuanjia_list))
# print(a)
