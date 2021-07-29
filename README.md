# BIlibiliTop
爬取B站排行榜的全部信息
# 目标网站:

https://www.bilibili.com/v/popular/rank/all                     [全站]

https://www.bilibili.com/v/popular/rank/bangumi           [番剧]

https://www.bilibili.com/v/popular/rank/guochan           [国产动画]

https://www.bilibili.com/v/popular/rank/guochuang       [国创相关]

https://www.bilibili.com/v/popular/rank/documentary    [纪录片]

https://www.bilibili.com/v/popular/rank/douga               [动画]

https://www.bilibili.com/v/popular/rank/music               [音乐]

https://www.bilibili.com/v/popular/rank/dance               [舞蹈]

https://www.bilibili.com/v/popular/rank/game                [游戏]

https://www.bilibili.com/v/popular/rank/technology        [知识]

https://www.bilibili.com/v/popular/rank/digital                [数码]

https://www.bilibili.com/v/popular/rank/life                     [生活]

https://www.bilibili.com/v/popular/rank/food                  [美食]

https://www.bilibili.com/v/popular/rank/animal               [动物圈]

https://www.bilibili.com/v/popular/rank/kichiku              [鬼畜]

https://www.bilibili.com/v/popular/rank/fashion              [时尚]

https://www.bilibili.com/v/popular/rank/ent                    [娱乐]

https://www.bilibili.com/v/popular/rank/cinephile           [影视]

https://www.bilibili.com/v/popular/rank/movie                [电影]

https://www.bilibili.com/v/popular/rank/tv                      [电视剧]

https://www.bilibili.com/v/popular/rank/origin                 [原创]

https://www.bilibili.com/v/popular/rank/rookie                [新人]
# 任务目标：爬取B站排行榜不同分类的全部内容
![img](https://docimg5.docs.qq.com/image/gVNcB-ozfoHF-ExfYj9-lg?w=1352&h=307)
# 实验过程
使用Xpath 获取网页信息
## 获取全部分类
```xpath
//ul[@class='rank-tab']/li/text()
```
![img](https://docimg2.docs.qq.com/image/-4Cimklb7opYv-SHb8INBg?w=1168&h=544)
## 获取排名
```xpath
//div[@class='num']/text()
```
![img](https://docimg3.docs.qq.com/image/wWKZgFJLgYsa5Q-bZByeIg?w=1364&h=539)
## 获取视频标题
```xpath
//div[@class='info']/a[@class='title']/text()
```
![img](https://docimg6.docs.qq.com/image/auZs_3PzpJmhMnfV4wpsIQ?w=1365&h=571)
## 获取播放量
```xpath
//i[@class='b-icon play']//following::text()[1]
```
![img](https://docimg5.docs.qq.com/image/-ytKPgbqh6WypzxLqHyOCg?w=1366&h=556)
## 获取弹幕数
```xpath
//i[@class='b-icon view']//following::text()[1]
```
![img](https://docimg5.docs.qq.com/image/XKrhMzeg2gV9IGyNkWWJdw?w=1363&h=532)
## 获取综合得分
```xpath
//div[@class='pts']/div/text()
```
![img](https://docimg1.docs.qq.com/image/PPHpnv3wDom2XLoFZDVy8g?w=1360&h=523)
## 获取网址
```xpath
//div[@class='info']/a/@href
```
![img](https://docimg4.docs.qq.com/image/EdADJ5mR5FmIPqdwJsDrYw?w=1365&h=509)
## 获取作者
```xpath
//i[@class='b-icon author']//following::text()[1]
```
![img](https://docimg8.docs.qq.com/image/qA-3XnOSh42P_pa2HbxyoA?w=1366&h=551)

## 获取作者个人空间
```xpath
//div[@class='detail']/a/@href
```
![img](https://docimg5.docs.qq.com/image/gUuy_W_igp_zB2-yuoD7Ow?w=1366&h=552)

## 获取更新情况
```xpath
//div[@class='pgc-info']/text()
```
![img](https://docimg10.docs.qq.com/image/3W5kITuX-WBc0M5PE8FtLA?w=1920&h=896)

## 获取收藏量
```
//i[@class='fav']//following::text()[1]
```
![img](https://docimg7.docs.qq.com/image/3x_G4wcR-FFJ2hZ1bi_4bQ?w=1920&h=902)
