#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.translator import XTranslator
import os

# Tester


# Find all docx files
docsToTranslate = []


# Find all docx in folder to translate
for path, subdirs, files in os.walk("app/docsToTranslate/"):
    for name in files:
        if os.path.splitext(os.path.join(path, name))[1] == ".docx":
            docsToTranslate.append(name)

for file in docsToTranslate:
    XTranslator(
        "docsToTranslate/" + file, "docsToTranslate/translatedDocs/TRANSLATED_" + file
    )

# Todo fix path for translation input and output relative to translator.py

# Test on precommit
