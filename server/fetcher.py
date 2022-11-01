import psycopg2
import psycopg2.extras
def fetcharr():
    try:
        connection = psycopg2.connect(host="localhost", port=5432, user="postgres", password="Jennicson1",
                                      database="medcrypt")
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        sql = """SELECT * FROM filetable"""
        cursor.execute(sql)
        c = cursor.fetchall()
        for x in c:
            for g in x:
                print(c)
        return c
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return "Error in database error 800"
    finally:
        if connection:
            cursor.close()
            connection.close()

