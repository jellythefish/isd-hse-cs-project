import chardet
import os

def detect_encoding(file_path):
    with open(file_path, 'rb') as fh:
        result = chardet.detect(fh.read())
        print("Initial Encoding: " + result["encoding"])
    return result['encoding']