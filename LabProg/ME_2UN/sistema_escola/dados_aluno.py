
dados_aluno = 'sistema_escola/dados_exportados/aluno.txt'

from sistema_escola import dados_pessoa as p 

class aluno (p.pessoa): 
    def __init__(self):
        self.rg = " "
        self.cpf = " "
        self.convenio = " "
        self.matricula = " "
        self.facebook = " "
        self.linkedin = " "
        self.instagram = " "
        self.lista_aluno = " "
        super().__init__()

    def cadastro_aluno (self):
        super().cadastrar_pessoa() 
        self.rg = input('Digite o RG: ')
        self.cpf = input('Digite o CPF: ')
        self.convenio = input('Digite o convenio: ')
        self.matricula = input('Digite a matricula: ')
        self.facebook = input('Digite o facebook: ')
        self.linkedin = input('Digite o linkedin: ')
        self.instagram = input('Digite o instagram: ')
        
        self.lista_aluno = [self.nome, self.celular, self.email, self.rg, self.cpf, self.convenio, self.matricula, self.facebook, self.linkedin, self.instagram]

        print('Cadastro realizado com sucesso! ')

        self.salvar()
    
    def salvar(self):
        with open(dados_aluno, 'a') as dados: 
            dados.write(str(self.lista_aluno + '\n'))


    def exibir_aluno(self):
        print ('[nome, celular, email, rg, cpf, convenio, matricula, facebook, linkedin, instagram]')
        with open (dados_aluno, 'r') as arquivo:
            for linha in arquivo:
                linhas_em_brancos = linha.strip()
                print(linhas_em_brancos)



