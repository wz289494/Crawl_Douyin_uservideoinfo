# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pandas as pd

class DouyinuserPipeline:
    def open_spider(self, spider):
        # 创建一个空的 DataFrame，用于存储数据
        self.df = pd.DataFrame(columns=['视频链接','视频标题','视频获赞'])

    def process_item(self, item, spider):
        # 将项目添加到 DataFrame 中
        new_data = pd.DataFrame({
            '视频链接': [item['video_url']],
            '视频标题': [item['video_name']],
            '视频获赞': [item['video_like']]
        })
        self.df = pd.concat([self.df, new_data], ignore_index=True)
        return item

    def close_spider(self, spider):
        # 将 DataFrame 写入 xlsx 文件
        self.df.to_excel('学习机测评（宇辉老师）.xlsx', index=False)
