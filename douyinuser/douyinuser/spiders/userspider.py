import scrapy
from bs4 import BeautifulSoup
from douyinuser.items import DouyinuserItem


class UserspiderSpider(scrapy.Spider):
    name = "userspider"
    user_url = 'https://www.douyin.com/user/MS4wLjABAAAAf1dw9GBXb2zJRltBLO5gYsQJ80cIwSPeYAIeJ6lKuYQGcTn7Z1537gtVIR0SnamB'

    def start_requests(self):

        yield scrapy.Request(url=self.user_url, callback=self.parse)

    def parse(self, response):
        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 定位到特定的ul元素
        target_ul = soup.select_one(
            '#douyin-right-container > div:nth-of-type(2) > div > div > div:nth-of-type(3) > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > ul')

        # 确保ul元素被找到
        if target_ul:
            # 遍历ul下的所有li标签
            li_tags = target_ul.find_all('li')

        for li in li_tags:
            # 在每个li标签下找到a标签
            a_tag = li.find('a')

            # 提取a标签的href属性
            href = a_tag['href'] if a_tag else None
            # 构造新的视频链接
            video_link = f'https://www.douyin.com/video/{href.split("/")[-1]}' if href else None

            # 在a标签内找到img标签
            img_tag = a_tag.find('img') if a_tag else None

            # 提取img标签的alt属性
            alt_text = img_tag['alt'] if img_tag else None

            # 在每个li标签下找到目标的span标签
            like_span = li.select_one('div a div span.YzDRRUWc')

            # 提取span标签中的文本，即点赞数
            likes = like_span.get_text() if like_span else None

            # 数据储存
            item = DouyinuserItem()
            item['video_url'] = video_link
            item['video_name'] = alt_text
            item['video_like'] = likes

            print(item)

            yield item

