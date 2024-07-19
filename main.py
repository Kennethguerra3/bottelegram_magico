import telebot
from telebot import types

# Conexión con nuestro BOT
TOKEN = '7453993387:AAFkO8Fy0DBvB7kwrume1QUqrr4lIo2HQdY'

bot = telebot.TeleBot(TOKEN)

# Configurar comandos sugeridos
def set_bot_commands():
    bot_commands = [
        telebot.types.BotCommand('/start', 'Iniciar bot'),
        telebot.types.BotCommand('/help', 'Obtener ayuda'),
        telebot.types.BotCommand('/productos', 'Ver productos')
    ]
    bot.set_my_commands(bot_commands)

# Manejador para el comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    welcome_message = (
        f'🎉 ¡Hola {user_name}! 🎉\n\n'
        f'🎩 Bienvenido a Mágico, la magia del lavado 🧼✨\n\n'
        f'🌟 Aquí encontrarás los mejores productos para que tu ropa siempre luzca impecable y con un aroma irresistible.\n\n'
        f'📌 Tu ID de usuario es: {user_id}\n\n'
        f'📺 Mira nuestro video promocional: [Ver Video](https://www.youtube.com/watch?v=SA5KjZDdRDo)'
    )
    bot.send_message(message.chat.id, welcome_message, parse_mode='Markdown')
    send_product_options(message)

# Manejador para el comando /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Puedes interactuar conmigo usando comandos (/productos, /start, /help).')

# Manejador para el comando /productos
@bot.message_handler(commands=['productos'])
def send_product_options(message):
    markup = types.InlineKeyboardMarkup(row_width=1)

    # Botón para Detergente Mágico
    btn_detergente_magico = types.InlineKeyboardButton('Detergente Mágico', callback_data='detergente_magico_info')
    markup.add(btn_detergente_magico)
    
    # Botón para Detergente Bravo
    btn_detergente_bravo = types.InlineKeyboardButton('Detergente Bravo', callback_data='detergente_bravo_info')
    markup.add(btn_detergente_bravo)

    bot.send_message(message.chat.id, "¿Quieres ropa suave y con un aroma irresistible? Elige entre nuestras Marcas:", reply_markup=markup)

# Manejador para las respuestas a los botones de productos
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'detergente_magico_info':
        markup = types.InlineKeyboardMarkup()

        # Subcategorías de Detergente Mágico
        btn_detergente_140gr = types.InlineKeyboardButton('60 unid. x 140 gr - Precio: S/ 60.00', callback_data='detergente_140gr')
        btn_detergente_280gr = types.InlineKeyboardButton('30 unid. x 280 gr - Precio: S/ 54.00', callback_data='detergente_280gr')
        btn_detergente_800gr = types.InlineKeyboardButton('12 unid. x 800 gr - Precio: S/ 66.00', callback_data='detergente_800gr')
        btn_detergente_2_5kg = types.InlineKeyboardButton('6 unid. x 2.5 Kilos - Precio: S/ 106.8', callback_data='detergente_2_5kg')
        btn_detergente_4kg = types.InlineKeyboardButton('4 unid. x 4 Kilos - Precio: S/ 107.20', callback_data='detergente_4kg')
        btn_detergente_magico_14kg = types.InlineKeyboardButton('1 unid. x 14 kg - Precio: S/ 84.00', callback_data='detergente_magico_14kg')

        markup.add(btn_detergente_140gr, btn_detergente_280gr, btn_detergente_800gr, btn_detergente_2_5kg, btn_detergente_4kg, btn_detergente_magico_14kg)

        bot.send_message(call.message.chat.id, "Selecciona una presentación del Detergente Mágico:", reply_markup=markup)
    
    elif call.data == 'detergente_bravo_info':
        markup = types.InlineKeyboardMarkup()

        # Subcategorías de Detergente Bravo
        btn_detergente_bravo_15kg = types.InlineKeyboardButton('1 unid. x 15 kg - Precio: S/ 75.00', callback_data='detergente_bravo_15kg')

        markup.add(btn_detergente_bravo_15kg)

        bot.send_message(call.message.chat.id, "Selecciona una presentación del Detergente Bravo:", reply_markup=markup)

    # Detergente Mágico
    elif call.data == 'detergente_140gr':
        send_detergente_info(call.message.chat.id, 'Detergente Mágico', '60 unid. x 140 gr', 'S/ 60.00', 'https://vi6q5t5yw8yq4mbl-87836950834.shopifypreview.com/products_preview?preview_key=93f43b1944f532d2212d4c0f896dc6e2')
    elif call.data == 'detergente_280gr':
        send_detergente_info(call.message.chat.id, 'Detergente Mágico', '30 unid. x 280 gr', 'S/ 54.00', 'https://vi6q5t5yw8yq4mbl-87836950834.shopifypreview.com/products_preview?preview_key=d7fe816faa16ae47a69e6f9c33cf4e47')
    elif call.data == 'detergente_800gr':
        send_detergente_info(call.message.chat.id, 'Detergente Mágico', '12 unid. x 800 gr', 'S/ 66.00', 'https://vi6q5t5yw8yq4mbl-87836950834.shopifypreview.com/products_preview?preview_key=ca9ea08fc8500cc63b9701e618dee2be')
    elif call.data == 'detergente_2_5kg':
        send_detergente_info(call.message.chat.id, 'Detergente Mágico', '6 unid. x 2.5 Kilos', 'S/ 106.80', 'https://vi6q5t5yw8yq4mbl-87836950834.shopifypreview.com/products_preview?preview_key=caa4e56c65f978b952fe46615096f4d1')
    elif call.data == 'detergente_4kg':
        send_detergente_info(call.message.chat.id, 'Detergente Mágico', '4 unid. x 4 Kilos', 'S/ 107.20', 'https://vi6q5t5yw8yq4mbl-87836950834.shopifypreview.com/products_preview?preview_key=925ba4348cd1f97ac56f7c18117cac9b')
    elif call.data == 'detergente_magico_14kg':
        send_detergente_info(call.message.chat.id, 'Detergente Mágico', '1 unid. x 14 kg', 'S/ 84.00', 'https://vi6q5t5yw8yq4mbl-87836950834.shopifypreview.com/products_preview?preview_key=76bf84d6f107b6c310287d0a27e44d05')
    
    # Detergente Bravo
    elif call.data == 'detergente_bravo_15kg':
        send_detergente_info(call.message.chat.id, 'Detergente Bravo', '1 unid. x 15 kg', 'S/ 75.00', 'https://vi6q5t5yw8yq4mbl-87836950834.shopifypreview.com/products_preview?preview_key=2d7a7e523e506199ed12c5fb551d1edd')

def send_detergente_info(chat_id, product_name, presentacion, precio, url):
    markup = types.InlineKeyboardMarkup()
    btn_comprar = types.InlineKeyboardButton('Comprar', url=url)
    btn_distribuidor = types.InlineKeyboardButton('Nuevo Distribuidor', url='https://agendalo.io/warbush/distribuidor-mayoristas')
    markup.add(btn_comprar, btn_distribuidor)

    bot.send_photo(chat_id,
                   photo='https://cdn.shopify.com/s/files/1/0878/3695/0834/files/Banner.jpg?v=1720843335',
                   caption=f'**{product_name}**\n\n'
                           f'Presentación: {presentacion}\n'
                           f'Precio: {precio}',
                   reply_markup=markup)

# Manejador para cualquier otro mensaje
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, 'No entendí tu solicitud.')

if __name__ == "__main__":
    set_bot_commands()
    bot.polling(none_stop=True)
