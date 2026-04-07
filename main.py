import math
import random

# Gerar número aleatório entre 1 e 100
numero_secreto = int(random.random() * 100 + 1)

tentativas_restantes = 7
tentativas_feitas = 0

print("--- JOGO DA ADIVINHAÇÃO ---")
print("Tenta adivinhar o número secreto entre 1 e 100.")
print(f"Tens {tentativas_restantes} tentativas disponíveis.")

while tentativas_restantes > 0:
    entrada = input("\nDigita o teu palpite (ou 'sair'): ").strip().lower()

    if entrada == 'sair':
        print(f"Saíste do jogo. O número era {numero_secreto}.")
        break

    # Converter palpite para número
    if not entrada.isdigit():
        print("Por favor, insere um número inteiro válido.")
        continue

    palpite = int(entrada)
    tentativas_feitas += 1
    tentativas_restantes -= 1

    # Estruturas de controle de fluxo (if-else) para verificar o palpite
    if palpite == numero_secreto:
        print(f"PARABÉNS! Acertaste o número em {tentativas_feitas} tentativas!")
        break
    else:
        # Fornecer dicas se o palpite estiver errado
        if palpite < numero_secreto:
            print(f"DICA: O número secreto é MAIOR que {palpite}.")
        else:
            print(f"DICA: O número secreto é MENOR que {palpite}.")
        
        if tentativas_restantes > 0:
            print(f"Ainda tens {tentativas_restantes} tentativas.")
        else:
            print(f"\nGAME OVER! Esgotaste as tuas tentativas. O número era {numero_secreto}.")
