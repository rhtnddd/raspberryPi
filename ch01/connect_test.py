import pymysql

conn=pymysql.connect(host='localhost', user='mingyu', password='q1w2e3',db='shopping1_db')

cur=conn.cursor()

cur.execute('select avg(age) from CUSTOMER where adress="경기"')

result=cur.fetchone()

print(int(result[0]))

cur.close()
conn.close()
