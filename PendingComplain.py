import mysql.connector


def view_null_remarks_updation():
    # Establishing connection with MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="db_name"
    )

    try:
        cur = conn.cursor()

        # SQL statement to select records where r_updationtime is NULL
        select_query = "SELECT * FROM complaints WHERE r_updationtime IS NULL"

        # Execute the SELECT query
        cur.execute(select_query)

        # Fetch all the records that match the criteria
        records = cur.fetchall()

        # Display the results
        if records:
            print("Complaints where r_updationtime is NULL:")
            for record in records:
                print(f"Complaint ID: {record[0]}, Customer Name: {record[2]}, Customer Mobile No: {record[3]}")
        else:
            print("No complaints found where Remarks Updation Timing  is NULL.")

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
