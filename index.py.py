import sqlite3 as sq

conn = sq.connect("PhoneBook1")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Names (
    ID INTEGER PRIMARY KEY,
    FName TEXT,
    Surname TEXT,
    PNumber TEXT
    )             
""")

#check if the table has only just been made...
cur.execute("SELECT COUNT(*) FROM Names")
count = cur.fetchone()[0]
if count == 0: #if so, populate it with the sample data
    with open("pbook_sample.txt", 'r') as f:
        for row in f:
            x = row.strip().split(', ')
            cur.execute("INSERT INTO Names (ID, FName, Surname, PNumber) VALUES (?, ?, ?, ?)", (int(x[0]), x[1], x[2], x[3]))
    conn.commit()

while True:
    print("Main menu")
    print("\n")
    print("1) View phone book")
    print("2) Add to phone book")
    print("3) Search for surname")
    print("4) Delete person from phone book")
    print("5) Quit")
    
    try:
        opt = int(input("Input your selection: "))
        match opt:
            case 1:
                cur.execute("SELECT * FROM Names") #selects all fields from the table...
                for row in cur.fetchall(): #iterates through the rows and returns them
                    print(row)
            case 2:
                new_record = input("Input your record separated by commas (no whitespace): ")
                x = new_record.strip.split(',')
                cur.execute("INSERT INTO Names (ID, FName, Surname, PNumber) VALUES (?, ?, ?, ?)", (int(x[0]), x[1], x[2], x[3]))
                conn.commit()
            case 3:
                sur_search = input("Input the surname (case sensitive): ")
                cur.execute("SELECT Surname FROM Names WHERE Surname == ?", (sur_search,)) #the comma after sur_search is because the parameter MUST be a tuple
                print(cur.fetchall())
            case 4:
                id_del = int(input("Enter the ID of the record to delete: "))
                cur.execute("DELETE FROM Names WHERE ID == ?", (id_del))
                conn.commit()
                print("Succesfully deleted the record, if it exists.")
            case 5:
                break
    except:
        print("Invalid input.")