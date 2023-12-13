# Teste Elevador

from Elevador import Elevador
import random

# Criação e instância do objeto
e1 = Elevador(andarAtual=0, portaAberta=True, peso=random.random() * 1000)

# Imprimindo o Status do Elevador
print('\n\t\t\t -- Elevador Parado -- ')
print(e1)

# Subir
print('\n\t\t\t -- Subindo -- ')
e1.subir(5)

# Exibir o Elevador no 5º andar
print('\n\t\t\t -- Elevador no 5º andar --')
print(e1)

# Descer
print('\n\t\t\t -- Descendo -- ')
e1.descer(0)

# Exibir o Elevador de volta ao Térreo
print('\n\t\t\t -- Elevador de volta ao Térreo --')
print(e1)