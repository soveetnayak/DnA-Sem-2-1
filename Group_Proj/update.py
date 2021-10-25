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
        print("0. Exit")
        print("1. Book_Name")
        print("2. Edition")
        print("3. ISBN_value")
        print("4. Price")
        print("5. Author_id")
        print("6. Publisher_id")
        print("7. Genre_id")
        print("8. Status")
        
        
        print("Enter book_id")
        book_id = int(input())
        choice = int(input("Enter your choice: "))


        if choice == 1:
            book_name = input("Enter the new Book_name: ")
            query = "Update Books SET Book_name = %s where Book_id = %s" %(book_name,book_id)
            print("Book_name updated successfully")

        elif choice == 2:
            edition = input("Enter the new Edition: ")
            query = "Update Books SET Edition = %s where Book_id = %s" %(edition,book_id)
            print("Edition updated successfully")

        elif choice == 3:
            isbn_value = input("Enter the new ISBN_value: ")
            query = "Update Books SET ISBN_value = %s where Book_id = %s" %(isbn_value,book_id)
            print("ISBN_value updated successfully")

        elif choice == 4:
            price = input("Enter the new Price: ")
            query = "Update Books SET Price = %s WHERE Book_id = %s" %(price,book_id)
            print("Price updated successfully")


        elif choice == 5:
            author_id = input("Enter the new Author_id: ")
            query = "Update Books SET Author_id = %s where Book_id = %s" %(author_id,book_id)
            print("Author_id updated successfully")


        elif choice == 6:
            publisher_id = input("Enter the new Publisher_id: ")
            query = "Update Books SET Publisher_id = %s where Book_id = %s" %(publisher_id,book_id)
            print("Publisher_id updated successfully")

        
        elif choice == 7:
            genre_id = input("Enter the new Genre_id: ")
            query = "Update Books SET Genre_id = %s WHERE Book_id = %s" %(genre_id,book_id)
            print("Genre_id updated successfully")


        elif choice == 8:
            status = input("Enter the new Status: ")
            query = "Update Books SET Status = %s where Book_id = %s" %(status,book_id)
            print("Status updated successfully")


        elif choice == 0:
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

        


def updatestoragedetails(con,cur):
    try:

        print("Which field would you like to change in TABLE Storage\n")

        query = "Select * from Storage;"
        print("Check1\n")
        # data = db_con(con, cur, query)
        # print("Check2\n")
        # # Display all the article details
        # print("Articles available:", 'green', attrs=['bold'])
        # print(data, headers=['Storage_id', 'Shelf_no', 'Rack_no', 'Storage_type'])
        # print("")

        
        print("Enter Book_id")
        Book_id = int(input())

        # Select the detail to change
        print("What detail would you like to change?")
        print("0. Exit")
        print("1. Shelf_no")
        print("2. Rack_no")
        
        
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            shelf_no = input("Enter the new Shelf_no: ")
            query = "Update Storage SET Shelf_no = %s where Book_id = %s" %(shelf_no,Book_id)
            print("Shelf_no updated successfully")

        elif choice == 2:
            rack_no = input("Enter the new Rack_no: ")
            query = "Update Storage SET Rack_no = %s where Book_id = %s" %(rack_no,Book_id)
            print("Rack_no updated successfully")

        elif choice == 0:
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

    


def updatememberdetails(con,cur):
    try:

        print("Which field would you like to change in TABLE Members\n")

        query = "Select * from Members;"
        print("Check1\n")
        # data = db_con(con, cur, query)
        # print("Check2\n")
        # # Display all the article details
        # print("Articles available:", 'green', attrs=['bold'])
        # print(data, headers=['Member_id', 'Name', 'Mobile_no', 'Address'])
        # print("")


         # Member_id
        print("Enter Member_id")
        Member_id = int(input())

        # Select the detail to change
        print("What detail would you like to change?")
        print("0. Exit")

       
        
        print("1. First_name")
        # Last_name
        print("2. Last_name")
        # # Date_of_birth
        # print("5. Date_of_birth")   # you can't change the date of birth

        # Address
        print("3. Address")
        
        # Membership_expiration
        print("4. Membership_expiration")


        choice = int(input("Enter your choice: "))

        
        if choice == 1:
            first_name = input("Enter the new First_name: ")
            query = "Update Members SET First_Name = %s where Member_id = %s" %(first_name,Member_id)
            print("First_name updated successfully")

        elif choice == 2:
            last_name = input("Enter the new Last_name: ")
            query = "Update Members SET Last_Name = %s where Member_id = %s" %(last_name,Member_id)
            print("Last_name updated successfully")

        elif choice == 3:
            House_no = input("Enter the new House number ")
            Locality = input("Enter the new Locality: ")
            City = input("Enter the new City: ")
            Pin_Code = input("Enter the new Pin_Code: ")

            query = "Update Members SET House_no = %s, Locality = %s, City = %s, Pin_Code = %s where Member_id = %s" %(House_no,Locality,City,Pin_Code,Member_id)
 

        elif choice == 4:
            membership_expiration = input("Enter the new Membership_expiration: ")
            query = "Update Members SET Membership_expiration = %s where Member_id = %s" %(membership_expiration,Member_id)
            print("Membership_expiration updated successfully")

        elif choice == 0:
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




def updatestaffdetails(con,cur):
    try:

        print("Which field would you like to change in TABLE Staff\n")

        query = "Select * from Staff;"
        print("Check1\n")

         # Staff_id
        print("Enter Staff_id")
        Staff_id = int(input())

        # Select the detail to change
        print("What detail would you like to change?")
        print("0. Exit")

       
        
        print("1. First_name")
        # Last_name
        print("2. Last_name")
        # # Date_of_birth
        # print("5. Date_of_birth")   # you can't change the date of birth

        # Address
        print("3. Address")
        
        # Designation
        print("4. Designation")

        # Duty
        print("5. Duty")



        choice = int(input("Enter your choice: "))

        
        if choice == 1:
            first_name = input("Enter the new First_Name: ")
            query = "Update Staff SET First_name = %s where Staff_id = %s" %(first_name,Staff_id)
            print("First_name updated successfully")

        elif choice == 2:
            last_name = input("Enter the new Last_Name: ")
            query = "Update Staff SET Last_name = %s where Staff_id = %s" %(last_name,Staff_id)
            print("Last_name updated successfully")

        elif choice == 3:
            House_no = input("Enter the new House number ")
            Locality = input("Enter the new Locality: ")
            City = input("Enter the new City: ")
            Pin_Code = input("Enter the new Pin_Code: ")

            query = "Update Staff SET House_no = %s, Locality = %s, City = %s, Pin_Code = %s where Staff_id = %s" %(House_no,Locality,City,Pin_Code,Staff_id)


        elif choice == 4:
            designation = input("Enter the new Designation: ")
            query = "Update Staff SET Designation = %s where Staff_id = %s" %(designation,Staff_id)
            print("Designation updated successfully")

        elif choice == 5:
            duty = input("Enter the new Duty: ")
            query = "Update Staff SET Duty = %s where Staff_id = %s" %(duty,Staff_id)
            print("Duty updated successfully")

        elif choice == 0:
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

    
        
       

        




        








