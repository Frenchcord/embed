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
# ajouter un field
```py
embed.add_field(nom="nom du field", valeur="Valeure du field")
```
## mettre un field pas en ligne
```py
embed.add_field(nom="nom du field", valeur="Valeure du field", inline=False)
```
## mettre un field en ligne (en ligne par defaut)
```py
embed.add_field(nom="nom du field", valeur="Valeure du field", inline=True)
```
# mettre un thumbnail sur un embed
```py
embed.set_thumbnail(url="url du thumbnail")
```
## mettre un proxy pour l'image du thumbnail
```py
embed.set_thumbnail(url="url du thumbnail", proxy_url="url du proxy")
```
## mettre un thumbnail d'une taille precise
```py
embed.set_thumbnail(url="url du thumbnail", width=taille, height=taille)
```
# mettre un footer sur un embed
```py
embed.set_footer(text="texte du footer")
```
## mettre une icone sur le footer
```py
embed.set_footer(text="texte du footer", icon_url="url de l'icone du footer")
```
## mettre un proxy sur l'icone du footer
```py
embed.set_footer(text="texte du footer", icon_url="url de l'icone du footer", proxy_url="url du proxy")
```

# mettre un(e) auteur sur l'embed
```py
embed.set_auteur(nom="nom de l'auteur")
```
## mettre un lien sur l'auteur
```py
embed.set_auteur(nom="nom de l'auteur", url="lien de l'auteur")
```
## mettre un lien avec un proxy sur l'auteur
```py
embed.set_auteur(nom="nom de l'auteur", url="lien de l'auteur", proxy_url="url d'un proxy")
```
## mettre une icone sur l'auteur
```py
embed.set_auteur(icon_url="url de l'icone")
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
