from pdfminer.high_level import extract_text
import re
import time
from fpdf import FPDF
import os

os.system ("color")

print("\033[1m" + "\t\t****************************")
print("\t\t*\t\t\t   *")
print("\t\t*      "+"\033[4;31m"+"HEADING"+ "\033[0m" + "\033[1m" +"DISSECTOR    *")
print("\t\t*\t\t\t   *")
print("\t\t****************************\n" + "\033[0m")
print("\033[1;36m" + "\tMade by Salman Sohail\n" + "\033[0m")

filename = input("Enter research paper PDF name with extension (.pdf): ")
text = extract_text(filename)
text2 = text.encode('utf-8')

pattern = r'(?<=\n)^[0-9]\.\D\s*.*?(?=\n)'
check_reference = r'References|REFERENCES'
reference = re.findall(check_reference, text, re.M)
headers = []
raw_headers = re.findall(pattern,text,re.M)

print(reference)
for heading in raw_headers:
    heading = heading.replace("\n",' ')
    heading2 = heading.replace(","," ")
    headers.append(heading2)
print(headers)

heading_amount = len(headers)
count = 0
i = 0
while (count <= (heading_amount)):
    try:    
        if (count == heading_amount):
            start_index = text.find(reference[0])
            end_index = (len(text)-1)
        else:
            start_index = text.find(headers[count])
            if (count == heading_amount - 1):
                end_index = text.find(reference[0])
            else:    
                end_index = text.find(headers[count + 1])
    except:
        break

    # Extract the text between the delimiters
    extracted_text = text[start_index:end_index]
    extracted_text.encode('utf-8')
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', size=12)
    pdf.multi_cell(0, 5,extracted_text)
    if (count == heading_amount):
        pdf.output(filename + " REFERENCES" +".pdf")
    else:
        pdf.output(headers[i] +".pdf")
    count += 1
    i += 1
