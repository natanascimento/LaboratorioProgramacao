#Menu#

from sistema_escola import dados_pessoa as p
from sistema_escola import dados_aluno as a
from sistema_escola import dados_tecnico as t
from sistema_escola import dados_professor as f
from sistema_escola import dados_curso as c
from sistema_escola import folha_pagamento as fp

class menu:

    def __init__(self):
        self.opcao = ' '
        self.subopcao = ' '
        self.p = p.pessoa()
        self.a = a.aluno()
        self.t = t.tecnico_administrativo()
        self.f = f.professor()
        self.c = c.curso()
        self.fp = fp.folha()

    def main_menu(self):
        print('     Sistema Escolar')
        print('---------------------------')
        print('1 - Pessoa\n2 - Aluno\n3 - Tecnico Adiminstrativo\n4 - Professor\n5 - Curso\n6 - Folha de Pagamento')
        print('---------------------------')
        self.opcao = input('Informe uma opção: ')
        
        if self.opcao == '1':
            print('---------------------------')
            print('1  -  Cadastrar Pessoa \n2  -  Exibir Pessoa')
            print('---------------------------')
            self.subopcao = input('Informe uma opção: ')

            if self.subopcao == '1':
                self.p.cadastrar_pessoa()
            if self.subopcao == '2':
                self.p.exibir()
        
        if self.opcao == '2':
            print('---------------------------')
            print('1  - Cadastrar Aluno\n2  -  Exibir Aluno')
            print('---------------------------')
            self.subopcao = input('Informe uma opção: ')

            if self.subopcao == '1':
                self.a.cadastro_aluno()
            if self.subopcao == '2':
                self.a.exibir_aluno()
        
        if self.opcao == '3':
            print('---------------------------')
            print('1  -  Cadastrar Tecnico Administrativo \n2  -  Exibir Tecnico Administrativo')
            print('---------------------------')
            self.subopcao = input('Informe uma opção: ')

            if self.subopcao == '1':
                self.t.cadastro_tecnico_administrativo()
            if self.subopcao == '2':
                self.t.exibir()
        
        if self.opcao == '4':
            print('---------------------------')
            print('1  -  Cadastrar Professor\n2  -  Exibir Professor')
            print('---------------------------')
            self.subopcao = input('Informe uma opção: ')

            if self.subopcao == '1': 
                self.f.cadastrar_professor()
            if self.subopcao == '2':
                self.f.exibir()
        
        if self.opcao == '5':
            print('---------------------------')
            print('1 - Cadastrar Curso\n2 - Exibir Curso\n3 - Exibir Valor Total do Curso')
            print('---------------------------')
            self.subopcao = input('Informe uma opção: ')

            if self.subopcao == '1':
                self.c.cadastrar_curso()
            if self.subopcao == '2':
                self.c.exibir()   
            if self.subopcao == '3':
                self.c.exibir_valor()

        if self.opcao == '6':
            print('---------------------------')
            print('1 - Exibir Folha')
            print('---------------------------')
            self.subopcao = input('Informe uma opção: ')

            if self.subopcao == '1':
                self.fp.set_salario_prof()

main = menu()
main.main_menu()