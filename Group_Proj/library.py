import subprocess as sp
import pymysql
import pymysql.cursors
import insert 
import delete 
#import update
import queries

#Function that maps helper functions to option entered by user
def dispatch(ch,con,cur):

    if(ch == 'a'):
        insert.enterbookdetails(con,cur)
    elif(ch == 'b' ):
        delete.deletebookdetails(con,cur)
    elif(ch == 'c'):
        insert.entermagazinedetails(con,cur)
    elif(ch == 'd'):
        delete.deletemagazinedetails(con,cur)
    elif(ch == 'e'):
        insert.entermemberdetails(con,cur)
    elif(ch == 'f'):
        delete.deletememberdetails(con,cur)
    elif(ch == 'g'):
        insert.enterstaffdetails(con,cur)
    elif(ch == 'h'):
        delete.deletestaffdetails(con,cur)
    elif(ch == 'm'):
        queries.query_1(con,cur)
    elif(ch == 'n'):
        queries.query_2(con,cur)
    elif(ch == 'o'):
        queries.query_3(con,cur)
    elif(ch == 'p'):
        queries.query_4(con,cur)
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

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter ANY key to CONTINUE >")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                
                print("a. Insert Book")
                print("b. Delete Book") 
                print("c. Insert Magazine")
                print("d. Delete Magazine")
                print("e. New Member")  
                print("f. Remove Member")
                print("g. New Staff member")
                print("h. Remove Staff member")  
                print("z. Logout")
                ch = input("Enter choice > ")
                tmp = sp.call('clear', shell=True)
                if ch == 'z':
                    exit()
                else:
                    dispatch(ch,con,cur)
                    tmp = input("Enter any key to CONTINUE >")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter ANY key to CONTINUE >")