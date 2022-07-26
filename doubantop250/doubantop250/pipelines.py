# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter

class DbPipeline:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306,
                                                user='root', password='123456',
                                                database='py', charset='utf8mb4',
                                                autocommit=True)
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()


    def process_item(self, item, spider):
        link = item.get('link' , '')
        img_src = item.get('img_src' , '')
        chinese_name = item.get('chinese_name' , '')
        foreign_name = item.get('foreign_name' , '')
        score = item.get('score' , '')
        number_ratings = item.get('number_ratings' , '')
        overview = item.get('overview' , '')
        details = item.get('details' , '')
        self.cursor.execute(
            'insert into tb_douban (info_link, pic_link, cname, fname, score, rated, info, introduction) values ( %s, %s, %s, %s, %s, %s, %s, %s)',(link, img_src, chinese_name, foreign_name, score, number_ratings, overview, details)
        )
        return item

# class DbPipeline:
#     def __init__(self):
#         self.conn = pymysql.connect(host='127.0.0.1', port=3306,
#                                                 user='root', password='123456',
#                                                 database='py', charset='utf8mb4',
#                                                 autocommit=True)
#         self.cursor = self.conn.cursor()
#         self.data = []
#
#     def close_spider(self, spider):
#         if len(self.data) > 0:
#             self._write_to_db()
#         self.conn.close()
#
#
#
#     def process_item(self, item, spider):
#         link = item.get('link' , '')
#         img_src = item.get('img_src' , '')
#         chinese_name = item.get('chinese_name' , '')
#         foreign_name = item.get('foreign_name' , '')
#         score = item.get('score' , '')
#         number_ratings = item.get('number_ratings' , '')
#         overview = item.get('overview' , '')
#         details = item.get('details' , '')
#         self.data.append((link, img_src, chinese_name, foreign_name, score, number_ratings, overview, details))
#         if len(self.data) == 75:
#             self._write_to_db()
#             self.data.clear()
#         # self.cursor.execute(
#         #     'insert into tb_douban (info_link, pic_link, cname, fname, score, rated, info, introduction) values ( %s, %s, %s, %s, %s, %s, %s, %s)',(link, img_src, chinese_name, foreign_name, score, number_ratings, overview, details)
#         # )
#         return item
#
#     def _write_to_db(self):
#         self.cursor.executemany(
#             'insert into tb_douban (info_link, pic_link, cname, fname, score, rated, info, introduction) values ( %s, %s, %s, %s, %s, %s, %s, %s)',
#             self.data)
#         self.conn.commit()
#


class Doubantop250Pipeline:
    def process_item(self, item, spider):
        return item


