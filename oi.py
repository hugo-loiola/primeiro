# Programa de calculo de notas do IESB.

class Aluno:
    def __init__(self,nome,idade,curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
    
    def eu(self):
        print(f'Meu nome é {self.nome}, tenho {self.idade} e faço o curso de{self.curso} na minha faculdade')
    
    def nota(self):
        
        print('~'*10)
        print('Nota IESB')
        print('~'*10)

        p1=int(input('Coloque a nota da P1: '))
        p2=int(input('Coloque a nota da P2: '))

        nota1 = {
        'p1':p1,
        'p2':p2,
        }

        media = ((nota1['p1'] * 0.4) + (nota1['p2'] * 0.6))

        print(media)
        
        if media < 5:
            p3=int(input('Você não alcançou a média! Coloque a nota da P3: '))
            nova_nota = min(nota1,key=nota1.get)
            nota1[nova_nota] = p3
            media = ((nota1['p1'] * 0.4) + (nota1['p2'] * 0.6))
            print(f'Esta é a sua nova média {media}')
            if media < 5:
            	print(f'Infelizmente você não consegiua atingir a média.')
		else:
			print('Parabéns! Você consegiu passar.')
# Chamar a função e colocar os dados. 
user_name = input("Coloque seu nome: ")
user_age = int(input("Coloque sua idade: "))
user_course = input("Coloque seu curos: ")
hugo = Aluno(user_name, user_age, user_course)
hugo.eu()
hugo.nota()
