dados_professor = 'sistema_escola/dados_exportados/professor.txt'
dados_salarioprof = 'sistema_escola/dados_exportados/salario_prof.txt'

from sistema_escola import dados_pessoa as p 

class professor (p.pessoa): 
    def __init__(self): 
        self.matricula_professor = " "
        self.titulacao = " "
        self.especialidade = " "
        self.plus_salario = " "
        self.salario_hora = " "
        self.linkedin = " "
        self.lattes = " "
        self.nivel = " "
        self.lista_professor = ' '
        self.describenivel = ' '
        self.lista_salario_prof = ' '
        super().__init__()

    def cadastrar_professor(self):
        super().cadastrar_pessoa() 
        self.matricula_professor = input('Digite a matricula do professor: ')
        self.titulacao = input('Digite a titulação: ')
        self.especialidade = input('Digite a especialidade: ')
        self.plus_salario= input('Digite o plus salario: ')
        self.salario_hora = input('Digite o salario por hora: ')
        self.linkedin = input('Digite o Linkedin: ')
        self.lattes = input('Digite o lattes: ')
        self.nivel = float(input('Digite o nivel: '))
        
        self.lista_professor = [self.nome, self.celular, self.email, self.matricula_professor, self.titulacao, self.especialidade, self.plus_salario, self.salario_hora, self.linkedin, self.lattes, self.nivel]
    
        print('Cadastro realizado com sucesso! ')

        self.describe_nivel_prof()
        self.salvar()


    def describe_nivel_prof(self):
        if self.nivel == 1:
            self.describenivel = 2570.00
            self.lista_salario_prof = [self.describenivel]
        if self.nivel == 2:
            self.describenivel = 3685.00
            self.lista_salario_prof = [self.describenivel]
        if self.nivel == 3:
            self.describenivel = 4843.33
            self.lista_salario_prof = [self.describenivel]
        if self.nivel == 4:
            self.describenivel = 5223.77
            self.lista_salario_prof = [self.describenivel]
        self.salvar_salario()

    def salvar_salario(self):
        with open(dados_salarioprof, 'a') as dados_salario:
            dados_salario.write(float(self.lista_salario_prof))

    def exibir_salario (self):
        with open(dados_salarioprof, 'r') as arquivo_salario:
            for linha in arquivo_salario:
                linhas_em_branco = linha.strip()
                print(linhas_em_branco)

    def salvar(self):
        with open(dados_professor, 'a') as dados:
            dados.write(str(self.lista_professor))
    

    def exibir(self):
        print ('[nome, celular, email, matricula_professor, titulação, especialidade, plus_salario, salario_hora, linkedin, lattes, nivel]')
        with open(dados_professor, 'r') as arquivo:
            for linha in arquivo:
                linhas_em_brancos = linha.strip()
                print(linhas_em_brancos)

