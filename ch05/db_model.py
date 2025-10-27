import pymysql
conn = pymysql.connect(
    host='localhost',
    user='mingyu',
    password='q1w2e3',
    db='study_db',
    charset='utf8mb4'
)
cur = conn.cursor(pymysql.cursors.DictCursor)

def add_now(temp, hum):
    cur.execute(
        "INSERT INTO record_dht(temperature, humidity) VALUES (%s, %s)",
        (temp, hum)
    )
    conn.commit()
def get_all_records():
    cur.execute('SELECT * FROM record_dht ORDER BY id DESC')
    result = cur.fetchall()
    return result
def close_connection():
    cur.close()
    conn.close()