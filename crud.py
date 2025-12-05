import mysql.connector
try:
    conn = mysql.connector.connect (
        user = 'root',
        password = 'Jaysoni@8877',
        host = '127.0.0.1',
        database = 'indigo'
    )
    cursor = conn.cursor()
    print('Connection Established')
except:
    print('Connection Error!!')

# cursor.execute('CREATE DATABASE indigo')

# cursor.execute("""
# CREATE TABLE airport(
#     airport_id INTEGER PRIMARY KEY,
#     Code VARCHAR(10) NOT NULL,
#     City VARCHAR(50) NOT NULL,
#     name VARCHAR(255) NOT NULL
# )
# """)
# conn.commit()

# cursor.execute("""
#     INSERT INTO airport VALUES
#     (1,'DEL', 'New Delhi', 'IGIA'),
#     (2, 'CCU', 'Kolkata', 'NSCA'),
#     (3, 'BOM', 'Mumbai', 'CSMA'),
#     (4, 'AHM', 'Ahmedabad', 'SVIA')
# """)
# conn.commit()

# cursor.execute('SELECT * FROM airport WHERE airport_id > 1')
# data = cursor.fetchall()
# print(data)
#
# for i in data:
#     print(i[3])

# cursor.execute("""
# UPDATE airport
# SET name = 'CSMA'
# WHERE airport_id = 3
# """)
# conn.commit()

cursor.execute("""
DELETE FROM airport WHERE airport_id = 3
""")
conn.commit()