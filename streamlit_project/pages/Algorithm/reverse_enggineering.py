import json
import re
import string
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
import keywords

# Initialize the list to store extracted features
features = []

# Iterate over each annotated paper
for paper in annotated_data:
    labeled_data_url = paper['Labeled Data']
    title_annotation = None
    authors_annotation = None
    publisher_annotation = None
    volume_annotation = None
    keywords_annotation = None
    date_annotation = None
    
    # Find the annotations for the metadata fields
    for obj in paper['Label']['objects']:
        if obj['title'] == 'title':
            title_annotation = obj
        elif obj['title'] == 'authors':
            authors_annotation = obj
        elif obj['title'] == 'publisher':
            publisher_annotation = obj
        elif obj['title'] == 'volume':
            volume_annotation = obj
        elif obj['title'] == 'keywords':
            keywords_annotation = obj
        elif obj['title'] == 'date_of_publication':
            date_annotation = obj
    
    if title_annotation:
        # Extract features for title
        title_value = title_annotation['value']
        title_bbox = title_annotation['bbox']
        title_page = title_annotation['page']
        
        # Perform feature extraction specific to title
        # Example: Extracting words and part-of-speech tags from the title
        title_words = word_tokenize(title_value)
        title_pos = nltk.pos_tag(title_words)
        
    if authors_annotation:
        # Extract features for authors
        authors_value = authors_annotation['value']
        authors_bbox = authors_annotation['bbox']
        authors_page = authors_annotation['page']
        
        # Perform feature extraction specific to authors
        # Example: Extracting words and part-of-speech tags from the authors
        authors_words = word_tokenize(authors_value)
        authors_pos = nltk.pos_tag(authors_words)
        
    if publisher_annotation:
        # Extract features for publisher
        publisher_value = publisher_annotation['value']
        publisher_bbox = publisher_annotation['bbox']
        publisher_page = publisher_annotation['page']
        
        # Perform feature extraction specific to publisher
        # Example: Extracting words and part-of-speech tags from the publisher
        publisher_words = word_tokenize(publisher_value)
        publisher_pos = nltk.pos_tag(publisher_words)
        
    if volume_annotation:
        # Extract features for volume
        volume_value = volume_annotation['value']
        volume_bbox = volume_annotation['bbox']
        volume_page = volume_annotation['page']
        
        # Perform feature extraction specific to volume
        # Example: Extracting words and part-of-speech tags from the volume
        volume_words = word_tokenize(volume_value)
        volume_pos = nltk.pos_tag(volume_words)
        
    if keywords_annotation:
        # Extract features for keywords
        keywords_value = keywords_annotation['value']
        keywords_bbox = keywords_annotation['bbox']
        keywords_page = keywords_annotation['page']
        
        # Perform feature extraction specific to keywords
        # Example: Extracting words and part-of-speech tags from the keywords
        keywords_words = word_tokenize(keywords_value)
        keywords_pos = nltk.pos_tag(keywords_words)
        
    if date_annotation:
        # Extract features for date_of_publication
        date_value = date_annotation['value']
        date_bbox = date_annotation['bbox']
        date_page = date_annotation['page']
        
        # Perform feature extraction specific to date_of_publication
        # Example: Extracting words and part-of-speech tags from the date_of_publication
        date_words = word_tokenize(date_value)
        date_pos = nltk.pos_tag(date_words)
        
    # Create a dictionary of features for the paper
    paper_features = {
        'Title': {
            'Value': title_value,
            'Words': title_words,
            'POS': title_pos
        },
        'Authors': {
            'Value': authors_value,
            'Words': authors_words,
            'POS': authors_pos
        },
        'Publisher': {
            'Value': publisher_value,
            'Words': publisher_words,
            'POS': publisher_pos
        },
        'Volume': {
            'Value': volume_value,
            'Words': volume_words,
            'POS': volume_pos
        },
        'Keywords': {
            'Value': keywords_value,
            'Words': keywords_words,
            'POS': keywords_pos
        },
        'Date of Publication': {
            'Value': date_value,
            'Words': date_words,
            'POS': date_pos
        },
        'Labeled Data': labeled_data_url,
        'Title Bbox': title_bbox,
        'Title Page': title_page,
        'Authors Bbox': authors_bbox,
        'Authors Page': authors_page,
        'Publisher Bbox': publisher_bbox,
        'Publisher Page': publisher_page,
        'Volume Bbox': volume_bbox,
        'Volume Page': volume_page,
        'Keywords Bbox': keywords_bbox,
        'Keywords Page': keywords_page,
        'Date Bbox': date_bbox,
        'Date Page': date_page
    }
    
    # Append the features to the list
    features.append(paper_features)
