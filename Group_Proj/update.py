import subprocess as sp
import pymysql
import pymysql.cursors

'''
a. Update status/details of a book issued.
b. Update details of storage (example- new shelf/rack added).
c. Update details (like Mobile_no/Address) of a member/staff.
'''

def db_con(username, password, query):
	db = pymysql.connect("localhost", username, password, "data_kedavra")
	with db.cursor() as cur:
		cur.execute(query)
		data = cur.fetchall()
		db.commit()

	return data


def updatebookdetails(con,cur):
    try:

        print("Which field would you like to change in TABLE Books\n")

        query = "Select * from Books;"
        data = db_con(con, cur, query)
        # Display all the article details
        print("Articles available:", 'green', attrs=['bold'])
        print(data, headers=['Book_id', 'Book_Name', 'Edition', 'ISBN_value', 'Price', 'Author_id', 'Publisher_id', 'Genre_id', 'Status'])
        print("")

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
            query = "Update Books set Book_id = %s where Book_id = %s"
            db_con(con, cur, query, (book_id, book_id))
            print("Book_id updated successfully")

        elif choice == 2:
            book_name = input("Enter the new Book_name: ")
            query = "Update Books set Book_name = %s where Book_id = %s"
            db_con(con, cur, query, (book_name, book_id))
            print("Book_name updated successfully")

        elif choice == 3:
            edition = input("Enter the new Edition: ")
            query = "Update Books set Edition = %s where Book_id = %s"
            db_con(con, cur, query, (edition, book_id))
            print("Edition updated successfully")

        elif choice == 4:
            isbn_value = input("Enter the new ISBN_value: ")
            query = "Update Books set ISBN_value = %s where Book_id = %s"
            db_con(con, cur, query, (isbn_value, book_id))
            print("ISBN_value updated successfully")

        elif choice == 5:
            price = input("Enter the new Price: ")
            query = "Update Books set Price = %s where Book_id = %s"
            db_con(con, cur, query, (price, book_id))
            print("Price updated successfully")


        elif choice == 6:
            author_id = input("Enter the new Author_id: ")
            query = "Update Books set Author_id = %s where Book_id = %s"
            db_con(con, cur, query, (author_id, book_id))
            print("Author_id updated successfully")


        elif choice == 7:
            publisher_id = input("Enter the new Publisher_id: ")
            query = "Update Books set Publisher_id = %s where Book_id = %s"
            db_con(con, cur, query, (publisher_id, book_id))
            print("Publisher_id updated successfully")

        
        elif choice == 8:
            genre_id = input("Enter the new Genre_id: ")
            query = "Update Books set Genre_id = %s where Book_id = %s"
            db_con(con, cur, query, (genre_id, book_id))
            print("Genre_id updated successfully")


        elif choice == 9:
            status = input("Enter the new Status: ")
            query = "Update Books set Status = %s where Book_id = %s"
            db_con(con, cur, query, (status, book_id))
            print("Status updated successfully")


        elif choice == 10:
            print("Exiting")
            return

        else:
            print("Invalid choice")
            return

        

    except Exception as e:
        print("Error:", e)
        return

        


        









