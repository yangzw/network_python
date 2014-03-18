#!/usr/bin/env python
# Basic connection to MySQL with mysqldb - Chapter 14
# connect_mysqldb.py

import MySQLdb

print "Connecting..."
dbh = MySQLdb.connect(user = 'root', passwd = '123123', db = "volunteersystem")
print "Connection successful."

cursor = dbh.cursor()
cursor.execute("Select * from org")
result = cursor.fetchall()

print "Obtained %d rows" % cursor.rowcount

print '*' * 20    
for row in result:
    print ', '.join([str(row[0]), str(row[1]), str(row[2])])

for column in cursor.description:
    print column


#cursor.execute("insert org (pwd, name, totalmem, email, phone, mpname) values ('fuck1','you',10,'fuck@you.com',1521805807,'ff')");
#dbh.commit()

#cursor.execute("Select * from org")
#result = cursor.fetchall()

#print '*' * 20    
#for row in result:
#    print ', '.join([str(row[0]), str(row[1]), str(row[2])])
#
cursor.close()            
dbh.close()
