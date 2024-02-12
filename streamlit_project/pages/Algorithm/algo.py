import PyPDF2
from datetime import datetime
import re
from bs4 import BeautifulSoup
import reverse_enggineering
from keywords import research_topics

def extract_metadata(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)

    print("Metadata -------------")
    metadata = reader.metadata
    print(metadata)

    number_of_pages = len(reader.pages)
    print("\n\nNo of pages:", number_of_pages)

    print("----------------")
    title = metadata.get('/Title', 'N/A')
    volume = metadata.get('/PTEX.Fullbanner', 'N/A')
    publishers = metadata.get('/Creator', 'N/A')
    authors = metadata.get('/Author', 'N/A')
    date_of_publication = metadata.get('/CreationDate','N/A')
    keywords = metadata.get('/Keywords', 'N/A')

    # Extracting the relevant information from publishers authors
    if authors != 'N/A':
        authors.replace('and',',').replace('&',',')
        authors.replace(" ,", ",").replace(", ", ",")
        authors_list = list(authors.split(','))

        for i in range(len(authors_list)):
            author = authors_list[i]
            j = 0
            while j < len(author):
                if not author[j].isalpha() and not author[j].isspace():
                    break
                j += 1
            authors_list[i] = author[:j]

        authors = ','.join(authors_list)

    # Extracting the relevant information from publishers
    #remove unnecessary characters
    if publishers != 'N/A':
        i = 0
        while i in range(0, len(publishers)):
            if publishers[i].isalpha() or publishers[i].isspace():
                i += 1
            else:
                break

        publishers = publishers[:i]


    # Extracting the relevant information from keywords
    if keywords != 'N/A':
        keywords.replace(';',',')
        keywords_list = list(keywords.split(','))

        for keyword in keywords_list:
            keyword.strip()
            i = 0
            while i in range(0, len(keyword)):
                if keyword[i].isalnum() or keyword[i].isspace():
                    i += 1
                else:
                    keyword.replace(keyword[i], '')
                    i += 1
            keyword = keyword[:i]
        keywords = ','.join(str(e) for e in keywords_list)

    else:
        words = title.split().capitalize()

        # Finding the common words between the research topics list and the title
        common_words = [word for word in words if word in research_topics]
        keywords = ''
        for word in common_words:
            keywords += word
            keywords += ','

    # Change format of date
    try:
        if(date_of_publication[0] == 'D'):
            date_obj = datetime.strptime(date_of_publication[2:-7], '%Y%m%d%H%M%S')
            formatted_date = date_obj.strftime('%B %d, %Y')
        else:
            formatted_date = date_of_publication
    except:
        formatted_date = metadata.get('/CreationDate--Text', 'N/A')

    print("Title:", title)
    print("Volume:", volume[:2])
    print("Publisher:", publishers)
    print("author:", authors)
    print("keywords:", keywords)
    print("Date of Publication:", formatted_date)

# PDF metadata extraction
paper_name = "papers/mathematics-09-01276.pdf"
extract_metadata(paper_name)