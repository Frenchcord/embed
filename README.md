# embed
Tout sur les embeds de Frenchcord
# créer un embed
```py
from frenchcord import Embed, color_random
embed = Embed(titre"titre", description="desc", couleur=color_random())
```
# mettre une photo sur un embed
```py
embed.set_image(url="url de la photo")
```
## mettre un proxy sur l'image
```py
embed.set_image(url="url de la photo", proxy_url="une url de proxy")
```
## mettre une taille speifique
```py
embed.set_image(url="url de la photo", width=taille, height=taille)
```
## tout les champs
```py
embed.set_image(url="url de la photo", proxy_url="une url de proxy", width=taille, height=taille)
```
# mettre une video sur un embed
```py
embed.set_video(url="url de la video")
```
## mettre un proxy sur la video
```py
embed.set_video(url="url de la video", proxy_url="une url de proxy")
```
## mettre une taille speifique
```py
embed.set_video(url="url de la video", width=taille, height=taille)
```
## tout les champs
```py
embed.set_video(url="url de la video", proxy_url="une url de proxy", width=taille, height=taille)
```
# prendre le json de l'embed
```py
embed_json = embed.json
```
# envoyer un embed
```py
# anglais
channel.send(embeds=[embed])
# francais
salon.envoyer(embeds=[embed])
```
