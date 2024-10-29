# bot.py

from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update
from twitter_search import search_adpod_tweets, post_tweet_comment
from llm_comment import generate_adpod_comment
from config import TELEGRAM_BOT_TOKEN

# Variable to store tweet links and texts
tweet_results = []

# Start command handler
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Welcome! Use /search to find AdPod tweets, and /comment to comment on them."
    )

# Search tweets command handler
def search_tweets(update: Update, context: CallbackContext):
    global tweet_results
    update.message.reply_text("Searching for AdPod tweets...")
    tweet_results = search_adpod_tweets()

    if tweet_results:
        for tweet_text, tweet_url in tweet_results:
            update.message.reply_text(f"{tweet_url}")
        update.message.reply_text("Use /comment to comment on the retrieved tweets.")
    else:
        update.message.reply_text("No tweets found.")

# Comment tweets command handler
def comment_tweets(update: Update, context: CallbackContext):
    global tweet_results
    if tweet_results:
        for tweet_text, tweet_url in tweet_results:
            # Generate comment using the LLM
            comment = generate_adpod_comment(tweet_text)
            # Post comment on Twitter
            comment_status = post_tweet_comment(tweet_url, comment)
            update.message.reply_text(f"Posted comment: {comment_status}")
    else:
        update.message.reply_text("No tweets found to comment on. Use /search first.")

def main():
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Define command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("search", search_tweets))
    dispatcher.add_handler(CommandHandler("comment", comment_tweets))

    # Start polling for messages
    updater.start_polling()
    print("Bot is running...")
    updater.idle()

if __name__ == '__main__':
    main()
