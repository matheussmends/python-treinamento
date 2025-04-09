def coletar_dados():
    print("Preencha seus dados abaixo:\n")
    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    idade = input("Idade: ")
    sexo = input("Sexo: ")
    endereco = input("Endereço: ")
    
    ficha = f"""
    ==== FICHA DE DADOS ====
    Nome: {nome}
    CPF: {cpf}
    Idade: {idade} anos
    Sexo: {sexo}
    Endereço: {endereco}
    =========================
    """
    
    return ficha

if __name__ == "__main__":
    ficha = coletar_dados()
    print(ficha)