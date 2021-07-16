# Programa de calculo de notas do IESB

Como pode se notar, eu utilizei a **class** Aluno para uma melhor compreensão e fazer esse algoritimo mais 'amigável'.

~~~python
class Aluno:
    def __init__(self,nome,idade,nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota
~~~

---

Depois, apliquei diversos **methods** para chamalos e fazer a operação da nota e *strings* para um estilo melhor.

Se quiser pode só copiar este código abaixo ou modificalo e começar a testar :

~~~python
hugo = Aluno('Hugo',18,'ADS')
hugo.eu()
hugo.nota()
~~~