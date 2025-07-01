import sqlite3

database=input("Input database name: ")

print("""
      1.CREATE
      2.INSERT
      3.UPDATE
      4.DELETE
      5.ADD
      """)
newinput=input("""would you like to create a new table,
                  insert into a column,
                  update the data in a column,
                  add a new column or delete a table: """).lower()

input1=input("table name: ")


first=sqlite3.connect(f"{database}")
second=first.cursor()


def create():
    input2=input("table column name: ")
    input3=input("table column name: ")
    second.execute(F"CREATE TABLE IF NOT EXISTS {input1}({input2} INTEGER, {input3} TEXT)")
    print(f"Table {input1} created successfully.")

def insert():
    input2=input(" table column name: ")
    input3=input(" table column name: ")
    userinput=int(input("input: "))
    secondinput=input("Enter: ")
    second.execute(F"INSERT INTO {input1}({input2} ,{input3}) VALUES({userinput},'{secondinput}')")
    print("Record inserted successfully.")

def update():
    try:
      input2=input(" table column name: ")
      input3=input(" table column name: ")
      column_to_identify=int(input("Enter the id of  the column:  "))
      column_to_updaate=input("Enter what you want to change the product to: ")
      second.execute(F"UPDATE {input1} SET {input3}='{column_to_updaate}' WHERE {input2}={column_to_identify}")
      print("Updated successfully")
    except:
        print("Values Were Invalid, Please try again")
        exit()

def drop():
    second.execute(f"DROP TABLE {input1}")
    print("table deleted successfully")

def add():
   print("""
         1.TEXT
         2.INTEGER
         """)
   newsinput=input("Specify the if you want to add a text or integer(number): ")
   new_column=input("Specify column name: ")
   if newsinput=="1":
    second.execute(f"ALTER TABLE {input1} ADD COLUMN {new_column} TEXT")
    print("table added successfully")
   else:
      if newsinput=="2":
         second.execute(f"ALTER TABLE {input1} ADD COLUMN {new_column} INTEGER")
         print("table added successfully")
    
         
   

if newinput=="1":
   create()
else:
    if newinput == "2":
        insert()
    else:
        if newinput=="3":
            update()
        else:
         if newinput=="4":
            drop()
         else:
            if newinput=="5":
               add()
            else:
             print("invalid input!!")


first.commit()
first.close()
