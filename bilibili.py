'''
Author: qqilin1213
Date: 2021-03-27 15:20:19
LastEditors: qqilin1213
LastEditTime: 2021-03-28 18:57:33
'''
import os

import xlwt
import requests
import datetime

from lxml import etree

# 使用代理
proxies = {"http": "**********"}

headers = {
    'user-agent': '*********'
}

base_url = 'https:'

url = 'https://www.bilibili.com/v/popular/rank/all'

# 存放所有的排行榜的网址
url_all = list()
# 存放排行榜的分类
list_sort = list()
# 存放排行榜的数据
list_all = list()
list_bangumi = list()
list_guochan = list()
list_guochuang = list()
list_documentary = list()
list_douga = list()
list_music = list()
list_dance = list()
list_game = list()
list_technology = list()
list_digital = list()
list_life = list()
list_food = list()
list_animal = list()
list_kichiku = list()
list_fashion = list()
list_ent = list()
list_cinephile = list()
list_movie = list()
list_tv = list()
list_origin = list()
list_rookie = list()

# 全部排行榜数据集
lists = [list_all, list_bangumi, list_guochan, list_guochuang, list_documentary, list_douga, list_music, list_dance, list_game, list_technology, list_digital,
         list_life, list_food, list_animal, list_kichiku, list_fashion, list_ent, list_cinephile, list_movie, list_tv, list_origin, list_rookie]

# 网址关键字与分类的字典
sorts_dire = {}

# 获取当前时间
today = datetime.datetime.today()
time = today.strftime("%Y-%m-%d")
# 生成名为当前时间的文件夹
try:
    os.makedirs(time)
except Exception:
    # print(result)
    pass

'''
@name: get_url
@msg: 解析网页并返回
@param url
@return html
'''


def get_url(url):
    response_data = requests.get(
        url=url, headers=headers, proxies=proxies).text
    html = etree.HTML(response_data)
    return html


'''
@name: get_all_url
@msg: 获取所有分类的网址
@param [list] target_list
@return [list] 全部网址
'''


def get_all_url(target_list):
    sorts = ['all', 'bangumi', 'guochan', 'guochuang', 'documentary', 'douga', 'music', 'dance', 'game', 'technology', 'digital', 'life',
             'food', 'animal', 'kichiku', 'fashion', 'ent', 'cinephile', 'movie', 'tv', 'origin', 'rookie']
    j = 0
    for i in target_list:
        sorts_dire[i] = sorts[j]
        j += 1
    # print(sorts_dire)
    base_link = 'https://www.bilibili.com/v/popular/rank/'
    for item in sorts:
        url_all.append(base_link+item)
    return url_all


'''
@name: get_sort
@msg: 获取不同排行榜的类别名
@param {str} url
@param {list} target_list
@return {list} target_list
'''


def get_sort(url, target_list):
    response_data = requests.get(
        url=url, headers=headers, proxies=proxies).text
    html = etree.HTML(response_data)
    sorts = html.xpath("//ul[@class='rank-tab']/li/text()")
    length = len(sorts)
    for i in range(length):
        sort = sorts[i]
        target_list.append(sort)
    return target_list


'''
@name: get_target_info
@msg: 获取该网页的全部信息
@param {str} url
@param {str} filename
@param {list} target_list
@return {list} target_list
'''


def get_target_info(url, filename, target_list):
    html = get_url(url)
    # 共同拥有
    rank = html.xpath("//div[@class='num']/text()")
    info_list_num = len(rank)
    # print(len(rank))
    titles = html.xpath("//div[@class='info']/a[@class='title']/text()")
    # print(title[0])
    # print(len(title))
    playnums = html.xpath("//i[@class='b-icon play']//following::text()[1]")
    danmunums = html.xpath("//i[@class='b-icon view']//following::text()[1]")
    scores = html.xpath("//div[@class='pts']/div/text()")
    vedio_urls = html.xpath("//div[@class='info']/a/@href")
    # 除 番剧，国产动画，纪录片，电影，电视剧  ，其他区域 独有的
    if (filename != "番剧" or filename != "国产动画" or filename != "纪录片" or filename != "电影" or filename != "电视剧"):
        # print(filename)
        authors = html.xpath(
            "//i[@class='b-icon author']//following::text()[1]")
        author_urls = html.xpath("//div[@class='detail']/a/@href")
    # # 番剧，国产动画，纪录片，电影，电视剧 独有
    if (filename == "番剧" or filename == "国产动画" or filename == "纪录片" or filename == "电影" or filename == "电视剧"):
        # print(url)
        pgc_infos = html.xpath("//div[@class='pgc-info']/text()")  # 番剧更新情况
        likes = html.xpath("//i[@class='fav']//following::text()[1]")  # 收藏量
        # print(pgc_infos)
        # print(likes)
        for i in range(info_list_num):
            num = rank[i]
            title = titles[i].replace('"', "'")
            pgc_info = pgc_infos[i]
            playnum = playnums[i].replace('\n', '').replace(' ', '')
            danmunum = danmunums[i].replace('\n', '').replace(' ', '')
            score = scores[i]
            vedio_url = base_url + vedio_urls[i][2:]
            like = likes[i].replace('\n', '').replace(' ', '')
            # target_list.append([num, vedio_url, title, author,playnum,danmunum,score])
            target_list.append({
                'rank': num,
                'vedio_url': vedio_url,
                'title': title,
                'pgc_info': pgc_info,
                'like': like,
                'playnum': playnum,
                'danmunum': danmunum,
                'score': score
            })
        return target_list
    # sorts = html.xpath("//ul[@class='rank-tab']/li/text()")
    else:
        for i in range(info_list_num):
            num = rank[i]
            title = titles[i].replace('"', "'")
            author = authors[i].replace('\n', '').replace(' ', '')
            playnum = playnums[i].replace('\n', '').replace(' ', '')
            danmunum = danmunums[i].replace('\n', '').replace(' ', '')
            score = scores[i]
            vedio_url = base_url + vedio_urls[i][2:]
            author_url = base_url + author_urls[i]
            # target_list.append([num, vedio_url, title, author,playnum,
            # danmunum,score])
            target_list.append({
                'rank': num,
                'vedio_url': vedio_url,
                'title': title,
                'author': author,
                'author_url': author_url,
                'playnum': playnum,
                'danmunum': danmunum,
                'score': score
            })
            # print(target_list)
        return target_list


'''
@name: write_Excel
@msg: 将爬取的数据写入Excel文件中
@param {str} url
@param {str} filename
@param {str} list
@return {*}
'''


def write_Excel(url, filename, list):
    workbook = xlwt.Workbook()  # 定义表格
    sheet = workbook.add_sheet("b站热门视频")  # 添加sheet的name
    xstyle = xlwt.XFStyle()  # 实例化表格样式对象
    xstyle.alignment.horz = 0x02  # 字体居中
    xstyle.alignment.vert = 0x01
    video_list = get_target_info(url, filename, list)
    if (filename == "番剧" or filename == "国产动画" or filename == "纪录片" or
            filename == "电影" or filename == "电视剧"):
        head = ['视频名', '更新情况', '收藏量', '排名', '播放量', '弹幕数', '综合得分']
        for h in range(len(head)):
            sheet.write(0, h, head[h], xstyle)
        i = 1
        for item in video_list:
            # 向单元格(视频名)添加该视频的超链接
            # 设置超链接
            title_data = 'HYPERLINK("' + \
                item["vedio_url"] + '";"' + item["title"] + '")'
            # print(title_data)
            sheet.col(0).width = int(256 * len(title_data) * 3 / 5)  # 设置列宽
            sheet.write(i, 0, xlwt.Formula(title_data), xstyle)
            sheet.write(i, 1, item["pgc_info"], xstyle)
            sheet.write(i, 2, item["like"], xstyle)
            sheet.write(i, 3, item["rank"], xstyle)
            sheet.write(i, 4, item["playnum"], xstyle)
            sheet.write(i, 5, item["danmunum"], xstyle)
            sheet.write(i, 6, item["score"], xstyle)
            i += 1
    else:
        head = ['视频名', '作者', '排名', '播放量', '弹幕数', '综合得分']
        for h in range(len(head)):
            sheet.write(0, h, head[h], xstyle)
        o = 1
        for item in video_list:
            # 向单元格(视频名)添加该视频的超链接
            # 设置超链接
            title_data = 'HYPERLINK("' + \
                item["vedio_url"] + '";"' + item["title"] + '")'
            # print(title_data)
            sheet.col(0).width = int(256 * len(title_data) * 3 / 5)  # 设置列宽
            sheet.write(o, 0, xlwt.Formula(title_data), xstyle)
            # 设置超链接
            name_data = 'HYPERLINK("' + item["author_url"] + \
                '";"' + item["author"] + '")'
            # print(name_data)
            sheet.col(1).width = int(256 * len(name_data) * 3 / 5)
            sheet.write(o, 1, xlwt.Formula(name_data), xstyle)
            sheet.write(o, 2, item["rank"], xstyle)
            sheet.write(o, 3, item["playnum"], xstyle)
            sheet.write(o, 4, item["danmunum"], xstyle)
            sheet.write(o, 5, item["score"], xstyle)
            o += 1
    # 如果文件存在，则将其删除
    newdir = os.path.dirname(__file__)     # 相对路径
    newpath = os.path.join(newdir, time)   # 新建文件夹路径
    file = "b站" + filename + "排行榜.xls"
    if os.path.exists(file):
        os.remove(file)
    workbook.save(newpath + "/" + file)


'''
@name: main
@msg: 主函数
'''
if __name__ == '__main__':
    sort_list = get_sort(url, list_sort)
    urls = get_all_url(sort_list)
    index = 0
    for url in urls:
        for key, value in sorts_dire.items():
            # base_url 的长度为 40
            if value == url[40:]:
                # print(key)
                # print(lists[index])
                # print(url)
                write_Excel(url, key, lists[index])
                print(url, key, "爬取完毕")

        index += 1

    # print(sort_list)
    # write_Excel()
