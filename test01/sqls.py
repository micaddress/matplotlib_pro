# -- coding: utf-8 --
"""
    author:michael

    project:matplotlib_pro

    date:2020/6/4

"""
import os
path = "c:\\Users\\Administrator\\Desktop\\2"
# 获取当前文件夹中的文件名称列表
filenames = os.listdir(path)
result = path + "\\sqls.txt"
# 打开当前目录下的result.txt文件，如果没有则创建
file = open(result, 'w+', encoding="utf-8")
# 向文件中写入字符

# 先遍历文件名
for filename in filenames:
    filepath = path + '/'
    filepath = filepath + filename
    f_n = filename.split('.')[0]
    file.write('''
        SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for '''+f_n+'''
-- ----------------------------
DROP TABLE IF EXISTS `'''+f_n+'''`;
CREATE TABLE `'''+f_n+'''`  (
  `id` bigint(20) NOT NULL,
  `recordtime` datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  `province` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `city` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `total_sales` float(255, 0) NULL DEFAULT NULL,
  `area` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `area_sales` bigint(255) NULL DEFAULT NULL,
  `street` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `street_sales` bigint(255) NULL DEFAULT NULL,
  `street_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `detail_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `xiaoqu_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `room_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `room_mianji` float(255, 2) NULL DEFAULT NULL,
  `saled_price` float(255, 1) NULL DEFAULT NULL,
  `until_price` float(255, 1) NULL DEFAULT NULL,
  `sale_price` float(255, 2) NULL DEFAULT NULL,
  `saled_time` int(255) NULL DEFAULT NULL,
  `danwei` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `chaoxiang` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `zhuangxiu` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `build_year` int(255) NULL DEFAULT NULL,
  `floors` int(255) NULL DEFAULT NULL,
  `infloor` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `deal_date` int(11) NULL DEFAULT NULL,
  `danwei_type` bigint(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `index_'''+f_n+'''`(`detail_url`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

    ''')
    # 遍历单个文件，读取行数
    # for line in open(filepath, encoding="utf-8"):
    #     file.writelines(line)
    # file.write('\n')
    print(filename)
# 关闭文件
file.close()