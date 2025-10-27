import pymysql

conn = pymysql.connect(host='localhost', user='mingyu', password='q1w2e3', db='study_db')
cur = conn.cursor()

def add_now(temp, hum):
    cur.execute(f"insert into record_dht(tmperature, humidity) values('{temp}', '{hum}')")
    conn.commit()

def add_record():
    cur.execute(f'select * from record_dht')
    conn.commit()
