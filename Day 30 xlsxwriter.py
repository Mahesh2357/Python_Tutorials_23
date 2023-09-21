'''Working with Excel in Python
XlsxWriter is a pythonmodule for writing files in the XLSX file format.
It can be used to write text, numbers and formulas to multiple worksheets.
Also it supports features such as formatting, images, charts, page setup, auto filters, conditional formatting and many others.
Use this command to install xlsxwriter module.
pip install xlsxwriter (Preferred installer program)
NOTE: Throughout XlsxWriter, rows and columns are zero indexed.
      The first cell in a worksheet, A1 is (0, 0), B1 is (0, 1), A2 is (1, 0), B2 is (1, 1)..similarly for all'''

import xlsxwriter
workbook = xlsxwriter.Workbook('employee.xlsx') # workbook is an object of the excel file.
worksheet = workbook.add_worksheet("My Sheet")
worksheet.write('A1','hello')
worksheet.write('A2','Welcome')
worksheet.write('A3','xlsxwriter')
worksheet.write('A4','module')
workbook.close()

print('--------------------------')

workbook = xlsxwriter.Workbook('employee.xlsx') # workbook is an object of the excel file.
worksheet = workbook.add_worksheet("My Sheet")
r=c=0
l=['gana','vikas','anant']
for i in l:
    worksheet.write(r,c,i)
    r+= 1
workbook.close()

print('-----------------------------')

workbook = xlsxwriter.Workbook('employee.xlsx') # workbook is an object of the excel file.
worksheet = workbook.add_worksheet("My Sheet")
r=c=0
l=[['gana',30000],['vikas',45000],['anant',56000]]
for i in l:
    worksheet.write(r,c,i[0])
    c+=1
    worksheet.write(r,c,i[1])
    r+= 1
    c=0
workbook.close()

print('----------------------------------------')
import sqlite3
conn = sqlite3.connect("Mydata.db")
cursor = conn.cursor()
try:
    cursor.execute("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY AUTOINCREMENT,name CHAR(100))")
    print("Table created successfully")
except Exception as e:
    print('Error:',e)
finally:
    conn.close()


"new"
import sqlite3
conn = sqlite3.connect("Mydata.db")
cursor = conn.cursor()
try:
    name = input("Enter name: ")
    cursor.execute("INSERT INTO employee (name) VALUES(?)",(name,))
    conn.commit()
    print("'%d' Insertion Successfull...!!"%(cursor.rowcount))
except Exception as e:
    print('Error:',e)
finally:
    conn.close()

"continuation"
import sqlite3
conn = sqlite3.connect("Mydata.db")
cursor = conn.cursor()
#name = input("Enter name: ")
try:
    cursor.execute("""select * from employee""")
    d = cursor.fetchall()
    for i in d:
        print(i)
except Exception as e:
    print('Error:',e)
finally:
    conn.close()