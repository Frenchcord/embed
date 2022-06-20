from random import randint
class colors:
  default: int = 0
  teal: int = 0x1abc9c
  dark_teal: int = 0x11806a
  green: int = 0x2ecc71
  dark_green: int = 0x1f8b4c
  blue: int = 0x3498db
  dark_blue: int = 0x206694
  purple: int = 0x9b59b6
  dark_purple: int = 0x71368a
  magenta: int = 0xe91e63
  dark_magenta: int = 0xad1457
  gold: int = 0xf1c40f
  dark_gold: int = 0xc27c0e
  orange: int = 0xe67e22
  dark_orange: int = 0xa84300
  red: int = 0xe74c3c
  dark_red: int = 0x992d22
  lighter_grey: int = 0x95a5a6
  dark_grey: int = 0x607d8b
  light_grey: int = 0x979c9f
  darker_grey: int = 0x546e7a
  blurple: int = 0x7289da
  greyple: int = 0x99aab5
class couleurs:
  defaut: int = 0
  teal: int = 0x1abc9c
  dark_teal: int = 0x11806a
  vert: int = 0x2ecc71
  dark_vert: int = 0x1f8b4c
  bleue: int = 0x3498db
  dark_bleue: int = 0x206694
  mauve: int = 0x9b59b6
  dark_mauve: int = 0x71368a
  rose: int = 0xe91e63
  dark_rose: int = 0xad1457
  gold: int = 0xf1c40f
  dark_gold: int = 0xc27c0e
  orange: int = 0xe67e22
  dark_orange: int = 0xa84300
  rouge: int = 0xe74c3c
  dark_rouge: int = 0x992d22
  lighter_gris: int = 0x95a5a6
  dark_gris: int = 0x607d8b
  clair_gris: int = 0x979c9f
  darker_gris: int = 0x546e7a
  blurple: int = 0x7289da
  greyple: int = 0x99aab5
colorlist: list = [
  0x99aab5,
  0x7289da,
  0x546e7a,
  0x979c9f,
  0x607d8b,
  0x95a5a6,
  0x992d22,
  0xe74c3c,
  0xa84300,
  0xe67e22,
  0xc27c0e,
  0xf1c40f,
  0xad1457,
  0xe91e63,
  0x71368a,
  0x9b59b6,
  0x206694,
  0x3498db,
  0x1f8b4c,
  0x2ecc71,
  0x11806a,
  0x1abc9c,
  0
]
def color_random():
  return colorlist[randint(0, len(colorlist))]

def color_valide(couleur: int):
  return couleur in colorlist

def random_liste(len_list: int):
  listee: list = []
  max: int = len(colorlist)
  for i in range(len_list): listee.append(colorlist[randint(0, max)])
  return listee
