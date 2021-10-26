# DNA Project Phase-4
# Library

# Team - UP TO DATA
1. Soveet Kumar Nayak (2020101086)
2. Naimeesh Narayan Tiwari (2020101074)
3. Khushi Agarwal (2020101092)


Run `python3 library.py` to run the python scripts.


### All the commands our code can run:

* **enterbookdetails(con,cur)** :- This function is present in the insert.py file. It is used to insert the details of a new book.

* **deletebookdetails(con,cur)** :- This function is present in the delete.py file. It is used to delete all the details of a prticular book on the basis of the attribute given by the user.


* **entermagazinedetails(con,cur)** :- This function is present in the insert.py file. It is used to insert the details of a new magazine.

* **deletemagazinedetails(con,cur)** :- This function is present in the delete.py file. It is used to delete all the details of a prticular magazine on the basis of the attribute given by the user.


* **entermemberdetails(con,cur)** :- This function is present in the insert.py file. It is used to insert the details of a new member when he joins.

* **deletememberdetails(con,cur)** :- This function is present in the delete.py file. It is used to delete all the details of a prticular member on the basis of the attribute given by the user,i.e,when a member ends his membership.


* **enterstaffdetails(con,cur)** :- This function is present in the insert.py file. It is used to insert the details of a new staff on recruiting them.

* **deletestaffdetails(con,cur)** :- This function is present in the delete.py file. It is used to delete all the details of a prticular staff on the basis of the attribute given by the user,i.e., when a staff is removed from his job.


* **updatebookdetails(con,cur)** :- This function is present in the update.py file. This function asks the user the field details they want to change and take the new data and Update the details of the book accordingly.

* **updatememberdetails(con,cur)** :- This function is present in the update.py file. This function asks the user the field details they want to change and take the new data and Update the details of a member accordingly.

* **updatestaffdetails(con,cur)** :- This function is present in the update.py file. This function asks the user the field details they want to change and take the new data and Update the details of a staff accordingly.

* **updatestoragedetails(con,cur)** :- This function is present in the update.py file. This function asks the user the field details they want to change and take the new data and Update the details of the storage table accordingly.

Books stats
* **query_1(con,cur)** :- This function is present in the queries.py file. It is an Aggregate query. It prints the Books stats such as AVERAGE_PRICE, MAX_PRICE, MIN_PRICE [of a book].

Number of books of a particular genre
* **query_2(con,cur)** :- This function is present in the queries.py file.It is an Analysis query. It prints the total number of books of a particular genre(entered by the user).

Names of members living in a particular city
* **query_3(con,cur)** :- This function is present in the queries.py file.It is a Projection query. It prints the mames of all the members living in a particular city(given by the user).

List of issued books
* **query_4(con,cur)** :- This function is present in the queries.py file.It is a Selection query. It lists all the issued books.

Search for Books starting with a particular word
* **query_5(con,cur)** :- This function is present in the queries.py file.It is a Search query.It Search for Books starting with a particular word and prints the Book_id and Book_Name.

`Note`: The MYSQL tables used by us included `References` and `DELETE ON CASCADE` that deletes any children Foreign Key rows in other tables. For example, on deleting an entry in Book table, it would automatically delete respective entries in Multi_Authors and Multi_Genres where Foreign Key would be defined.