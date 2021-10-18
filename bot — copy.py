from vkbottle.bot import Bot, Message

bot = Bot("vk token")

@bot.on.message(text="персил")
async def handler(_) -> str:
    return "топ"

@bot.on.message(text="пидор")
async def handler(_) -> str:
    return "говноед"

@bot.on.message(text="тайд")
async def handler(_) -> str:
    return "фу бля, пшел нах"

@bot.on.message(text="алкаш")
async def handler(_) -> str:
    return "да я и так знаю, шо админ алкаш, а когда админ набухаеться в стельку пьяным, он начинаем буянить в беседе"

@bot.on.message(text="я люблю мужиков")
async def handler(_) -> str:
    return "!кик @none"

@bot.on.message(text="тайдоеды")
async def handler(_) -> str:
    return "ебланы"

@bot.on.message(text="свинья")
async def handler(_) -> str:
    return "ща сам станешь свиньей!"

@bot.on.message(text="win102018tv")
async def handler(_) -> str:
    return "top, forever, tide - dick, fuck"

@bot.on.message(text="алл")
async def handler(_) -> str:
    return "@all, троллим всех аллам)))"

@bot.on.message(text="пидор")
async def handler(_) -> str:
    return "говноед"

@bot.on.message(text="tide")
async def handler(_) -> str:
    return "дерьмо"

@bot.on.message(text="фас")
async def handler(_) -> str:
    return "я тебе не сабака, нахой"

@bot.on.message(text="кто любит тайд")
async def handler(_) -> str:
    return "тот говноед"

@bot.on.message(text="зеленая ограда")
async def handler(_) -> str:
    return "девки выебли папа так ему и надо, опа, опа зеленая ограда, девки выебли папа так ему и надо"

@bot.on.message(text="30 лет")
async def handler(_) -> str:
    return "спасибо, что родили меня на свет"

@bot.on.message(text="путин")
async def handler(_) -> str:
    return "я пожалуй промолчу, а то боюсь посадят"

@bot.on.message(text="хочу жрать")
async def handler(_) -> str:
    return "так иди и пожри, долбан"


@bot.on.message(text="водка")
async def handler(_) -> str:
    return "водка пива, под конец корпоратива, выполняем нормативы под восточный массивы, водка пиво водка пиво пож конец корпоратива, да я понял шо ты русский на держи пожри закуски, от двух капелек табаски покраснели твои глазки"
    
@bot.on.message(text="говноед")
async def handler(_) -> str:
    return "ты"
    
@bot.on.message(text="Tide")
async def handler(_) -> str:
    return "фуууууууууууууууууууууууууу..... говноед"
    
@bot.on.message(text="бухать")
async def handler(_) -> str:
    return "если админ так пишет значит он рили ща пойдет бухать и позже срать в беседе, дайте ему кик"
    
@bot.on.message(text="Есть идеи еще, что-то добавить пишите")
async def handler(_) -> str:
    return "пишите в лс @botsamogon"
    
@bot.on.message(text="samogon")
async def handler(_) -> str:
    return "@botsamogon"
    
@bot.on.message(text="группа")
async def handler(_) -> str:
    return "@botsamogon"
    
@bot.on.message(text="самогон")
async def handler(_) -> str:
    return "@botsamogon"
    
@bot.on.message(text="Самогон")
async def handler(_) -> str:
    return "@botsamogon"
    
@bot.on.message(text="Samogon")
async def handler(_) -> str:
    return "@botsamogon"

bot.run_forever()
