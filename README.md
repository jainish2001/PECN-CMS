# PECN-CMS
# Priya Electronics & Cable Network Complaint Management System (PECN-CMS)

Welcome to **PECN Complaint Management System (PECN-CMS)**, a Python-based application designed for managing customer complaints efficiently. The system allows users to register complaints, update remarks, view complaints with null remarks, and retrieve specific complaint details.

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

bash
Copy
mysql -u root -p
Create the database for PECN-CMS:

sql
Copy
CREATE DATABASE pecn_complaints;
USE pecn_complaints;
2. Create Complaints Table
Run the following SQL code to create the complaints table that will store the complaint details:

sql
Copy
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

host: Usually "localhost", unless you are using a remote database.

user: Your MySQL username (default is "root").

password: Your MySQL password.

database: "pecn_complaints" (or whatever database name you used).

For example, you will need to modify the connection part of the scripts like so:

python
Copy
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",  # Replace with your MySQL password
    database="pecn_complaints"
)
Installation
Clone the repository (or download the files) to your local machine:

bash
Copy
git clone https://github.com/yourusername/PECN-CMS.git
cd PECN-CMS
Install the required dependencies:

bash
Copy
pip install -r requirements.txt
Run the Complaint Management System: Navigate to the folder containing the scripts and run:

bash
Copy
python PECN-CMS.py
Packaging into Executable (Optional)
To create a standalone executable using PyInstaller, run the following command:

bash
Copy
pyinstaller --onefile PECN-CMS.py
After the build process, you will find the executable in the dist/ directory.

Usage
Once the application is running, the following menu will be displayed:

sql
Copy
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

Troubleshooting
"ModuleNotFoundError": Ensure all required modules are installed and located in the same directory as the script, or within your Python environment.

PyInstaller Errors: If PyInstaller fails to locate modules, try using the --add-data flag to include external files.

Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. Ensure your contributions are well-tested and documented.

How to contribute:
Fork the repository.

Create a new feature branch.

Make your changes and commit them.

Open a pull request describing your changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

markdown
Copy

---

This Markdown file is structured for clarity and readability. It includes:

- **Title** and overview of the project
- **Features** of the system
- **Database setup** instructions (with SQL code for table creation)
- **Installation** and **Packaging** instructions
- **Usage instructions** for interacting with the system
- **Troubleshooting tips**
- **Contributing** guidelines
- **License** information

You can copy-paste this content into a `README.md` file for your project. Let me know if you need f## Prerequisites

Before using the system, ensure the following are installed on your system:

- **Python 3.x**: Download from [python.org](https://www.python.org/downloads/).
- **MySQL**: Ensure MySQL is installed and running. Download it from [MySQL](https://dev.mysql.com/downloads/).
- **Required Python Libraries**: Install the necessary libraries by running the following command:
  ```bash
  pip install mysql-connector-python pywhatkit
  ```

## Database Setup

The system relies on a MySQL database to store complaint data. Follow these steps to set up the database:

### 1. **Create Database**

Log into MySQL using your terminal or MySQL Workbench:

```bash
mysql -u root -p
```

Create the database for PECN-CMS:

```sql
CREATE DATABASE pecn_complaints;
USE pecn_complaints;
```

### 2. **Create Complaints Table**

Run the following SQL code to create the `complaints` table that will store the complaint details:

```sql
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
```

### 3. **Configure Database Connection in Scripts**

In each Python script (`RegisterComplain.py`, `ComplainUpdate.py`, `PendingComplain.py`, `SpecificComplain.py`), update the database connection credentials to match your MySQL setup. Replace the following placeholders:

- `host`: Usually `"localhost"`, unless you are using a remote database.
- `user`: Your MySQL username (default is `"root"`).
- `password`: Your MySQL password.
- `database`: `"pecn_complaints"` (or whatever database name you used).

For example, you will need to modify the connection part of the scripts like so:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",  # Replace with your MySQL password
    database="pecn_complaints"
)
```

## Installation

1. Clone the repository (or download the files) to your local machine:

   ```bash
   git clone https://github.com/yourusername/PECN-CMS.git
   cd PECN-CMS
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Complaint Management System**:
   Navigate to the folder containing the scripts and run:

   ```bash
   python PECN-CMS.py
   ```

## Packaging into Executable (Optional)

To create a standalone executable using **PyInstaller**, run the following command:

```bash
pyinstaller --onefile PECN-CMS.py
```

After the build process, you will find the executable in the `dist/` directory.

## Usage

Once the application is running, the following menu will be displayed:

```
Welcome to Priya Electronics & Cable Network 
Complaint Management System (PECN-CMS)
1. Register a new complaint
2. Update remarks for a complaint
3. View complaints with NULL remarks updation time
4. View details of a specific complaint
5. Exit
Enter your choice:
```

- **Option 1**: Register a new complaint by entering customer information, mobile number, complaint type, etc.
- **Option 2**: Update remarks for an existing complaint by entering its complaint ID and new remarks.
- **Option 3**: View all complaints that do not yet have remarks or have missing update timestamps.
- **Option 4**: View detailed information of a specific complaint by providing its complaint ID.
- **Option 5**: Exit the application.

## Troubleshooting

- **"ModuleNotFoundError"**: Ensure all required modules are installed and located in the same directory as the script, or within your Python environment.
- **PyInstaller Errors**: If PyInstaller fails to locate modules, try using the `--add-data` flag to include external files.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. Ensure your contributions are well-tested and documented.

### How to contribute:
1. Fork the repository.
2. Create a new feature branch.
3. Make your changes and commit them.
4. Open a pull request describing your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

---

This Markdown file is structured for clarity and readability. It includes:

- **Title** and overview of the project
- **Features** of the system
- **Database setup** instructions (with SQL code for table creation)
- **Installation** and **Packaging** instructions
- **Usage instructions** for interacting with the system
- **Troubleshooting tips**
- **Contributing** guidelines
- **License** information

You can copy-paste this content into a `README.md` file for your project. Let me know if you need further changes!
