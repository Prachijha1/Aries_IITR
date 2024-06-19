from flask import Flask, request, render_template, jsonify
import fitz  # PyMuPDF
from transformers import pipeline
import os

app = Flask(__name__)
qa_model = pipeline("question-answering")

# Define the upload folder
UPLOAD_FOLDER = 'uploads'
# Create the uploads directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def answer_question(question, context):
    result = qa_model(question=question, context=context)
    return result['answer']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        # Save the file to the uploads directory
        pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(pdf_path)
        context = extract_text_from_pdf(pdf_path)
        # Pass context to the question.html template
        return render_template('question.html', context=context)
    return "File upload failed"

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')
    context = data.get('context')
    if not question or not context:
        return jsonify({'error': 'Question and context are required'}), 400
    try:
        answer = answer_question(question, context)
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
