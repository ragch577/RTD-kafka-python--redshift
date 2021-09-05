from kafka import KafkaConsumer
import psycopg2
from json import loads

consumer = KafkaConsumer('awskafkatopic',bootstrap_servers=['b-1.mskcsv.******.c4.kafka.eu-north-1.amazonaws.com:9092'],consumer_timeout_ms=10000)


#conn = psycopg2.connect(
#            database = "mskdatabase",
#            user = "postgres",
#            password = "Admin1234",
#            host = "database-1.**********.eu-north-1.rds.amazonaws.com",
#            port = "5432"
#            )

# Add your RDS IP address here.
conn = psycopg2.connect(dbname='mskdatabase',user='postgres',host='**.***.***.***',password='Admin1234',port='5432')

#conn.close()
#def postgres_test():
#    try:
#        conn = psycopg2.connect(dbname='mskdatabase',user='postgres',host='base-1.************.eu-north-1.rds.amazonaws.com',
#                password='Admin1234',port='5432')
#conn.close()
#        return print("Connected to DB successfully")
#    except:
#        return print("Connection failed")

#postgres_test()

cur = conn.cursor()


try:
cur.execute("SELECT * FROM msksc.cust_dat")
except psycopg2.Error as e:
print(e)
num = 0
for msg in consumer:
#consumer.commit()
num = num + 1
rec_data = msg.value.decode('utf-8')
r = rec_data.replace('"','')
record = r.strip('\\n')
f_rec = record.split(",")
id = f_rec[0]
timestamp = f_rec[1]
longitude = f_rec[2]
latitude = f_rec[3]
print(name)
print(city)
print(record)
query = "INSERT INTO msksc.cust_dat(id, timestamp, longitude,latitude) VALUES (%s,%s, %s, %s);"
data = (id,timestamp,longitude,latitude)
cur.execute(query, data)
#cur.fetchall()

consumer.close()
conn.commit()
cur.fetchall()
conn.close()