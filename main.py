# Import all needed libraries
import requests
import pandas as pd
from template import xmltemplate
import datefinder
import datetime

# Define some variables that will not change
now = datetime.datetime.now()
csv = "doi_input_datasets.txt"

# Define the address of the DOI site
doisite = "https://doi-test.stfc.ac.uk/metadata"

columns = ['IDENTIFIER', 'CREATOR', 'TITLE', 'PUBLISHER', 'TIME_COVERAGE', 'TYPE', 'LANGUAGE', 'FORMAT',
           'NUMBER_OF_RECORDS', 'RIGHTS', 'DESCRIPTION', 'SUBJECT', 'GEOGRAPHICAL_COVERAGE', 'LANDING_PAGE']
values = ['IDENTIFIER', 'CREATOR', 'TITLE', 'PUBLISHER', 'TIME_COVERAGE', 'TYPE', 'LANGUAGE', 'FORMAT',
          'NUMBER_OF_RECORDS', 'RIGHTS', 'DESCRIPTION', 'SUBJECT', 'GEOGRAPHICAL_COVERAGE', 'LANDING_PAGE', 'DOI']

df = pd.read_csv(csv, sep=']')

rc = df.shape[0]
i = 0
c = 0


# Pull the requested row of data from the CSV file and stores it in the 'values' list

def fetch_values(rowindex: int):
    inc = 0
    while inc < len(columns):
        values[inc] = df.get_value(rowindex, columns[inc])
        inc += 1


def filloutxml(doivalues: list):
    metadata = xmltemplate.replace("doiIDENTIFIER", str(doivalues[0]))
    metadata = metadata.replace("doiCREATOR", str(doivalues[1]))
    metadata = metadata.replace("doiTITLE", str(doivalues[2]))
    metadata = metadata.replace("doiPUBLISHER", str(doivalues[3]))
    metadata = metadata.replace("doiTIME_COVERAGE", str(now.year))
    metadata = metadata.replace("doiSUBJECT", str(doivalues[11]))
    metadata = metadata.replace("doiLANGUAGE", str(doivalues[6]))
    metadata = metadata.replace("doiTYPE", str(doivalues[5]))
    metadata = metadata.replace("doiNUMBER_OF_RECORDS", str(doivalues[8]))
    metadata = metadata.replace("doiFORMAT", str(doivalues[7]))
    metadata = metadata.replace("doiRIGHTS", str(doivalues[9]))
    metadata = metadata.replace("doiDESCRIPTION", str(doivalues[10]))
    metadata = metadata.replace("doiGEOGRAPHICAL_COVERAGE", str(doivalues[12]))

    return metadata


def savexmlfile(filledmetadata: str):
    filename = str(values[0]) + " generated metadata.xml"
    filesave = open(filename, 'w+')
    filesave.write(filledmetadata)


# Functions below are for input validation

def selectdate(doiDATE: str):
    matches = datefinder.find_dates(doiDATE)
