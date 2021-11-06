import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """COPY into each staging table using the queries in `copy_table_queries`.

    Takes a connection to a database and a cursor using that connection and 
    executes all the queries in the `copy_table_queries` list.

    Args:
        conn (conection): A connection to the database
        cur (cursor): A cursor using the `conn` connection
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """INSERT into each final table using the queries in `insert_table_queries`.

    Takes a connection to a database and a cursor using that connection and 
    executes all the queries in the `insert_table_queries` list.

    Args:
        conn (conection): A connection to the database
        cur (cursor): A cursor using the `conn` connection
    """
    
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """Creates a connection and a cursor using that connection to the database 
    whose attributes are listed in the config file, and runs the 
    load_staging_tables and insert_tables functions.
    """
    config = configparser.ConfigParser()
    config.read("dwh.cfg")

    conn = psycopg2.connect(
        "host={} dbname={} user={} password={} port={}".format(
            *config["CLUSTER"].values()
        )
    )
    cur = conn.cursor()

    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
