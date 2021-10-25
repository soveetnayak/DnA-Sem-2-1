import subprocess as sp
import pymysql
import pymysql.cursors
import insert 
import delete 
import update
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
    elif(ch == 'i'):
        update.updatebookdetails(con,cur)
    elif(ch == 'j'):
        update.updatememberdetails(con,cur)
    elif(ch == 'k'):
        update.updatestoragedetails(con,cur)
    elif(ch == 'l'):
        update.updatestaffdetails(con,cur)
    
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
                              password="Mybirthdayison6",
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
                
                print("1. Add Book to Library")
                print("2. Add Magazine to Library")
                print("3. Add new Member")
                print("4. Add new Staff")
                # print("5. Add Genre")
                # print("6. Add Author")
                # print("7. Add Publisher")
                # print("8. Add Book Issue details")
                # print("9. Add Storage details")

                print("31. Remove Book") 
                print("32. Remove Magazine")
                print("33. Remove Member")
                print("34. Remove Staff")
                # print("35. Remove Genre")
                # print("36. Remove Author")
                # print("37. Remove Publisher")

                print("61. Update Book details")
                print("62. Update Magazine details")
                print("63. Update Member details")
                print("64. Update Staff details")
                print("65. Update Storage details")

                print("91. Books stats")
                print("92. Number of books of a particular genre")
                print("93. Names of members living in a particular city")
                print("94. List of issued books")

                print("0. Quit")
                option = input("Enter choice > ")
                tmp = sp.call('clear', shell=True)
                if option == 0:
                    exit()
                else:
                    dispatch(option,con,cur)
                    tmp = input("Enter any key to CONTINUE >")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter ANY key to CONTINUE >")