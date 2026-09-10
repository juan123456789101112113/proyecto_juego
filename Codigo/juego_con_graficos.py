import random as r

# ---------------------------------------------------------------
# Arte ASCII del juego
# ---------------------------------------------------------------

BANNER = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║              EL  PACTO  DE  LAS  TRES  PUERTAS               ║
║                                                              ║
║                            Umbra                             ║
╚══════════════════════════════════════════════════════════════╝
          ┌───────┐        ┌───────┐        ┌───────┐
          │ ╭───╮ │        │ ╭───╮ │        │ ╭───╮ │
          │ │   │ │        │ │   │ │        │ │   │ │
          │ │ ● │ │        │ │ ● │ │        │ │ ● │ │
          │ ╰───╯ │        │ ╰───╯ │        │ ╰───╯ │
          └───────┘        └───────┘        └───────┘
           PUERTA I        PUERTA II        PUERTA III
"""

ARTE_BANE = """
                        ▄▄▄▄▄▄▄▄▄▄▄
                     ▄█▀           ▀█▄
                    █▌   ▄▄     ▄▄   ▐█
                    █▌  ▐██▌   ▐██▌  ▐█
                    █▌   ▀▀     ▀▀   ▐█
                     █▄  ╱▔▔▔▔▔╲  ▄█
                      ▀█▄ ║║║║║ ▄█▀
                        ▀▀▀▀▀▀▀▀▀
                      ┃┃┃┃┃┃┃┃┃┃┃┃┃
"""

ARTE_AZAZEL = """
              ╲╲╲                       ╱╱╱
            ╲╲  ╲╲╲                 ╱╱╱  ╱╱
              ╲╲╲  ╲╲╲    ▄▄▄    ╱╱╱  ╱╱╱
                 ╲╲╲   ▄█▀   ▀█▄   ╱╱╱
                      █▌ ◣   ◢ ▐█
                      █▌   ▼   ▐█
                       █▄ ═══ ▄█
                        ▀█▄▄▄█▀
                     ░░░ ▀▀▀▀▀ ░░░
"""

ARTE_MEPHISTO = """
                  ╲╲                     ╱╱
                   ╲╲╲                 ╱╱╱
                    ╲╲╲▄▄▄▄▄▄▄▄▄▄▄▄▄╱╱╱
                     ▄█▀           ▀█▄
                    █▌  ◤◥       ◤◥  ▐█
                    █▌   ●       ●   ▐█
                    █▌    ╲_____╱    ▐█
                     ▀█▄  ╱╲╱╲╱╲╱╲  ▄█▀
                       ▀▀▀▀▀▀▀▀▀▀▀▀▀
"""

ARTE_VICTORIA = """
              ╔════════════════════════════════╗
              ║   L A   S U P E R F I C I E    ║
              ╚════════════════════════════════╝
                   ░░░░░░░░░░░░░░░░░░░░░
                  ░░  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ░░
                 ░░  █               █  ░░
                 ░░  █    ABIERTA    █  ░░
                 ░░  █               █  ░░
                  ░░ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ░░
"""

ARTE_DERROTA = """
              ╔════════════════════════════════╗
              ║  D E U D A   P E N D I E N T E ║
              ╚════════════════════════════════╝
                        ▄▄▄▄▄▄▄▄▄▄▄
                     ▄█▀▀         ▀▀█▄
                    █▌   ✕       ✕   ▐█
                    █▌               ▐█
                     ▀█▄▄  ▄▄▄▄▄  ▄▄█▀
                        ▀▀▀▀▀▀▀▀▀▀▀
"""




def barra (actual, maximo, ancho):
  # Devuelve una barra de progreso en texto, por ejemplo [████░░░░]
  if actual < 0:
    actual = 0
  llenos = int((actual / maximo) * ancho)
  return "[" + "█" * llenos + "░" * (ancho - llenos) + "]"


def mostrar_estado (persona, enemigo):
  # Panel con las barras de vida y voluntad de los dos combatientes
  print("  ┌─────────────────────────────────────────────────┐")
  print(f"  │ TU     VIDA     {barra(persona['vida'], persona['vida_max'], 20)} {int(persona['vida']):>4}/{persona['vida_max']:<4}│")
  print(f"  │        VOLUNTAD {barra(persona['energia'], persona['energia_max'], 20)} {int(persona['energia']):>4}/{persona['energia_max']:<4}│")
  print("  ├─────────────────────────────────────────────────┤")
  print(f"  │ {enemigo['nombre'].upper():<8} VIDA   {barra(enemigo['vida'], enemigo['vida_max'], 20)} {int(enemigo['vida']):>4}/{enemigo['vida_max']:<4}│")
  print("  └─────────────────────────────────────────────────┘")


def ataque_personaje (ataques):
  if persona['energia'] < ataques['costo_energia']:
      print(f"No te queda voluntad suficiente para invocar {ataques['nombre']}.")
      return False
  daño = r.randint(ataques['daño_min'], ataques['daño_max'])
  if daño == ataques['daño_max']:
    print("El filo alcanza su límite y se desborda. ¡Golpe crítico!")
    daño = daño * 0.5 + daño
    enemigo['vida'] -= daño
    if enemigo['vida'] < 0:
      enemigo['vida'] = 0
    persona['energia'] -= ataques['costo_energia']
  else:
    enemigo['vida'] -= daño
    if enemigo['vida'] < 0:
      enemigo['vida'] = 0
    persona['energia'] -= ataques['costo_energia']

  print(f"Invocas {ataques['nombre']}: {daño} de daño")
  print(f"{ataques['relato']}")
  print(f"Te queda {persona['energia']} de voluntad")
  print(f"A {enemigo['nombre']} le quedan {enemigo['vida']} latidos")
  return True


def vida (persona):
  if persona['vida'] >= persona['vida_max']:
      print("La vida prestada no crece más allá de lo pactado.")
      return False

  persona['vida'] += 50
  if persona['vida'] > persona['vida_max']:
      persona['vida'] = persona['vida_max']

  print("Recompones 50 latidos de vida prestada.")
  print(f"Tu vida actual es de {persona['vida']} latidos")
  return True


def comportamiento_villanos (villanos):
  golpe = r.randint(1, 4)
  if golpe == 1:
    golpe_villano = r.randint(villanos['daño_min'], villanos['daño_max'])
    print(f"{villanos['nombre']} descarga un golpe: {golpe_villano} de daño")
    return golpe_villano
  elif golpe == 2:
    golpe_villano = r.randint(villanos['daño_min'], villanos['daño_max'])
    golpe_villano = golpe_villano * 0.5 + golpe_villano
    print(f"¡{villanos['nombre']} ataca con todo! {golpe_villano} de daño")
    return golpe_villano
  elif golpe == 3:
    golpe_villano = r.randint(villanos['daño_min'], villanos['daño_max'])
    print(f"{villanos['nombre']} descarga un golpe: {golpe_villano} de daño")
    return golpe_villano
  else:
    print(villanos['resiste'])
    print(f"Le quedan {villanos['vida']} latidos")
    return 0


Bane = {
    "nombre": "Bane",
    "titulo": "el Quebrantador",
    "entrada": "Bane, el Quebrantador, bloquea la Primera Puerta.\nFue el primer mortal en firmar. Ya no queda nada humano bajo la máscara.",
    "resiste": "Bane se resiste a tu ataque.",
    "caida": "La Primera Puerta se abre. Lo que hay detrás no es una salida.",
    "arte": ARTE_BANE,
    "vida": 200,
    "vida_max": 200,
    "daño_min": 10,
    "daño_max": 30
}

Azazel = {
    "nombre": "Azazel",
    "titulo": "señor de la ceniza",
    "entrada": "Azazel, señor de la ceniza, extiende lo que le queda de alas.\nSe le encargó cargar las culpas ajenas. Volvió del desierto sin ganas de devolver nada.",
    "resiste": "Azazel se cubre con las alas quemadas y no ataca.",
    "caida": "La Segunda Puerta cede. Desde aquí ya se intuye la superficie.",
    "arte": ARTE_AZAZEL,
    "vida": 300,
    "vida_max": 300,
    "daño_min": 40,
    "daño_max": 60
}

Mephisto = {
    "nombre": "Mephisto",
    "titulo": "eco del abismo",
    "entrada": "Mephisto no guarda la Tercera Puerta.\nMephisto ES la Tercera Puerta. Y sonríe al reconocer sus propias armas.",
    "resiste": "Mephisto se aparta sin prisa. Sabe que tiene toda una eternidad.",
    "caida": "Mephisto cae. La Tercera Puerta se abre y se ve la superficie.",
    "arte": ARTE_MEPHISTO,
    "vida": 400,
    "vida_max": 400,
    "daño_min": 70,
    "daño_max": 90
}

persona = {
    "vida": 500,
    "vida_max": 500,
    "energia": 500,
    "energia_max": 500
}

ataque1 = {
    "nombre": "Corte Fantasma",
    "relato": "Es el recuerdo de la herida que lo mató. Lo único que sigue siendo suyo.",
    "daño_min": 10,
    "daño_max": 30,
    "costo_energia": 30
}

ataque2 = {
    "nombre": "Furia Arcana",
    "relato": "Por un instante son miles de voces: los que firmaron antes que tú y no llegaron.",
    "daño_min": 40,
    "daño_max": 60,
    "costo_energia": 50
}

ataque3 = {
    "nombre": "Cataclismo Oscuro",
    "relato": "El abismo se desborda por tus manos, sin control.",
    "daño_min": 70,
    "daño_max": 100,
    "costo_energia": 100
}


ataques = [ataque1, ataque2, ataque3]

villanos = [Bane, Azazel, Mephisto]


while True:
  print(BANNER)
  print("Moriste con una deuda sin saldar, y en el fondo del Abismo alguien")
  print("te ofreció un trato. Aceptaste. Lo primero que entregaste fue tu nombre.")
  print("Despiertas con 500 latidos de vida prestada y 500 de voluntad.")
  print("Tres puertas te separan de la superficie. Alguien las guarda.")
  print()

  derrota = False

  for vida_villano in villanos:
    vida_villano['vida'] = vida_villano['vida_max']

  persona['vida'] = persona['vida_max']
  persona['energia'] = persona['energia_max']

  for enemigo in villanos:
    print("\n" + "-" * 70)
    print(enemigo['arte'])
    print(enemigo['entrada'])
    print(f"{enemigo['nombre']} · {enemigo['titulo']} · {enemigo['vida']} latidos")
    print("-" * 70)

    while persona['vida'] > 0 and enemigo['vida'] > 0:

      cubierto = False

      persona['energia'] += 40
      if persona['energia'] > persona['energia_max']:
        persona['energia'] = persona['energia_max']

      print("")
      mostrar_estado(persona, enemigo)

      print("\n¿Qué quieres hacer?")
      print("1. Invocar un arma")
      print("2. Recomponerte")
      print("3. Ponerte en guardia")

      try:
        opcion = int(input("Ingrese una opción: "))
      except:
        print("Ingrese una opción válida")
        continue

      if opcion == 1:
          print("1. Corte Fantasma      (30 de voluntad)")
          print("2. Furia Arcana        (50 de voluntad)")
          print("3. Cataclismo Oscuro  (100 de voluntad)")

          try:
            ataque = int(input("Ingrese el ataque que desea usar: "))
          except:
            print("Ingrese una opción válida")
            continue

          if ataque == 1:
            se_ataco = ataque_personaje(ataque1)
          elif ataque == 2:
            se_ataco = ataque_personaje(ataque2)
          elif ataque == 3:
            se_ataco = ataque_personaje(ataque3)
          else :
            print("Ingrese una opción válida")
            continue
          if se_ataco == False:
            continue

      elif opcion == 2:
          se_curo = vida(persona)
          if se_curo == False:
            continue
      elif opcion == 3:
          print("Te pones en guardia. Es un gesto viejo, anterior al pacto.")
          print("Lo poco que el Abismo no controla.")
          cubierto = True
      else:
          print("Ingrese una opción válida")
          continue

      if enemigo['vida'] > 0:
        daño_recibido = comportamiento_villanos(enemigo)

        if cubierto:
          daño_recibido -= 50

          if daño_recibido < 0:
            daño_recibido = 0

          print(f"Tu guardia absorbe parte del golpe: recibes {daño_recibido}")

        persona['vida'] -= daño_recibido
        if persona['vida'] < 0:
          persona['vida'] = 0
        print(f"Te quedan {persona['vida']} latidos")

    if persona['vida'] <= 0:
        print(ARTE_DERROTA)
        print("La deuda queda sin saldar.")
        print("El Abismo cobra lo que le corresponde. FIN DEL JUEGO.")
        derrota = True
        break
    else:
        print("\n" + enemigo['caida'])

  if derrota:
      while True:
        continuar = input("¿Vuelves a bajar? s/n ").lower()
      if continuar == "s" or continuar == "n":
        break
      print("Responda s o n")

      if continuar == "n":
        print("\nDices que no.")
        print("Nadie sabe qué pasa cuando alguien dice que no. Nunca había ocurrido.")
        break

  if enemigo['vida'] <= 0:
    print(ARTE_VICTORIA)
    print("Cruzas la Tercera Puerta y ves la superficie.")
    print("Ves, también, que las puertas se cierran otra vez a tu espalda.")
    print()
    print("Derrotar a Mephisto con las armas de Mephisto no rompe el pacto.")
    print("Lo renueva.")
    print("=" * 70)

    while True:
      continuar = input("¿Vuelves a bajar? s/n ").lower()
      if continuar == "s" or continuar == "n":
        break
      print("Responda s o n")

    if continuar == "n":
      print("\nDices que no.")
      print("Nadie sabe qué pasa cuando alguien dice que no. Nunca había ocurrido.")
      break