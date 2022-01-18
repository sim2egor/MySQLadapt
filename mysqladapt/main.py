# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import mysqlconnector
db=mysqlconnector.dbmysq
db.execute("SELECT COUNT(*) count FROM isphere.session "
                "WHERE sessionstatusid=2 AND sourceid=55 "
                "AND unix_timestamp(now())-unix_timestamp(lasttime)>600")
for i in db.cursor:
    print(i)
# cursor.close()
# cnx.close()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
