"""Collect Articles from several sources.
Saves them into a Postgres Database
"""

from configparser import ConfigParser
import psycopg2
from psycopg2 import sql
from config import config

import newspaper

class MediaDB:
    
    def __init__():
        pass

    def config(self, filename='database.ini', section='postgresql'):
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db

    def insert(self, table_name, data):
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # read connection parameters
            params = self.config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)
            
            # create a cursor
            cur = conn.cursor()
            
            # execute a statement
            # Construct the SQL query for insertion
            columns = sql.SQL(', ').join(map(sql.Identifier, data.keys()))
            values = sql.SQL(', ').join(map(sql.Placeholder, data.values()))
            query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
                sql.Identifier(table_name),
                columns,
                values
            )

            # Execute the query
            cur.execute(query, data)

            # Commit the changes to the database
            conn.commit()

            print("Data inserted successfully.")
        
        # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            # Close the cursor and connection
            if cur:
                cur.close()
            if conn:
                conn.close()

class Collector:
    def __init__(self):
        self.article_urls = []
        self.article_titles = []
        self.article_texts = []
    
    def article_list(self, source_url):
        paper = newspaper.build(source_url)
        for article in paper.articles:
            self.article_urls.append(article.url)
            self.article_titles.append(article.title)
            self.article_texts.append(article.text)

    def full_list(self, source_urls):
        for source_url in source_urls:
            self.article_list(source_url)

