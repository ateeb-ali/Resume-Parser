# Basic Resume Parser

## 1. Introduction
The goal of this project is to develop a basic Resume Parser that can automatically extract key information from resumes in PDF format. The extracted data includes the candidate’s email address, phone number, university name, and relevant skills based on a predefined list.

## 2. Problem Statement
Recruiters often receive hundreds of resumes for a single job posting, making manual screening time-consuming and inefficient. There is a need for a simple tool that can automatically extract and summarize relevant information from resumes to streamline the initial screening process.

## 3. Objectives
- Extract text from a resume in PDF format. (should be named `resume.pdf`)
- Identify and extract the candidate’s:
  - Email address
  - Phone number
  - University or educational institution
  - Skills (matched from a `skills.txt` file)
- Display the extracted information in a clean format.

## 4. Tools & Technologies
- **Python**: Programming language used for development.
- **PyMuPDF (fitz)**: Library used to extract text from PDF files.
- **spaCy**: NLP library used for future enhancements (currently initialized).
- **Regular Expressions**: Used for pattern matching of emails and phone numbers.
- **Text File (`skills.txt`)**: Contains a list of skills to match against the resume content.

## 5. How It Works
- The PDF resume is read and converted into plain text using PyMuPDF.
- Regular expressions are applied to extract emails and phone numbers.
- A simple keyword-matching technique is used to identify the university name.
- The skills are matched against a list from `skills.txt` to identify relevant technical competencies.

## 6. Future Enhancements
- Use NLP techniques (via spaCy) to improve the accuracy of entity extraction.
- Add support for multiple resumes (batch processing).
- Export extracted data to CSV or JSON format for integration into HR systems.
- Develop a basic GUI or web interface for user interaction.

## 7. Conclusion
This Resume Parser provides a foundation for automating the resume screening process. While it’s a basic implementation, it demonstrates how Python and simple NLP techniques can be used to extract valuable data from documents and can be improved further with advanced features.
