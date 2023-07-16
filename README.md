![cli2cloud logo cover](https://github.com/thekaranatic/cli2cloud/assets/56465610/f5dcbb05-9f0e-4cb6-bc2b-72fc8735f6c6)

# cli2cloud

[![thekaranatic - cli2cloud](https://img.shields.io/static/v1?label=thekaranatic&message=cli2cloud&color=blue&logo=github)](https://github.com/thekaranatic/cli2cloud "Go to GitHub repo") [![stars - cli2cloud](https://img.shields.io/github/stars/thekaranatic/cli2cloud?style=social)](https://github.com/thekaranatic/cli2cloud) [![forks - cli2cloud](https://img.shields.io/github/forks/thekaranatic/cli2cloud?style=social)](https://github.com/thekaranatic/cli2cloud) [![wakatime](https://wakatime.com/badge/user/bf88ca6a-7335-436d-bf81-82f32bc434c2/project/b551b3c7-6b8c-4b04-82d4-6e27488c3113.svg)](https://wakatime.com/badge/user/bf88ca6a-7335-436d-bf81-82f32bc434c2/project/b551b3c7-6b8c-4b04-82d4-6e27488c3113) [![Generic badge](https://img.shields.io/badge/version-0.9.9-yellow.svg)](https://shields.io/) [![made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![built with appwrite](https://img.shields.io/badge/Appwrite-F02E65?style=for-the-badge&logo=Appwrite&logoColor=black) [![GitHub release](https://img.shields.io/github/release/thekaranatic/cli2cloud?include_prereleases=&sort=semver&color=blue)](https://github.com/thekaranatic/cli2cloud/releases/) [![License](https://img.shields.io/badge/License-MIT-blue)](#license)

This is a Python-based CLI app that provides easy and efficient file management capabilities, including uploading, deleting, downloading, and listing files over the cloud. Whether you're a developer, a data analyst, or simply someone who needs to efficiently manage files, cli2cloud empowers you to take control of your files with ease

## Supported Commands

The app facilitates following commands

- `-h` `--help`   :   About application

- `-newb` `--newbucket`   :   Create new bucket on the cloud

- `-delb` `--deletebucket`   :   Delete bucket from the cloud

- `-up` `--upload`   :   Upload files to the cloud

- `-del` `--delete`   :   Delete files from the cloud

- `-dwl` `--download`   :   Download files from the cloud

- `-ls` `--list`   :   List files from the cloud

## Prerequisites:
- Python 3.x
- Required Python packages (install using `pip`):
    - Appwrite Python SDK (`appwrite`)
    - `argparse`
    - `rich`

## Installation:
1. Create an Appwrite account and setup your project.
2. Copy the **API Endpoint**, **Project ID** & **API Key**.
3. Previews:

    - >![appwrite-projectId](https://github.com/thekaranatic/cli2cloud/assets/56465610/42995fff-924d-455e-ba57-efcfed638a97)
    - >![appwrite-apiKey](https://github.com/thekaranatic/cli2cloud/assets/56465610/2673b1f3-f004-4362-acb5-92bf602c8500)

4. Create a `.env` file in the project's root directory.
5. Add the following environment parameters:
    ```env
        API_ENDPOINT=
        PROJECT_ID=
        API_KEY=
    ```

6. Clone the repository IN A DIRECTORY OF FILES YOU WOULD LIKE TO MANAGE (upload, delete, etc.):
    git clone https://github.com/thekaranatic/cli2cloud.git

7. Navigate to the project directory:
    cd cli2cloud

8. Install the required packages:
    pip install -r requirements.txt

9. Start managing your files!

Please note that you may need to modify the commands based on your operating system and Python environment.

### Running in the App in a virtual Environment
To run cli2cloud in a virtual environment:
- ```shell
    python3 -m venv venv
  ```
- ```shell
    .\env\Scripts\activate
  ```
- ```shell
    pip install -r requirements.txt
  ```
- ```shell
    python app.py <command>
  ```
---
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


## Demo
[Watch the demo](https://vimeo.com/836294019)

## License
Licensed under [MIT License](https://github.com/thekaranatic/cli2cloud/blob/main/LICENSE) by [@thekaranatic](https://github.com/thekaranatic).
