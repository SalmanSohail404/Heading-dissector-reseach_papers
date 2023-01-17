# Heading-dissector-reseach_papers
The purpose of this program is to be able to dissect headings from PDF and extract the text between the headings from research papers and them separate them into separate individual PDFs for each one. It uses python to accomplish the task. It extracts headings using a specific regex to determine headers and stores them into an array and then simply extracts the text between each array element. 
Libraries Used: pdfminer.six (To extract the text), re (To determine the headers), fpdf (To create separate PDF for each heading and its following text).

