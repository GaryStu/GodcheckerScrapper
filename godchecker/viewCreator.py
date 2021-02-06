import logging
import sqlite3


class ViewCreator():
    def __init__(self):
        self.connection = sqlite3.connect("god.db")
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.create_mythology_view()
        self.create_statistics_view()

    def create_mythology_view(self):
        # Create a separate view based on each mythology
        mythologies = self.cursor.execute("SELECT DISTINCT mythology FROM gods;").fetchall()
        for row in mythologies:
            mythology = row['mythology'].replace(" ", "_")
            view_name = mythology + "_gods"
            self.cursor.execute("DROP VIEW IF EXISTS " + view_name + ";")
            self.cursor.execute(
                "CREATE VIEW " + view_name + " AS " + 
                "SELECT * FROM gods WHERE mythology='" + mythology + "';",
            )
            self.connection.commit()
        
    def create_statistics_view(self):
        # Create a view for general statistics for each mythology
        mythologies = self.cursor.execute("SELECT DISTINCT mythology FROM gods;").fetchall()
        self.cursor.execute(
            "CREATE VIEW statistics AS " +
            "SELECT * FROM " + 
            "(SELECT mythology, COUNT(DISTINCT NAME) as distinct_name_count FROM gods GROUP BY mythology) " +
            "NATURAL JOIN " +
            "(SELECT mythology, COUNT(DISTINCT NAME) as good_gods_count FROM gods WHERE good_evil ='GREAT' OR good_evil='GOOD' OR good_evil='OKAY' GROUP BY mythology) " +
            "NATURAL JOIN " +
            "(SELECT mythology, COUNT(DISTINCT NAME) as evil_gods_count FROM gods WHERE good_evil ='NOT OKAY' OR good_evil='BAD' OR good_evil='TOTALLY EVIL' GROUP BY mythology) " +
            "NATURAL JOIN " +
            "(SELECT mythology, COUNT(*) as good_male_count FROM gods WHERE gender='Male' AND (good_evil ='GREAT' OR good_evil='GOOD' OR good_evil='OKAY') GROUP BY mythology); " +
            "NATURAL JOIN " +
            "(SELECT mythology, COUNT(*) as evil_male_count FROM gods WHERE gender='Male' AND (good_evil ='NOT OKAY' OR good_evil='BAD' OR good_evil='TOTALLY EVIL') GROUP BY mythology); " +
            "NATURAL JOIN " +
            "(SELECT mythology, COUNT(*) as good_female_count FROM gods WHERE gender='Female' AND (good_evil ='GREAT' OR good_evil='GOOD' OR good_evil='OKAY') GROUP BY mythology); " +
            "NATURAL JOIN " +
            "(SELECT mythology, COUNT(*) as evil_female_count FROM gods WHERE gender='Female' AND (good_evil ='NOT OKAY' OR good_evil='BAD' OR good_evil='TOTALLY EVIL') GROUP BY mythology); " +
            "NATURAL JOIN " +

        )



        
        


if __name__ == '__main__':
    viewCreator = ViewCreator()
    viewCreator.create_mythology_view()
    