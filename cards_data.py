# -*- coding: utf-8 -*-
"""
Listado MANUAL de todas las cartas del Santuario Arcano.

Esta es una lista plana y editable a mano: agrega, borra o modifica
entradas de CARDS libremente. No hay ninguna función que invente o
genere cartas automáticamente; todo lo que está aquí es literal.

Cada carta es un dict con:
  id         -> entero único (no lo repitas entre cartas)
  name       -> nombre que se muestra
  rarity     -> "comun" | "rara" | "epica" | "legendaria"
  categorias -> LISTA de textos libres (ej. ["Fuego", "Bestia"]).
                Una carta puede tener una o varias. Se muestran junto
                a la rareza, y se pueden usar para filtrar en Colección.
  image      -> nombre del archivo .png dentro de static/images/cards/
  flavor     -> breve descripción/lore. Se muestra en la carta y su ficha.

No hay campo de emoji/icono: si una carta todavía no tiene imagen, se
muestran automáticamente las iniciales de su nombre en su lugar.
"""

CARDS = [
    {
        "id": 1,
        "name": "Lotería de nombres (El autógrafo)",
        "rarity": "comun",
        "categorias": ["En equipo"],
        "image": "1.png",
        "flavor": "¡A ganar en el cachipún para conocer los hobbies de tus nuevos amigos!"
    },
    {
        "id": 2,
        "name": "Juego de aplausos",
        "rarity": "comun",
        "categorias": ["Coordinacion", "Reaccion"],
        "image": "2.png",
        "flavor": "Sigue al líder: si la mano sube, ¡aplaude o sisea sin dudar!"
    },
    {
        "id": 3,
        "name": "Toque y Fama",
        "rarity": "rara",
        "categorias": ["Coordinacion"],
        "image": "3.png",
        "flavor": "Descifra el código numérico antes de que tu rival descubra el tuyo."
    },
    {
        "id": 4,
        "name": "Bingo de la Lotería de nombres",
        "rarity": "comun",
        "categorias": ["En equipo"],
        "image": "4.png",
        "flavor": "El azar de la pizarra decidirá quién completa su cartón primero."
    },
    {
        "id": 5,
        "name": "Aplausos musicales",
        "rarity": "comun",
        "categorias": ["Coordinacion", "Reaccion"],
        "image": "5.png",
        "flavor": "¿Pan o Parapan? Mantén el ritmo y no te pierdas en el compás."
    },
    {
        "id": 6,
        "name": "1,2,3",
        "rarity": "comun",
        "categorias": ["Coordinacion", "Reaccion"],
        "image": "6.png",
        "flavor": "Cambia los números por gestos locos y pon a prueba tu memoria corporal."
    },
    {
        "id": 7,
        "name": "Juego del Cazador/Cachipún gigante",
        "rarity": "rara",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "7.png",
        "flavor": "Piedra, papel o tijera a escala masiva. ¡Coordina a todo tu batallón!"
    },
    {
        "id": 8,
        "name": "Juan José Bonilla",
        "rarity": "rara",
        "categorias": ["Coordinacion", "En equipo"],
        "image": "8.png",
        "flavor": "Canta el canon, levántate y agáchate sin perder la concentración."
    },
    {
        "id": 9,
        "name": "Cara y Sello",
        "rarity": "comun",
        "categorias": ["Reaccion", "Coordinacion"],
        "image": "9.png",
        "flavor": "Choca las palmas de frente o de espaldas a la velocidad de la luz."
    },
    {
        "id": 10,
        "name": "¿Cuántas ovejas bajan del cerro?",
        "rarity": "rara",
        "categorias": ["Reaccion"],
        "image": "10.png",
        "flavor": "Escucha bien la pregunta, porque los aplausos son solo un distractor."
    },
    {
        "id": 11,
        "name": "Pitipiti/Mickey Mouse",
        "rarity": "epica",
        "categorias": ["Coordinacion"],
        "image": "11.png",
        "flavor": "El truco no está en el canto, sino en imitar el último y sutil movimiento."
    },
    {
        "id": 12,
        "name": "¿Quién tiene la pelota?",
        "rarity": "rara",
        "categorias": ["Reaccion"],
        "image": "12.png",
        "flavor": "La pelota imaginaria vuela, pero solo el más atento sabrá quién la atrapó."
    },
    {
        "id": 13,
        "name": "3 puntos bajan",
        "rarity": "legendaria",
        "categorias": ["Coordinacion"],
        "image": "13.png",
        "flavor": "Todavía no descubrimos como funciona."
    },
    {
        "id": 14,
        "name": "Cachipún suma",
        "rarity": "rara",
        "categorias": ["Reaccion"],
        "image": "14.png",
        "flavor": "Saca tus dedos, calcula rápido y adivina la suma antes que tu pareja."
    },
    {
        "id": 15,
        "name": "Abecedario humano",
        "rarity": "epica",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "15.png",
        "flavor": "Usa tu cuerpo y el de tus amigos para moldear las letras de la victoria."
    },
    {
        "id": 16,
        "name": "Lazarillo",
        "rarity": "comun",
        "categorias": ["En equipo"],
        "image": "16.png",
        "flavor": "Cierra los ojos y confía ciegamente en la guía de tu compañero."
    },
    {
        "id": 17,
        "name": "Pinta Mitosis",
        "rarity": "rara",
        "categorias": ["En equipo", "Reaccion"],
        "image": "17.png",
        "flavor": "Un contagio imparable de parejas atrapando del brazo al resto del grupo."
    },
    {
        "id": 18,
        "name": "Remolino",
        "rarity": "comun",
        "categorias": ["Coordinacion"],
        "image": "18.png",
        "flavor": "Gira, concéntrate y mantén la atención en el torbellino del juego."
    },
    {
        "id": 19,
        "name": "Nunca de a Tres",
        "rarity": "rara",
        "categorias": ["Reaccion", "En equipo"],
        "image": "19.png",
        "flavor": "Muévete rápido y busca tu lugar, ¡porque tres son multitud!"
    },
    {
        "id": 20,
        "name": "Nudo Humano",
        "rarity": "epica",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "20.png",
        "flavor": "Enrédate las manos y trabaja en equipo para volver a formar un círculo limpio."
    },
    {
        "id": 21,
        "name": "Bitcoin",
        "rarity": "rara",
        "categorias": ["En equipo"],
        "image": "21.png",
        "flavor": "Invierte tu energía y muévete al ritmo de esta dinámica de valor."
    },
    {
        "id": 22,
        "name": "Pinta espejo",
        "rarity": "comun",
        "categorias": ["Coordinacion", "Reaccion"],
        "image": "22.png",
        "flavor": "Refleja los movimientos de tu perseguidor y escapa con estilo."
    },
    {
        "id": 23,
        "name": "Pinta inodoro",
        "rarity": "comun",
        "categorias": ["Reaccion"],
        "image": "23.png",
        "flavor": "¡Si te atrapan te congelas como un inodoro hasta que tiren la cadena!"
    },
    {
        "id": 24,
        "name": "Pinta selfie",
        "rarity": "comun",
        "categorias": ["Reaccion", "En equipo"],
        "image": "24.png",
        "flavor": "¡Sonríe a la cámara si te atrapan y espera el rescate de tu equipo!"
    },
    {
        "id": 25,
        "name": "Invasión",
        "rarity": "rara",
        "categorias": ["En equipo"],
        "image": "25.png",
        "flavor": "Conquista el territorio enemigo coordinando a todo tu escuadrón."
    },
    {
        "id": 26,
        "name": "Voltear la tortuga",
        "rarity": "epica",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "26.png",
        "flavor": "Fuerza, resistencia y maña para dar vuelta a tus compañeros en el suelo."
    },
    {
        "id": 27,
        "name": "Yo tengo un tren",
        "rarity": "comun",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "27.png",
        "flavor": "Súbete al vagón del ritmo y avanza junto a toda la sección cantando."
    },
    {
        "id": 28,
        "name": "Futbol scout",
        "rarity": "rara",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "28.png",
        "flavor": "Una divertida variante del fútbol tradicional con el espíritu de la naturaleza."
    },
    {
        "id": 29,
        "name": "Zorro gallina pollo",
        "rarity": "rara",
        "categorias": ["Reaccion", "En equipo"],
        "image": "29.png",
        "flavor": "Lidera a tus polluelos y reacciona rápido antes de que el zorro ataque."
    },
    {
        "id": 30,
        "name": "Pinta pelota",
        "rarity": "rara",
        "categorias": ["En equipo", "Reaccion"],
        "image": "30.png",
        "flavor": "Colabora con tu equipo para pintar a todos usando el balón veloz."
    },
    {
        "id": 31,
        "name": "Piratas del caribe",
        "rarity": "epica",
        "categorias": ["En equipo"],
        "image": "31.png",
        "flavor": "Navega con agilidad y diseña la mejor estrategia para saquear el tesoro."
    },
    {
        "id": 32,
        "name": "Cuerpo a tierra",
        "rarity": "rara",
        "categorias": ["Reaccion"],
        "image": "32.png",
        "flavor": "¡Agilidad y fuerza de brazos al instante cuando se da la orden!"
    },
    {
        "id": 33,
        "name": "Submarino",
        "rarity": "epica",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "33.png",
        "flavor": "Navegación a ciegas guiada puramente por la confianza y comunicación no verbal."
    },
    {
        "id": 34,
        "name": "10 pases",
        "rarity": "rara",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "34.png",
        "flavor": "Mantén el balón lejos del rival y encesta tras completar la serie perfecta."
    },
    {
        "id": 35,
        "name": "Cable Eléctrico",
        "rarity": "rara",
        "categorias": ["Reaccion", "En equipo"],
        "image": "35.png",
        "flavor": "Transmite el impulso por la fila y corre a atrapar el cono de la victoria."
    },
    {
        "id": 36,
        "name": "Postas: simple, arrastre y transporte",
        "rarity": "rara",
        "categorias": ["En equipo"],
        "image": "36.png",
        "flavor": "Velocidad pura y relevos llevando a tus compañeros a la meta final."
    },
    {
        "id": 37,
        "name": "Calles y avenidas: Calle, avenida, rotonda, pasaje",
        "rarity": "rara",
        "categorias": ["Coordinacion", "Reaccion"],
        "image": "37.png",
        "flavor": "Cambia tu orientación al instante y confunde a los corredores del laberinto."
    },
    {
        "id": 38,
        "name": "Gato y Ratón",
        "rarity": "epica",
        "categorias": ["Reaccion", "En equipo"],
        "image": "38.png",
        "flavor": "Escapa por los caminos cambiantes antes de que las garras del gato te alcancen."
    },
    {
        "id": 39,
        "name": "Aro Móvil",
        "rarity": "rara",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "39.png",
        "flavor": "Apunta al objetivo en movimiento para calentar motores con tu equipo."
    },
    {
        "id": 40,
        "name": "Airball",
        "rarity": "comun",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "40.png",
        "flavor": "Baloncesto cooperativo sin roce físico; pases limpios y perfectos en el aire."
    },
    {
        "id": 41,
        "name": "Protegiendo la corona del rey",
        "rarity": "epica",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "41.png",
        "flavor": "Forma un escudo humano y defiende la corona con agilidad y estrategia."
    },
    {
        "id": 42,
        "name": "El auto de mi jefe",
        "rarity": "comun",
        "categorias": ["Coordinacion"],
        "image": "42.png",
        "flavor": "Pon a prueba tu memoria y coordina tus gestos en este divertido viaje musical."
    },
    {
        "id": 43,
        "name": "Contando hasta 15",
        "rarity": "comun",
        "categorias": ["Coordinacion"],
        "image": "43.png",
        "flavor": "Sincronía perfecta y concentración matemática para llegar al número objetivo."
    },
    {
        "id": 44,
        "name": "Pacman",
        "rarity": "rara",
        "categorias": ["Reaccion", "En equipo"],
        "image": "44.png",
        "flavor": "Muévete solo por las líneas delimitadas y esquiva al Pacman del pañuelo."
    },
    {
        "id": 45,
        "name": "Netball",
        "rarity": "legendaria",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "45.png",
        "flavor": "Pases en tres áreas sin botar ni caminar. ¡Busca la cesta rival!"
    },
    {
        "id": 46,
        "name": "Cachipún alemán",
        "rarity": "epica",
        "categorias": ["En equipo", "Reaccion"],
        "image": "46.png",
        "flavor": "Una carrera frenética por la línea donde el cachipún decide quién avanza."
    },
    {
        "id": 47,
        "name": "Juego de canto 'Hay un hoyo en el fondo del mar'",
        "rarity": "comun",
        "categorias": ["Coordinacion"],
        "image": "47.png",
        "flavor": "Acumula palabras en tu memoria sin perder el ritmo ni la afinación."
    },
    {
        "id": 48,
        "name": "Frisbee",
        "rarity": "comun",
        "categorias": ["Coordinacion"],
        "image": "48.png",
        "flavor": "Domina el vuelo del disco y perfecciona tus lanzamientos de calentamiento."
    },
    {
        "id": 49,
        "name": "Ultimate",
        "rarity": "legendaria",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "49.png",
        "flavor": "Atrapa el disco en la zona de anotación sin contacto físico ni carreras con posesión."
    },
    {
        "id": 50,
        "name": "Memorice",
        "rarity": "rara",
        "categorias": ["En equipo", "Reaccion"],
        "image": "50.png",
        "flavor": "Corre en parejas, levanta las tarjetas del suelo y recuerda su ubicación exacta."
    },
    {
        "id": 51,
        "name": "Buscaminas",
        "rarity": "epica",
        "categorias": ["En equipo"],
        "image": "51.png",
        "flavor": "Adivina el camino cuadriculado y evita pisar las bombas ocultas del tablero."
    },
    {
        "id": 52,
        "name": "Sigue la huella",
        "rarity": "epica",
        "categorias": ["Coordinacion", "Reaccion"],
        "image": "52.png",
        "flavor": "Saltos precisos con los pies y palmas al suelo siguiendo el ritmo del tapete."
    },
    {
        "id": 53,
        "name": "Cuncuna (Tela)",
        "rarity": "rara",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "53.png",
        "flavor": "Haz rodar la gran tela circular en parejas y corre coordinado hacia la meta."
    },
    {
        "id": 54,
        "name": "Lanzamiento a ciegas",
        "rarity": "epica",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "54.png",
        "flavor": "Lanza con los ojos vendados y confía en que tu compañero atrape el balón."
    },
    {
        "id": 55,
        "name": "Aram sam sam",
        "rarity": "comun",
        "categorias": ["Coordinacion", "Reaccion"],
        "image": "55.png",
        "flavor": "Canta en círculo y asocia gestos rápidos con cada palabra de la canción."
    },
    {
        "id": 56,
        "name": "Kahoot",
        "rarity": "comun",
        "categorias": ["Reaccion"],
        "image": "56.png",
        "flavor": "El conocimiento es poder, ¡pero la velocidad de respuesta te dará el podio!"
    },
    {
        "id": 57,
        "name": "Salto de cuerda en grupo",
        "rarity": "epica",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "57.png",
        "flavor": "Cinco saltos perfectos de todo el equipo sin interrumpir el giro de la cuerda."
    },
    {
        "id": 58,
        "name": "Colpbol",
        "rarity": "legendaria",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "58.png",
        "flavor": "Toques de primera con las manos hacia la portería; máxima inclusión y pase obligatorio."
    },
    {
        "id": 59,
        "name": "Aplauso del Torero",
        "rarity": "comun",
        "categorias": ["Coordinacion"],
        "image": "59.png",
        "flavor": "Mímica y ritmo taurino para divertirse y romper el hielo en grupo."
    },
    {
        "id": 60,
        "name": "Nadie sabe para quien trabaja",
        "rarity": "comun",
        "categorias": ["Reaccion"],
        "image": "60.png",
        "flavor": "¡Aprovecha el esfuerzo ajeno en el último segundo del juego!"
    },
    {
        "id": 61,
        "name": "Quemadas",
        "rarity": "rara",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "61.png",
        "flavor": "Esquiva los pelotazos y quédate en el campo para eliminar a la escuadra rival."
    },
    {
        "id": 62,
        "name": "Naciones",
        "rarity": "epica",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "62.png",
        "flavor": "Elimina al rival, rescata a tus compañeros desde el fondo y vacía el campo."
    },
    {
        "id": 63,
        "name": "Dodgeball",
        "rarity": "epica",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "63.png",
        "flavor": "Corre por los balones al sonar el silbato y lanza con precisión milimétrica."
    },
    {
        "id": 64,
        "name": "Guerra de gladiadores",
        "rarity": "epica",
        "categorias": ["En equipo"],
        "image": "64.png",
        "flavor": "Un combate de equilibrio, agilidad y astucia para coronar al último gladiador."
    },
    {
        "id": 65,
        "name": "Virus",
        "rarity": "rara",
        "categorias": ["En equipo", "Reaccion"],
        "image": "65.png",
        "flavor": "Si te contagias, ¡espera a que cuatro compañeros simulen una ambulancia y te salven!"
    },
    {
        "id": 66,
        "name": "Pichón",
        "rarity": "rara",
        "categorias": ["Reaccion", "Predeportivo"],
        "image": "66.png",
        "flavor": "Cruza el pasillo central esquivando los balones de los costados para puntuar."
    },
    {
        "id": 67,
        "name": "Musaraña",
        "rarity": "rara",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "67.png",
        "flavor": "Interpreta las señas del director y corre a la fila para adivinar primero."
    },
    {
        "id": 68,
        "name": "Amitzy Chami Chami e le petit tivo tivo",
        "rarity": "comun",
        "categorias": ["Coordinacion", "En equipo"],
        "image": "68.png",
        "flavor": "Cruza los pies, salta y baja tus manos hasta los tobillos del compañero cantando."
    },
    {
        "id": 69,
        "name": "Paracaidas en equipo",
        "rarity": "epica",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "69.png",
        "flavor": "Lanza el balón al cielo usando la lona redonda y coordina la recepción perfecta."
    },
    {
        "id": 70,
        "name": "Bosque encantado",
        "rarity": "rara",
        "categorias": ["En equipo", "Reaccion"],
        "image": "70.png",
        "flavor": "Esquiva al hechicero o conviértete en un árbol congelado que atrapa con las manos."
    },
    {
        "id": 71,
        "name": "4 esquinas",
        "rarity": "rara",
        "categorias": ["En equipo", "Reaccion"],
        "image": "71.png",
        "flavor": "¡Corre a una esquina al sonar la señal y evita que tu equipo quede atrapado al medio!"
    },
    {
        "id": 72,
        "name": "Cosechando a ciegas",
        "rarity": "epica",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "72.png",
        "flavor": "Recoge las lentejas con los ojos vendados siguiendo los gritos de tu guía."
    },
    {
        "id": 73,
        "name": "Gato estrategia velocidad",
        "rarity": "rara",
        "categorias": ["En equipo", "Reaccion"],
        "image": "73.png",
        "flavor": "Piensa rápido y corre para alinear tus tres fichas antes que el oponente."
    },
    {
        "id": 74,
        "name": "Agrupa2 colaborativo comunicación no verbal",
        "rarity": "rara",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "74.png",
        "flavor": "Agrúpenase en silencio absoluto usando señas, miradas y sincronía."
    },
    {
        "id": 75,
        "name": "El ferrocarril reacción velocidad",
        "rarity": "comun",
        "categorias": ["Reaccion"],
        "image": "75.png",
        "flavor": "¡Engancha los vagones a toda marcha al escuchar la señal de partida!"
    },
    {
        "id": 76,
        "name": "Alibaba y los 40 coordinamos comunicación creatividad",
        "rarity": "rara",
        "categorias": ["Coordinacion"],
        "image": "76.png",
        "flavor": "Sigue la secuencia de movimientos corporales creativos sin perder el hilo."
    },
    {
        "id": 77,
        "name": "Rayuela de la zapatilla precisión",
        "rarity": "comun",
        "categorias": ["Coordinacion"],
        "image": "77.png",
        "flavor": "Calcula la distancia y lanza tu zapatilla buscando el tiro perfecto."
    },
    {
        "id": 78,
        "name": "El tiburón: sobrevivencia, Colaborativo",
        "rarity": "epica",
        "categorias": ["En equipo"],
        "image": "78.png",
        "flavor": "¡Sálvate en la plataforma flotante colaborando con tus compañeros antes del ataque!"
    },
    {
        "id": 79,
        "name": "Fútbol 4 esquinas",
        "rarity": "legendaria",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "79.png",
        "flavor": "Dos balones en juego y cuatro arcos donde anotar. ¡Ataca cualquier esquina menos la tuya!"
    },
    {
        "id": 80,
        "name": "Vuelta al universo",
        "rarity": "rara",
        "categorias": ["En equipo"],
        "image": "80.png",
        "flavor": "Una carrera cósmica de relevos a máxima velocidad alrededor del espacio."
    },
    {
        "id": 81,
        "name": "Nación gol",
        "rarity": "rara",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "81.png",
        "flavor": "Combina la estrategia del balón quemado con anotaciones directas al arco rival."
    },
    {
        "id": 82,
        "name": "Vuelta al mundo",
        "rarity": "epica",
        "categorias": ["En equipo", "Reaccion"],
        "image": "82.png",
        "flavor": "Patea lejos, pasa el balón bajo las piernas y corre alrededor de todo tu equipo."
    },
    {
        "id": 83,
        "name": "Bapne",
        "rarity": "rara",
        "categorias": ["Coordinacion"],
        "image": "83.png",
        "flavor": "Percusión corporal a cuatro tiempos para desafiar tu ritmo y concentración mental."
    },
    {
        "id": 84,
        "name": "Carrera de elefante",
        "rarity": "epica",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "84.png",
        "flavor": "Avanza en hilera con las manos entrelazadas entre las piernas sin soltarte."
    },
    {
        "id": 85,
        "name": "Gallina ponedora",
        "rarity": "epica",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "85.png",
        "flavor": "Salta con la pelota entre las piernas y encéstala con precisión en el nido."
    },
    {
        "id": 86,
        "name": "Zorba",
        "rarity": "epica",
        "categorias": ["En equipo", "Reaccion"],
        "image": "86.png",
        "flavor": "Escucha tu número, atrapa el pañuelo central y corre a tu base sin ser pintado."
    },
    {
        "id": 87,
        "name": "Artzikirol",
        "rarity": "legendaria",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "87.png",
        "flavor": "Fusión perfecta de fútbol y handball; da pases rápidos antes de que te alcancen."
    },
    {
        "id": 88,
        "name": "Bota cones",
        "rarity": "comun",
        "categorias": ["Predeportivo"],
        "image": "88.png",
        "flavor": "Apunta y derriba los conos del rival con lanzamientos manuales precisos."
    },
    {
        "id": 89,
        "name": "Derribar el ovni",
        "rarity": "rara",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "89.png",
        "flavor": "Apunta al platillo flotante central coordinando la puntería de tu escuadrón."
    },
    {
        "id": 90,
        "name": "Sky",
        "rarity": "rara",
        "categorias": ["Coordinacion"],
        "image": "90.png",
        "flavor": "Desplazamiento coordinado y pasos sincronizados para alcanzar la meta."
    },
    {
        "id": 91,
        "name": "Impulso electrico",
        "rarity": "comun",
        "categorias": ["Reaccion"],
        "image": "91.png",
        "flavor": "Siente la corriente invisible en tus manos y reacciona antes que el oponente."
    },
    {
        "id": 92,
        "name": "Tripela",
        "rarity": "legendaria",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "92.png",
        "flavor": "Un emocionante deporte alternativo que desafía tus pases con las manos y el juego con los pies."
    },
    {
        "id": 93,
        "name": "Aguilucho",
        "rarity": "rara",
        "categorias": ["Reaccion"],
        "image": "93.png",
        "flavor": "Vuela alto y esquiva los intentos de captura del oponente con reflejos rápidos."
    },
    {
        "id": 94,
        "name": "Torombolo",
        "rarity": "comun",
        "categorias": ["Reaccion"],
        "image": "94.png",
        "flavor": "Mantén el balón lejos de la persona al centro en este clásico círculo de pases."
    },
    {
        "id": 95,
        "name": "Kin ball",
        "rarity": "legendaria",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "95.png",
        "flavor": "Sostén y golpea la gigantesca pelota rosa en un reto de pura cooperación internacional."
    },
    {
        "id": 96,
        "name": "Paleta",
        "rarity": "comun",
        "categorias": ["Predeportivo", "Coordinacion"],
        "image": "96.png",
        "flavor": "Golpes certeros y control de la trayectoria con tu paleta de madera."
    },
    {
        "id": 97,
        "name": "Badminton",
        "rarity": "rara",
        "categorias": ["Predeportivo", "Coordinacion"],
        "image": "97.png",
        "flavor": "Lanza el volante sobre la red con toques suaves, reflejos y precisión."
    },
    {
        "id": 98,
        "name": "El cono",
        "rarity": "comun",
        "categorias": ["Reaccion"],
        "image": "98.png",
        "flavor": "Mantén la vista fija en el objetivo y reacciona al instante ante la señal del cono."
    },
    {
        "id": 99,
        "name": "Hermanos de gol",
        "rarity": "rara",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "99.png",
        "flavor": "Duplas coordinadas buscando romper la defensa para anotar un gol fraternal."
    },
    {
        "id": 100,
        "name": "Que no toque el suelo",
        "rarity": "rara",
        "categorias": ["Coordinacion", "En equipo"],
        "image": "100.png",
        "flavor": "Mantén el balón vivo en el aire usando cualquier parte permitida de tu cuerpo."
    },
    {
        "id": 101,
        "name": "Invasión total",
        "rarity": "epica",
        "categorias": ["En equipo"],
        "image": "101.png",
        "flavor": "Despliega a tu equipo por todo el territorio rival para una conquista absoluta."
    },
    {
        "id": 102,
        "name": "Etapas",
        "rarity": "epica",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "102.png",
        "flavor": "Supera las cuatro fases del circuito: pases por aro, a caballito, saltos y más."
    },
    {
        "id": 103,
        "name": "Pinfuvote",
        "rarity": "legendaria",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "103.png",
        "flavor": "Ping-pong, fútbol, voley y tenis en una sola cancha con puntuación según el golpe."
    },
    {
        "id": 104,
        "name": "Casa inquilino terremoto",
        "rarity": "rara",
        "categorias": ["Reaccion", "Coordinacion"],
        "image": "104.png",
        "flavor": "Forma casas con tus brazos o cámbiate de hogar cuando la tierra empiece a temblar."
    },
    {
        "id": 105,
        "name": "Colisión de planetas",
        "rarity": "epica",
        "categorias": ["En equipo", "Reaccion"],
        "image": "105.png",
        "flavor": "Lanza pelotas pequeñas para empujar el planeta gigante hacia la línea rival."
    },
    {
        "id": 106,
        "name": "Náufragos silenciosos",
        "rarity": "epica",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "106.png",
        "flavor": "Avanza sobre colchonetas en absoluto silencio para recuperar la lenteja dorada."
    },
    {
        "id": 107,
        "name": "Boom",
        "rarity": "rara",
        "categorias": ["Reaccion"],
        "image": "107.png",
        "flavor": "Choca las manos rápido o haz una sentadilla antes de que el tiempo explote."
    },
    {
        "id": 108,
        "name": "Cara y Sello (Educadoras)",
        "rarity": "comun",
        "categorias": ["Reaccion", "Coordinacion"],
        "image": "108.png",
        "flavor": "Una divertida adaptación del clásico reflejo de palmas de frente o de espalda."
    },
    {
        "id": 109,
        "name": "Abecedario (Educadoras)",
        "rarity": "comun",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "109.png",
        "flavor": "Forma figuras y letras corporales con el entusiasmo de la primera infancia."
    },
    {
        "id": 110,
        "name": "Traslado de la pelota (Educadoras)",
        "rarity": "rara",
        "categorias": ["Coordinacion", "En equipo"],
        "image": "110.png",
        "flavor": "Lleva el balón a salvo compartiendo el esfuerzo y balance con tu equipo."
    },
    {
        "id": 111,
        "name": "Pirámide (Educadoras)",
        "rarity": "epica",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "111.png",
        "flavor": "Equilibrio, balance y confianza grupal para edificar la estructura humana más alta."
    },
    {
        "id": 112,
        "name": "Palitos chinos (Educadoras)",
        "rarity": "rara",
        "categorias": ["Coordinacion"],
        "image": "112.png",
        "flavor": "Pulsos firmes y precisión quirúrgica para retirar varillas sin mover el resto."
    },
    {
        "id": 113,
        "name": "Jaula (Educadoras)",
        "rarity": "rara",
        "categorias": ["En equipo"],
        "image": "113.png",
        "flavor": "Mantén el control dentro del perímetro sin dejar escapar los objetivos asignados."
    },
    {
        "id": 114,
        "name": "Bebelinda (Educadoras)",
        "rarity": "comun",
        "categorias": ["Coordinacion"],
        "image": "114.png",
        "flavor": "Canta el ritmo de Camalundi acelerando la velocidad y los gestos progresivamente."
    },
    {
        "id": 115,
        "name": "Roba colores",
        "rarity": "rara",
        "categorias": ["En equipo", "Reaccion"],
        "image": "115.png",
        "flavor": "Asalta las bases enemigas para recolectar las fichas del color indicado a tiempo."
    },
    {
        "id": 116,
        "name": "TOMBO",
        "rarity": "epica",
        "categorias": ["En equipo", "Reaccion"],
        "image": "116.png",
        "flavor": "Lanza, corre por los aros bases y detente de golpe cuando el tombador grite ¡TOMBO!"
    },
    {
        "id": 117,
        "name": "Fuego cruzado",
        "rarity": "epica",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "117.png",
        "flavor": "Esquiva la gigantesca kin-ball, traslada las bombas y despeja tu zona."
    },
    {
        "id": 118,
        "name": "BasXball",
        "rarity": "legendaria",
        "categorias": ["Predeportivo"],
        "image": "118.png",
        "flavor": "Variante X del baloncesto, no apta para cardiacos."
    },
    {
        "id": 119,
        "name": "Circulo mortal",
        "rarity": "epica",
        "categorias": ["En equipo", "Reaccion"],
        "image": "119.png",
        "flavor": "Quédate inmóvil cuando el quemador entre al ula-ula o esquiva el tiro definitivo."
    },
    {
        "id": 120,
        "name": "Cono alemán",
        "rarity": "epica",
        "categorias": ["Reaccion", "Coordinacion"],
        "image": "120.png",
        "flavor": "Sigue las órdenes corporales y lánzate por el cono central a máxima velocidad."
    },
    {
        "id": 121,
        "name": "Torre de Babel",
        "rarity": "legendaria",
        "categorias": ["Reaccion", "En equipo"],
        "image": "121.png",
        "flavor": "Grita tu palabra al centro de la cancha y encuentra a tu gemelo de tarjeta."
    },
    {
        "id": 122,
        "name": "Cuncuna",
        "rarity": "rara",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "122.png",
        "flavor": "Tómense de los tobillos sentados en el suelo y avancen en una sincronía perfecta de ida y vuelta."
    },
    {
        "id": 123,
        "name": "Conquista",
        "rarity": "epica",
        "categorias": ["En equipo", "Reaccion"],
        "image": "123.png",
        "flavor": "Roba el cono enemigo despojando al guardián de su peto trasero con sigilo y velocidad."
    },
    {
        "id": 124,
        "name": "Pivote-Up!",
        "rarity": "rara",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "124.png",
        "flavor": "Botea estilo básquet y asiste al pivote del aro para un manotazo letal directo al arco."
    },
    {
        "id": 125,
        "name": "Asedio al castillo",
        "rarity": "epica",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "125.png",
        "flavor": "Pivotea sin correr con la pelota y lanza desde fuera del área de protección para derribar la torre de conos."
    },
    {
        "id": 126,
        "name": "Tapitas",
        "rarity": "epica",
        "categorias": ["En equipo", "Reaccion"],
        "image": "126.png",
        "flavor": "Derriba las tapas, escapa de los cazadores y reconstruye la torre completa a escondidas."
    },
    {
        "id": 127,
        "name": "Serpientes",
        "rarity": "rara",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "127.png",
        "flavor": "Crece sujetando los hombros de tus capturas usando el tallarín flotador con toques suaves."
    },
    {
        "id": 128,
        "name": "Rescate Numerico",
        "rarity": "rara",
        "categorias": ["Reaccion", "En equipo"],
        "image": "128.png",
        "flavor": "Escucha tu número, corre veloz al círculo central y lleva la tarjeta de puntaje a tu base."
    },
    {
        "id": 129,
        "name": "Policias y Ladrones",
        "rarity": "epica",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "129.png",
        "flavor": "Completa tres pases obligatorios antes de asegurar el botín de pelotas en la zona segura."
    },
    {
        "id": 130,
        "name": "Penales borrachos",
        "rarity": "epica",
        "categorias": ["Coordinacion"],
        "image": "130.png",
        "flavor": "Ideal para jugarlo en el tercer tiempo."
    },
    {
        "id": 131,
        "name": "LADRONES DE CINTAS",
        "rarity": "epica",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "131.png",
        "flavor": "Pases hacia atrás estilo rugby mientras proteges tu cinta trasera de las manos enemigas."
    },
    {
        "id": 132,
        "name": "El hombre azul",
        "rarity": "rara",
        "categorias": ["Reaccion"],
        "image": "132.png",
        "flavor": "Cruza la línea central antes de que el hombre azul te toque y te sume a sus filas congeladas."
    },
    {
        "id": 133,
        "name": "Cazadores de zonas",
        "rarity": "epica",
        "categorias": ["Predeportivo", "Coordinacion"],
        "image": "133.png",
        "flavor": "Lanza y atrapa el Frisbee limpiamente en el aire sobre las zonas de mayor puntaje."
    },
    {
        "id": 134,
        "name": "Cazadores de colores",
        "rarity": "rara",
        "categorias": ["Reaccion", "En equipo"],
        "image": "134.png",
        "flavor": "Persigue a tu color objetivo y rescata a tus aliados congelados con un doble high five en salto."
    },
    {
        "id": 135,
        "name": "CAMPO MINADO",
        "rarity": "epica",
        "categorias": ["En equipo", "Coordinacion"],
        "image": "135.png",
        "flavor": "Cruza el terreno a ciegas tras dar tres vueltas, guiado puramente por las voces de tu equipo."
    },
    {
        "id": 136,
        "name": "Bola tóxica",
        "rarity": "epica",
        "categorias": ["Reaccion"],
        "image": "136.png",
        "flavor": "Recupera las lentejas del verdugo, mientras esquivas su bola tóxica."
    },
    {
        "id": 137,
        "name": "ARAÑA EN LA TELARAÑA",
        "rarity": "rara",
        "categorias": ["Reaccion", "En equipo"],
        "image": "137.png",
        "flavor": "Cruza la franja central de la cancha esquivando los tallarines de natación de las arañas hambrientas."
    },
    {
        "id": 138,
        "name": "\"25\"",
        "rarity": "legendaria",
        "categorias": ["Predeportivo", "En equipo"],
        "image": "138.png",
        "flavor": "Goles espectaculares de cabeza, taquito o chilena a un solo arquero para acumular 25 puntos."
    },
    {
        "id": 139,
        "name": "Pollitos de colores",
        "rarity": "epica",
        "categorias": ["En equipo", "Reaccion"],
        "image": "139.png",
        "flavor": "Roba los huevos del centro esquivando el giro implacable de la garra del halcón guardián."
    }
]

# --- No edites debajo de esta línea: son solo utilidades de búsqueda ---

RARITY_ORDER = ["comun", "rara", "epica", "legendaria"]

RARITY_LABELS = {
    "comun": "Común",
    "rara": "Rara",
    "epica": "Épica",
    "legendaria": "Legendaria",
}

# Pesos de aparición por rareza dentro de un sobre (deben sumar 1.0)
RARITY_WEIGHTS = {
    "comun": 0.58,
    "rara": 0.28,
    "epica": 0.11,
    "legendaria": 0.03,
}

CARDS_BY_ID = {c["id"]: c for c in CARDS}
CARDS_BY_RARITY = {r: [c for c in CARDS if c["rarity"] == r] for r in RARITY_ORDER}
TOTAL_CARDS = len(CARDS)

# Todas las categorías usadas, en orden alfabético (para armar filtros, etc.)
ALL_CATEGORIES = sorted({cat for c in CARDS for cat in c["categorias"]})
