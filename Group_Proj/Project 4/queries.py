import subprocess as sp
import pymysql
import pymysql.cursors

'''
Total books, Total available books, AVERAGE_PRICE, MAX_PRICE, MIN_PRICE [of a book]
'''

def query_1(con,cur):
    try:
        cur.execute("SELECT COUNT(*) FROM Books")
        result = cur.fetchone()
        print("Total number of books: ",result['COUNT(*)'])

        cur.execute("SELECT COUNT(*) FROM Books WHERE Status = 'Available'")
        result = cur.fetchone()
        print("Total number of available books: ",result['COUNT(*)'])

        cur.execute("SELECT AVG(Price) FROM Books")
        result = cur.fetchone()
        print("Average cost of all the books in the library: ",result['AVG(Price)'])

        cur.execute("SELECT MAX(Price) FROM Books")
        result = cur.fetchone()
        print("Max price of a book: ",result['MAX(Price)'])

        cur.execute("SELECT MIN(Price) FROM Books")
        result = cur.fetchone()
        print("Min price of a book: ",result['MIN(Price)'])

    except Exception as e:
        print(e)


    return


'''
Books by Genres (ex. Total number of books under biography genre)
'''

def query_2(con,cur):

    genre = input("Enter the genre: ")
    query = "SELECT COUNT(*) AS Total_Books FROM(SELECT * FROM Books INNER JOIN (SELECT Book_Id AS IDBook FROM Multi_Genres WHERE Genre_Id=(SELECT Genre_Id From Genre WHERE Genre_Name= '%s'))AS Table1 ON Books.Book_Id=Table1.IdBook)As Table2;" % (genre)
    cur.execute(query)
    result = cur.fetchone()
    print("Total number of books under %s genre: %s" % (genre,result['Total_Books']))

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
    cur.execute("SELECT * FROM Books WHERE Status = 'Borrowed'")
    result = cur.fetchall()
    print("List of books issued to someone: ")
    for row in result:
        print(row['Book_id'],row['Book_Name'])

    return 

'''
Searching for Books starting with a particular word
'''

def query_5(con,cur):
    word = input("Enter the starting search word: ")
    cur.execute("SELECT Book_id,Book_Name FROM (SELECT *,LOCATE('%s', Book_Name) AS Search FROM Books) AS Table1 WHERE Search=1;" % (word))
    result = cur.fetchall()
    print("List of books starting with %s: " % (word))
    for row in result:
        print(row['Book_id'],row['Book_Name'])

    return