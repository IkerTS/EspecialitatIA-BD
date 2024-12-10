# Bot Telegram

## Objectiu
Creació d'un BOT molt simple que sigui capaç de respondre a algunes de les accions que li demanem amb Python.

## Tema
El bot interactua amb l'API de Mercadona i permet gestionar productes en un carret de compra. Els usuaris poden cercar productes per ID, afegir-los al carret i veure el contingut del carret.

## Característiques

- **`/help`**: Mostra una llista de comandes disponibles.
- **`/showprd [ID]`**: Mostra la informació d'un producte de Mercadona, donada la seva ID (per exemple, `/showprd 4240`).
- **`/addcart [ID] [Quantitat]`**: Afegeix un producte al carret de compra, especificant la quantitat (per exemple, `/addcart 4240 2`).
- **`/showcart`**: Mostra el contingut del carret de compra amb els detalls dels productes afegits.

## Requisits

- **Provat en Python 3.12.7**
  
### Llibreries necessàries:

- `python-telegram-bot`: Per interactuar amb l'API de Telegram.
- `pandas`: Per gestionar les dades del carret.
- `requests`: Per fer peticions a l'API de Mercadona.
- `python-dotenv`: Per carregar el token del Bot des d'un fitxer `.env`.

## Funcions

### help
Envia un missatge amb una benvinguda i la llista de comandes disponibles 

### showprd
Envia un missatge mostran informació sobre un producte a traves del seu identificador:  
`Nom`, `ID`, `Imatge Producte`, `Preu`, `Origen`, `Ingredients`

### addcart
Crea un DataFrame (`Id Producte`, `Nom Producte`, `Quantitat`, `Preu Unitat`, `Preu Total`) amb informació del producte (`ID`, `Nom`, `Preu`) junt amb la quantitat que s'afegeix 
al carret per calcular el preu total de cada producte i guardar-ho en format JSON orientat a columnes:  `col1: {fila0: valor, fila1: valor}, col2: {fila0: valor, fila1: valor}`.    
Si ja s'havia afegit un producte abans, carregarà el fitxer anterior i afegir-la el nou producte, també si s'afegeix un producte que ja estava, només sumarà la quantitat afegida.

### showcart

