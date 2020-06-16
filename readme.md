<h1><p align="center">Bulk Docx Translator</p></h1>

## Basic Usage

Bulk translator for docx files using the google translator service.
- Add files to translate to: `app/doccToTranslate`
- Run   `main.py`
- See translated files in `app/docsToTranslate/translatedDocs`


## Python Setup & Installation (Python 3.7.6) [Download Link](https://www.python.org/downloads/release/python-376/)

For Windows:
```
# Create your virtual environment
virtualenv venv

# Activate your virtual environment
venv/scripts/activate

#Install Modules
pip install -r requirements.txt
```

## Requirements

1) Pandoc
Visit `https://pandoc.org/installing.html` and download the installer for windows. 
or `choco install pandoc` with elevated an elevated console so PATH is written. 

2) Create or log in to GCP and create a project for [Goolge Translate Services](https://console.cloud.google.com/apis/library/translate.googleapis.com) 

3) Add the API to the project

4) Add the project ID to your .env as `GOOGLE_PROJECT_ID`

## Running the translator
```
#Run Tester
python main.py
```

Work in progress...


Made with ☕️ in 🇲🇽