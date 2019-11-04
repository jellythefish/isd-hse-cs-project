import chardet
import os
import sys
import subprocess

root_directory = os.path.dirname(os.path.abspath(__file__))[:-7]

def detect_encoding(file_path):
    with open(file_path, 'rb') as fh:
        result = chardet.detect(fh.read())
        print("Initial Encoding: " + result["encoding"])
    return result['encoding']