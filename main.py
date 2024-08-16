import textwrap

import nextcord
from pilmoji import Pilmoji
from PIL import Image, ImageFont, ImageDraw
from nextcord.ext import commands

TESTING_GUILD_ID = xxxxxxx


def find_font_size(text, font, image, target_width_ratio):
    tested_font_size = 100
    tested_font = ImageFont.truetype(font, tested_font_size)
    observed_width, observed_height = get_text_size(text, image, tested_font)
    estimated_font_size = tested_font_size / (observed_width / image.width) * target_width_ratio
    return round(estimated_font_size)

def get_text_size(text, image, font):
    im = Image.new('RGB', (image.width, image.height))
    draw = ImageDraw.Draw(im)
    return draw.textsize(text, font)

bot = commands.Bot()
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.slash_command(description="Imagem da Monga Coen com Texto Personalizado", guild_ids=[TESTING_GUILD_ID])
async def coen(interaction: nextcord.Interaction, arg: str):
    arg = arg.upper()
    textp = arg
    size = 255
    lines = 4
    if (len(arg) > 3):
        size = 150
        lines = 8

    if arg.startswith('<'):
        lines = 100
        size = 255


    arg = textwrap.fill(text=arg, width=lines)
    image = Image.open('base.jpg')
    font = ImageFont.truetype('EqualSans_Demo.ttf', size)
    await interaction.response.defer()
    with Pilmoji(image) as pilmoji:
        pilmoji.text((35, 100), arg, fill="white", font=font)
        image.save("result.jpg")
    await interaction.send(f'{textp}!', files=[nextcord.File('result.jpg')])

bot.run('xxxxxxxx')
