# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import datetime
import mysql.connector

cnx = mysql.connector.connect(
    user='phpmyadmin',
    password='shthyyKsbaZ65wkD',
    host='127.0.0.1',
    database='isphere'
)
cursor = cnx.cursor()
hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)
query1 = ("SELECT COUNT(*) count FROM isphere.session "
          "WHERE sessionstatusid=2 AND sourceid=55 AND unix_timestamp(now())-unix_timestamp(lasttime)>600")

cursor.execute(query1)
for i in cursor:
    print(i)
cursor.close()
cnx.close()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
