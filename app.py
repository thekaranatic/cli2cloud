# import standard 'os' & 'pathlib' module to perform file operations 
# import third-party 'argparse' module to handle parsing/passing of arguments through CLI
# import 'fileformats.py' file to use the list 'list_file-formats' to validate filetypes 

import os
from pathlib import Path
import random as rnd
import secrets
import string

import argparse

from fileformats import tuple_fileformats as ext

# import appwrite libraries to use their storage bucket services
from appwrite.client import Client
from appwrite.services.storage import Storage
import appwrite.input_file


# the messages below will be used relatively to prompt that there is an error with files
INVALID_FILETYPE_MSG = "ERROR: %s is either invalid or we do not support this file. Please re-check the file."
INVALID_PATH_MSG = "ERROR: Looks like file path/name is invalid. Path '%s' does not exist."

files = ['ada.txt','karan.txt','file.txt']

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
    return filename.endswith(ext)

def validate_filepath(filename):
    """Validates file path in the system and returns in 'bool'"""
    return os.path.exists(filename)

def login():
    username = input("What's your username? ")
    password = input("What's your password? ")

    print("Hi, %s. You are in!"% username)

def logout():
    print("You are logged out.")   

def upload(args):
    """
    Uploads the specified file to the cloud.
    Supports only one file currently.
    Returns msg if file or filetype is invalid or not in existence.
    """
    
    # get the filename
    filename = args.upload[0]

    # validate file name/path
    validate_file(filename)

    PATH = Path(__file__)
    print(PATH)
    # help(storage.create_file())

    client = Client()
    storage = Storage(client)

    (client
        .set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
        .set_project('5df5acd0d48c2') # Your project ID
        .set_key('919c2d18fb5d4...a2ae413da83346ad2') # Your secret API key
    )

    storage = Storage(client)

    result = storage.create_bucket('[BUCKET_ID]', '[NAME]', )

    # client.set_endpoint('https://cloud.appwrite.io/v1')
    # client.set_project('647c49a7e79df168b264')
    # client.set_key('7e62fbf81b373436fc3b6a7b798ba14a8fc6b2e7dcf1ea7b865b96ef10cc2ef2d540e883bff4515fb68f09b7fab128fd2278c63b0f99a42a60ea48330819302f85bf96494a7033f2915b8198993384cf25270460c8aa27d70dbf84874cc30b5408bd7e07c52c7e9d6ecfc499cfd7de6ed6016abbe0b5386bd19aef5716409f93')

    # FILE_ID = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(0,20))    
    # result = storage.create_file('647f207c336d08d20e1f',FILE_ID,filename)
    # print(result)
    
    # check if file already exists, if False, upload the specified file and notify user
    # if filename in files:
    #     # if True, ask user to whether replace the file else take no action
    #     response = input("%s already exists. Would you like to update the file [y/n]?"%filename)
    #     if 'y' in response:
    #         files.remove(filename)
    #         files.append(filename)
    #         print("%s updated successfully 💯." %filename)
    #         return
    #     else:
    #         print("Rest free 🙌🏼. No action taken.")
    #         return
    # else:
    #     files.append(filename)
    #     print("Yep there it goes 🚀. %s uploaded successfully." %filename)
    #     return

def delete(args):
    """
    Deletes the specified file from the cloud. 
    Supports only one file currently
    Returns False if file or filetype is invalid or not in existence.
    """

    # get the filename
    filename = args.delete[0]

    # validate file name/path
    validate_file(filename)

    # check if file already exists, 
    if filename in files:
        # if True, delete the file and notify user
        files.remove(filename)
        print("Trashed! %s deleted successfully." %filename)
        return
    # if False, notify user that file doesnt exist or ask to recheck filename & enter again
    else:
        print("%s doesn't exist in your cloud. Try re-checking the filename and enter again."%filename)
        return

def download(args):
    """
    Downloads the specified file from the cloud.
    Returns False if file or filetype is invalid or not in existence.
    """

    # get the filename
    filename = args.download[0]

    # validate file name/path
    validate_file(filename)

    if filename in files:
        # if True, download the file and notify user
        print("Right there! %s downloaded successfully in path 'x://y/z'" %filename)
        return
    # if False, notify user that file doesnt exist or ask to recheck filename & enter again
    else:
        print("%s doesn't exist in your cloud. Try re-checking the filename and enter again."%filename)
        return

def list_files():
    """
    Lists all the file present in the cloud.
    Returns False if file or filetype is invalid or not in existence.
    """

    for f in files:
        print(f)
    return

def details(args):
    """
    Lists out details/metadata of files in the cloud.
    Returns False if file or filetype is invalid or not in existence.
    """

    # get the filename
    filename = args.details[0]

    # validate file name/path
    validate_file(filename)

    # dummy code to represent: details/metadata of a file
    # prints the file name
    # prints the length of file name as size of the file ;)
    print("\n")
    print("FILE\t\tSIZE")
    print("-------------\t-------")
    print(filename + " \t" + str(len(filename)))

def new_bucket():
    client = Client()
    storage = Storage(client)

    (client
        .set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
        .set_project('647c49a7e79df168b264') # Your project ID
        .set_key('7e62fbf81b373436fc3b6a7b798ba14a8fc6b2e7dcf1ea7b865b96ef10cc2ef2d540e883bff4515fb68f09b7fab128fd2278c63b0f99a42a60ea48330819302f85bf96494a7033f2915b8198993384cf25270460c8aa27d70dbf84874cc30b5408bd7e07c52c7e9d6ecfc499cfd7de6ed6016abbe0b5386bd19aef5716409f93') # Your secret API key
    )

    storage = Storage(client)

    BUCKET_ID = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(0,20))
    
    result = storage.create_bucket(BUCKET_ID, 'bucket-1')
    response = result
    print(response)


def main():

    parser = argparse.ArgumentParser(description="A personal cloud storage cli application")

    parser.add_argument("-lin", "--login", type=str, nargs='*',
                        metavar="login", help="Login to your personal cloud")
    
    parser.add_argument("-lout", "--logout", type=str, nargs='*',
                        metavar="logout", help="Logout from your personal cloud")

    parser.add_argument("-up", "--upload", type=str, nargs='*',
                        metavar="upload", help="Upload files to the cloud")
    
    parser.add_argument("-del", "--delete", type=str, nargs='*',
                        metavar="delete", help="Delete files from the cloud")

    parser.add_argument("-dwl", "--download", type=str, nargs='*',
                        metavar="download", help="Download files from the cloud")
    
    parser.add_argument("-ls", "--list", type=str, nargs='*',
                        metavar="list", help="List files from the cloud")
    
    parser.add_argument("-dtl", "--details", type=str, nargs='*',
                        metavar="delete", help="Delete files from the cloud")

    parser.add_argument("-nbuck", "--newbucket", type=str, nargs='*',
                        metavar="newbucket", help="Create new bucket on the cloud")


    # parse args from STDIN
    args = parser.parse_args()

    # call the functions depending on the type of arg
    if args.login != None:
        login()
    elif args.logout != None:
        logout()
    elif args.upload != None:
        upload(args)
    elif args.delete != None:
        delete(args)
    elif args.download != None:
        download(args)
    elif args.list != None:
        list_files()
    elif args.details != None:
        details(args)
    elif args.newbucket != None:
        new_bucket()

if __name__ == "__main__":
    # calling the main fucntion
    main()
