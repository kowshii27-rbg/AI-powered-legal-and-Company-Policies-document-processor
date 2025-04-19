from app.core.document_processor import DocumentProcessor

def test_document_analysis():
    # Create a sample text document
    with open("sample.txt", "w") as f:
        f.write("""
PRIVACY POLICY

Last Updated: January 1, 2024

1. Introduction
This Privacy Policy describes how we collect, use, and handle your personal information.

2. Data Collection
We collect the following types of information:
- Personal information (name, email)
- Usage data
- Device information

3. Data Usage
Your data is used for:
- Providing services
- Improving user experience
- Analytics

4. Data Protection
We implement security measures to protect your data.

5. Data Retention
We retain data for 12 months after last use.

6. Your Rights
You have the right to:
- Access your data
- Request deletion
- Opt out of marketing

7. Contact
For privacy concerns, contact: privacy@example.com
""")

    # Initialize document processor
    processor = DocumentProcessor()
    
    # Process the document
    try:
        result = processor.process_document("sample.txt")
        print("\nDocument Analysis Result:")
        print("------------------------")
        print(result['summary'])
        print("\nStatus:", result['status'])
        print("Timestamp:", result['timestamp'])
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_document_analysis() 