import random as r

persona = {"vida":200,
           "vida_max":200,
           "energia":500,
           "energia_max":500
}

villano = {"vida":200,
           "vida_max":200
}

ataque1 = {"nombre":"corte_fantasma",
           "daño_min":10,
           "daño_max":30,
           "costo_energia":30
}

ataque2 = {"nombre":"Furia Arcana",
           "daño_min":40,
           "daño_max":60,
           "costo_energia":50
}

ataque3 = {"nombre":"Cataclismo Oscuro",
           "daño_min":70,
           "daño_max":100,
           "costo_energia":100
}

ataques = [ataque1, ataque2, ataque3]

def calculo1 (ataques):
  daño = r.randint(ataques['daño_min'], ataques['daño_max'])
  if daño == ataques['daño_max']:
    print("¡Golpe Crítico!")
    daño = daño * 2
    villano['vida'] -= daño
    persona['energia'] -= ataques['costo_energia']