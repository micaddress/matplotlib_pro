# -- coding: utf-8 --
import requests
from lxml import etree
import json
import re
import os

class kugou():

    def startkugou(self):
        for i in range(23, 24):
            print(i)
            res = requests.get('https://www.kugou.com/yy/rank/home/%s-8888.html?from=rank' % str(i))
            self.get_song(res)

    def get_song(self, res):
        html = etree.HTML(res.content.decode('utf8'))
        content = html.xpath('//script[10]')
        content2 = content[0].text
        # 解析出json列表，类型是str
        content1 = content2.split('global.features =')[1].split('(function()')[0].strip()[0:-1]
        try:
            # 转换成json数据 /html/body/div[1]/div[3]
            content = json.loads(content1)
            for i in range(len(content)):
                hash = content[i]["Hash"]
                file_name = content[i]["FileName"]
                hash_url = "http://www.kugou.com/yy/index.php?r=play/getdata&hash=" + hash
                hash_content = requests.get(hash_url)
                play_url = ''.join(re.findall('"play_url":"(.*?)"', hash_content.text))
                lyrics = ''.join(re.findall('"lyrics":"(.*?)"', hash_content.text))
                real_download_url = play_url.replace("\\", "")
                try:
                    # if os.path.exists('kugou/' + file_name + '.txt'):
                    #     print(file_name + " 歌词已经存在")
                    #     # continue
                    # else:
                    with open('kugou/' + file_name + '.txt', 'w', encoding='utf8')as f:
                        f.write(lyrics.encode('utf8').decode('unicode_escape'))
                    print(file_name + "歌词已下载完成！")
                    # if os.path.exists('kugou/' + file_name + '.mp3'):
                    #     print(file_name+" 歌曲已经存在")
                    #     # continue
                    # else:
                    with open('kugou/' + file_name + ".mp3", "wb")as fp:
                        fp.write(requests.get(real_download_url).content)
                    print(file_name + "歌曲已下载完成！")
                except OSError as e:
                    print("出现异常" + file_name)
                    file_name = self.validateTitle(file_name)
                    # if os.path.exists('kugou/' + file_name + '.txt'):
                    #     print(file_name + " 歌词已经存在")
                    #     # continue
                    # else:
                    with open('kugou/' + file_name + '.txt', 'w', encoding='utf8')as f:
                        f.write(lyrics.encode('utf8').decode('unicode_escape'))
                    print(file_name + "歌词已下载完成！")
                    # if os.path.exists('kugou/' + file_name + '.mp3'):
                    #     print(file_name + " 歌曲已经存在")
                    #     # continue
                    # else:
                    with open('kugou/' + file_name + ".mp3", "wb")as fp:
                        fp.write(requests.get(real_download_url).content)
                    print(file_name + "歌曲已下载完成！")


        except json.decoder.JSONDecodeError as e:
            print(e)
            print(content2)
            content1 = content2.split('global.features =')[1].strip().split('(function() {')[0].strip()
            content1 = content1[0:-1]
            print(content1)

    def validateTitle(self, file_name):
        """ 将 title 名字 规则化
        :param title: title name 字符串
        :return: 文件命名支持的字符串        """
        rstr = r"[\=\(\)\,\/\\\:\*\?\"\<\>\|\' ']"  # '= ( ) ， / \ : * ? " < > |  '   还有空格
        new_title = re.sub(rstr, "_", file_name)  # 替换为下划线
        return new_title

if __name__ == '__main__':
    kugou().startkugou()







