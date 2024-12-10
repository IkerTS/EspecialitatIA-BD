# Bot Telegram  
Objectiu: Creacio d'un BOT molt simple que sigui capaç de respondre a algunes de les accions que li demanem amb Python    
Tema: Interactua amb l'API de Mercadona i gestionar productes en un carret de compra. El bot permet als usuaris cercar productes per ID, afegir-los al carret i veure el contingut del carret.  
Característiques    
  **-/help**: Mostra una llista de comandes disponibles.
  **-/showprd [ID]**: Mostra la informació d'un producte de Mercadona, donada la seva ID (per exemple, /showprd 4240).
  **-/addcart [ID] [Quantitat]**: Afegeix un producte al carret de compra, especificant la quantitat (per exemple, /addcart 4240 2).
  **-/showcart**: Mostra el contingut del carret de compra amb els detalls dels productes afegits.
Requisits
  Python 3.12.3 o superior
  Llibreries necessàries:
  python-telegram-bot (per interactuar amb l'API de Telegram)
  pandas (per gestionar les dades del carret)
  requests (per fer peticions a l'API de Mercadona)
  python-dotenv (per carregar el token des d'un fitxer .env)

