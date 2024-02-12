import streamlit as st
import base64
import mysql.connector
from mysql.connector import Error
import random
import PyPDF2

# connecting to mysql database
connection = mysql.connector.connect(
    host='localhost',
    port='3307',
    user='root',
    passwd='Anni@123',
    auth_plugin='mysql_native_password',
    database='seproject'
)

#connection is successful
if connection.is_connected():
    print("````````Connected to database for search```````")
    db_Info = connection.get_server_info()
    print("Connected to MySQl Server versiob ", db_Info)
else:
    print("````````Unable to connect to database````````")

cursor = connection.cursor()

st.subheader("Help us in finding your paper by specifying some details")

# select unique keywords from database
keyword_select_query = "SELECT DISTINCT keyword FROM DOCUMENTS"
cursor.execute(keyword_select_query)
rows = cursor.fetchall()

keywords = [row[0] for row in rows]

unique_keywords = set()
for each_string in keywords:
    split_values = each_string.split(',')
    for value in split_values:
        unique_keywords.add(value.strip())

unique_keywords = list(unique_keywords)

st.write('\n')
selected_type = st.multiselect('Select type', list(
    ['Article', 'Journal', 'Book Chapter']))
selected_params = st.text_input(
    "Enter title, publisher's or author's name").lower()
selected_keywords = st.multiselect('Choose the topic', list(unique_keywords))

selected_params = selected_params.strip()

if st.button("Submit"):
    search_query = "SELECT * FROM DOCUMENTS WHERE 1=1"
    search_params = []

    if selected_params:
        search_query += " AND (title_of_doc LIKE %s OR publisher LIKE %s OR authors LIKE %s)"
        search_params += [f"%{selected_params}%",
                          f"%{selected_params}%", f"%{selected_params}%"]

    if selected_keywords:
        keyword_conditions = " OR ".join(
            ["keyword LIKE %s"] * len(selected_keywords))
        search_query += " AND (" + keyword_conditions + ")"
        search_params += [f"%{keyword}%" for keyword in selected_keywords]

    if selected_type:
        type_conditions = " OR ".join(["type = %s"] * len(selected_type))
        search_query += " AND (" + type_conditions + ")"
        search_params += selected_type

    cursor.execute(search_query, search_params)
    search_results = cursor.fetchall()

    for result in search_results:
        docID = result[0]
        doc = result[1]
        title_of_doc = result[2]
        authors = result[3]
        publisher = result[4]
        date_of_publication = result[5]
        keyword = result[6]

        print(type(doc))

        # Display the search results using st.write or any other method you prefer
        st.write("\n")
        st.subheader(title_of_doc)
        st.caption(keyword)
        with st.expander('Details:', expanded=False):
            st.write("authors:", authors)
            st.write("publisher:", publisher)
            st.write("date_of_publication:", date_of_publication)

            # Create a Base64 encoded string from the binary data
            encoded_pdf = base64.b64encode(doc)
            # Convert the encoded PDF back to a string
            base64_pdf = encoded_pdf.decode('utf-8')

            download_filename = f"{title_of_doc}.pdf"
            count = random.randint(1, 10000000)
            st.download_button("Download the paper", data=base64_pdf, file_name=download_filename, mime='application/octet-stream', key=count)

            st.write("\n")
