
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)
pdf.cell(200, 10, txt="Hello World!", ln=1, align="C")
pdf.output("2020-12-10 Hands-on Task for Nora.pdf")

