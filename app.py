import streamlit as st
import os
from dotenv import load_dotenv
import pdfplumber
import pytesseract
from PIL import Image
import docx
import PyPDF2
import numpy as np
import pandas as pd
from transformers import pipeline
import torch
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title=" AI powered legal and Company Policies document processor",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    .stFileUploader>div>div>div {
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Document Processing")
st.sidebar.markdown("---")
st.sidebar.markdown("### Upload Document")
uploaded_file = st.sidebar.file_uploader(
    "Choose a file",
    type=['pdf', 'docx', 'txt', 'png', 'jpg', 'jpeg'],
    help="Upload a document for processing"
)

# Main content
st.title("📄 AI powered legal and Company Policies document processor")
st.markdown("---")

# Initialize session state
if 'processed_text' not in st.session_state:
    st.session_state.processed_text = None
if 'summary' not in st.session_state:
    st.session_state.summary = None

# File processing function
def process_file(file):
    file_extension = file.name.split('.')[-1].lower()
    
    if file_extension == 'pdf':
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
    elif file_extension in ['docx']:
        doc = docx.Document(file)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    elif file_extension in ['png', 'jpg', 'jpeg']:
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
    else:  # txt
        text = file.getvalue().decode()
    
    return text

# Keyword extraction function using NLTK
def extract_keywords(text, num_keywords=10):
    # Tokenize the text
    tokens = word_tokenize(text.lower())
    
    # Remove stopwords and non-alphabetic tokens
    stop_words = set(stopwords.words('english'))
    words = [word for word in tokens if word.isalpha() and word not in stop_words]
    
    # Get frequency distribution
    fdist = FreqDist(words)
    
    # Return most common words
    return [word for word, _ in fdist.most_common(num_keywords)]

# Main processing logic
if uploaded_file is not None:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Document")
        if uploaded_file.name.endswith(('.png', '.jpg', '.jpeg')):
            st.image(uploaded_file)
        else:
            st.text_area("Document Content", process_file(uploaded_file), height=300)
    
    with col2:
        st.subheader("Processed Results")
        if st.button("Process Document"):
            with st.spinner("Processing document..."):
                # Process the document
                processed_text = process_file(uploaded_file)
                st.session_state.processed_text = processed_text
                
                # Initialize summarization pipeline
                summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
                
                # Generate summary
                summary = summarizer(processed_text, max_length=130, min_length=30, do_sample=False)
                st.session_state.summary = summary[0]['summary_text']
                
                st.success("Document processed successfully!")
                
                # Display results
                st.markdown("### Summary")
                st.write(st.session_state.summary)
                
                # Additional processing options
                st.markdown("### Additional Options")
                if st.button("Extract Keywords"):
                    keywords = extract_keywords(processed_text)
                    st.write("Keywords:", ", ".join(keywords))
else:
    st.info("👈 Please upload a document using the sidebar to get started!")
    st.markdown("""
    ### Supported File Types:
    - PDF Documents
    - Word Documents (.docx)
    - Text Files (.txt)
    - Images (.png, .jpg, .jpeg)
    """)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit") 