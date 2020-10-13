import psycopg2
from config import config


def get_florence_pictures():
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        # print error if Exception is thrown or there is a DatabaseError
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
