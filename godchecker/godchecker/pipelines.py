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
            + "mythology TEXT NOT NULL,"
            + "pronounciation TEXT,"
            + "alt_names TEXT,"
            + "gender TEXT,"
            + "type TEXT,"
            + "area_or_people TEXT,"
            + "celeb_or_feast_day TEXT,"
            + "in_charge_of TEXT,"
            + "area_of_expertise TEXT,"
            + "role TEXT,"
            + "good_evil TEXT,"
            + "popularity_index TEXT,"
            + "birth_death_dates TEXT,"
            + "name_meaning TEXT,"
            + "associated_with TEXT"
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
                + "(name, mythology, pronounciation, alt_names, gender, type, area_or_people, celeb_or_feast_day,"
                + "in_charge_of, area_of_expertise, role, good_evil, popularity_index, birth_death_dates, name_meaning, associated_with) "
                + "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (item.get('name'), item.get('mythology'), item.get('pronounciation'), item.get('alt_names'), item.get('gender'), item.get('type'),
                item.get('area_or_people'), item.get('celeb_or_feast_day'), item.get('in_charge_of'), item.get('area_of_expertise'),
                item.get('role'), item.get('good_evil'), item.get('popularity_index'), item.get('birth_death_dates'), item.get('name_meaning'), item.get('associated_with'))
            )

            self.connection.commit()

            logging.debug(f'Item stored: {item}')
        return item
        
