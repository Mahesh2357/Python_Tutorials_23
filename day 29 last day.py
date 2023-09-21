#pip means preffered installer programmer
import xlsxwriter
workbook=xlsxwriter.Workbook('employer.xlsx')
worksheet=workbook.add_worksheet("My Sheet")
worksheet.write('A1','Hello')
worksheet.write('A2','welcome')
worksheet.write('A3','xlsxwriter')
worksheet.write('A4','module')
workbook.close()

print("^^^^^^^^^^^^^^")

import xlsxwriter
workbook=xlsxwriter.Workbook('employer.xlsx')
worksheet=workbook.add_worksheet("My Sheet")
r=c=0
l=['Gana' ,"Vikas", 'Anant']
for i in l:
    worksheet.write(r,c,i)
    r +=1
workbook.close()
print("&&&&&&&")

import xlsxwriter
workbook=xlsxwriter.Workbook('employer.xlsx')
worksheet=workbook.add_worksheet("My Sheet")
r=c=0
l=[['Gana',30000] ,["Vikas",29000], ['Anant',30000]]
for i in l:
    worksheet.write(r,c,i[0])
    c +=1
    worksheet.write(r,c,i[1])
    r +=1
    c=0
workbook.close()

print("%%%%%%%%")



'''import sqlite3
conn=sqlite3.connect('example.db')
name=input("Enter name:")
cursor=conn.cursor()


try:
   cursor.execute("INSERT INTO employee (name) VALUES (?)",(name, ))
   conn.commit()
   print("'%d' record inserted" %(cursor.rowcount))
except Exception as e:
   print("Error:",e)
finally:
    conn.close()'''


import sqlite3
import xlsxwriter
workbook=xlsxwriter.Workbook('demo1.xlsx')
worksheet=workbook.add_worksheet("My Data")
conn=sqlite3.connect('example.db')
cursor=conn.cursor()
r=c=0

try:
   cursor.execute("""select * from employee""")
   d=cursor.fetchall()
   for i in d:
       worksheet.write(r,c,i[0])
       c +=1
       worksheet.write(r,c,i[1])
except Exception as e:
   print("Error:",e)
finally:
    conn.close()