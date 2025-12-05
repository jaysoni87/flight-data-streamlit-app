import mysql.connector
class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect (
                user = 'root',
                password = 'Jaysoni@8877',
                host = '127.0.0.1',
                database = 'flights'
            )
            self.cursor = self.conn.cursor()
            print('Connection Established')
        except:
            print('Connection Error!!')

    def fetch_city_names(self):
        city = []
        self.cursor.execute("""SELECT distinct(Destination) from flights
                                union
                            select distinct(Source) from flights""")
        data = self.cursor.fetchall()
        for item in data:
            city.append(item[0])
        return city

    def fetch_all_flights(self,source, destination):
        self.cursor.execute("""
        select Airline, Route, Dep_Time, Duration, Price from flights where Source = '{}' AND Destination = '{}'
    """.format(source, destination))

        data = self.cursor.fetchall()
        return data

    def fetch_airline_frequency(self):
        airline = []
        frequency = []

        self.cursor.execute("""
        select Airline,count(*) from flights
        group by Airline""")

        data = self.cursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])
        return airline, frequency

    def busy_airport(self):
        city = []
        frequency = []

        self.cursor.execute("""
        select Source,count(*) from 
        (select source from flights union all select destination from flights)t
        group by t.source
        order by count(*) desc""")

        data = self.cursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])
        return city, frequency


    def daily_frequency(self):
        date = []
        frequency = []

        self.cursor.execute("""
        select Date_of_Journey,count(*) from flights
        group by Date_of_Journey""")

        data = self.cursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])
        return date, frequency



