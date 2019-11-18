import subprocess
import platform
from pathlib import Path

os = platform.system()

def convert_encoding(root_path, initial_encoding, final_encoding):
    if os == "Windows":
        iconv = str(Path(f"{root_path}/iconv/bin/iconv.exe"))
    
    elif os == "Darwin" or os == "Linux": 
        iconv = "iconv"

    encodings_string = f" -f {initial_encoding} -t {final_encoding} "
    input_file_path = str(Path(f"{root_path}/target-files/input.txt"))
    output_sym = " > "
    output_file_path = str(Path(f"{root_path}/target-files/{final_encoding}-converted.txt"))
    cmd = f"\"{iconv}\" {encodings_string} \"{input_file_path}\" {output_sym} \"{output_file_path}\""

    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError:
        raise