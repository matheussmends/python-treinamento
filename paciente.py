# PARADIGMA IMPERATIVO

"""
Paradigma Imperativo - Fortran - Sequencia, Decisao e a Iteracao
Paradigma Estruturado - C - structs
Paradigma Procedural - Python 
"""

def Registrar(nome, idade, cpf, email):
    paciente = {'nome': nome, 'idade': idade, 'cpf': cpf, 'email': email} # uso do dicionario{} para ter maior controle de acesso das variaveis
    return paciente


# Reuso e Coesao

# PARADIGMA ORIENTADO A OBJETOS

"""
Classe - Um conjunto de objetos com as mesmas caracteristicas
Objeto - Representação do mundo real como um tipo de dado de uma classe
Construtor - É uma função criada implicitamente com o mesmo nome da classe
Atributo - São as variaveis de uma classe
"""

class Paciente:
    
    def __init__(self, nome, idade, cpf, email):
        print("Acessei o construtor")
        self.nome = nome 
        self.idade = idade
        self.cpf = cpf
        self.email = email


"""
Simulação de Eventos Discretos -> Paradigma Orientado á Objeto
Relacao -> Destacando funcoes e variaveis

------------------------------

Conceitos estruturais

-Classe

Classe é uma estrutura que abstrai um conjunto de objetos com caracteristicas similares. Definindo o comportamento dos seus objetos atraves das estruturas?

1- Atributos
2- Métodos

A classe define um tipo de dado abstrato
"""

# Abstracao
# Reuso e coesao
# Acoplamento, heranca, polimorfismo, GAP semantico

"""

Conceitos fundamentais

-Abstrcao

Processo pelo qual se isolam atributos de um objeto, considerando os que certos grupos de objetos tenham em comum

-Reuso

Nao existe pior pratica em programacao do que repetir codigo.

"""

