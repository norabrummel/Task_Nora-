from fpdf import FPDF
title = "2020-12-10 Hands-on Task for Nora" 
input1 = "Input 1"
pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=18)
pdf.cell(200, 10, txt=title + input1, ln=1, align="L")
pdf.output("/files/2020-12-10 Hands-on Task for Nora.pdf")
         
