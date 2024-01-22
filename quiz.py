print("Seja Bem Vindo ao Quiz!")
answer_user = input("Quer iniciar? (S/N)")

if answer_user != "S":
    quit()

score = 0 

print ("Começando...")
print ("Quem descobriu o Brasil? \n (A) Pedro Alvares Cabral \n (B) Dom Pedro 2 \n (C) Pero Vaz de Caminha \n (D) Pedro Gabriel \n")
answer_1 = input("Resposta:  ")

if answer_1 == "A":
    print("Acertooou!")
    score = score + 1
else:
    print("Errou :( ")



print ("Quanto tempo a luz do Sol demora para chegar a terra? \n (A) 12 minutos \n (B) 3 horas \n (C) 8 minutos \n (D) 30 segundos \n")
answer_2 = input("Resposta:  ")

if answer_2 == "C":
    print("Acertooou!")
    score = score + 1
else:
    print("Errou :( ")



print ("Qual a montanha mais alta do Brasil? \n (A) Pico Paraná \n (B) Pico da Neblina \n (C) Monte Roraima \n (D) Pico da Bandeira \n")
answer_3 = input("Resposta:  ")

if answer_3 == "B":
    print("Acertooou!")
    score = score + 1
else:
    print("Errou :( ")



print ("Qual o maior animal terrestre? \n (A) Baleia Azul \n (B) Dinossauro \n (C) Girafa \n (D) Elefante Africano \n")
answer_4 = input("Resposta:  ")

if answer_4 == "D":
    print("Acertooou!")
    score = score + 1
    print("O elefante africano é o maior animal terrestre. Ele pode medir até 4 metros de altura e 7 de comprimento. Seu peso pode chegar até 8 toneladas. ")
else:
    print("Errou :( ")
    print("O elefante africano é o maior animal terrestre. Ele pode medir até 4 metros de altura e 7 de comprimento. Seu peso pode chegar até 8 toneladas.")



print ("Qual tipo sanguíneo é considerado o doador universal? \n (A) Tipo A \n (B) Tipo B \n (C) Tipo O \n (D) Tipo AB \n")
answer_5 = input("Resposta:  ")

if answer_5 == "C":
    print("Acertooou!")
    score = score + 1
else:
    print("Errou :( ")



print ("Quais destes não é considerado um Planeta? \n (A) Vênus \n (B) Urano \n (C) Mercúrio \n (D) Plutão \n")
answer_6 = input("Resposta:  ")

if answer_6 == "D":
    print("Acertooou!")
    score = score + 1
else:
    print("Errou :( ")



print ("Qual a maior floresta tropical do Mundo? \n (A) Mata Atlântica \n (B) Pantanal \n (C) Floresta Amazônica \n (D) Floresta Asiática \n")
answer_7 = input("Resposta:  ")

if answer_7 == "C":
    print("Acertooou!")
    score = score + 1
else:
    print("Errou :( ")



print ("Quem pintou Monalisa? \n (A) Van Gogh \n (B) Leonardo Da Vinci \n (C) Pablo Picasso \n (D) Tarsila do Amaral \n")
answer_8 = input("Resposta:  ")

if answer_8 == "B":
    print("Acertooou!")
    score = score + 1
else:
    print("Errou :( ")



print ("Qual destas substâncias faz parte a composição do vidro? \n (A) Álcool \n (B) Petróleo \n (C) Celulose \n (D) Areia \n")
answer_9 = input("Resposta:  ")

if answer_9 == "D":
    print("Acertooou!")
    score = score + 1
else:
    print("Errou :( ")



print ("Qual animal produz o som mais alto? \n (A) Baleia Azul \n (B) Leão \n (C) Bugio \n (D) Elefante Africano \n")
answer_10 = input("Resposta:  ")

if answer_10 == "A":
    print("Acertooou!")
    score = score + 1
else:
    print("Errou :( ")



print ("Qual o menor e o maior país do mundo? \n (A) Vaticano e Rússia \n (B) Vaticano e China \n (C) Marrocos e Rússia \n (D) Brasil e China \n")
answer_11 = input("Resposta:  ")

if answer_11 == "A":
    print("Acertooou!")
    score = score + 1
else:
    print("Errou :( ")

print(f"Fim do Quiz! Você acertou: {score}/11")
if score < 5:
    print ("Você conseguiu terminar !")
if score == 11:
    print ("Parabéns você acertou todas as perguntas!")

