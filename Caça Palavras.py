#Início do Código

import os

#Definindo variáveis
palavra_secreta = "casco" #Insira a palavra para o usuário
vitoria = f'Você ganhou! A palavra secreta era {palavra_secreta}'
qtd_letras_palavra_secreta = len(palavra_secreta)
erro_invalido = "Digite uma letra válida"
letras_acertadas = ''
contador = 0

#App

while True:
    entrada = input(str("Digite sua primeira letra: "))
    contador += 1
    if len(entrada) == 1: #Se o usuario digitou apenas 1 letra
        if entrada in palavra_secreta:
            letras_acertadas += entrada
        palavra_formada = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta #Revela 1 letra e mantém as demais letras ocultas
            else:
                palavra_formada += "*" #Retorna apenas asteriscos para o usuário
        print(palavra_formada)
    else:
        print("Digite um valor válido")
        continue
    if palavra_formada == palavra_secreta: #Final do jogo
        print("Você ganhou!")
        print('A palavra formada era: ',palavra_formada)
        print("Número de tentativas: ",contador)
        contador = 0
        letras_acertadas = ''
        reset = input('Digite qualquer tecla para resetar: ')
        if reset != "":
            os.system('cls') #Reseta o terminal