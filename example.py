from app.core.document_processor import DocumentProcessor
from app.core.compliance_checker import ComplianceChecker
from app.core.summarizer import DocumentSummarizer
import os
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize components
    processor = DocumentProcessor()
    compliance_checker = ComplianceChecker()
    summarizer = DocumentSummarizer()
    
    # Example document path
    document_path = "example_documents/privacy_policy.pdf"
    
    try:
        # Process document
        print("Processing document...")
        processing_result = processor.process_document(document_path)
        
        # Check compliance
        print("\nChecking GDPR compliance...")
        text = processor.extract_text(document_path)
        compliance_result = compliance_checker.check_compliance(text, regulation_type="gdpr")
        
        if compliance_result["compliance_status"] == "non_compliant":
            print("\nCompliance issues found:")
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
            
            # Get suggestions for corrections
            suggestions = compliance_checker.suggest_corrections(compliance_result)
            print("\nSuggested Corrections:")
            print(suggestions)
        else:
            print("Document is compliant with GDPR regulations.")
        
        # Generate summary
        print("\nGenerating document summary...")
        summary_report = summarizer.generate_summary_report(text)
        print("\nSummary Report:")
        print(summary_report)
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 