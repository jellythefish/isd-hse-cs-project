from flask import Flask, request, send_file, Response
from pathlib import Path
from scripts.detect_encoding import detect_encoding
from scripts.converter import convert_encoding
import subprocess

root_path = Path.cwd() # cwd is for current working directory
# All paths in this project are os adabtable (Windows/Unix path styles)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/convert/<output_type>', methods=['GET', 'POST'])
def upload_file(output_type=None):
    if request.method == 'POST':
        f = request.files['file']
        input_file_path = str(Path("target-files/input.txt"))
        f.save(input_file_path)

    initial_file_encoding = detect_encoding(input_file_path) 

    try:
        convert_encoding(root_path, initial_file_encoding, output_type)
    except Exception as e:
        return Response("HTTP_400_BAD_REQUEST: " + str(e.output), 400)

    output_file_path = str(Path(f"target-files/{output_type}-converted.txt"))
    return send_file(output_file_path)

if __name__ == "__main__":
    app.run()