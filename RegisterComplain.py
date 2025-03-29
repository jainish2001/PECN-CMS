import time
import datetime
import pywhatkit as pw
import mysql.connector


def register_complaint():
    # Establishing connection with MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="db_name"
    )
    print(conn.connection_id)

    try:
        # Get the current time and format it as a string
        t = time.ctime()
        print(t)

        v = datetime.datetime.now()
        h = v.hour
        m = v.minute + 2

        # Check if minute exceeds 59, adjust hour accordingly
        if m > 59:
            h += 1
            m = m % 60

        a = input("Type 1 for Staff Dinesh\n"
                  "Type 2 for Staff Kuldeep\n"
                  "Type 3 for Staff Govind\n"
                  "4 to enter number by yourself\n"
                  "Enter the value (1, 2, 3 or 4): ")

        if a == '1':
            a = "+918003958958"
        elif a == '2':
            a = "+918003958958"
        elif a == '3':
            a = "+918003958958"
        elif a == 'j':
            a = "+918003958958"
        else:
            print("Enter the number : ")
            a = input("+91")
            a = str("+91" + a)
        print('\n', "------------------------------------------------------------", '\n')
        print("Staff M. No. : ", a)
        # a = "+918003958958"
        b1 = input("Enter customer mobile number. : ")
        b2 = input("Enter customer name. : ")
        b3 = input("Enter customer address : ")
        b4 = input("Enter complain type. : ")

        # Create the message string using concatenation
        b = "Customer M. No : " + b1 + '\n' \
            + "Customer Name : " + b2 + '\n' \
            + "Customer Address : " + b3 + '\n' \
            + "Complain Type : " + b4 + '\n'

        c = h
        d = m

        # Convert the message content to a string
        b = str(b)

        # Send the WhatsApp message
        # pw.sendwhatmsg(a, b, c, d)

        cur = conn.cursor()

        # Add 'c_address' to the value_insertion tuple
        value_insertion = (t, b2, b1, b3, b4, " ")

        # Table format
        # CREATE TABLE complaints (comp_id INT AUTO_INCREMENT PRIMARY KEY, datetime VARCHAR(30), cust_name VARCHAR(50), c_no VARCHAR(15), c_address VARCHAR(100), comp_type VARCHAR(30), remarks VARCHAR(40));
        s = "INSERT INTO complaints (datetime, cust_name, c_no, c_address, comp_type, remarks) VALUES (%s, %s, %s, %s, %s, %s)"

        cur.execute(s, value_insertion)
        conn.commit()

        # Get the last inserted auto-incremented comp_id
        comp_id = cur.lastrowid

        # Display the comp_id
        # print("Complaint ID:", comp_id)

        # Create the message string using concatenation

        b = "Complaint ID : " + str(comp_id) + '\n' \
            + "Customer M. No : " + b1 + '\n' \
            + "Customer Name : " + b2 + '\n' \
            + "Customer Address : " + b3 + '\n' \
            + "Complain Type : " + b4 + '\n'
        print('\n', "-------------------------------------", '\n')
        print(b)
        # Send the WhatsApp message
        pw.sendwhatmsg(a, b, c, d)

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        # Close the cursor and the connection in the final block to ensure they are closed properly
        if cur:
            cur.close()
        if conn:
            conn.close()
    print('\n', "-------------------------------------------------------------", '\n')
    pass
