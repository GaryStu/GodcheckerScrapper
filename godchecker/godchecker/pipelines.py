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
            + "area_or_people TEXT,"
            + "celeb_or_feast_day TEXT NOT NULL,"
            + "in_charge_of TEXT,"
            + "area_of_expertise TEXT,"
            + "role TEXT,"
            + "good_evil TEXT NOT NULL,"
            + "popularity_index TEXT,"
            + "birth_death_dates TEXT"
            + ");"
        )
        self.connection.commit()

    def process_item(self, item, spider):
        # logging.debug(f'{item}')
        self.cursor.execute("SELECT * FROM gods WHERE name=?", (item['name'],))
        result = self.cursor.fetchone()
        if result:
            logging.debug(f'Item is already in database: {item}')
        else :
            self.cursor.execute(
                "INSERT INTO gods "
                + "(name, pronounciation, alt_names, gender, type, area_or_people, celeb_or_feast_day,"
                + "in_charge_of, area_of_expertise, role, good_evil, popularity_index) "
                + "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                # (item['name'], item['pronounciation'], item['alt_names'], item['gender'], item['type'],
                # item['area_or_people'], item['celeb_or_feast_day'], item['in_charge_of'], item['area_of_expertise'],
                # item['role'], item['good_evil'], item['popularity_index'])
                (item.get('name'), item.get('pronounciation'), item.get('alt_names'), item.get('gender'), item.get('type'),
                item.get('area_or_people'), item.get('celeb_or_feast_day'), item.get('in_charge_of'), item.get('area_of_expertise'),
                item.get('role'), item.get('good_evil'), item.get('popularity_index'))
            )

            self.connection.commit()

            logging.debug(f'Item stored: {item}')
        return item
        
