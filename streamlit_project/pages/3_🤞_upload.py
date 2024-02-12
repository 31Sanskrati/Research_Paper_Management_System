import streamlit as st
import base64
import mysql.connector
from mysql.connector import Error
import PyPDF2
from datetime import datetime

research_topics = [
    # Artificial Intelligence
    "Artificial Intelligence",
    "AI",
    "Machine Intelligence",
    "Cognitive Computing",
    
    # Machine Learning
    "Machine Learning",
    "ML",
    "Statistical Learning",
    "Pattern Recognition",
    
    # Computer Vision
    "Computer Vision",
    "CV",
    "Image Analysis",
    "Visual Perception",
    
    # Natural Language Processing
    "Natural Language Processing",
    "NLP",
    "Text Mining",
    "Language Understanding",
    
    # Data Mining
    "Data Mining",
    "DM",
    "Knowledge Discovery",
    "Pattern Mining",
    
    # Big Data Analytics
    "Big Data Analytics",
    "Large-scale Data Analysis",
    "Data-driven Decision Making",
    
    # Internet of Things (IoT)
    "Internet of Things",
    "IoT",
    "Embedded Systems",
    "Smart Devices",
    
    # Cloud Computing
    "Cloud Computing",
    "Distributed Computing",
    "Virtualization",
    
    # Distributed Systems
    "Distributed Systems",
    "Parallel Computing",
    "Cluster Computing",
    
    # Computer Networks
    "Computer Networks",
    "Network Protocols",
    "Network Security",
    
    # Wireless Sensor Networks
    "Wireless Sensor Networks",
    "Sensor Data Fusion",
    "Energy Harvesting",
    
    # Blockchain Technology
    "Blockchain Technology",
    "Distributed Ledger",
    "Cryptocurrency",
    
    # Cybersecurity
    "Cybersecurity",
    "Information Security",
    "Network Defense",
    
    # Privacy and Data Protection
    "Privacy and Data Protection",
    "Data Privacy",
    "Anonymization Techniques",
    
    # Human-Computer Interaction
    "Human-Computer Interaction",
    "User Experience",
    "Interface Design",
    
    # Virtual Reality
    "Virtual Reality",
    "VR",
    "Immersive Environments",
    "Virtual Simulation",
    
    # Augmented Reality
    "Augmented Reality",
    "AR",
    "Mixed Reality",
    "AR Applications",
    
    # Computer Graphics
    "Computer Graphics",
    "Rendering Techniques",
    "Geometric Modeling",
    
    # Image Processing
    "Image Processing",
    "Image Restoration",
    "Feature Extraction",
    
    # Information Retrieval
    "Information Retrieval",
    "Search Engines",
    "Text Classification",
    
    # Data Science
    "Data Science",
    "Data Analysis",
    "Predictive Modeling",
    
    # Bioinformatics
    "Bioinformatics",
    "Computational Genomics",
    "Protein Structure Prediction",
    
    # Computational Biology
    "Computational Biology",
    "Computational Genetics",
    "Systems Biology",
    
    # Robotics
    "Robotics",
    "Robot Control",
    "Autonomous Systems",
    
    # Autonomous Systems
    "Autonomous Systems",
    "Unmanned Vehicles",
    "Intelligent Agents",
    
    # Embedded Systems
    "Embedded Systems",
    "Real-time Systems",
    "Embedded Software",
    
    # Operating Systems
    "Operating Systems",
    "Kernel Design",
    "Process Scheduling",
    
    # Compiler Design
    "Compiler Design",
    "Language Translation",
    "Code Optimization",
    
    # Software Engineering
    "Software Engineering",
    "Software Development Process",
    "Requirements Engineering",
    
    # Programming Languages
    "Programming Languages",
    "Language Design",
    "Compiler Construction",
    
    # Computer Architecture
    "Computer Architecture",
    "Instruction Set Design",
    "Microarchitecture",
    "Memory Hierarchy",
    "Parallel Processing",
    
    # High-Performance Computing
    "High-Performance Computing",
    "Supercomputing",
    "Parallel Algorithms",
    
    # Quantum Computing
    "Quantum Computing",
    "Quantum Algorithms",
    "Quantum Information Theory",
    
    # Cryptography
    "Cryptography",
    "Encryption",
    "Cryptographic Protocols",
    
    # Game Development
    "Game Development",
    "Game Design",
    "Game Engines",
    
    # Mobile App Development
    "Mobile App Development",
    "iOS Development",
    "Android Development",
    
    # Web Development
    "Web Development",
    "Front-end Development",
    "Back-end Development",
    
    # Social Networks
    "Social Networks",
    "Online Communities",
    "Social Media Analysis",
    
    # Data Visualization
    "Data Visualization",
    "Information Graphics",
    "Visual Analytics",
    
    # Ethical Hacking
    "Ethical Hacking",
    "Penetration Testing",
    "Vulnerability Assessment",
    
    # Artificial Neural Networks
    "Artificial Neural Networks",
    "Deep Learning",
    "Neurocomputing",
    
    # Evolutionary Algorithms
    "Evolutionary Algorithms",
    "Genetic Algorithms",
    "Evolutionary Optimization",
    
    # Computer-Assisted Education
    "Computer-Assisted Education",
    "E-Learning",
    "Intelligent Tutoring Systems",
    
    # Virtual Learning Environments
    "Virtual Learning Environments",
    "Online Learning Platforms",
    "Digital Learning Tools",
    
    # Natural Computing
    "Natural Computing",
    "Biologically Inspired Computing",
    "Swarm Intelligence",
    
    # Digital Image Processing
    "Digital Image Processing",
    "Image Enhancement",
    "Image Compression",
    
    # Pattern Recognition
    "Pattern Recognition",
    "Feature Detection",
    "Classification Algorithms",
    
    # Computational Linguistics
    "Computational Linguistics",
    "Language Modeling",
    "Text-to-Speech Synthesis",
    
    # Computational Geometry
    "Computational Geometry",
    "Geometric Algorithms",
    "Spatial Data Structures",
    
    # Computer Algebra Systems
    "Computer Algebra Systems",
    "Symbolic Computation",
    "Mathematical Reasoning",
    
    # Network Security
    "Network Security",
    "Intrusion Detection",
    "Firewall Technologies",
    
    # Software Testing
    "Software Testing",
    "Test Automation",
    "Quality Assurance",
    
    # Information Security
    "Information Security",
    "Data Protection",
    "Access Control",
    
    # Internet Security
    "Internet Security",
    "Web Security",
    "Secure Protocols",
    
    # Computer Forensics
    "Computer Forensics",
    "Digital Evidence Analysis",
    "Incident Response",
    
    # Multimedia Systems
    "Multimedia Systems",
    "Multimedia Compression",
    "Multimedia Retrieval",
    
    # Bio-inspired Computing
    "Bio-inspired Computing",
    "Swarm Robotics",
    "Biologically Motivated Algorithms",
    
    # Internet of Things Security
    "Internet of Things Security",
    "IoT Privacy",
    "Device Authentication",
    
    # Cloud Security
    "Cloud Security",
    "Secure Cloud Architectures",
    "Data Privacy in the Cloud",
    
    # Quantum Cryptography
    "Quantum Cryptography",
    "Quantum Key Distribution",
    "Post-Quantum Cryptography",
    
    # Human-Robot Interaction
    "Human-Robot Interaction",
    "Robot Behavior",
    "Social Robotics",
    
    # Ubiquitous Computing
    "Ubiquitous Computing",
    "Pervasive Technology",
    "Mobile Sensing",
    
    # Autonomous Vehicles
    "Autonomous Vehicles",
    "Self-Driving Cars",
    "Intelligent Transportation Systems",
    
    # Software-defined Networking
    "Software-defined Networking",
    "SDN",
    "Network Virtualization",
    "Network Management",
    
    # Neuromorphic Computing
    "Neuromorphic Computing",
    "Brain-Inspired Computing",
    "Neuromorphic Engineering",
    
    # Data Compression
    "Data Compression",
    "Lossless Compression",
    "Image and Video Compression",
    
    # Computational Neuroscience
    "Computational Neuroscience",
    "Neural Modeling",
    "Brain Signal Analysis",
    
    # Green Computing
    "Green Computing",
    "Energy-Efficient Algorithms",
    "Sustainable Computing",
    
    # Pervasive Computing
    "Pervasive Computing",
    "Ubiquitous Technology",
    "Context-Aware Systems",
    
    # Mobile Computing
    "Mobile Computing",
    "Mobile Networking",
    "Mobile Applications",
    
    # Health Informatics
    "Health Informatics",
    "Electronic Health Records",
    "Medical Data Analysis",
    
    # Digital Forensics
    "Digital Forensics",
    "Cybercrime Investigation",
    "Network Traffic Analysis",
    
    # Wireless Communication
    "Wireless Communication",
    "Mobile Networks",
    "Wireless Sensor Networks",
    
    # Data Warehousing
    "Data Warehousing",
    "Data Integration",
    "Online Analytical Processing",
    
    # Knowledge Representation and Reasoning
    "Knowledge Representation and Reasoning",
    "Ontology Engineering",
    "Logic Programming",
    
    # Internet Algorithms
    "Internet Algorithms",
    "Graph Algorithms",
    "Network Routing",
    
    # Recommender Systems
    "Recommender Systems",
    "Collaborative Filtering",
    "Content-based Filtering",
    
    # Fault-tolerant Systems
    "Fault-tolerant Systems",
    "Reliability Engineering",
    "Redundancy Techniques",
    
    # Computer Music
    "Computer Music",
    "Audio Synthesis",
    "Music Information Retrieval",
    
    # Data Privacy
    "Data Privacy",
    "Privacy-preserving Techniques",
    "Anonymity and Identity Protection",
    
    # Geographic Information Systems
    "Geographic Information Systems",
    "Spatial Data Analysis",
    "Geospatial Visualization",
    
    # Internet of Medical Things
    "Internet of Medical Things",
    "IoMT",
    "Medical Device Connectivity",
    "Remote Patient Monitoring",
    
    # Geometric Algorithms
    "Geometric Algorithms",
    "Computational Geometry",
    "Geometric Data Structures",
    
    # Fuzzy Systems
    "Fuzzy Systems",
    "Fuzzy Logic",
    "Fuzzy Control",
    
    # Evolutionary Robotics
    "Evolutionary Robotics",
    "Robot Evolution",
    "Robotic Adaptation",
    
    # Quantum Machine Learning
    "Quantum Machine Learning",
    "Quantum-enhanced Learning",
    "Quantum Neural Networks"
]


def extract_metadata(pdf_file):
    uploaded_paper = pdf_file
    empID = st.session_state['empID']
    print(empID)

    reader = PyPDF2.PdfReader(pdf_file)

    print("Metadata -------------")
    metadata = reader.metadata
    print(metadata)

    print("----------------")
    title_of_doc = metadata.get('/Title', 'N/A')
    publishers = metadata.get('/Creator', 'N/A')
    authors = metadata.get('/Author', 'N/A')
    date_of_publication = metadata.get('/CreationDate','N/A')
    keywords = metadata.get('/Keywords', 'N/A')

    # Extracting the relevant information from publishers authors
    if authors != 'N/A':
        authors = authors.replace('and', ',').replace('&', ',')
        authors_list = authors.split(',')

        for i in range(len(authors_list)):
            author = authors_list[i].strip()
            author = ''.join(c for c in author if c.isalpha() or c.isspace())
            authors_list[i] = author

        authors = ', '.join(authors_list)


    # Extracting the relevant information from publishers
    if publishers != 'N/A':
        publishers = publishers.strip().split(',')[0]

    # Extracting the relevant information from keywords
    if keywords != 'N/A':
        keywords = keywords.replace(';', ',')
        keywords_list = keywords.split(',')

        for i in range(len(keywords_list)):
            keyword = keywords_list[i].strip()
            keyword = ''.join(c for c in keyword if c.isalnum() or c.isspace())
            keywords_list[i] = keyword

        keywords = ','.join(keywords_list)

    else:
        words = [item.capitalize() for item in title_of_doc.split()]

        # Finding the common words between the research topics list and the title
        common_words = [word for word in words if word in research_topics]
        keywords = ','.join(common_words)

    # Change format of date
    try:
        if date_of_publication[0] == 'D':
            date_obj = datetime.strptime(date_of_publication[2:-7], '%Y%m%d%H%M%S')
            formatted_date = date_obj.strftime('%B %d, %Y')
        else:
            formatted_date = date_of_publication
    except:
        formatted_date = metadata.get('/CreationDate--Text', 'N/A')

    print("Title:", title_of_doc)
    print("Publisher:", publishers)
    print("Author:", authors)
    print("Keywords:", keywords)
    print("Date of Publication:", formatted_date)

    upload_to_database(uploaded_paper, title_of_doc, authors, publishers, formatted_date, keywords, empID)

def upload_to_database(uploaded_paper, title_of_doc, authors, publisher, date_of_publication, keywords, empID):
    connection = mysql.connector.connect(
            host='localhost',
            port='3307',
            user='root',
            passwd='Anni@123',
            auth_plugin='mysql_native_password',
            database='seproject'
        )

    # connection is successful
    if connection.is_connected():
        print("------- Connected to database for uploading -------")
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
    else:
        print("------- Unable to connect to the database -------")
        return

    cursor = connection.cursor()
    research_paper = uploaded_paper.read()

    # Check if the combination already exists in the database
    check_query = "SELECT * FROM DOCUMENTS WHERE title_of_doc = %s AND authors = %s AND publisher = %s AND date_of_publication = %s AND keyword = %s"
    cursor.execute(check_query, (str(title_of_doc), str(authors), str(publisher), str(date_of_publication), str(keywords)))
    result = cursor.fetchone()


    if result is not None:
        print("paper already existed")
    else:
        # Insert the research paper into the database
        insert_query = "INSERT INTO DOCUMENTS (doc, title_of_doc, authors, publisher, date_of_publication, keyword, empID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        insert_tuple = (research_paper, str(title_of_doc), str(authors), str(publisher), str(date_of_publication), str(keywords), str(empID))
        
        try:
            cursor.execute(insert_query, insert_tuple)
            connection.commit()
            cursor.nextset()  # Move to the next result set to skip any unread result
            cursor.close()
            connection.close()
        except Error as e:
            st.error(f"Error occurred: {e}")
            st.error(f"Error details: {cursor._executed}")

    st.success("Research Paper Uploaded")

    # Close the cursor and connection when finished
    cursor.close()
    connection.close()


st.subheader("Upload your Research Paper")
st.caption("Please make sure the file is in pdf format")
st.write("\n")

#upload research paper
uploaded_paper = st.file_uploader('Upload your research paper', type=['pdf'])

if uploaded_paper is not None:
    # Show PDF
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'empID' not in st.session_state:
        st.session_state['empID'] = None

    research_paper = uploaded_paper.read()
    base64_pdf = base64.b64encode(research_paper).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="720" height="350" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

    # Submit the paper
    if st.session_state['logged_in']:
        if st.button('Submit'):
            extract_metadata(uploaded_paper)
    else:
        st.session_state['logged_in'] = False
        st.info("Please login first to upload")