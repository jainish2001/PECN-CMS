import mysql.connector


def view_complaint_details():
    # Establishing connection with MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="db_name"
    )

    try:
        cur = conn.cursor()

        # Assuming you have comp_id value from user input or some other source
        comp_id_to_display = input("Enter complain id: "'\n')

        # SQL statement to select all details of the specified comp_id
        select_query = "SELECT * FROM complaints WHERE comp_id = %s"

        # Execute the SELECT query with comp_id_to_display as a parameter
        cur.execute(select_query, (comp_id_to_display,))

        # Fetch the record that matches the criteria
        record = cur.fetchone()

        # Display the results
        if record:
            print("Details of Complaint with comp_id", comp_id_to_display)
            print(f"Complaint ID: {record[0]}")
            print(f"DateTime: {record[1]}")
            print(f"Customer Name: {record[2]}")
            print(f"Customer Mobile No: {record[3]}")
            print(f"Customer Address: {record[4]}")
            print(f"Complaint Type: {record[5]}")
            print(f"Remarks: {record[6]}")
            print(f"Remarks Timing: {record[7]}")
        else:
            print("No details found for the specified comp_id.")

    except mysql.connector.Error as e:
        print("An error occurred:", str(e))

    finally:
        # Close the cursor and the connection in the final block to ensure they are closed properly
        if cur:
            cur.close()
        if conn:
            conn.close()
    print('\n', "-------------------------------------------------------------", '\n')
    pass
