# json ?
Vous pouvez recuperer le format json de l'embed pour executer des requetes directes a l'api
# comment faire?
## recuperez le json
```py
json = embed.json
```
## envoyer l'embed
```py
import requests
payload: dict = {
  "embeds": [json]
}
requests.post('https://discord.com/api/v10/channels/Channeld/messages', data=payload, authorization=bot.token)
```
