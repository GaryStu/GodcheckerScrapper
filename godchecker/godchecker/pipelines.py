# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from typing import Optional
import logging
import sqlite3

class GodcheckerPipeline(object):
    def __init__(self):
        self.connection = sqlite3.connect('god.db')
        self.cursor = self.connection.cursor()
        self.connection.row_factory = sqlite3.Row
        self.init_db()

    def init_db(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS gods ("
            + "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
            + "name TEXT UNIQUE NOT NULL,"
            + "pronounciation TEXT,"
            + "alt_names TEXT,"
            + "gender TEXT NOT NULL,"
            + "type TEXT NOT NULL,"
            + "area_or_people TEXT NOT NULL,"
            + "celeb_or_feast_day TEXT NOT NULL,"
            + "in_charge_of TEXT NOT NULL,"
            + "area_of_expertise TEXT NOT NULL,"
            + "role TEXT NOT NULL,"
            + "good_evil TEXT NOT NULL,"
            + "popularity_index TEXT NOT NULL"
            + ");"
        )
        self.connection.commit()

    def process_item(self, item, spider):
        self.cursor.exeucte("SELECT * FROM gods WHERE name=?", item['name'])
        result = self.cursor.fetchone()
        if result:
            logging.debug(f'Item is already in database: {item}')
        else :
            self.cursor.execute(
                "INSERT INTO gods "
                + "(name, pronounciation, alt_names, gender, type, area_or_people, celeb_or_feast_day,"
                + "in_charge_of, area_of_expertise, role, good_evil, popularity_index) "
                + "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (item['name'], item['pronounciation'], item['alt_names'], item['gender'], item['type'],
                item['area_or_people'], item['celeb_or_feast_day'], item['in_charge_of'], item['area_of_expertise'],
                item['role'], item['good_evil'], item['popularity_index'])
            )

            self.connection.commit()

            logging.debug(f'Item stored: {item}')
        return item
        
