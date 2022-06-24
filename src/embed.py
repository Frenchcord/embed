from colorama import Fore
from .color import colorlist
class Embed:
  def __init__(self, titre: str = None, description: str = None, couleur = None):
    self.json: dict = {}
    if titre is not None: self.json['title']: str = titre
    if description is not None: self.json['description']: str = description
    if couleur is not None: 
      if couleur not in colorlist: raise ValueError(f'{couleur} est une couleure invalide voici une liste de couleurs valides.' + '\n'.join(colorlist))
      self.json['color'] = couleur

  def set_titre(self, titre: str):
    self.json['title']: str = titre

  def set_title(self, title: str):
    self.json['title']: str = title

  def set_description(self, description: str):
    self.json['description']: str = description

  def set_couleur(self, couleur):
    if couleur not in colorlist: raise ValueError(f'{couleur} est une couleure invalide voici une liste de couleurs valides.' + '\n'.join(colorlist))
    self.json['color'] = couleur

  def set_color(self, color):
    self.json['color'] = color

  def set_image(self, url: str = None, *, proxy_url: str = None, height: int = None, width: int = None):
    if url is None and proxy_url is None and height is None and width is None: return UselessCode()
    if 'image' not in self.json: self.json['image']: dict = {}
    if url is not None: self.json['image']['url']: str = url
    if proxy_url is not None: self.json['image']['proxy_url']: str = proxy_url
    if height is not None: self.json['image']['height']: int = height
    if width is not None: self.json['image']['width']: int = width

  def set_video(self, url: str = None, *, proxy_url: str = None, height: int = None, width: int = None):
    if url is None and proxy_url is None and height is None and width is None: return UselessCode()
    if 'video' not in self.json: self.json['video']: dict = {}
    if url is not None: self.json['video']['url']: str = url
    if proxy_url is not None: self.json['video']['proxy_url']: str = proxy_url
    if height is not None: self.json['video']['height']: int = height
    if width is not None: self.json['video']['width']: int = width

  def set_auteur(self, nom: str = None, url: str = None, icon_url: str = None, *, proxy_url: str = None):
    if url is None and proxy_url is None and url is None and icon_url is None: return UselessCode()
    if 'author' not in self.json: self.json['author']: dict = {}
    if nom is not None: self.json['author']['nom']: str = nom
    if url is not None: self.json['author']['url']: str = url
    if icon_url is not None: self.json['author']['icon_url']: str = icon_url
    if proxy_url is not None: self.json['author']['proxy_url']: str = proxy_url

  def set_thumbnail(self, url: str = None, proxy_url: str = None, height: int = None, width: int = None):
    if 'thumbnail' not in self.json: self.json['thumbnail']: dict = {}
    if url is None and proxy_url is None and height is None and width is None: return UselessCode()
    if url is not None: self.json['thumbnail']['url']: str = url
    if proxy_url is not None: self.json['thumbnail']['proxy_url']: str = proxy_url
    if height is not None: self.json['thumbnail']['height']: int = height
    if width is not None: self.json['thumbnail']['width']: int = width

  def set_footer(self, text: str = None, *, icon_url: str = None, proxy_url: str = None):
    if 'footer' not in self.json: self.json['footer']: dict = {}
    if text is None and icon_url is None and proxy_url is None: return UselessCode()
    if text is not None: self.json['footer']['text']: str = text
    if icon_url is not None: self.json['footer']['icon_url']: str = icon_url
    if proxy_url is not None: self.json['footer']['proxy_url']: str = proxy_url

  def add_field(self, nom: str, valeur: str, *, inline: bool = True):
    if 'fields' not in self.json: self.json['fields']: list = []
    if len(self.json['fields']) > 25: raise ValueError('La limite de fields est de 25.')
    self.json['fields'].append({'name': nom, 'value': valeur, 'inline': inline})
                    
def UselessCode():
  try:
    raise ValueError('WARNING\nCode inutile')
  except Exception as e:
    print(Fore.YELLOW + e)
