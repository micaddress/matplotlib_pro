# -- coding: utf-8 --
"""
    author:michael

    project:matplotlib_pro

    date:2020/2/4

"""
import test01.get_new_pneumonia_DB as get_np_DB


def get_select(sql):

    get_np_DB.cursor.execute(sql)
    result = get_np_DB.cursor.fetchall()
    result_list = list(result)

    return result_list





