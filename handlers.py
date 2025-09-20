import os
import screen_brightness_control as sbc
import ctypes
import numpy as np
import webbrowser
import urllib.parse
import cpuinfo
import psutil
import pynvml
import wmi
from PIL import ImageGrab

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile

import keyboards as kb

from config import ALLOWED_USER_ID


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Using this bot u can manipulate your pc from a distance.\n'
                         '<i>/start</i> or <i>/main</i> opens the main menu.\n'
                         f'To continue choose the option below.',
                         reply_markup=kb.inline_main, parse_mode="HTML")

@router.message(Command("main"))
async def main(message: Message):
    await message.answer(f'Using this bot u can manipulate your pc from a distance.\n'
                         '<i>/start</i> or <i>/main</i> opens the main menu.\n'
                         f'To continue choose the option below.',
                         reply_markup=kb.inline_main, parse_mode="HTML")

@router.callback_query(F.data == 'back')
async def back(callback: CallbackQuery):
    await callback.message.edit_text(f'Using this bot u can manipulate your pc from a distance.\n'
                         '<i>/start</i> or <i>/main</i> opens the main menu.\n'
                         f'To continue choose the option below.',
                         reply_markup=kb.inline_main, parse_mode="HTML")

@router.callback_query(F.data == 'power')
async def power(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Choose the option below.', reply_markup=kb.inline_power)

@router.callback_query(F.data.startswith("sys_"))
async def handle_sys(callback: CallbackQuery):
    if callback.from_user.id != ALLOWED_USER_ID:
        await callback.answer("Unauthorised user❌")
        return

    try:
        if callback.data == "sys_lock":
            os.system("rundll32.exe user32.dll,LockWorkStation")
            await callback.answer('PC is Locked🔒', show_alert=True)
        elif callback.data == "sys_sleep":
            await callback.answer('PC is Sleeping😴', show_alert=True)
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif callback.data == "sys_shut":
            await callback.answer('Shutting Down...', show_alert=True)
            os.system("shutdown /s /t 1")
        elif callback.data == "sys_restart":
            await callback.answer('Restarting...', show_alert=True)
            os.system("shutdown /r /t 1")
    except Exception:
        await callback.answer("Something went wrong.")

@router.callback_query(F.data == 'sound')
async def sound(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Choose the option below.', reply_markup=kb.inline_sound)

@router.callback_query(F.data.startswith("vol_"))
async def handle_vol(callback: CallbackQuery):
    if callback.from_user.id != ALLOWED_USER_ID:
        await callback.answer("Unauthorised user❌")
        return

    try:
        if callback.data == "vol_mute":
            await callback.answer('')
            os.system("nircmd.exe mutesysvolume 1")
        elif callback.data == "vol_unmute":
            await callback.answer('')
            os.system("nircmd.exe mutesysvolume 0")
        elif callback.data == "vol_25":
            await callback.answer('')
            os.system("nircmd.exe setsysvolume 16384")
        elif callback.data == "vol_50":
            await callback.answer('')
            os.system("nircmd.exe setsysvolume 32767")
        elif callback.data == "vol_75":
            await callback.answer('')
            os.system("nircmd.exe setsysvolume 49152")
        elif callback.data == "vol_100":
            await callback.answer('')
            os.system("nircmd.exe setsysvolume 65535")
    except Exception:
        await callback.answer("Something went wrong.")

@router.callback_query(F.data == 'brightness')
async def brightness(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Choose the option below.', reply_markup=kb.inline_brightness_nl_off)

def set_gamma(r, g, b):
    gamma_array = np.zeros((3, 256), dtype=np.uint16)
    for i in range(256):
        gamma_array[0][i] = min(65535, int(((i / 255.0) ** (1.0 / r)) * 65535 + 0.5))
        gamma_array[1][i] = min(65535, int(((i / 255.0) ** (1.0 / g)) * 65535 + 0.5))
        gamma_array[2][i] = min(65535, int(((i / 255.0) ** (1.0 / b)) * 65535 + 0.5))
    ramp = gamma_array.flatten().tobytes()
    hdc = ctypes.windll.user32.GetDC(0)
    ctypes.windll.gdi32.SetDeviceGammaRamp(hdc, ramp)

@router.callback_query(F.data.startswith("bright_"))
async def handle_brightness(callback: CallbackQuery):
    if callback.from_user.id != ALLOWED_USER_ID:
        await callback.answer("Unauthorised user❌")
        return

    try:
        if callback.data == "bright_0":
            await callback.answer('')
            sbc.set_brightness(0)
        elif callback.data == "bright_50":
            await callback.answer('')
            sbc.set_brightness(50)
        elif callback.data == "bright_100":
            await callback.answer('')
            sbc.set_brightness(100)
        elif callback.data == "bright_night_light_on":
            await callback.answer('')
            await callback.message.edit_text("Choose the option below.", reply_markup=kb.inline_brightness_nl_on)
            set_gamma(1.0, 0.885, 0.72)
        elif callback.data == "bright_night_light_off":
            await callback.answer('')
            await callback.message.edit_text("Choose the option below.", reply_markup=kb.inline_brightness_nl_off)
            set_gamma(1.0, 1.0, 1.0)
    except Exception:
        await callback.answer("Something went wrong.")

@router.callback_query(F.data == 'apps')
async def apps(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Choose the option below.', reply_markup=kb.inline_apps)

@router.callback_query(F.data.startswith("app_"))
async def handle_apps(callback: CallbackQuery):
    if callback.from_user.id != ALLOWED_USER_ID:
        await callback.answer("Unauthorised user❌")
        return

    try:
        if callback.data == "app_browser":
            await callback.answer('')
            url = 'https://www.google.com'
            webbrowser.open(url)
            await callback.message.edit_text('Choose the website you want to navigate to.\n'
                                             'To search by prompt type <i>/search</i>',
                                                reply_markup=kb.inline_browser, parse_mode="HTML")
        elif callback.data == "app_telegram":
            await callback.answer('')
            os.startfile("C:/Users/prisyaga_/AppData/Roaming/Telegram Desktop/Telegram.exe")
        elif callback.data == "app_discord":
            await callback.answer('')
            os.startfile("C:/Users/prisyaga_/AppData/Local/Discord/app-1.0.9205/Discord.exe")
        elif callback.data == "app_spotify":
            await callback.answer('')
            os.startfile("C:/Users/prisyaga_/AppData/Roaming/Spotify/Spotify.exe")
    except Exception:
        await callback.answer("Something went wrong.")

@router.callback_query(F.data == 'back_to_apps')
async def back_to_apps(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Choose the option below.', reply_markup=kb.inline_apps)

@router.callback_query(F.data.startswith("web_"))
async def handle_browser(callback: CallbackQuery):
    if callback.from_user.id != ALLOWED_USER_ID:
        await callback.answer("Unauthorised user❌")
        return

    try:
        if callback.data == "web_gmail":
            await callback.answer('')
            webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
        elif callback.data == "web_youtube":
            await callback.answer('')
            webbrowser.open("https://www.youtube.com/")
        elif callback.data == "web_github":
            await callback.answer('')
            webbrowser.open("https://www.github.com/")
        elif callback.data == "web_instagram":
            await callback.answer('')
            webbrowser.open("https://www.instagram.com/")
        elif callback.data == "web_schedule":
            await callback.answer('')
            webbrowser.open("https://schedule.kpi.ua/?groupId=12311ac1-4e15-4586-9485-4209eaa36451")
    except Exception:
        await callback.answer("Something went wrong.")

@router.message(Command("search"))
async def search(message: Message):
    await message.reply("Type what you want to search following the example below:\n"
                        "search_<i>your prompt</i>", parse_mode="HTML")

@router.message(F.text.startswith("search_"))
async def search_by_prompt(message: Message):
    if message.from_user.id != ALLOWED_USER_ID:
        await message.answer("Unauthorised user❌")
        return

    try:
        prompt = message.text[7:].strip()
        encoded_prompt = urllib.parse.quote_plus(prompt)

        webbrowser.open(f"https://www.google.com/search?q={encoded_prompt}")
        await message.answer(f'🔍Searching for <i>{prompt}</i>...', reply_markup=kb.inline_back_to_main,
                                                                         parse_mode="HTML")
    except Exception:
        await message.answer("Something went wrong.")

@router.callback_query(F.data == "system")
async def system(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Choose the option below.', reply_markup=kb.inline_system)

@router.callback_query(F.data == "screenshot")
async def screenshot(callback: CallbackQuery):
    if callback.from_user.id != ALLOWED_USER_ID:
        await callback.answer("Unauthorised user❌")
        return
    try:
        screenshot = ImageGrab.grab()
        screenshot.save("screenshot.png")

        photo = FSInputFile("screenshot.png")
        await callback.answer('')
        await callback.message.answer_photo(photo, caption="Screenshot was taken!", reply_markup=kb.inline_system_back_from_screenshot)
        os.remove("screenshot.png")
    except Exception:
        await callback.answer("Something went wrong.")

@router.callback_query(F.data == "back_from_screenshot")
async def back_from_screenshot(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(f'Using this bot u can manipulate your pc from a distance.\n'
                         '<i>/start</i> or <i>/main</i> opens the main menu.\n'
                         f'To continue choose the option below.',
                         reply_markup=kb.inline_main, parse_mode="HTML")

@router.callback_query(F.data == "info")
async def system_info(callback: CallbackQuery):
    if callback.from_user.id != ALLOWED_USER_ID:
        await callback.answer("Unauthorised user❌")
        return

    try:
        cpu_info = cpuinfo.get_cpu_info()
        ram = psutil.virtual_memory()
        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)
        gpu_name = pynvml.nvmlDeviceGetName(handle)
        gpu_mem = pynvml.nvmlDeviceGetMemoryInfo(handle)
        c = wmi.WMI()
        disk = c.Win32_DiskDrive()[0]

        await callback.answer('')
        await callback.message.answer(f'\tHere is your system info!\n'
                                      f'\n<b>CPU</b>: {cpu_info['brand_raw']}\n'
                                      f'<b>GPU</b>: {gpu_name}, {gpu_mem.total // (1024**2)} MB\n'
                                      f'<b>RAM</b>: {round(ram.total / (1024**3), 2)} GB\n'
                                      f'<b>Drive</b>: {disk.Caption}, MediaType: {disk.MediaType}, Size: {int(disk.Size) // (1024**3)} GB\n',
                                        parse_mode="HTML", reply_markup=kb.inline_system)
    except Exception:
        await callback.answer("Something went wrong.")