
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Tokens e links (variáveis de ambiente recomendadas no Render)
BOT_TOKEN = os.getenv("BOT_TOKEN")
PIX_LINK = os.getenv("PIX_LINK")
CREDIT_LINK = os.getenv("CREDIT_LINK")
GROUP_LINK = os.getenv("GROUP_LINK")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💳 Pagar com Cartão", url=CREDIT_LINK)],
        [InlineKeyboardButton("⚡ Pagar com Pix", url=PIX_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Olá! Escolha a forma de pagamento abaixo:", reply_markup=reply_markup
    )

async def confirm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"✅ Pagamento confirmado! Acesse o grupo: {GROUP_LINK}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("confirm", confirm))
    app.run_polling()
