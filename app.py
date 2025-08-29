from flask import Flask, request, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/supabase-upload', methods=['POST'])
def supabase_upload():
    auth_header = request.headers.get('Authorization')
    if auth_header != 'Bearer mysecrettoken':
        return "Unauthorized", 401

    filename = request.form.get('filename')
    pages = request.form.get('pages')
    file_url = request.form.get('file_url')
    payment_id = request.form.get('payment_id')

    print("Received print job:")
    print("Filename:", filename)
    print("Pages:", pages)
    print("File URL:", file_url)
    print("Payment ID:", payment_id)

    return "Print job received successfully!"
