import PyPDF2
import csv
import pandas as pd
from pprint import pprint
import re

csv_file = 'AtlasTest.csv'
#Use PyPDF2 to read the PDF file 
with open('./AtlasTest.pdf', 'rb') as pdf_file:
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    num_pages = read_pdf.getNumPages()
    strtext = ""

    
    #Loops through PDF file to get the number of pages and append to strtext
    for page_index in range(num_pages):
        page = read_pdf.getPage(page_index)
        strtext += page.extractText()
    strtext = strtext.replace('\n','')
    with open('./PDFout.txt', 'w') as out_file:
        out_file.write(strtext)


    #Find the Reporting Period (regex matches first two strings after colon)
    TO_Report_Period = re.search(r'TO Reporting Period:\s(\w+ \w+)', strtext, re.IGNORECASE)
    MSR_Report_Period = TO_Report_Period.groups()[0]
    print(MSR_Report_Period)


    #Find the Task Order Number (regex searches for first string after colon and space)
    TO_Number = re.search(r'TO Number:\s(\w+)', strtext, re.IGNORECASE)
    MSR_Number = TO_Number.groups()[0]
    print(MSR_Number)


    #Find the Contract Number (regex matches characters in hyphens after colon)
    Contract_Number = re.search(r'Contract Number and Title:\s(\w+(?:-\w+)+)', strtext, re.IGNORECASE)
    MSR_CNumber = Contract_Number.groups()[0]
    print(MSR_CNumber)


    # Find Subcontractor (regex matches first three characters after colon)
    sub_cont = re.search(r'Subcontractor:\s(\w+ \w+ \w+)', strtext, re.IGNORECASE)
    MSR_sub = sub_cont.groups()[0]
    print(MSR_sub)


    #### Regex Positive Lookahead Assertion - splits on P which has a 'WS 6.# - string' following (***if this is a '-' problem, look at this line***)
    parts = re.split('P(?=WS \d+.\d+ - .+)', strtext)
    parts_dict = {}


    #Loops through parts to find and creates a list of each PWS with its bullets
    #Updates parts_dict with new value strings (removes double spaces and creates key and value pairings)
    for part in parts:
        #Creates a list for each part - separates each bullet info
        row_parts = part.split('  ')                                         ######## Has to do with the long dash in parentheses
        # row_parts = re.split('(?<=\)\s+)', part)
        # row_parts = re.split('(?<=\)\s\s\w)', part)
        # row_parts = re.split('(?=\)\s\s)', part)
        # row_parts = re.split('\s\s(?=\d+.\d)', part)
        row_parts = [part for part in row_parts if part not in ['']]
        key = row_parts[0]
        value = row_parts[1:]
        d = {key: value}
        parts_dict.update(d)
    data = dict([(k, pd.Series(v)) for k,v in parts_dict.items()])


    #Creating DataFrame using Pandas and write to CSV file
    df = pd.DataFrame(data)
    df_melt = pd.melt(df)
    df_melt.dropna(axis=0, inplace=True, how='any')
    df_melt = pd.DataFrame(df_melt)
    df_melt['TO Reporting Period'] = MSR_Report_Period
    df_melt['Task Order Number'] = MSR_Number
    df_melt['Contract Number'] = MSR_CNumber
    df_melt['Subcontractor'] = MSR_sub
    df_melt.rename(columns={"variable": "PWS Title", "value": "PWS Info"}, inplace=True)
    df_melt.to_csv(csv_file, index=False, encoding='utf-8')
