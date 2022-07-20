import psycopg2


def update_table(publisherId, establishedYear):
    try:
        connection = psycopg2.connect(user="admin", password="12345678", host="172.22.240.1", port="5432",
                                      database="admin")
        cursor = connection.cursor()
        # Update single record now
        sql_update_query = """Update publisher set publisher_estd = %s where publisher_id = %s"""
        cursor.execute(sql_update_query, (establishedYear, publisherId))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# call the update function
publisherId = 3
establishedYear = 2001
# update_table(publisherId, establishedYear)

publisherId = 5
establishedYear = 1999
# update_table(publisherId, establishedYear)


def update_table_name(publisher_name, establisher_nome):
    try:
        connection = psycopg2.connect(user="admin", password="12345678", host="172.22.240.1", port="5432",
                                      database="admin")
        cursor = connection.cursor()
        # Update single record now
        sql_update_query = """Update publisher set publisher_name = %s where publisher_name = %s"""
        cursor.execute(sql_update_query, (establisher_nome, publisher_name))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# call the update function
publisher_name = 'Springer'
establisher_nome = 'Vini'
update_table_name(publisher_name, establisher_nome)
