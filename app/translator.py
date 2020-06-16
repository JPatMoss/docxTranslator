#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mammoth
from dotenv import load_dotenv
from google.cloud import translate
import pypandoc
import os
load_dotenv()

class XTranslator():
    '''
    Main classs to translate any docx file using google services.
    '''
    


    def __init__(self, inputfilePath,outputfilePath):

        self.project_id = os.getenv('GOOGLE_PROJECT_ID')
        self.outputfilePath = outputfilePath
        #Start conversion and translation
        self.mdToConvert = self.fileReceiver(inputfilePath)
        #Convert md to docx
        self.fileConverter(self.mdToConvert,outputfilePath)

        
    def translate_text(self,text="YOUR_TEXT_TO_TRANSLATE"):
        """Translating Text."""

        client = translate.TranslationServiceClient()

        parent = client.location_path(self.project_id, "global")

        response = client.translate_text(
            
            parent=parent,
            contents=[text],
            mime_type="text/html",  # mime types: text/plain, text/html
            source_language_code="en-US",
            target_language_code="es-MX",
        )
        # Display the translation for each input text provided


        with open(self.outputfilePath, "w", encoding='utf-8') as file:
            for translation in response.translations:
                file.write(translation.translated_text)
    def fileReceiver(self,docxInputFilename):
        with open(str(docxInputFilename), "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html = result.value
            #Send to translator
            self.translate_text(html)
            #Write output to md
        with open(str(docxInputFilename)+".md", "w", encoding='utf-8') as file:
            file.write(html)
        return file.name

    def fileConverter(self,mdInputfile,docxOutfile):
        pypandoc.convert_file(mdInputfile, 'docx',outputfile=docxOutfile)

