import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """Drop each table using the queries in `drop_table_queries` list.

    Takes a connection to a database and a cursor using that connection and 
    executes all the queries in the `drop_table_queries` list.

    Args:
        conn (conection): A connection to the database
        cur (cursor): A cursor using the `conn` connection
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """Create each table using the queries in `create_table_queries` list.

    Takes a connection to a database and a cursor using that connection and 
    executes all the queries in the `create_table_queries` list.

    Args:
        conn (conection): A connection to the database
        cur (cursor): A cursor using the `conn` connection
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """Creates a connection and a cursor using that connection to the database 
    whose attributes are listed in the config file, and runs the drop_tables and
    create_tables functions.
    """
    config = configparser.ConfigParser()
    config.read("dwh.cfg")

    conn = psycopg2.connect(
        "host={} dbname={} user={} password={} port={}".format(
            *config["CLUSTER"].values()
        )
    )
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
