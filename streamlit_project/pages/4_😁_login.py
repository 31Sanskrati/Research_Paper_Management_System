import streamlit as st
import mysql.connector
import bcrypt

# Connect to MySQL database
def connect_to_db():
    connection = mysql.connector.connect(
        host = 'localhost',
        port = '3307',
        user = 'root',
        passwd = 'Anni@123',
        auth_plugin='mysql_native_password',
        database = 'seproject'
    )
    return connection

# Check if the username and password match
def authenticate(username, password):
    connection = connect_to_db()
    cursor = connection.cursor()
    
    query = "SELECT * FROM USERS WHERE empID = %s AND password = %s"
    cursor.execute(query, (username, password))
    
    result = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    if result:
        return True
    else:
        return False
    
# Create a new user
def create_user(username, password):
    connection = connect_to_db()
    cursor = connection.cursor()
    
    # Check if the empID already exists in the database
    query = "SELECT * FROM USERS WHERE empID = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    
    if result:
        st.warning("Employee ID already registered. Use different ID.")
    else:
        # Insert the user into the database
        query = "INSERT INTO USERS (empID, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        connection.commit()
        st.success("Successfully added to database! You can now log in.")
    
    cursor.close()
    connection.close()


# Login page
def login():
    st.title("Let's get you authenticated")
    st.caption("Don't worry, I'll add you to the database")

    empID = str(st.text_input("Employee ID"))
    password = str(st.text_input("Password", type="password"))

    login_clicked = st.button("Login")
    add_to_db_clicked = False

    if login_clicked:
        if authenticate(empID, password):
            st.success("Authentication successful!")
            st.session_state['logged_in'] = True
            st.session_state['empID'] = empID
        else:
            st.error("Something went wrong")
            add_to_db_clicked = True

    if add_to_db_clicked:
        create_user(empID, password)

# Main function
def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    login()

if __name__ == '__main__':
    main()
