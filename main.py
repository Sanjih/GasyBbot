from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Remplace par ton vrai token
TOKEN = "8488607629:AAF07ZVKslEWRZX_0trFJCfB4FxAQCwpbZs"

# Commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salut ! Je suis ton bot Telegram. 🚀\n"
        "Utilise /help pour voir les commandes."
    )

# Commande /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commandes disponibles :\n"
        "/start - Démarrer le bot\n"
        "/help - Voir l'aide"
    )

def main():
    # Crée l'application
    app = Application.builder().token(TOKEN).build()

    # Ajoute les gestionnaires de commandes
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Démarre le bot
    print("Bot en marche... 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
