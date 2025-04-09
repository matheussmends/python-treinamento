import pydf

pdf = pydf.generate_pdf('<h>Meu pdf gerado com python</h1>')
with open('outro_pdf.pdf', 'wb') as f:
    f.write(pdf)