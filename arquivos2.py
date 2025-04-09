from pydf import generate_pdf

pdf = generate_pdf("<h1>Ola mundo</h1><p>testando meu documento</p>")

with open("meuarquivo.pdf", "wb") as arquivo:
    arquivo.write(pdf)
