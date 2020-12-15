from fpdf import FPDF
import sys

title = "2020-12-10 Hands-on Task for Nora \n" 
n = len(sys.argv)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=18)
pdf.multi_cell(0, 10, txt=title, align="L") 
for i in range(1, n):
    pdf.multi_cell(0, 10, txt=("\n%s" % sys.argv[i]), align="L") 

pdf.output("/files/2020-12-10 Hands-on Task for Nora.pdf")
         
