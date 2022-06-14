# embed
Tout sur les embeds de Frenchcord
# créer un embed
```py
from frenchcord import Embed, color_random
embed = Embed(titre"titre", description="desc", couleur=color_random())
```
# mettre une photo sur un embed
```py
embed.set_image(url="url de la photo", proxy_url="une url de proxy", width=taille, height=taille)
```
