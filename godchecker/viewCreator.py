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
        # mythologies = self.cursor.execute("SELECT DISTINCT mythology FROM gods;").fetchall()
        
        self.cursor.execute("DROP VIEW IF EXISTS 'statistics';")
        self.cursor.execute(
            "CREATE VIEW statistics AS " +
            "SELECT * FROM " +
            "(SELECT mythology, COUNT(name) as distinct_name_count FROM gods GROUP BY mythology) " +
            "NATURAL JOIN " +
            "(WITH cte(mythology, count) AS (SELECT mythology, COUNT(name) FROM gods WHERE good_evil in ('GREAT', 'GOOD', 'OKAY') GROUP BY mythology)  " +
            "SELECT mythology, 0 AS good_gods_count FROM (SELECT mythology FROM gods EXCEPT SELECT mythology FROM cte) UNION SELECT * FROM cte) " +
            "NATURAL JOIN " +
            "(WITH cte(mythology, count) AS (SELECT mythology, COUNT(name) FROM gods WHERE good_evil in ('NOT OKAY', 'BAD', 'TOTALLY EVIL') GROUP BY mythology)  " +
            "SELECT mythology, 0 AS evil_gods_count FROM (SELECT mythology FROM gods EXCEPT SELECT mythology FROM cte) UNION SELECT * FROM cte) " +
            "NATURAL JOIN " +
            "(WITH cte(mythology, count) AS (SELECT mythology, COUNT(name) FROM gods WHERE good_evil='NEUTRAL' GROUP BY mythology)  " +
            "SELECT mythology, 0 AS neutral_gods_count FROM (SELECT mythology FROM gods EXCEPT SELECT mythology FROM cte) UNION SELECT * FROM cte) " +
            "NATURAL JOIN " +
            "(WITH cte(mythology, count) AS (SELECT mythology, COUNT(name) FROM gods WHERE gender='Male' AND (good_evil in ('NOT OKAY', 'BAD', 'TOTALLY EVIL')) GROUP BY mythology)  " +
            "SELECT mythology, 0 AS evil_males_count FROM (SELECT mythology FROM gods EXCEPT SELECT mythology FROM cte) UNION SELECT * FROM cte) " +
            "NATURAL JOIN " +
            "(WITH cte(mythology, count) AS (SELECT mythology, COUNT(name) FROM gods WHERE gender='Female' AND (good_evil in ('NOT OKAY', 'BAD', 'TOTALLY EVIL')) GROUP BY mythology)  " +
            "SELECT mythology, 0 AS evil_females_count FROM (SELECT mythology FROM gods EXCEPT SELECT mythology FROM cte) UNION SELECT * FROM cte) " +
            "NATURAL JOIN " +
            "(WITH cte(mythology, count) AS (SELECT mythology, COUNT(name) FROM gods WHERE gender='Male' AND (good_evil in ('GREAT', 'GOOD', 'OKAY')) GROUP BY mythology)  " +
            "SELECT mythology, 0 AS good_males_count FROM (SELECT mythology FROM gods EXCEPT SELECT mythology FROM cte) UNION SELECT * FROM cte) " +
            "NATURAL JOIN " +
            "(WITH cte(mythology, count) AS (SELECT mythology, COUNT(name) FROM gods WHERE gender='Female' AND (good_evil in ('GREAT', 'GOOD', 'OKAY')) GROUP BY mythology)  " +
            "SELECT mythology, 0 AS good_females_count FROM (SELECT mythology FROM gods EXCEPT SELECT mythology FROM cte) UNION SELECT * FROM cte) " +
            "NATURAL JOIN " +
            "(WITH cte(mythology, count) AS (SELECT mythology, COUNT(DISTINCT type) FROM gods GROUP BY mythology) " +
            "SELECT mythology, 0 AS distinct_types_count FROM (SELECT mythology FROM gods EXCEPT SELECT mythology FROM cte) UNION SELECT * FROM cte) " +
            "NATURAL JOIN " +
            "(WITH cte(mythology, count) AS (SELECT mythology, COUNT(DISTINCT celeb_or_feast_day) FROM gods GROUP BY mythology) " +
            "SELECT mythology, 0 AS feast_day_count FROM (SELECT mythology FROM gods EXCEPT SELECT mythology FROM cte) UNION SELECT * FROM cte) " +
            "NATURAL JOIN " +
            "(WITH cte(mythology, count) AS (SELECT mythology, COUNT(DISTINCT area_of_expertise) FROM gods GROUP BY mythology)  " +
            "SELECT mythology, 0 AS area_of_expertise_count FROM (SELECT mythology FROM gods EXCEPT SELECT mythology FROM cte) UNION SELECT * FROM cte) " +
            "NATURAL JOIN " +
            "(SELECT mythology, AVG(CAST(popularity_index AS INT)) FROM gods GROUP BY mythology) " +
            ";"
        )
        self.connection.commit()



        
        


if __name__ == '__main__':
    viewCreator = ViewCreator()
    viewCreator.create_mythology_view()
    viewCreator.create_statistics_view()
    