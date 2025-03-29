import mysql.connector


def update_remarks():
    # Establishing connection with MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="db_name"
    )

    try:
        # Assuming you have comp_id and remarks values from user input or some other source
        comp_id_to_update = input("Enter complain id: ")
        new_remarks = input("Enter remarks: ")

        cur = conn.cursor()

        # SQL statement to update the remarks and r_updationtime for the specified comp_id
        update_query = "UPDATE complaints SET remarks = %s, r_updationtime = NOW() WHERE comp_id = %s"

        # Execute the update query with the new_remarks and comp_id_to_update as parameters
        cur.execute(update_query, (new_remarks, comp_id_to_update))

        # Check if any row was affected by the update query
        if cur.rowcount > 0:
            print("Remarks updated successfully!")
        else:
            print("No rows were updated. Please check the complaint ID.")

        # Commit the changes to the database
        conn.commit()

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
