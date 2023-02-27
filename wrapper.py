def auth(func):
    async def wrapper(message):
        if message.chat.id != 368553201:
            return await message.answer(f'You dont have rules!')
        return await func(message)
    return wrapper