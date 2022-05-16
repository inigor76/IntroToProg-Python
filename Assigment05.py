# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Inigor, 14.05.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt" # data storage file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
objFile = open(strFile, "w")
dicRow = {"Task": "vacuum", "Priority": "1"}
objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
dicRow = {"Task": "mop", "Priority": "2"}
objFile.write(dicRow["Task"] + "," + dicRow["Priority"])

# -- Input/Output -- #
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
# Show the current items in the table
    if (strChoice.strip() == '1'):
        objFile = open(strFile, "r")
        for row in objFile:
            lstRow = row.split(",")
            dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}
            lstTable.append(dicRow)
        print(lstTable)
        continue
# Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Task: ")
        strPriority = input("Priority: ")
        lstTable.append({"Task": strTask, "Priority": strPriority})
        print(lstTable)
        continue
# Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strTask = input("Task to Remove: ")
        for row in lstTable:
            if row["Task"].lower() == strTask.lower():
                lstTable.remove(row)
                print(lstTable)
            else:
                print("row not found")
        continue
# Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + "," + str(row["Priority"] + "\n"))
        print("File is saved and closed")
        continue
# Exit program
    elif (strChoice.strip() == '5'):
        objFile.close()
        print("Bye-bye!")
    break
