import logging
import sqlite3


class ViewCreator():
    def __init__(self):
        self.connection = sqlite3.connect("god.db")
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.create_mythology_view()

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
        
        


if __name__ == '__main__':
    viewCreator = ViewCreator()
    viewCreator.create_mythology_view()
    