import subprocess as sp
import pymysql
import pymysql.cursors

'''
AVERAGE_PRICE, MAX_PRICE, MIN_PRICE [of a book]
'''

def query_1(con,cur):
    cur.execute("SELECT COUNT(*) FROM books")
    result = cur.fetchone()
    print("Total number of books: ",result[0])

    cur.execute("SELECT AVG(Price) FROM Books")
    result = cur.fetchone()
    print("Average cost of all the books in the library: ",result[0])

    cur.execute("SELECT MAX(Price) FROM Books")
    result = cur.fetchone()
    print("Max price of a book: ",result[0])

    cur.execute("SELECT MIN(Price) FROM Books")
    result = cur.fetchone()
    print("Min price of a book: ",result[0])

    return


'''
Books by Genres (ex. Total number of books under biography genre)
'''
#SELECT COUNT(*) AS Total_Books FROM (SELECT * FROM Books,(SELECT * FROM Multi_Genres WHERE Genre_Id=(SELECT Genre_Id From Genre WHERE Genre_Name="x"))AS Table1 WHERE Books.Book_Id=Table1.Book_Id);
#SELECT COUNT(*) AS Total_Books FROM (SELECT * FROM Books INNER JOIN (SELECT * FROM Multi_Genres WHERE Genre_Id=(SELECT Genre_Id From Genre WHERE Genre_Name="x"))AS Table1 ON Books.Book_Id=Table1.Book_Id);
#Replace x by value enteres by the user

def query_2(con,cur):

    genre = input("Enter the genre: ")
    query = "SELECT COUNT(*) FROM Books WHERE Genre = %s" % genre
    cur.execute(query)
    result = cur.fetchone()
    print("Total number of books under %s genre: %s",genre,result[0])

    return

'''
Project all the member’s names who live in the city ‘Hyderabad’
'''

def query_3(con,cur):
    city = input("Enter the city: ")
    query = "SELECT First_Name,Last_Name FROM Members WHERE City = '%s'" % city
    cur.execute(query)
    result = cur.fetchall()
    print("List of members living in %s: "% (city))
    for row in result:
        print(row['First_Name'],row['Last_Name'])

    return

'''
List all the books that are issued to someone.
'''

def query_4(con,cur):
    cur.execute("SELECT * FROM Books WHERE Status = Borrowed")
    result = cur.fetchall()
    print("List of books issued to someone: ")
    for row in result:
        print(row)

    return 


