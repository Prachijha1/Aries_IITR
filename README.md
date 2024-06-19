
# PDF Answering AI

This is a Flask application that allows users to upload PDF files, extract text from them, and then ask questions about the text using a question-answering model from the `transformers` library.

## Features

- Upload PDF files
- Extract text from PDF files
- Ask questions about the extracted text
- Receive answers to questions using a pre-trained QA model

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/flask-qa-app.git
    cd flask-qa-app
    ```

2. Create a virtual environment:

    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```sh
    python app.py
    ```

2. Open a web browser and go to `http://127.0.0.1:5000`.

3. Upload a PDF file and ask questions about its content.

## Project Structure

- `app.py`: The main application file containing routes and logic for uploading files, extracting text, and answering questions.
- `templates/`: Directory containing HTML templates for rendering web pages.
  - `index.html`: The home page template for uploading PDF files.
  - `question.html`: The template for displaying extracted text and asking questions.
- `uploads/`: Directory where uploaded PDF files are stored. This directory is created automatically if it doesn't exist.

## Routes

- `/`: GET request to render the home page.
- `/upload`: POST request to handle PDF file uploads.
- `/ask`: POST request to handle question-answering.

## Example

To see the application in action, follow these steps:

1. Start the Flask server by running `python app.py`.
2. Upload a PDF file using the form on the home page.
3. After uploading, you'll be redirected to a page where you can see the extracted text and ask questions about it.

## Dependencies

- Flask: A micro web framework for Python.
- PyMuPDF (fitz): A library for extracting text from PDF files.
- transformers: A library for natural language processing models from Hugging Face.

## License

This project is licensed under the MIT License.
## Requirements
      1. Flask
      2. PyMuPDF
      3. transformers
      4. torch

## Dependencies

- Flask
- PyMuPDF
- transformers
