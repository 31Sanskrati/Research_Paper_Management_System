# Research Paper Management System
The Research Paper Management System is a sophisticated software solution designed to streamline the process of uploading, organizing, and retrieving research papers for researchers and academics. This system aims to simplify the management of research papers by automating metadata extraction and providing powerful search capabilities, ultimately enhancing productivity.

## Overview
Uploading and managing research papers manually can be time-consuming and error-prone. The Research Paper Management System addresses these challenges by automating the extraction of metadata from uploaded papers, eliminating the need for manual data entry. Researchers can easily upload their papers and quickly retrieve them using the system's robust search functionality.

## Key Features
- **Automatic Metadata Extraction:** Extracts metadata like title, authors, and keywords from uploaded papers, saving time.
- **Search and Retrieval:** Offers fast and accurate search based on title, author, or keywords.
- **Security and Privacy:** Implements encryption and access controls to protect user data.
- **Mobile Compatibility:** Provides a responsive interface for mobile devices.
- **User-Friendly Interface:** Offers an intuitive interface for easy navigation and interaction.

## Technology Stack
The Research Paper Management System utilizes the following technologies:

- Frontend: Streamlit, Python
- Backend: Python
- Database: MySQL
- Libraries: PyPDF2, BeautifulSoup

## Setup Instructions
To set up the Research Paper Management System locally, follow these steps:

1. Clone the repository from GitHub:
`git clone <repository_url>`
2. Install Python if not already installed. You can download it from the official Python website.
3. Create a virtual environment:
`python -m venv env`
4. Activate the virtual environment:
Windows:
`env\Scripts\activate`
Linux/Mac:
`source env/bin/activate`
5. Install required Python packages:
`pip install streamlit mysql-connector-python PyPDF2 beautifulsoup4`
6. Set up MySQL database and create a database for the application.
7. Configure the database connection in the application code.
8. Run the application:
`streamlit run app.py`

*By providing automated metadata extraction, efficient document organization, and robust security measures, the Research Paper Management System simplifies research paper management and enhances productivity for researchers and academics.*
