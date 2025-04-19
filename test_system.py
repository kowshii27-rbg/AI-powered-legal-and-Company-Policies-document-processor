from app.core.document_processor import DocumentProcessor
from app.core.compliance_checker import ComplianceChecker
from app.core.summarizer import DocumentSummarizer

def test_document_analysis():
    # Initialize components
    processor = DocumentProcessor()
    compliance_checker = ComplianceChecker()
    summarizer = DocumentSummarizer()
    
    # Test document path
    document_path = "example_documents/privacy_policy.txt"
    
    try:
        # 1. Process and analyze document
        print("\n=== Document Analysis ===")
        text = processor.extract_text(document_path)
        analysis_result = processor.analyze_content(text)
        print("\nDocument Summary:")
        print(analysis_result['summary'])
        
        # 2. Check GDPR compliance
        print("\n=== GDPR Compliance Check ===")
        compliance_result = compliance_checker.check_compliance(text, regulation_type="gdpr")
        print(f"\nCompliance Status: {compliance_result['compliance_status']}")
        print(f"Risk Level: {compliance_result['risk_level']}")
        
        if compliance_result["missing_clauses"]:
            print("\nMissing Clauses:")
            for clause in compliance_result["missing_clauses"]:
                print(f"- {clause}")
        
        if compliance_result["prohibited_terms_found"]:
            print("\nProhibited Terms Found:")
            for term in compliance_result["prohibited_terms_found"]:
                print(f"- {term['term']}")
                print(f"  Analysis: {term['context_analysis']}")
        
        # 3. Generate detailed summary
        print("\n=== Detailed Summary ===")
        summary_report = summarizer.generate_summary_report(text)
        print(summary_report)
        
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Cleanup resources
        processor.cleanup()

if __name__ == "__main__":
    test_document_analysis() 