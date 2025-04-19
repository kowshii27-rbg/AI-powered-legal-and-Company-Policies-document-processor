from app.core.document_processor import DocumentProcessor
from app.core.compliance_checker import ComplianceChecker
from app.core.summarizer import DocumentSummarizer
import os

def test_document_processing():
    # Create output directory if it doesn't exist
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Sample text for testing
    test_text = """
    Privacy Policy

    1. Data Collection
    We collect personal information including name, email, and usage data.
    This data is used to improve our services and user experience.

    2. Data Protection
    All data is encrypted and stored securely on our servers.
    We implement industry-standard security measures to protect your information.

    3. User Rights
    Users have the right to:
    - Access their personal data
    - Request data deletion
    - Opt out of data collection
    - Receive data in portable format

    4. Data Retention
    We retain user data for as long as necessary to provide our services.
    Users can request deletion of their data at any time.

    5. Third-party Sharing
    We do not share personal information with third parties without explicit consent.
    Some anonymous data may be shared for analytics purposes.
    """

    try:
        # Initialize processors
        doc_processor = DocumentProcessor()
        compliance_checker = ComplianceChecker()
        summarizer = DocumentSummarizer()

        print("\n=== Document Analysis ===")
        analysis = doc_processor.analyze_content(test_text)
        print("\nDocument Analysis:")
        print(analysis['summary'])
        # Save analysis results
        doc_processor.save_to_file(analysis, os.path.join(output_dir, "document_analysis.txt"))

        print("\n=== Compliance Check ===")
        compliance = compliance_checker.check_compliance(test_text, "gdpr")
        print("\nCompliance Status:", compliance['compliance_status'])
        print("Risk Level:", compliance['risk_level'])
        if compliance['missing_clauses']:
            print("\nMissing Clauses:")
            for clause in compliance['missing_clauses']:
                print(f"- {clause}")
        if compliance['recommendations']:
            print("\nRecommendations:")
            for rec in compliance['recommendations']:
                print(f"- {rec}")
        # Save compliance results
        compliance_checker.save_to_file(compliance, os.path.join(output_dir, "compliance_check.txt"))

        print("\n=== Document Summary ===")
        summary = summarizer.summarize(test_text)
        print("\nExecutive Summary:")
        print(summary['executive_summary'])
        print("\nKey Points:")
        for point in summary['key_points']:
            print(f"- {point}")
        # Save summary results
        summarizer.save_to_file(summary, os.path.join(output_dir, "document_summary.txt"))

        print("\nAll reports have been saved to the 'output' directory.")

    except Exception as e:
        print(f"Error during testing: {str(e)}")
    finally:
        # Cleanup
        doc_processor.cleanup()
        compliance_checker.cleanup()
        summarizer.cleanup()

if __name__ == "__main__":
    test_document_processing() 