import matplotlib.pyplot as plt

#Crie um gráfico de linha que mostre a altura de uma planta ao longo de 5 semanas. Use os dados fixos:
#semanas [1, 2, 3, 4, 5] e alturas [3, 6, 9, 12, 15] cm.

plt.plot([1, 2, 3, 4, 5], [3, 6, 9, 12, 15])
plt.title("Gráfico de Linha")
plt.xlabel("Semanas")
plt.ylabel("Altura(cm)")
plt.show()

#Peça ao usuário para digitar o nome de 3 matérias e suas respectivas notas. Depois, crie um gráfico de barras com esses dados
a = float(input("Digite a nota de Matemática:"))
b = float(input("Digite a nota de Português:"))
c = float(input("Digite a nota de Design Digital:"))


categorias = ['Matemática', 'Português', 'Design Digital']
valores = [a, b, c]
plt.bar(categorias, valores)
plt.title("Gráfico de Barras")
plt.show()

#Crie um gráfico de pizza que mostre a preferência de transporte das pessoas. Use os dados fixos: Ônibus
#(40%), Carro (30%), Bicicleta (20%), A pé (10%).

fatias = [40, 30, 20, 10]
atividades = ['Ônibus', 'Carro', 'Bicicleta','A pé']
plt.pie(fatias, labels=atividades, autopct='%1.1f%%')
plt.title("Gráfico de Pizza")
plt.show()

#Peça ao usuário para digitar os batimentos cardíacos em três momentos: ao acordar, após exercício físico e após 10 minutos de descanso. Crie um gráfico de linha com esses dados.
a = float(input("Digite os BPMS ao Acordar:"))
b = float(input("Digite os BPMS após Exercicio Físico:"))
c = float(input("Digite os BPMS após 10min de descanso:"))


plt.plot( ["ao Acordar", "após Exercicio Físico", "após 10min de Descanso"], [a, b, c])
plt.title("Gráfico de Linha")
plt.xlabel("Momentos do Dia")
plt.ylabel("BPMS")
plt.show()

#Crie um gráfico de barras com as vendas de três sabores de sorvete: Chocolate (150), Morango (100), Baunilha (130).

categorias = ['Chocolate', 'Morango', 'Baunilha']
valores = [150, 100, 130]
plt.bar(categorias, valores)
plt.title("Gráfico de Barras")
plt.show()

#Peça ao usuário para informar quantas horas ele passou em um dia com sono, estudando e em lazer. Crie um gráfico de pizza com esses dados.
a = float(input("Digite o tempo que você passa dormindo(Horas):"))
b = float(input("Digite o tempo que você passa estudando(Horas):"))
c = float(input("Digite o tempo que você passa em Lazer(Horas):"))

fatias = [a, b, c]
atividades = ['Dormir', 'Estudar', 'Lazer']
plt.pie(fatias, labels=atividades, autopct='%1.1f%%')
plt.title("Gráfico de Pizza")
plt.show()

#Crie um gráfico de linha que mostre a velocidade de um carro ao longo do tempo. Use os dados: tempo [0, 5, 10, 15, 20] segundos e velocidade [0, 20, 40, 35, 50] km/h.

plt.plot([0, 5, 10, 15, 20], [0, 20, 40, 35, 50])
plt.title("Gráfico de Linha")
plt.xlabel("Tempo em segundos")
plt.ylabel("Velocidade em km/h")
plt.show()


#Peça ao usuário para digitar quantas bananas, maçãs e laranjas ele comeu na semana. Mostre os dados em um gráfico de barras.
a = float(input("Digite quantas bananas você comeu na semana:"))
b = float(input("Digite quantas maçãs você comeu na semana:"))
c = float(input("Digite quantas laranjas você comeu na semana:"))

categorias = ['Bananas', 'Maçãs', 'Laranjas']
valores = [a, b, c]
plt.bar(categorias, valores)
plt.title("Gráfico de Barras")
plt.show()

#Peça ao usuário para digitar quantas horas ele usa por dia as seguintes redes sociais: Instagram, YouTube, TikTok, WhatsApp e Outros. Crie um gráfico de pizza com essas informações.

a = float(input("Digite quantas horas por dia vocÊ passa no Instagram:"))
b = float(input("Digite quantas horas por dia vocÊ passa no Youtube:"))
c = float(input("Digite quantas horas por dia vocÊ passa no Tiktok:"))
d = float(input("Digite quantas horas por dia vocÊ passa no WhatsApp:"))
e = float(input("Digite quantas horas por dia vocÊ passa no Outros:"))

fatias = [a, b, c, d, e]
atividades = ['Instagram', 'Youtube', 'Tiktok','WhatsApp','Outros']
plt.pie(fatias, labels=atividades, autopct='%1.1f%%')
plt.title("Gráfico de Pizza")
plt.show()

#Peça ao usuário para digitar seu nível de energia (de 0 a 10) pela manhã, à tarde e à noite. Crie um gráfico de linha com esses dados
a = float(input("Digite seu nivel de Energia de Manhã(0 a 10):"))
b = float(input("Digite seu nivel de Energia de Tarde(0 a 10):"))
c = float(input("Digite seu nivel de Energia de Noite:(0 a 10)"))


plt.plot( ["Manhã", "Tarde", "Noite"], [a, b, c])
plt.title("Gráfico de Linha")
plt.xlabel("Momentos do Dia")
plt.ylabel("Niveis de Energia")
plt.show()