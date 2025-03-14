from telegram import Update, Bot
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from constants import *
from create_messages import *
from amazon_api import AmazonAPI

bot = Bot(token=TELEGRAM_TOKEN)


# message to the user when he starts the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or not update.effective_user:
        return

    await update.message.reply_text(
        f"Benvenuto {update.effective_user.first_name}, mandami il link amazon di un prodotto per "
        "creare il post sul tuo canale!"
    )


# TODO: identify the user who sends messages to the bot to prevent anyone with the bot's username from sending messages in the channel through it


# handle the message sent by the user (only amazon links are allowed)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or not update.message.text:
        return

    message_text = update.message.text
    # Check for single product Amazon URL pattern (contains /dp/ or /gp/product/)
    if "amazon." in message_text and (
        "/dp/" in message_text or "/gp/product/" in message_text
    ):
        print(message_text)
        amazon_api = AmazonAPI()

        # retry product information from amazon api
        product = amazon_api.get_product_from_url(message_text)
        print(product, '--product')
        # create the post for the channel
        formatted_message = create_product_post(product)
        if formatted_message == "Sorry, couldn't retrieve product information.":
            print("Error: Could not create product post")
            return

        # Get the image URL and ensure it exists
        image_url = None
        if (hasattr(product, 'images') and
            hasattr(product.images, 'primary') and
            hasattr(product.images.primary, 'large') and
            product.images.primary.large and
            product.images.primary.large.url):

            image_url = product.images.primary.large.url.replace('_SL500_', '_SL1500_')
            print(f"Using image URL: {image_url}")

            try:
                await bot.send_photo(
                    chat_id=CHANNEL_ID,
                    photo=image_url,
                    caption=formatted_message,
                    parse_mode="HTML"
                )
                return
            except Exception as e:
                print(f"Error sending photo: {str(e)}")

        # Fallback to text-only message if image sending fails or no image URL
        print(f"Sending text-only message to {CHANNEL_ID}")
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=formatted_message,
            parse_mode="HTML"
        )


app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()
