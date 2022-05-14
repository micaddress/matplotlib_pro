# encoding='utf-8'
import test.get_gold_DB as gold_DB
import numpy as np
import matplotlib.pyplot as plt
meiyuan_sql = 'select ke from gold_price where money_code = "USD" order by pub_time'
gold_DB.cursor.execute(meiyuan_sql)
gold_tuples = gold_DB.cursor.fetchall()
gold_list = []
for gold_tuple in gold_tuples:
    gold_list.append(gold_tuple[0])
# plt.scatter(np.arange(len(gold_list)),gold_list,s=0.1,c='blue')
plt.plot(np.arange(len(gold_list)),gold_list,c='red')
plt.show()

# meiyuan_zhesuanjia_numpy = np.array(meiyuan_zhesuanjia_list)
# meiyuan_pullDate_numpy = np.array(meiyuan_pullDate_list)
# print(meiyuan_zhesuanjia_numpy)
# print(meiyuan_pullDate_numpy)

# a = np.arange(len(meiyuan_zhesuanjia_list))
# print(a)
