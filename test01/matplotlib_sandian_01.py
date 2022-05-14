# encoding='utf-8'
import test01.get_huilv_DB as huilv_DB
import numpy as np
import matplotlib.pyplot as plt
# a = [1,2,3,4]
# print(a)
# xl = np.array(a)
# print(type(xl))
# print(xl)
#
# nu1 = np.arange(20)
# print(nu1)
meiyuan_sql = 'select zhesuanjia,pull_date from meiyuan'
huilv_DB.cursor.execute(meiyuan_sql)
meiyuan_tuples = huilv_DB.cursor.fetchall()
meiyuan_zhesuanjia_list = []
meiyuan_pullDate_list = []
for meiyuan_tuple in meiyuan_tuples:
    meiyuan_zhesuanjia_list.append(meiyuan_tuple[0])
    meiyuan_pullDate_list.append(meiyuan_tuple[1])
print(meiyuan_pullDate_list)
print(meiyuan_zhesuanjia_list)
plt.scatter(np.arange(len(meiyuan_zhesuanjia_list)),meiyuan_zhesuanjia_list)
plt.show()

# meiyuan_zhesuanjia_numpy = np.array(meiyuan_zhesuanjia_list)
# meiyuan_pullDate_numpy = np.array(meiyuan_pullDate_list)
# print(meiyuan_zhesuanjia_numpy)
# print(meiyuan_pullDate_numpy)

# a = np.arange(len(meiyuan_zhesuanjia_list))
# print(a)
