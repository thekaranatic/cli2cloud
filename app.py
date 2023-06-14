# import standard 'os' & 'pathlib' module to perform file operations 
import os

# for operations regarding creating dirs, generating rand str
from pathlib import Path
import random as rnd
import secrets
import string

# To convert a timestamp to the user's local time zone and display it in a user-friendly format
import datetime
from tzlocal import get_localzone

# import third-party 'argparse' module to handle parsing/passing of arguments through CLI
import argparse

# to beautify the terminal
from rich.console import Console
from rich.table import Table
from time import sleep

# import 'fileformats.py' file to use the list 'list_file-formats' to validate filetypes 
from fileformats import tuple_fileformats as ext

# import appwrite libraries to use their storage bucket services
from appwrite.client import Client
from appwrite.services.storage import Storage
from appwrite.input_file import InputFile
from appwrite.services.account import Account


# the messages below will be used relatively to prompt that there is an error with files
INVALID_FILETYPE_MSG = "🙀 ERROR: %s is either invalid or we do not support this file. Please re-check the file."
INVALID_PATH_MSG = "🙀 ERROR: Looks like file path/name is invalid. '%s' does not exist."

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

def get_bucket_id():
    """ Reads bucket_id (str) from a file and returns the same (str)"""
    data = open("./data/buckets.txt","r")
    bucket_id = data.read()
    return bucket_id

def get_file_id(filename):
    """ Reads file_id (str) from response after a request and returns the same (str)"""

    client = Client()

    (client
        .set_endpoint('https://cloud.appwrite.io/v1') # API Endpoint
        .set_project('647c49a7e79df168b264') # project ID
        .set_key('7e62fbf81b373436fc3b6a7b798ba14a8fc6b2e7dcf1ea7b865b96ef10cc2ef2d540e883bff4515fb68f09b7fab128fd2278c63b0f99a42a60ea48330819302f85bf96494a7033f2915b8198993384cf25270460c8aa27d70dbf84874cc30b5408bd7e07c52c7e9d6ecfc499cfd7de6ed6016abbe0b5386bd19aef5716409f93') # secret API key
    )

    storage = Storage(client)

    BUCKET_ID = get_bucket_id() # get bucket id from the file './data/buckets.txt'

    result = storage.list_files(BUCKET_ID)  # get files from the created bucket

    FILE_ID = None # set flag to None

    for file_info in result["files"]:
        if file_info["name"] == filename:
            FILE_ID = file_info["$id"]  # store file_id of the specified file that exists in the cloud 
            break

    if FILE_ID is not None:
        return FILE_ID
    else:
        return False

def upload(args):
    """
    Uploads the specified file to the cloud.
    Supports only one file currently.
    Returns msg if file or filetype is invalid or not in existence.
    """
    
    # get the filename
    filename = args.upload[0]
    FILEPATH = InputFile.from_path(filename) # get path of file (using appwrite's functions)

    # validate file name/path
    validate_file(filename)

    client = Client()

    (client
        .set_endpoint('https://cloud.appwrite.io/v1') # API Endpoint
        .set_project('647c49a7e79df168b264') # project ID
        .set_key('7e62fbf81b373436fc3b6a7b798ba14a8fc6b2e7dcf1ea7b865b96ef10cc2ef2d540e883bff4515fb68f09b7fab128fd2278c63b0f99a42a60ea48330819302f85bf96494a7033f2915b8198993384cf25270460c8aa27d70dbf84874cc30b5408bd7e07c52c7e9d6ecfc499cfd7de6ed6016abbe0b5386bd19aef5716409f93') # secret API key
    )

    storage = Storage(client)

    BUCKET_ID = get_bucket_id()
    FILE_ID = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(0,20))    
    response = storage.create_file(BUCKET_ID,FILE_ID,FILEPATH)
    
    if response != None:
        console = Console()
        with console.status("[blue]Preparing to fly high..", spinner="dots2") as status:
            sleep(1.5)
            console.print(f"There it goes 🚀. '{filename}' uploaded successfully.\n", style="green")
    return

def delete(args):
    """
    Deletes the specified file from the cloud. 
    Supports only one file currently
    Returns False if file or filetype is invalid or not in existence.
    """

    # get the filename
    filename = args.delete[0]

    client = Client()

    (client
        .set_endpoint('https://cloud.appwrite.io/v1') # API Endpoint
        .set_project('647c49a7e79df168b264') # project ID
        .set_key('7e62fbf81b373436fc3b6a7b798ba14a8fc6b2e7dcf1ea7b865b96ef10cc2ef2d540e883bff4515fb68f09b7fab128fd2278c63b0f99a42a60ea48330819302f85bf96494a7033f2915b8198993384cf25270460c8aa27d70dbf84874cc30b5408bd7e07c52c7e9d6ecfc499cfd7de6ed6016abbe0b5386bd19aef5716409f93') # secret API key
    )

    storage = Storage(client)

    BUCKET_ID = get_bucket_id()
    FILE_ID = get_file_id(filename)

    console = Console()

    if FILE_ID:
        response = storage.delete_file(BUCKET_ID, FILE_ID)  # delete specified file from the bucket
        if response != None:
            with console.status(f"[green]Deleting {filename} from the cloud.", spinner="dots2") as status:
                sleep(1.5)
                console.print("In the Trash! File '%s' is no longer in your cloud."%filename, style="red")
    else:
        console.print("%s doesn't exist in your cloud. Try re-checking the filename and enter again."%filename, style="blue")

def download(args):
    """
    Downloads the specified file from the cloud.
    Returns False if file or filetype is invalid or not in existence.
    """

    # get the filename
    filename = args.download[0]

    # validate file name/path
    validate_file(filename)

    client = Client()

    (client
        .set_endpoint('https://cloud.appwrite.io/v1') # API Endpoint
        .set_project('647c49a7e79df168b264') # project ID
        .set_key('7e62fbf81b373436fc3b6a7b798ba14a8fc6b2e7dcf1ea7b865b96ef10cc2ef2d540e883bff4515fb68f09b7fab128fd2278c63b0f99a42a60ea48330819302f85bf96494a7033f2915b8198993384cf25270460c8aa27d70dbf84874cc30b5408bd7e07c52c7e9d6ecfc499cfd7de6ed6016abbe0b5386bd19aef5716409f93') # secret API key
    )

    storage = Storage(client)

    BUCKET_ID = get_bucket_id()
    FILE_ID = get_file_id(filename)

    console = Console()

    if FILE_ID:
        response = storage.get_file_download(BUCKET_ID, FILE_ID)  # download specified file from the bucket
        if response is not None:
            # create destination directory
            path = os.getcwd()
            PATH = os.path.join(path,"downloads")
            os.makedirs(PATH, exist_ok=True)

            # extract the file name from response headers
            file_name = FILE_ID.split('/')[-1]

            # save the file to dest dir
            file_path = os.path.join(PATH, filename)
            with open(file_path, 'wb') as file:
                file.write(response)


            with console.status("[blue]Coming down..", spinner="earth") as status:
                sleep(1)
                console.print(f"Right there 🛬 '{filename}' is downloaded and saved to: {file_path}", style="green")
        else:
            console.print(f"🙀 Error occurred")
    else:
        console.print(f"Oops! '{filename}' doesn't exist in your cloud. Try re-checking the filename and enter again.")
        return

def list_files():
    """
    Lists all the file present in the cloud.
    """

    client = Client()
    (client
        .set_endpoint('https://cloud.appwrite.io/v1') # API Endpoint
        .set_project('647c49a7e79df168b264') # project ID
        .set_key('7e62fbf81b373436fc3b6a7b798ba14a8fc6b2e7dcf1ea7b865b96ef10cc2ef2d540e883bff4515fb68f09b7fab128fd2278c63b0f99a42a60ea48330819302f85bf96494a7033f2915b8198993384cf25270460c8aa27d70dbf84874cc30b5408bd7e07c52c7e9d6ecfc499cfd7de6ed6016abbe0b5386bd19aef5716409f93') # secret API key
    )

    BUCKET_ID = get_bucket_id()

    storage = Storage(client)
    result = storage.list_files(BUCKET_ID)  # get files from the created bucket

    console = Console()

    if result["files"] == []:
        print("\nYour cloud is empty 😐")
    else:
        with console.status("[blue]flying high to the cloud..", spinner="dots2") as status:
            sleep(1.5)

            status.update(status="[green] Coming down with files", 
                    spinner="earth")
            sleep(1.5)
            
            # table object to create a table
            table = Table(title="Files in your cloud")

            table.add_column("FILE", style="cyan", no_wrap=False) 
            table.add_column("CREATED", style="white", no_wrap=False) 
            table.add_column("TYPE", style="white", no_wrap=False) 
            table.add_column("SIZE (KB)", style="white", no_wrap=False ) 
            
            for file in result["files"]:

                # store details of file
                file_name = file["name"]
                timestamp = file["$createdAt"]
                file_type = file["mimeType"]
                file_size = file["sizeOriginal"]
                file_count = result["total"]

                # Convert the timestamp to a datetime object
                datetime_obj = datetime.datetime.fromisoformat(timestamp[:-6])

                # Get the user's local time zone
                user_timezone = get_localzone()

                # Convert the datetime object to the user's local time zone
                localized_datetime = datetime_obj.astimezone(user_timezone)

                # Format the localized datetime in a user-friendly format
                user_friendly_dtm = localized_datetime.strftime('%B %d, %Y  %H:%M')
                
                # print the content in a table
                table.add_row(file_name,user_friendly_dtm,file_type,str(file_size))

        # print the table
        console.print(table)
        console.print("\nYou have %s files in your cloud ☁️\n"%file_count)
            
def new_bucket():
    client = Client()

    # project settings
    (client
        .set_endpoint('https://cloud.appwrite.io/v1') # API Endpoint
        .set_project('647c49a7e79df168b264') # project ID
        .set_key('7e62fbf81b373436fc3b6a7b798ba14a8fc6b2e7dcf1ea7b865b96ef10cc2ef2d540e883bff4515fb68f09b7fab128fd2278c63b0f99a42a60ea48330819302f85bf96494a7033f2915b8198993384cf25270460c8aa27d70dbf84874cc30b5408bd7e07c52c7e9d6ecfc499cfd7de6ed6016abbe0b5386bd19aef5716409f93') # secret API key
    )

    # create a random alphanumeric string for Bucket ID always followed by prefix 'C2CBUCK'
    BUCKET_ID_RAND = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(0,13))
    BUCKET_ID = "c2cbuck" + BUCKET_ID_RAND

    BUCKET_NAME_RAND = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(0,13))
    BUCKET_NAME = "bucknam" + BUCKET_NAME_RAND
    
    # create the bucket and store the response
    storage = Storage(client)
    response = storage.create_bucket(BUCKET_ID, BUCKET_NAME) # create bucket

    if response != None:
        bucket_id = response['$id']

        # write the bucket_id into a file in order to fetch it whenever necessary
        br = open("./data/buckets.txt","w")
        br.write(bucket_id)

        console = Console()
        with console.status("[Creating bucket...]flying high to the cloud..", spinner="dots2") as status:
            sleep(3)

        console.print("Bucket created. You can now start using you cloud. Happy transfering 😃")

def main():
    parser = argparse.ArgumentParser(description="CLI2CLOUD is a powerful Python CLI app for effortless file management tasks such as uploading, deleting, downloading, and listing files. Whether you're a developer, a data analyst, or simply someone who needs to efficiently manage files, cli2cloud empowers you to take control of your files with ease", 
                                     epilog="Made with ❤️ by https://github.com/thekaranatic")

    parser.add_argument("-newb", "--newbucket", type=str, nargs='*',
                        metavar="newbucket", help="Create new bucket on the cloud")

    parser.add_argument("-up", "--upload", type=str, nargs='*',
                        metavar="upload", help="Upload files to the cloud")
    
    parser.add_argument("-del", "--delete", type=str, nargs='*',
                        metavar="delete", help="Delete files from the cloud")

    parser.add_argument("-dwl", "--download", type=str, nargs='*',
                        metavar="download", help="Download files from the cloud")
    
    parser.add_argument("-ls", "--list", type=str, nargs='*',
                        metavar="list", help="List files from the cloud")

    # parser.add_argument("--signup", type=str, nargs='*',
    #                     metavar="signup", help="Create an account")
    
    # parser.add_argument("--delacc", type=str, nargs='*',
    #                     metavar="deleteaccount", help="Delete account")

    # parser.add_argument("-lin", "--login", type=str, nargs='*',
    #                     metavar="login", help="Login to your personal cloud")
    
    # parser.add_argument("-lout", "--logout", type=str, nargs='*',
    #                     metavar="logout", help="Logout from your personal cloud")
    

    # parse args from STDIN
    args = parser.parse_args()

    # call the functions depending on the type of arg
    if args.newbucket != None:
        new_bucket()
    elif args.upload != None:
        upload(args)
    elif args.delete != None:
        delete(args)
    elif args.download != None:
        download(args)
    elif args.list != None:
        list_files()
    

if __name__ == "__main__":
    # calling the main fucntion
    main()