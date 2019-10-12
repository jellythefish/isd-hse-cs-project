import chardet
import os
import sys
import subprocess

root_directory = os.path.dirname(os.path.abspath(__file__))[:-7]

def detect_encoding(file_path):
    with open(file_path, 'rb') as fh:
        result = chardet.detect(fh.read())
    return result['encoding']


def encode_text(file_path, initial_encoding, final_encoding, txt_input_name):
    change_dir = f"cd \"{root_directory}iconv\\bin\\\" && iconv.exe"
    encodings_string = f" -c -f {initial_encoding} -t {final_encoding} \"{file_path}\""
    output_string = f" > \"{file_path[:-len(txt_input_name)]}{txt_input_name[:-4]}-{final_encoding}-converted.txt\""
    cmd = change_dir + encodings_string + output_string
    subprocess.Popen(cmd, shell=True)
    

if __name__ == "__main__":
    txt_input_name = "unknown.txt"
    file_path = root_directory + f'tests\{txt_input_name}'
    final_encoding = sys.argv[1] # требуемая кодировка (в которую конвертируем) передается извне
    initial_encoding = detect_encoding(file_path) # кодировка из которой конвертируем
    print(f"Initial Encoding: {initial_encoding}")
    encode_text(file_path, initial_encoding, final_encoding, txt_input_name)
