# -*- coding: utf-8 -*-
"""
Definición estática de los logros. Cada logro otorga sobres extra al ser
reclamado una vez cumplida su condición.

condition types:
  - open_packs        -> total de sobres abiertos >= value
  - unique_total      -> cartas distintas en la colección >= value
  - unique_rarity     -> cartas distintas de una rareza dada >= value (usa "rarity")
  - dupes_total       -> total de cartas obtenidas (contando repetidas) >= value
"""

ACHIEVEMENTS = [
    {
        "id": "first_pack",
        "name": "El Primer Sello Roto",
        "description": "Abre tu primer sobre.",
        "condition": "open_packs",
        "value": 1,
        "reward": 1,
    },
    {
        "id": "novice_collector",
        "name": "Aprendiz del Archivo",
        "description": "Consigue 10 cartas distintas.",
        "condition": "unique_total",
        "value": 10,
        "reward": 1,
    },
    {
        "id": "dedicated_collector",
        "name": "Guardián del Catálogo",
        "description": "Consigue 25 cartas distintas.",
        "condition": "unique_total",
        "value": 25,
        "reward": 2,
    },
    {
        "id": "expert_collector",
        "name": "Curador del Santuario",
        "description": "Consigue 45 cartas distintas.",
        "condition": "unique_total",
        "value": 45,
        "reward": 3,
    },
    {
        "id": "full_archive",
        "name": "El Archivo Completo",
        "description": "Completa el 100% de la colección.",
        "condition": "unique_total",
        "value": 72,
        "reward": 5,
    },
    {
        "id": "rare_hunter",
        "name": "Cazador de Rarezas",
        "description": "Consigue 10 cartas raras distintas.",
        "condition": "unique_rarity",
        "rarity": "rara",
        "value": 10,
        "reward": 2,
    },
    {
        "id": "epic_seeker",
        "name": "Buscador de lo Épico",
        "description": "Consigue 7 cartas épicas distintas.",
        "condition": "unique_rarity",
        "rarity": "epica",
        "value": 7,
        "reward": 2,
    },
    {
        "id": "legend_touch",
        "name": "Toque de Leyenda",
        "description": "Consigue tu primera carta legendaria.",
        "condition": "unique_rarity",
        "rarity": "legendaria",
        "value": 1,
        "reward": 3,
    },
    {
        "id": "favored_few",
        "name": "Favorito de los Antiguos",
        "description": "Consigue 4 cartas legendarias distintas.",
        "condition": "unique_rarity",
        "rarity": "legendaria",
        "value": 4,
        "reward": 4,
    },
    {
        "id": "all_legends",
        "name": "Panteón Completo",
        "description": "Consigue las 8 cartas legendarias.",
        "condition": "unique_rarity",
        "rarity": "legendaria",
        "value": 8,
        "reward": 5,
    },
    {
        "id": "steady_opener",
        "name": "Visitante Constante",
        "description": "Abre 10 sobres en total.",
        "condition": "open_packs",
        "value": 10,
        "reward": 1,
    },
    {
        "id": "veteran_opener",
        "name": "Veterano del Santuario",
        "description": "Abre 30 sobres en total.",
        "condition": "open_packs",
        "value": 30,
        "reward": 2,
    },
    {
        "id": "master_opener",
        "name": "Maestro del Santuario",
        "description": "Abre 60 sobres en total.",
        "condition": "open_packs",
        "value": 60,
        "reward": 3,
    },
    {
        "id": "hoarder",
        "name": "Acumulador Incansable",
        "description": "Reúne 100 cartas en total (cuentan las repetidas).",
        "condition": "dupes_total",
        "value": 100,
        "reward": 2,
    },
]

ACHIEVEMENTS_BY_ID = {a["id"]: a for a in ACHIEVEMENTS}
