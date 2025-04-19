# Legal Document Analysis Assistant

An AI-powered assistant that analyzes legal documents and company policies, providing intelligent insights, compliance checking, and automated summarization.

## Features

- **Document Analysis**: Process and understand legal documents and company policies using advanced NLP
- **Compliance Checking**: Automated detection of compliance issues with relevant regulations
- **Risk Assessment**: Identification of potential risks and vulnerabilities in legal documents
- **Smart Summarization**: AI-powered extraction of key points and important clauses
- **Search & Retrieval**: Efficient document storage and retrieval using ElasticSearch

## Tech Stack

- Python 3.9+
- BERT/GPT for NLP processing
- LangChain for AI orchestration
- ElasticSearch for document storage and search
- MongoDB for metadata and user data storage

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys and configuration
```

4. Start the services:
```bash
python run.py
```

## Project Structure

```
legal-assistant/
├── app/
│   ├── core/
│   │   ├── document_processor.py
│   │   ├── compliance_checker.py
│   │   └── summarizer.py
│   ├── models/
│   │   └── document.py
│   ├── utils/
│   │   ├── text_extraction.py
│   │   └── nlp_utils.py
│   └── config.py
├── tests/
├── data/
├── requirements.txt
└── README.md
```

## Configuration

The system requires the following API keys and configurations:
- OpenAI API key (for GPT integration)
- ElasticSearch credentials
- MongoDB connection string

## Usage

```python
from app.core.document_processor import DocumentProcessor

# Initialize the processor
processor = DocumentProcessor()

# Process a document
results = processor.analyze_document("path/to/document.pdf")
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

MIT License 