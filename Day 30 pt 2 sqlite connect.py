import sqlite3
import xlsxwriter

workbook = xlsxwriter.Workbook('demoy.xlsx')
worksheet = workbook.add_worksheet("My data")
conn = sqlite3.connect("Mydata.db")
cursor = conn.cursor()
r= c =0
try:
    cursor.execute("""select * from employee""")
    d = cursor.fetchall()
    for i in d:
        print(i)
except Exception as e:
    print('Error:',e)
finally:
    conn.close()