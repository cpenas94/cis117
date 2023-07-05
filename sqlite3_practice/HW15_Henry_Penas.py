import sqlite3

con = sqlite3.connect('web.db')
cur = con.cursor()

cur.execute("""CREATE TABLE gym_member
    (Name TEXT, End_Date DATE, Membership_Type TEXT)""")
print("Table created successfully")

cur.execute("""INSERT INTO gym_member (Name, End_Date, Membership_Type) VALUES
             ("John Doe", "2023-06-30", "Basic")""")
cur.execute("""INSERT INTO gym_member (Name, End_Date, Membership_Type) VALUES
             ("Jane Smith", "2022-09-14", "Premium")""")
cur.execute("""INSERT INTO gym_member (Name, End_Date, Membership_Type) VALUES
             ("Bob Johnson", "2022-10-31", "Basic")""")
con.commit()
print("Data inserted successfully")

print("\n" + "Selected Data Below:")
record = con.execute("""SELECT * from gym_member WHERE Membership_Type = 'Basic' """)
for row in record:
    print(f"Name = {row[0]}, End_Date = {row[1]}, Membership_Type = {row[2]}")

con.close()

