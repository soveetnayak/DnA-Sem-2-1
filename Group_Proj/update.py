import subprocess as sp
import pymysql
import pymysql.cursors

'''
a. Update status/details of a book issued.
b. Update details of storage (example- new shelf/rack added).
c. Update details (like Mobile_no/Address) of a member/staff.
'''

'''def db_con(username, password, query):
	db = pymysql.connect("localhost", username, password, "Library")
	with db.cursor() as cur:
		cur.execute(query)
		data = cur.fetchall()
		db.commit()

	return data'''


def updatebookdetails(con,cur):
    try:

        print("Which field would you like to change in TABLE Books\n")

        query = "Select * from Books;"
        print("Check1\n")
        # data = db_con(con, cur, query)
        # print("Check2\n")
        # # Display all the article details
        # print("Articles available:", 'green', attrs=['bold'])
        # print(data, headers=['Book_id', 'Book_Name', 'Edition', 'ISBN_value', 'Price', 'Author_id', 'Publisher_id', 'Genre_id', 'Status'])
        # print("")

        # Select the detail to change
        print("What detail would you like to change?")
        print("1. Book_id")
        print("2. Book_Name")
        print("3. Edition")
        print("4. ISBN_value")
        print("5. Price")
        print("6. Author_id")
        print("7. Publisher_id")
        print("8. Genre_id")
        print("9. Status")
        print("10. Exit")
        
        print("Enter book_id")
        book_id = int(input())
        choice = int(input("Enter your choice: "))

        if choice == 1:
            book_id = input("Enter the new Book_id: ")
            query = "Update Books SET Book_id = %s where Book_id = %s" %(book_id,book_id)
            print("Book_id updated successfully")

        elif choice == 2:
            book_name = input("Enter the new Book_name: ")
            query = "Update Books SET Book_name = %s where Book_id = %s" %(book_name,book_id)
            print("Book_name updated successfully")

        elif choice == 3:
            edition = input("Enter the new Edition: ")
            query = "Update Books SET Edition = %s where Book_id = %s" %(edition,book_id)
            print("Edition updated successfully")

        elif choice == 4:
            isbn_value = input("Enter the new ISBN_value: ")
            query = "Update Books SET ISBN_value = %s where Book_id = %s" %(isbn_value,book_id)
            print("ISBN_value updated successfully")

        elif choice == 5:
            price = input("Enter the new Price: ")
            query = "Update Books SET Price = %s WHERE Book_id = %s" %(price,book_id)
            print("Price updated successfully")


        elif choice == 6:
            author_id = input("Enter the new Author_id: ")
            query = "Update Books SET Author_id = %s where Book_id = %s" %(author_id,book_id)
            print("Author_id updated successfully")


        elif choice == 7:
            publisher_id = input("Enter the new Publisher_id: ")
            query = "Update Books SET Publisher_id = %s where Book_id = %s" %(publisher_id,book_id)
            print("Publisher_id updated successfully")

        
        elif choice == 8:
            genre_id = input("Enter the new Genre_id: ")
            query = "Update Books SET Genre_id = %s WHERE Book_id = %s" %(genre_id,book_id)
            print("Genre_id updated successfully")


        elif choice == 9:
            status = input("Enter the new Status: ")
            query = "Update Books SET Status = %s where Book_id = %s" %(status,book_id)
            print("Status updated successfully")


        elif choice == 10:
            print("Exiting")
            return

        else:
            print("Invalid choice")
            return

        print(query)
        cur.execute(query)
        con.commit()

        

    except Exception as e:
        print("Error:", e)
        return

        


        









