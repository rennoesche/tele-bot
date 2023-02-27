import json
import random

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

def generate_group(update, context):
    with open('members.json', 'r') as f:
        names = json.load(f)['members']

    random.shuffle(names)
    if context.args:
        group_sizes = [int(x) for x in context.args]
    else:
        group_sizes = [5, 5, 5, 5]
    num_groups = len(names) // sum(group_sizes)

    if len(names) % sum(group_sizes) != 0:
        num_groups += 1

    groups = []
    start = 0
    for i, size in enumerate(group_sizes):
        end = start + size
        group = names[start:end]
        groups.append(group)
        start = end

    message = ""
    for i, group in enumerate(groups):
        message += f"Group {i + 1}: {', '.join(group)}\n"

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def send_greeting(update, context):
    keyboard = [[InlineKeyboardButton("Generate Group", callback_data='generate_group')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Hello, How can I help you?.', reply_markup=reply_markup)

def button_click(update, context):
    query = update.callback_query
    query.answer()
    if query.data == 'generate_group':
        generate_group(update, context)
