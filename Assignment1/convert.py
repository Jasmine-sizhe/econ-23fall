import pdfkit

# Input HTML file and output PDF file paths
input_html = 'utah-econometrics.html'
output_pdf = 'output.pdf'

# Convert HTML to PDF
pdfkit.from_file(input_html, output_pdf)