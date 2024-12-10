from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update
from api import get_data_from_api, get_products_url
from dotenv import load_dotenv
import pandas as pd
import os.path

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Llista de comandes disponibles
    commands = (
        "- /help: Obtenir ajuda sobre el bot.\n"
        "- /showprd: Mostrar informació d'un producte de Mercadona per el seu identificador (ID). Ex: /showprd 4240\n"
        "- /addcart: Afegir productes al carrito on especificar el identificador del producte i la quantitat. Ex: /addcart 4240 2\n"
        "- /showcart: Veure carrito de la compra."
    )
    await update.message.reply_text(f"Hola! Soc un bot de proves de Telegram, pots declarar aquestes comandes:\n{commands}")

async def showprd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Extraccio de les dades a traves del parametre declarat
    data = get_data_from_api(get_products_url(int(context.args[0])))
    # Si no es troba el producte, es notifica
    if data == None:
      await update.message.reply_text(f"No s'ha trobat cap producte amb aquest identificador")
    info_prd = {
        "id_prd": data['id'],
        "name": data['details']['description'],
        "photo": data['photos'][0]['zoom'],
        "price": data['price_instructions']['unit_price'],
        "origin": data['details']['origin'],
        "ingredients": data['nutrition_information']['ingredients']
    }
    await update.message.reply_text(f"Nom: {info_prd['name']}\n")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=info_prd['photo'])
    await update.message.reply_text(f"ID: {info_prd['id_prd']}\nPreu: {info_prd['price']}\nOrigen: {info_prd['origin']}\nIngredients: {info_prd['ingredients']}")

async def addcart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Nom fitxer cistella
    data_file = f"cart-{update.message.from_user.username}-{update.message.chat.id}.json"
    # Extraccio de les dades a traves del parametre declarat
    prd_data = get_data_from_api(get_products_url(int(context.args[0])))
    # Si no es troba el producte, es notifica
    if prd_data == None:
      await update.message.reply_text(f"No s'ha trobat cap producte amb aquest identificador") 
    else:
        info_prd = {
            "id_prd": prd_data['id'],
            "name": prd_data['details']['description'],
            "price": prd_data['price_instructions']['unit_price']
        }

        if os.path.exists(data_file):
            df = pd.read_json(data_file, orient = 'columns')
            # Si el producte ja està en el carro, sumem la quantitat
            if info_prd['name'] in df['Nom Producte'].values:
                df.loc[df['Nom Producte'] == info_prd['name'], 'Quantitat'] += int(context.args[1])
            else:
                df.loc[len(df)] = [
                    info_prd['id_prd'],
                    info_prd['name'], 
                    int(context.args[1]), 
                    float(info_prd['price']), 
                    int(context.args[1]) * float(info_prd['price'])
                ]
        else:
            df = pd.DataFrame(columns=["Id Producte", "Nom Producte", "Quantitat", "Preu Unitat", "Preu Total"])
            df.loc[len(df)] = [
                info_prd['id_prd'],
                info_prd['name'],
                int(context.args[1]),
                float(info_prd['price']),
                int(context.args[1]) * float(info_prd['price'])
            ]
        
        df.to_json(data_file, orient = 'columns')
        await update.message.reply_text(f"S'ha afegit el producte a la cistella")

async def showcart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Nom fitxer cistella
    data_file = f"cart-{update.message.from_user.username}-{update.message.chat.id}.json"
    if os.path.exists(data_file):
        df = pd.read_json(data_file, orient = 'columns')
        df.loc[len(df)] = ['','','','',df['Preu Total'].sum()]
        tabla_markdown = df.to_markdown(index=False)
        await update.message.reply_text(f"```\n{tabla_markdown}\n```", parse_mode="MarkdownV2")
    else:
        await update.message.reply_text(f"No hi ha res a la cistella")
          
def main():
    # Declarar una constant amb access al TOKEN
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    
    application = Application.builder().token(TOKEN).build()
    # Comandes
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("showprd", showprd))
    application.add_handler(CommandHandler("addcart", addcart))
    application.add_handler(CommandHandler("showcart", showcart))

    # Executar el bot fins que l'usuari premi Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()