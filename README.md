# Priya Electronics & Cable Network Complaint Management System (PECN-CMS)

Welcome to **PECN Complaint Management System (PECN-CMS)**, a user-friendly Python-based application designed to streamline the process of managing customer complaints for **Priya Electronics & Cable Network**. This system allows staff members to efficiently register complaints, update remarks, track unresolved issues, and retrieve detailed complaint information, all in one place.

### About Priya Electronics & Cable Network (PECN)
'Priya Electronics & Cable Network is a local business' that provides electronics, internet/broadband and cable services to customers. The Complaint Management System (PECN-CMS) was developed to ensure that customer concerns are handled promptly, efficiently, and with clear records of each interaction.

### Technologies Used
The PECN-CMS is built using:

- **Python 3** – The core programming language for application development.

- **PyWhatKit Library** – Enables automation features, including sending WhatsApp messages for complaint notifications.

- **SQL** – Manages the structured complaint database, ensuring efficient storage and retrieval of information.

## Features

1. **Register a New Complaint**  
   Register new complaints with details like customer name, contact information, address, and complaint type.
   
2. **Update Complaint Remarks**  
   Update remarks for existing complaints to reflect the latest resolution or status.

3. **View Complaints with NULL Remarks**  
   View a list of complaints where remarks are yet to be updated, ensuring timely follow-up.

4. **View Details of a Specific Complaint**  
   Retrieve detailed information about any complaint based on its unique complaint ID.

5. **Exit**  
   Close the application after completing your tasks.

## Prerequisites

Before using the system, ensure the following are installed on your system:

- **Python 3.x**: Download from [python.org](https://www.python.org/downloads/).
- **MySQL**: Ensure MySQL is installed and running. Download it from [MySQL](https://dev.mysql.com/downloads/).
- **Required Python Libraries**: Install the necessary libraries by running the following command:
  ```bash
  pip install mysql-connector-python pywhatkit
Database Setup
The system relies on a MySQL database to store complaint data. Follow these steps to set up the database:

1. Create Database
Log into MySQL using your terminal or MySQL Workbench:

         mysql -u root -p
   

Create the database for PECN-CMS:

      CREATE DATABASE pecn_complaints;
      USE pecn_complaints;
      
2. Create Complaints Table
Run the following SQL code to create the complaints table that will store the complaint details:

         CREATE TABLE complaints (
          comp_id INT AUTO_INCREMENT PRIMARY KEY,
          datetime VARCHAR(30),
          cust_name VARCHAR(50),
          c_no VARCHAR(11),        -- Customer's mobile number (11 digits)
          c_address VARCHAR(150),  -- Customer's address (up to 150 characters)
          comp_type VARCHAR(30),   -- Type of the complaint
          remarks VARCHAR(40),     -- Remarks about the complaint
          r_updationtime TIMESTAMP -- Timestamp for when the remarks were last updated
         );
      

3. Configure Database Connection in Scripts

In each Python script (RegisterComplain.py, ComplainUpdate.py, PendingComplain.py, SpecificComplain.py), update the database connection credentials to match your MySQL setup. Replace the following placeholders:

host: Usually ```localhost```, unless you are using a remote database.

user: Your MySQL ```username``` (default is ```root```).

password: Your MySQL password.

database: ```db_name``` (write database name of your choice and do the changes in all files).

For example, you will need to modify the connection part of the scripts like so:
      
      conn = mysql.connector.connect(
          
          host="localhost",
          
          user="root",
          
          password="your_password",  # Replace with your MySQL password
          
          database="db_name"
          
      )

## Installation

Clone the repository (or download the files) to your local machine:
      
      git clone https://github.com/jainish2001/PECN-CMS.git
      cd PECN-CMS

Install the required dependencies:
      
      pip install -r requirements.txt

Run the Complaint Management System: Navigate to the folder containing the scripts and run:

      python PECN-CMS.py

Packaging into Executable (Optional)

To create a standalone executable using PyInstaller, run the following command:

      pyinstaller --onefile PECN-CMS.py

After the build process, you will find the executable in the ```dist/``` directory.

## Usage

Once the application is running, the following menu will be displayed:

      
      Welcome to Priya Electronics & Cable Network 
      
      Complaint Management System (PECN-CMS)
      
      1. Register a new complaint
      
      2. Update remarks for a complaint
      
      3. View complaints with NULL remarks updation time
      
      4. View details of a specific complaint
      
      5. Exit
      
      Enter your choice:
      
Option 1: Register a new complaint by entering customer information, mobile number, complaint type, etc.

Option 2: Update remarks for an existing complaint by entering its complaint ID and new remarks.

Option 3: View all complaints that do not yet have remarks or have missing update timestamps.

Option 4: View detailed information of a specific complaint by providing its complaint ID.

Option 5: Exit the application.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
