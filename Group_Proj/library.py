import subprocess as sp
import pymysql
import pymysql.cursors


def entermemberdetails():
    """
    Function to implement option 3
    """
    try: 
        row = {}
        print("Enter new member's details: ")
        row["Member_id"] = int(input("Member_id: "))
        row["Government_id"] = int(input("Government_id: "))
        row['Member_Name'] = (input("Member_Name: "))
        row[""] = input("Edition: ")
        row["ISBN_value"] = int(input("ISBN_value: "))
        row["Price"] = float(input("Price: "))
        row["Publisher_id"] = int(input("Publisher_id: "))
        row["Status"] = (input("Status: "))


        

    


def enterbookdetails():
    """
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        row = {}
        author={}
        genre={}
        print("Enter new Book's details: ")
        row["Book_id"] = int(input("Book_id: "))
        
        if (row["Book_id"] < 0):
            print("Book_id should be positive")
            

        row['Book_Name'] = (input("Book_Name: "))
        row["Edition"] = input("Edition: ")
        row["ISBN_value"] = int(input("ISBN_value: "))
        row["Price"] = float(input("Price: "))
        row["Publisher_id"] = int(input("Publisher_id: "))
        row["Status"] = (input("Status: "))

        auth = int(input("Number oow["Member_id"] = f authors: "))
        for i in range(auth):
            author[i] = int(input("Author_id: "))
        gen = int(input("Number of genres: "))
        for i in range(gen):
            genre[i] = int(input("Genre_id: "))


        query = "INSERT INTO Books VALUES(%d, '%s', '%s', %d, %f, %d, '%s' )" % (
            row["Book_id"], row["Book_Name"], row["Edition"], row["ISBN_value"], row["Price"], row["Publisher_id"], row["Status"])

        print(query)
        cur.execute(query)
        con.commit()

        for i in range(auth):
            query = "INSERT INTO Multi_Authors VALUES(%d, %d)" % (
                row["Book_id"], author[i])
            print(query)
            cur.execute(query)
            con.commit()

        for i in range(gen):
            query = "INSERT INTO Multi_Genres VALUES(%d, %d)" % (
                row["Book_id"], genre[i])
            print(query)
            cur.execute(query)
            con.commit()
            
        print("Inserted Into Database! ")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database!\n")
        print("> ", e)

    return

def deletebookdetails():
    
    try:
        row = {}
        print("Enter Book_id to delete: ")
        row["Book_id"] = int(input("Book_id: "))

        query = "DELETE FROM Books WHERE Book_id = %d" % (row["Book_id"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Deleted from Database! ")

    except Exception as e:
        con.rollback()
        print("Failed to delete into database!\n")
        print("> ", e)

    return

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        enterbookdetails()
    elif(ch == 2):
        deletebookdetails()
    elif(ch == 3):
        entermemberdetails()
    elif(ch == 4):
        deletememberdetails()
    elif(ch == 5):
        updatememberdetails()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    # username = input("Username: ")
    # password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              port=30306,
                              user="root",
                              password="shazam",
                              db="Library",
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.openow["Member_id"] = ):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter ANY key to CONTINUE >")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Insert Book details")  # Book Details
                print("2. Delete Book deatils") 
                print("3. New Member details")  # Promote Employee
                print("4. Remove Member")  # Employee Statistics
                print("5. Logout")
                ch = int(input("Enter choice > "))
                tmp = sp.call('clear', shell=True)
                if ch == 5:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE >")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter ANY key to CONTINUE >")
