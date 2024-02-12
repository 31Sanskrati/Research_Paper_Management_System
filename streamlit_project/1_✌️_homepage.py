import streamlit as st
import mysql.connector
from mysql.connector import Error
import matplotlib.pyplot as plt

css_example = '''                                                                                                                                                     
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
.fa-arrow-down {
    font-size: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100px; /* Adjust the height as needed */
}
</style>

<i class="fa-solid fa-arrow-down"></i>
'''

css_style = '''
<style>
.btn {
    background-color: red;
    color: white;
    font-size: 14px;
    padding: 8px 12px;
    border-radius: 8px;
    text-decoration: none;
}

.btn:hover {
    background-color: darkred;
}

.btn:visited {
    color: white;
}
</style>
'''

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

st.set_page_config(
    layout="wide",
    page_title='Research Paper Management System',
    page_icon='✌️'
)

st.markdown("<h1 style='text-align: center; padding: 15px;'>Research Paper Management System</h1>",
            unsafe_allow_html=True)

st.write("Our website allows users to upload their research paper, and using advanced machine learning algorithms, we extract key details such as author names, publishers, and titles. Our dashboard, built on the Streamlit platform, provides an intuitive user interface to make the process seamless and efficient. This tool is designed to save researchers time and effort, allowing them to focus on their core work rather than administrative tasks.")
st.write("\n\n\n\n")
st.write(css_example, unsafe_allow_html=True)
st.write("\n\n\n\n")

# LINE GRAPH FOR UNIQUE KEYWORDS
# get unique keywords
st.markdown("<h4 style='text-align: center; padding: 15px;'>Research Papers Details</h4>",
            unsafe_allow_html=True)
keyword_select_query = "SELECT keyword FROM DOCUMENTS"
cursor.execute(keyword_select_query)
rows = cursor.fetchall()

keywords = [row[0] for row in rows]

keyword_dic = {}
for each_string in keywords:
    split_values = each_string.split(',')
    for value in split_values:
        if value.strip() not in keyword_dic:
            keyword_dic[value.strip()] = 0
        keyword_dic[value.strip()] += 1

print(keyword_dic)

keywords = list(keyword_dic.keys())
frequencies_keywords = list(keyword_dic.values())

fig1, ax1 = plt.subplots(figsize=(12, 4), dpi=80, facecolor='#1f1f1f')

# Customize line graph properties
ax1.plot(keywords, frequencies_keywords, marker='o',
         linestyle='-', color='steelblue')

# Set labels and title
ax1.set_xlabel('Topics', fontsize=12, color='white')
ax1.set_ylabel('No. of research papers', fontsize=12, color='white')
ax1.set_title('No. of research papers uploaded on a particular topic',
              fontsize=14, color='white')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right', color='white')

# Set grid color
ax1.grid(color='gray', linestyle='--', linewidth=0.5)

# Set tick colors
ax1.tick_params(axis='x', colors='white')
ax1.tick_params(axis='y', colors='white')

# Set spines color
ax1.spines['bottom'].set_color('white')
ax1.spines['left'].set_color('white')

# Remove top and right spines
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.patch.set_alpha(0.0)

# Display the line graph using Streamlit
st.pyplot(fig1, facecolor='#1f1f1f')

# LINE GRAPH FOR UNIQUE PUBLISHERS
# get unique keywords
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
publisher_select_query = "SELECT publisher FROM DOCUMENTS"
cursor.execute(publisher_select_query)
rows = cursor.fetchall()

publishers = [row[0] for row in rows]

publisher_dic = {}
for each_string in publishers:
    split_values = each_string.split(',')
    for value in split_values:
        if value.strip() not in publisher_dic:
            publisher_dic[value.strip()] = 0
        publisher_dic[value.strip()] += 1

print(publisher_dic)

publishers_list = list(publisher_dic.keys())
frequencies_publisher = list(publisher_dic.values())

# Create a bar chart
fig, ax = plt.subplots(figsize=(12, 6), dpi=80, facecolor='#1f1f1f')

# Customize bar chart properties
ax.bar(publishers_list, frequencies_publisher, color='steelblue')

# Set labels and title
ax.set_xlabel('Publishers', fontsize=12, color='white')
ax.set_ylabel('No. of research papers', fontsize=12, color='white')
ax.set_title('No. of research papers uploaded from a particular publisher',
             fontsize=14, color='white')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right', color='white')

# Set grid color
ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Set tick colors
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

# Set spines color
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Set the overall background to transparent
ax.patch.set_alpha(0.0)

# Display the bar chart using Streamlit
st.pyplot(fig, facecolor='#1f1f1f')

st.write("")
st.write("\n")
st.markdown("<h4 style='text-align: center; padding: 15px;'>Become the part of the community</h4>",
            unsafe_allow_html=True)
st.write("\n")
st.write("This project aims to ease the process of uploading and managing research papers for researchers and academics. Help us achieveing this goal by joining the community, uploading your work and appreciating others work.")
st.write("")
st.write("")
st.markdown('<a href="/login" style="text-align: center; display:block; text-decoration: none; color: black; background-color: white; padding: 8px 4px;" target=_top>Join Community</a>', unsafe_allow_html=True)
