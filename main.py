import os
import time
from PyPDF2 import PdfFileWriter, PdfFileReader
from collections import OrderedDict


#  ------ Functions ------
#  ------ Checks if Working Directory Exists ------
def makeworkdir():
    working_dir = os.path.isdir('./PyTools')

    if working_dir:
        return
    else:
        try:
            print('Preparing for First Time setup...')
            time.sleep(3)
            os.mkdir('PyTools')
            print('Required prerequisites have been prepared, please re-run PyDF Helper...')
            return
        except:
            print('Failed to create the PyTools working directory... Was I started with Admin Privileges?')


#  ------ Checks for csv in the Working Directory ------
def checkworkdir():
    csvindir = os.path.isfile('PyTools/test.csv')
    pdfindir = os.path.isfile('PyTools/test.pdf')

    try:
        if csvindir:
            print('CSV Detected... ')
        else:
            print('Failed to detect CSV... Please place a CSV in the PyTools folder.')
    except:
        print('Failed to detect CSV in the PyTools Working Directory... Was I started with Admin Privileges?')

    try:
        if pdfindir:
            print('PDF Detected... ')
        else:
            print('Failed to detect PDF... Please place a PDF in the PyTools folder.')
    except:
        print('Failed to detect PDF in the PyTools Working Directory... Was I started with Admin Privileges?')


#  ------ Gets interactive field information from PDF's ------
#  def getfields(obj, tree=None, retval=None, fileobj=None):
#      fieldattributes = {'/FT': 'Field Type', '/Parent': 'Parent', '/T': 'Field Name', '/TU': 'Alternative Field Name',
#                         '/TM': 'Mapping Name', '/Ff': 'Field Flags', '/V': 'Value', '/DV': 'Default Value'}


try:
    working_dir = os.path.isdir('./PyTools')

    if working_dir:
        print('PyDF Helper v0.1')
        time.sleep(1)
    else:
        print('Preparing for First Time setup...')
        time.sleep(3)
        os.mkdir('PyTools')
        print('Required prerequisites have been prepared, please re-run PyDF Helper...')
        exit()
    makeworkdir()
    input('Please place CSV and PDF into the PyTools Working Directory then press Enter to Continue...')
    checkworkdir()
except:
    exit()
