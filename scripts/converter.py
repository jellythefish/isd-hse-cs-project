import subprocess
import platform
from pathlib import Path

os = platform.system()


def get_iconv_name(root_path):
    if os == "Windows":
        return str(Path(f"{root_path}/iconv/bin/iconv.exe"))
    elif os == "Darwin" or os == "Linux":
        return "iconv"


def get_available_formats(root_path):
    if os == "Windows":
        return subprocess.check_output([get_iconv_name(root_path), "-l"], text=True).split()
    else:
        return subprocess.check_output([get_iconv_name(root_path), "--list"], text=True).split(
            "//\n")


def convert_encoding(root_path, initial_encoding, final_encoding):
    iconv = get_iconv_name(root_path)
    encodings_string = f" -f {initial_encoding} -t {final_encoding} "
    input_file_path = str(Path(f"{root_path}/target-files/input.txt"))
    output_sym = " > "
    output_file_path = str(Path(f"{root_path}/target-files/{final_encoding}-converted.txt"))
    cmd = iconv + encodings_string + input_file_path + output_sym + output_file_path

    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError:
        raise
