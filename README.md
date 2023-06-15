# cli2cloud

This is a Python-based CLI app that provides easy and efficient file management capabilities, including uploading, deleting, downloading, and listing files. Whether you're a developer, a data analyst, or simply someone who needs to efficiently manage files, cli2cloud empowers you to take control of your files with ease

## Commands

The app facilitates following commands

`-h` `--help`   :   About application


`-newb` `--newbucket`   :   Create new bucket on the cloud


`-delb` `--deletebucket`   :   Delete bucket from the cloud


`-up` `--upload`   :   Upload files to the cloud


`-del` `--delete`   :   Delete files from the cloud


`-dwl` `--download`   :   Download files from the cloud


`-ls` `--list`   :   List files from the cloud


## Usage
1. Create a bucket first
   `python  app.py -newb`

2. Start managing your files:

    `python  app.py -up <filename> or <file_path>`
        `Upload file to the cloud

    `python  app.py -del <filename>`
        Delete file from the cloud.

    `python  app.py --dwl <filename>`
       Download files from the cloud.

    `python  app.py -ls <path>`
       List files from the cloud

3. Delete the bucket if you no longer wish to use the cloud/app (this deletes all your files on the cloud)
    python  app.py -delb

Please note that you may need to modify the commands based on your operating system and Python environment.


## Prerequisites:
- Python 3.x
- Required Python packages (install using `pip`):
    - requests
    - argparse

## Installation:
1. Clone the repository IN A DIRECTORY OF FILES YOU WOULD LIKE TO MANAGE (upload, delete, etc.):
    git clone https://github.com/thekaranatic/cli2cloud.git

2. Navigate to the project directory:
    cd cli2cloud

3. Install the required packages:
    pip install -r requirements.txt

4. Start managing your files!

Please note that you may need to modify the commands based on your operating system and Python environment.

## License