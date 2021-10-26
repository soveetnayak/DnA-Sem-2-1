import subprocess as sp
import pymysql
import pymysql.cursors

def deletebookdetails(con,cur):
    
    try:
        row = {}
        print("Enter Field name and Field value on the basis of which you want to delete(ex. Book_id = 1): ")
        row["name"] = input("Field: ")
        row["value"] = input("Value: ")
        
        query = "DELETE FROM Books WHERE %s = %s" % (row["name"], row["value"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Deleted from Database! ")

    except Exception as e:
        con.rollback()
        print("Failed to delete into database!\n")
        print("> ", e)

    return

def deletemagazinedetails(con,cur):
    
    try:
        row = {}
        print("Enter Field name and Field value on the basis of which you want to delete(ex. Magazine_Name = VOGUE): ")
        row["name"] = input("Field: ")
        row["value"] = input("Value: ")
        
        query = "DELETE FROM Magazine WHERE %s = %s" % (row["name"], row["value"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Deleted from Database! ")

    except Exception as e:
        con.rollback()
        print("Failed to delete into database!\n")
        print("> ", e)

    return



def deletememberdetails(con,cur):

    try:
        row = {}
        print("Enter Field name and Field value on the basis of which you want to delete: ")
        row["name"] = input("Field: ")
        row["value"] = input("Value: ")
        
        query = "DELETE FROM Members WHERE %s = %s" % (row["name"], row["value"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Deleted from Database! ")

    except Exception as e:
        con.rollback()
        print("Failed to delete into database!\n")
        print("> ", e)

def deletestaffdetails(con,cur):

    try:
        row = {}
        print("Enter Field name and Field value on the basis of which you want to delete: ")
        row["name"] = input("Field: ")
        row["value"] = input("Value: ")
        
        query = "DELETE FROM Staff WHERE %s = %s" % (row["name"], row["value"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Deleted from Database! ")

    except Exception as e:
        con.rollback()
        print("Failed to delete into database!\n")
        print("> ", e)






