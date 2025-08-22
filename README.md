# Document Q&A Web Application

This is a Flask-based web application that allows users to **upload documents** ('.txt', '.pdf', '.docx') and ask questions about their content and get answers relating to that content using **Google Gemini AI**. It also supports **user authentication** and **document management**.

---
## Features

- **User Authentication**: Register, login, and logout securely.
- **Document Management**: Upload multiple document formats (`.txt`, `.pdf`, `.docx`).
- **Q&A Functionality**: Ask questions about your uploaded documents and get AI-generated answers.
- **History Tracking**: Stores past questions and answers per document.
- **Secure Storage**: Uses SQLite for database storage.
- **Multi-File Support**: Handles text, PDF, and Word documents.

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/document-qa-app.git
cd document-qa-app
```

2. **Set up a virtual environment**
    `python -m venv venv`

3. **Activate the virtual environment** 
    On Windows use: `venv\Scripts\activate`

4. **Install dependencies**
    `pip install -r requirements.txt`

5. **Run the Flask application**
    From the terminal, run:
    `python backend/app.py`

## Testing

- To quickly test your app:
    -Use small sample documents:
        -TXT: a few lines about cats and dogs.
        -PDF: a few lines about the solar system.
        -DOCX: a few lines about programming.

- Ask questions that are clearly present in the text to verify answers.

- Ask questions not in the document to verify general knowledge fallback.
