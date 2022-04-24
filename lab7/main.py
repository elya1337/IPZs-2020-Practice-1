import sqlite3
import sys

db = sqlite3.connect('list')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS accounts (
    login TEXT,
    password TEXT
)""")
db.commit()
sql.execute("""CREATE TABLE IF NOT EXISTS your_tasks (
    task TEXT
)""")
db.commit()


def main():
    print("""
        ▒█░▒█ █▀▀█ █▀▀█ █▀▀█ █░░█ 　 ▒█▀▀▀ █▀▀█ █▀▀ ▀▀█▀▀ █▀▀ █▀▀█ 
        ▒█▀▀█ █▄▄█ █░░█ █░░█ █▄▄█ 　 ▒█▀▀▀ █▄▄█ ▀▀█ ░░█░░ █▀▀ █▄▄▀ 
        ▒█░▒█ ▀░░▀ █▀▀▀ █▀▀▀ ▄▄▄█ 　 ▒█▄▄▄ ▀░░▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀
        Welcome to TaskManager v24042022☺☺☺""")
    us_movement(login())


def reg():
    print("♣♣♣ SignUP in system ♣♣♣")
    us_log = input("♣♣♣ Your Login: ")
    us_pass = input("♣♣♣ Your Pass: ")
    user_confirming_password = input("♣♣♣ Confirm your Pass: ")
    us_tasks = ''
    sql.execute(f"SELECT task FROM your_tasks WHERE task = '{us_tasks}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO your_tasks VALUES (?)", (us_tasks,))
        db.commit()
        print("Task field created")
        return start_action()
    sql.execute(f"SELECT login FROM accounts WHERE login = '{us_log}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO accounts VALUES (?, ?)", (us_log, us_pass))
        db.commit()
        print("Congrats!You can use the program!")
        return start_action()
    else:
        print("Same account already created!")
    for value in sql.execute("SELECT * FROM accounts"):
        print(value)
    for value in sql.execute("SELECT * FROM your_tasks"):
        print(value)

    


def login():
    print("*** SignIn menu ***")
    us_log = input("*** Your Login: ")
    us_pass = input("*** Your Pass: ")

    sql.execute(f"SELECT login FROM accounts WHERE login = '{us_log}'")
    if sql.fetchone() is None:
        print("Your login or password have some different with my database!")
        user_action = input("Do you wont to create the account? (print if yes - 'y', if no - 'n')")
        if user_action == 'y':
            reg()
        else:
            False
    else:
        print("****************")
        print("Signing complete")
        return start_action()


def action_with_task(action):
    if action == "add new task":
        us_tasks = input("Print the task name: ")
        sql.execute(f"INSERT INTO your_tasks VALUES (?)", (us_tasks,))
        db.commit()
        print("Task successfully added!",
              "Returning to menu")
        start_action()
    elif action == "remove task":
        us_tasks = input("Print the task name that you need to delete: ")
        sql.execute(f"DELETE FROM your_tasks WHERE task = '{us_tasks}'")
        db.commit()
        print("Task successfully deleted! Returning to menu")
        start_action()
    elif action == "edit task":
        us_tasks = input("Print the task name: ")
        sql.execute(f"UPDATE your_tasks SET task = '{us_tasks}'")
        db.commit()
        print("Task successfully edited! Returning to menu")
        start_action()
    elif action == "check the task":
        for value in sql.execute("SELECT * FROM your_tasks"):
            print(value)
            db.commit()
            start_action()

def start_action():
    print("""Choose you action 
        1.Add new task <-
        2.Edit tasks <-
        3.Check the tasklist <-
        4.Remove the task <-
        5.Log out <-
        6.Create new account <-
        """)
    us_input = input("For choosing you action print number of him: ")
    return us_input

def us_movement(us_input):
    if us_input == "1":
        action_with_task("add new task")
    elif us_input == "2":
        action_with_task("edit task")
    elif us_input == "3":
        action_with_task("check the task")
    elif us_input == "4":
        action_with_task("remove task")
    elif us_input == "5":
        print("Logout process")
        print("...")
        print("..")
        print(".")
        sys.exit()
    elif us_input == "6":
        print("Open registration page")
        print("...")
        print("..")
        print(".")
        reg()





main()
