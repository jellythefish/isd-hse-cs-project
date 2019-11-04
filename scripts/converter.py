import chardet
import os
import sys
import subprocess
from scripts.detect_encoding import detect_encoding

root_directory = os.path.dirname(os.path.abspath(__file__))[:-7]

def encode_text(file_path, initial_encoding, final_encoding, txt_input_name):
    change_dir = f"cd \"{root_directory}iconv\\bin\\\" && iconv.exe"
    encodings_string = f" -c -f {initial_encoding} -t {final_encoding} \"{file_path}\""
    output_string = f" > \"{root_directory}target-files\{final_encoding}-converted.txt\""
    cmd = change_dir + encodings_string + output_string

    subprocess.Popen(cmd, shell=True)
