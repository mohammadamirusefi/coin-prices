import logging
import requests
from bs4 import BeautifulSoup
from lxml import etree
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format="%(asctim)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

async def btc_price(update: Update, content: ContextTypes.DEFAULT_TYPE) -> None:
    soup =BeautifulSoup(requests.get("https://coinmarketcap.com/currencies/bitcoin/").content,"lxml")
    dom=etree.HTML(str(soup))
    lst=dom.xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div/section/div/div[2]/span[1]/text()')[0]
    await update.message.reply_html(
        rf"btc price is {lst}$",
        
    )
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help_cammand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    await update.message.reply_text("Help")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    await update.message.reply_text(update.message.text)
    
async def personality(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"you are {user.mention_html()}",
        reply_markup=ForceReply(selective=True))

def main() -> None:

    application = Application.builder().token("8433308526:AAHj68OfYfr-ce5IRvpEMvdICgd3lKH7sFU").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help",help_cammand))
    application.add_handler(CommandHandler("who_am_i",personality))
    application.add_handler(CommandHandler("btc_price",btc_price))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()