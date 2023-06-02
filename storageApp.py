# import standard 'os' & 'pathlib' module to perform file operations 
# import third-party 'argparse' module to handle parsing/passing of arguments through CLI
import os
from pathlib import Path

import argparse

# the messages below will be used relatively to prompt that there is an error with files
INVALID_FILETYPE_MSG = "Error: Invalid file format. %s must be .txt file."
# INVALID_FILETYPE_MSG = "Error: The file is either invalid or we do not support this file. Please check your file again."

INVALID_PATH_MSG = "Error: Invalid file path/name. Path %s does not exist."

def validate_file(filename):
    """
    Validates file's type (format) and it's path
    Returns error messages
    """

    if not validate_filetype(filename):
        print(INVALID_FILETYPE_MSG%(filename))
        quit()
    elif not validate_filepath(filename):
        print(INVALID_PATH_MSG%(filename))
        quit()
    return

def validate_filetype(filename):
    """Validates file type/format and returns in 'bool'"""
    return filename.endswith('.txt')

def validate_filepath(filename):
    """Validates file path in the system and returns in 'bool'"""
    return os.path.exists(filename)

def upload(args):
    pass

def delete(args):
    pass

def download(args):
    pass

def list_files(args):
    pass

def details(args):
    pass

def show_path(args):
    """
    Returns path of the file entered.
    Returns False if path of the file does not exist.
    """

    # get the filename
    file = args.path[0]
    # print(file)


    filepath = Path(__file__)
    return print(filepath)

def main():
    """
    
    """
    parser = argparse.ArgumentParser(description="A personal cloud storage cli application")

    parser.add_argument("-u", "--upload", type=str, nargs='*',
                        metavar="upload", help="Upload files to the cloud")
    
    parser.add_argument("-del", "--delete", type=str, nargs='*',
                        metavar="delete", help="Delete files from the cloud")

    parser.add_argument("-dwl", "--download", type=str, nargs='*',
                        metavar="download", help="Download files from the cloud")
    
    parser.add_argument("-ls", "--list", type=str, nargs=1,
                        metavar="list", help="List files from the cloud")
    
    parser.add_argument("-det", "--details", type=str, nargs='*',
                        metavar="delete", help="Delete files from the cloud")
    
    # parser.add_argument("")