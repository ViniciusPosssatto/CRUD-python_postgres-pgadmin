import psycopg2


def deleteData(publisherId):
    try:
        connection = psycopg2.connect(user="admin", password="12345678", host="172.22.240.1", port="5432",
                                      database="admin")
        cursor = connection.cursor()

        # Update single record now
        sql_delete_query = """Delete from publisher\
        where publisher_id = %s"""
        cursor.execute(sql_delete_query, (publisherId,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


publisherId = 4
deleteData(publisherId)
