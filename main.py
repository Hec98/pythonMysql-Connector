from menu import menu, pausa
from db import dataBaseStructure, selectDataBase, selectLimit, insertData, updateData, deleteData

def main():
    title = "Menu"
    items = "1 Database Structure,\n2 Select database,\n3 Select database limit,\n4 Insert data,\n5 Update data,\n6 Delete data,\n7 Exit\n"

    repeat = True
    while repeat:
        opc = menu(title, items)

        if (opc == 1):
            dataBaseStructure()
            pausa(0)

        elif (opc == 2):
            selectDataBase()
            pausa(0)

        elif (opc == 3):
            limit = input('Enter the limit of records you should see: ')
            selectLimit(int(limit))
            pausa(0)

        elif (opc == 4):
            user = input('Enter a user: ')
            email = input('Enter an email: ')
            age = input('Enter an age: ')
            insertData(user, email, int(age))
            pausa()

        elif (opc == 5):
            idx = input('Enter a id: ')
            user = input('Enter a new user: ')
            email = input('Enter a new email: ')
            age = input('Enter a new age: ')
            updateData(int(idx), user, email, int(age))
            pausa()
        elif (opc == 6):
            idx = input('Enter a id: ')
            deleteData(idx)
            pausa()
    
        repeat = (opc < 7)

if __name__ == "__main__":
    main()
