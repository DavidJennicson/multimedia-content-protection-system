import psycopg2

from psycopg2 import *
from numpy.random import randint



def check(email):
    try:
        connection = psycopg2.connect(host="localhost", port=5432, user="postgres", password="Jennicson1",
                                      database="medcrypt")
        cursor = connection.cursor()
        sql = """SELECT COUNT(useremail) FROM accounts WHERE useremail=%s"""
        cursor.execute(sql, (email,))
        c = cursor.fetchone()
        print(c[0])
        return c[0]
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return "Error in database error 800"
    finally:
        if connection:
            cursor.close()
            connection.close()

def register(name,email,password):
    import psycopg2
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Jennicson1",
                                      host="localhost",
                                      port="5432",
                                      database="medcrypt")
        cursor = connection.cursor()
        acccheck=check(email)
        if (acccheck>=1):
            print("user already exists")
            return ("error:user already exists")
        # otp=randint(10000,999999)
        uid=randint(10000,99999)
        postgres_insert_query = """ INSERT INTO accounts VALUES (%s,%s,%s,%s)"""
        record_to_insert = (uid,email,password,name)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")
        # cd="""CREATE DATABASE %s"""
        # cursor.execute(cd,uid)
        # cursor.execute("""CREATE TABLE files (fileid varchar,filename varchar,filesize varchar,filetype varchar,filedate timestamp)""")
        # cursor.execute()
        return ({"success registered succesfully"})
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return ({"error failed to register"})
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# check('djennicson@gmail.com')