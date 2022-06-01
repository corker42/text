# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dytt2.items import Dytt2Item

class Dytt2Spider(CrawlSpider):
    name = 'dytt2_'
    allowed_domains = ['dytt8.net']
    start_urls = ['https://dytt8.net/html/gndy/dyzz/list_23_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'.+/gndy/dyzz/list_23_[1-3].html'),  follow=True),
        Rule(LinkExtractor(allow=r'.+gndy/dyzz/\d{8}/\d{5}.html'),  follow=False, callback='parse_item'),
    )

    def parse_item(self, response):
        title, year, area, category, lg, zm, show, duration, director, bjs, actors, profiles = ('暂无,' * 12).split(',')[
                                                                                               :-1]
        # 电影名：
        title = response.xpath('//h1/font[@color="#07519a"]/text()').get()
        # 获取其余信息
        infos = response.xpath('//div[@id="Zoom"]//text()').getall()

        def parse_info(info, rule):
            return info.replace(rule, '').strip()

        for index, info in enumerate(infos):
            # print(index,info)
            # 得到年代
            if info.startswith('◎年　　代'):
                year = parse_info(info, '◎年　　代')
            # 产地
            if info.startswith('◎产　　地'):
                area = parse_info(info, '◎产　　地')

                # print(area)
            # 类别
            if info.startswith('◎类　　别'):
                category = parse_info(info, '◎类　　别')
                # print(category)
            # 语言
            if info.startswith('◎语　　言'):
                lg = parse_info(info, '◎语　　言')
                # print(lg)
            # 字幕
            if info.startswith('◎字　　幕'):
                zm = parse_info(info, '◎字　　幕')
                # print(zm)
            # 上映日期
            if info.startswith('◎上映日期'):
                show = parse_info(info, '◎上映日期')
                # print(show)
            # 片长
            if info.startswith('◎片　　长'):
                duration = parse_info(info, '◎片　　长')
                # print(duration)
            # 导演
            if info.startswith('◎导　　演'):
                director = parse_info(info, '◎导　　演')
                # print(director)
            # ◎编　　剧
            if info.startswith('◎编　　剧'):
                bj = parse_info(info, '◎编　　剧')
                bjs = [bj]
                for x in range(index + 1, len(infos)):
                    bj = infos[x].strip()
                    if bj.startswith('◎'):
                        break
                    bjs.append(bj)
                bjs = "|".join(bjs)
                # print(bjs)
            # ◎主　　演
            if info.startswith('◎主　　演'):
                actor = parse_info(info, '◎主　　演')
                actors = [actor]
                for x in range(index + 1, len(infos)):
                    actor = infos[x].strip()
                    if actor.startswith('◎'):
                        break
                    actors.append(actor)
                actors = "|".join(actors)
                # print(actors)
            # 简介
            if info.startswith('◎简　　介'):
                profile = parse_info(info, '◎简　　介')
                profiles = [profile]
                for x in range(index + 1, len(infos)):
                    profile = infos[x].strip()
                    if profile.startswith('磁'):
                        break
                    profiles.append(profile)
                profiles = ''.join(profiles)
                print(profiles)
        item = Dytt2Item(title=title, year=year, area=area, category=category,
                         lg=lg, zm=zm, show=show, duration=duration,
                         director=director, bjs=bjs, actors=actors, profiles=profiles)
        yield item



