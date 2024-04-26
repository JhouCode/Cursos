from random import randint

lista_npcs = []


def criar_npc():
    level = randint(0, 50)
    
    novo_npc = {
        
        'nome': f"Monstro #{level}",
        'level': level,
        'dano': 5 * level,
        'hp': 100 * level,
    }
   

    lista_npcs.append(novo_npc)

def gerar_npc (n_npcs):

    for x in range(n_npcs)