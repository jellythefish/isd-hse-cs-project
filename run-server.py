import os
from flask import Flask, request, send_file
from scripts.detect_encoding import detect_encoding
from scripts.converter import encode_text

app = Flask(__name__)
root_directory = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/convert/<output_type>', methods=['GET', 'POST'])
def upload_file(output_type=None):
    if request.method == 'POST':
        f = request.files['file']
        f.save('./target-files/input.txt')

    convert(output_type)
    return send_file(root_directory + f"\\target-files\\{output_type}-converted.txt")


def convert(target_encoding):
    file_name = "input.txt"
    file_path = root_directory + f'\\target-files\{file_name}'
    initial_encoding = detect_encoding(file_path)
    encode_text(file_path, initial_encoding, target_encoding, file_name)

if __name__ == "__main__":
    app.run()