# encoding='utf-8'
import test.get_lianjia_DB as lianjia_DB

lianjia_sql = "SELECT TABLE_NAME,TABLE_ROWS FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA like 'michael_lianjia'"
lianjia_DB.cursor.execute(lianjia_sql)
table_names_results = lianjia_DB.cursor.fetchall()
for tn in table_names_results:
    table_name = tn[0]
    table_count = tn[1]
    print(table_name,table_count)
    # lianjia_DB.cursor.execute("select count(*) from "+table_name)
    # count_result = lianjia_DB.cursor.fetchone()
    # if count_result[0] == table_count:
    #     print('yes')
    # else:
    #     print('no')









