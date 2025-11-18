class Pessoa:
    def __init__(self,nome:str,idade:int):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}'


class Professor(Pessoa):
    def __init__(self, nome, idade,disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina
    def __str__(self):
        return f'{super().__str__()}\nDisciplina: {self.disciplina}'

class Aluno(Pessoa):
    def __init__(self, nome, idade,matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    def __str__(self):
        return f"{super().__str__()}\nMatricula: {self.matricula}"    


class Turma:
    def __init__(self,codigo,periodo):
        self.codigo = codigo
        self.periodo = periodo
        self.alunos = []
        self.professores = []

    def apresentar(self):
        print(f'Codigo: {self.codigo}\nPeriodo: {self.periodo}')
        print('Lista de alunos: ')
        for aluno in self.alunos:
            print(aluno.nome)
        print("Lista de Professores: ")    
        for professor in self.professores:
            print(f"{professor.nome} : {professor.disciplina}")

            

    def adicionar_aluno(self,aluno:Aluno):
        if isinstance(aluno,Aluno):
            self.alunos.append(aluno)
            return f"Aluno: {aluno.nome} adicionado a turma {self.codigo}"
        else:
            return "Coloque um aluno criado com a classe aluno!"
    
    def adicionar_professor(self, professor:Professor):
        if isinstance(professor,Professor):
            self.professores.append(professor)
            return f"Professor: {professor.nome} adicionado a turma {self.codigo}"
        else:
            return "Coloque um professor criado com a classe professor!"


aluno1 = Aluno('Vitao',20,"202411292")        
p1 = Professor('Gioliano',20,'Backend')
print(aluno1)
print(p1)
turma1 = Turma(20,2)
turma1.apresentar()
print(turma1.adicionar_aluno(aluno1))
print(turma1.adicionar_professor(p1))
turma1.apresentar()