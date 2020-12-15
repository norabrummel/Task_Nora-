from fpdf import FPDF
import sys

title = "2020-12-10 Hands-on Task for Nora \n" 
pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=18)
#pdf.cell(200, 10, txt=title, ln=1, align="L")
#pdf.multi_cell(0, 10, txt=title + input1 + "\n" + input2, align="L")
pdf.multi_cell(0, 10, txt=title + ("%s" % sys.argv[1]), align="L")
pdf.output("/files/2020-12-10 Hands-on Task for Nora.pdf")
         
