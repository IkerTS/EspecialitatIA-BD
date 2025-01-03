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

### /help
Enviar un missatge amb una benvinguda i la llista de comandes disponibles 

### /showprd
Enviar un missatge mostran informació sobre un producte a traves del seu identificador dintre de la informació consultada a la API de Mercadona amb les funcions `get_data_from_api`, `get_products_url`
 - `get_data_from_api`: Consultar a la url donada de get_products_url i retorna la informacio en format JSON.  
 - `get_products_url`: Retorna la url de la API amb el identificador del producte declarat.  
Informacio a mostrar:  
`Nom`, `ID`, `Imatge Producte`, `Preu`, `Origen`, `Ingredients`

### /addcart
Crea un DataFrame (`Id Producte`, `Nom Producte`, `Quantitat`, `Preu Unitat`, `Preu Total`) amb informació del producte (`ID`, `Nom`, `Preu`) junt amb la quantitat que s'afegeix
al carret per calcular el preu total de cada producte i guardar-ho en format JSON `cart-username-chatid.json` orientat a columnes:  
`col1: {fila0: valor, fila1: valor}, col2: {fila0: valor, fila1: valor}`.  

Si ja s'havia afegit un producte abans, carregarà el fitxer anterior i afegir el nou producte, també si s'afegeix un producte que ja estava, només sumarà la quantitat afegida.

### /showcart
Enviar un missatge amb format taula amb el carret dels productes on també ens donarà el preu total del carret.  
**Ha d'existir el fitxer on es guarda els productes**.

## Implementacio Extra  
Es poden implementar moltes funcions que podria estar molt interessant com un generador de contrasenyes, o un generador de rutes de mapes amb un formulari.
