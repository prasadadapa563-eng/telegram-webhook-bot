from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Flask(__name__)

application = Application.builder().token(BOT_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        movie = context.args[0]
        await update.message.reply_text(f"You requested: {movie}")
    else:
        await update.message.reply_text("Welcome! Use your movie link.")

application.add_handler(CommandHandler("start", start))
