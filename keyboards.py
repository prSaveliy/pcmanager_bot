from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Power options', callback_data='power'),
        InlineKeyboardButton(text='Sound options', callback_data='sound')],
    [InlineKeyboardButton(text='Brightness options', callback_data='brightness'),
        InlineKeyboardButton(text='Apps', callback_data='apps')],
    [InlineKeyboardButton(text='System', callback_data='system')]
])

inline_power = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Lock', callback_data='sys_lock'),
        InlineKeyboardButton(text='Shut down', callback_data='sys_shut')],
    [InlineKeyboardButton(text='Sleep', callback_data='sys_sleep'),
        InlineKeyboardButton(text='Restart', callback_data='sys_restart')],
    [InlineKeyboardButton(text='Back', callback_data='back')]
])

inline_sound = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Mute', callback_data='vol_mute'),
        InlineKeyboardButton(text='Unmute', callback_data='vol_unmute')],
    [InlineKeyboardButton(text='25%', callback_data='vol_25'),
        InlineKeyboardButton(text='50%', callback_data='vol_50')],
    [InlineKeyboardButton(text='75%', callback_data='vol_75'),
        InlineKeyboardButton(text='100%', callback_data='vol_100')],
    [InlineKeyboardButton(text='Back', callback_data='back')]
])

inline_brightness_nl_off = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='0%', callback_data='bright_0'),
        InlineKeyboardButton(text='50%', callback_data='bright_50')],
    [InlineKeyboardButton(text='100%', callback_data='bright_100'),
        InlineKeyboardButton(text='Night Light ON✅', callback_data='bright_night_light_on')],
    [InlineKeyboardButton(text='Back', callback_data='back')]
])

inline_brightness_nl_on = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='0%', callback_data='bright_0'),
        InlineKeyboardButton(text='50%', callback_data='bright_50')],
    [InlineKeyboardButton(text='100%', callback_data='bright_100'),
        InlineKeyboardButton(text='Night Light OFF❌', callback_data='bright_night_light_off')],
    [InlineKeyboardButton(text='Back', callback_data='back')]
])

inline_apps = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Browser🌐', callback_data='app_browser'),
        InlineKeyboardButton(text="Telegram✉️", callback_data='app_telegram')],
    [InlineKeyboardButton(text='Discord', callback_data='app_discord'),
        InlineKeyboardButton(text='Spotify', callback_data='app_spotify')],
    [InlineKeyboardButton(text='Back', callback_data='back')]
])

inline_browser = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Gmail', callback_data='web_gmail'),
        InlineKeyboardButton(text='YouTube', callback_data='web_youtube')],
    [InlineKeyboardButton(text='GitHub', callback_data='web_github'),
        InlineKeyboardButton(text='Instagram', callback_data='web_instagram')],
    [InlineKeyboardButton(text='KPI Schedule', callback_data='web_schedule')],
    [InlineKeyboardButton(text='Back', callback_data='back_to_apps')]
])

inline_back_to_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Back to main', callback_data='back')]
])

inline_system = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Screenshot', callback_data='screenshot'),
        InlineKeyboardButton(text='System Info', callback_data='info')],
    [InlineKeyboardButton(text='Back', callback_data='back')]
])

inline_system_back_from_screenshot = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Screenshot', callback_data='screenshot'),
        InlineKeyboardButton(text='System Info', callback_data='info')],
    [InlineKeyboardButton(text='Back', callback_data='back_from_screenshot')]
])

