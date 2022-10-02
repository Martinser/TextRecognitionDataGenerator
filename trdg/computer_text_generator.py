import random as rnd
from typing import Tuple
from PIL import Image, ImageColor, ImageDraw, ImageFilter, ImageFont
from trdg.utils import get_text_width, get_text_height
import numpy as np
import random
from fontTools.ttLib import TTFont



# Thai Unicode reference: https://jrgraphix.net/r/Unicode/0E00-0E7F
TH_TONE_MARKS = [
    "0xe47",
    "0xe48",
    "0xe49",
    "0xe4a",
    "0xe4b",
    "0xe4c",
    "0xe4d",
    "0xe4e",
]
TH_UNDER_VOWELS = ["0xe38", "0xe39", "\0xe3A"]
TH_UPPER_VOWELS = ["0xe31", "0xe34", "0xe35", "0xe36", "0xe37"]


def generate(
    text: str,
    font: str,
    text_color: str,
    font_size: int,
    orientation: int,
    space_width: int,
    character_spacing: int,
    fit: bool,
    word_split: bool,
    stroke_width: int = 0,
    stroke_fill: str = "#282828",
    fonts_wg:int=0,
) -> Tuple:


    if orientation == 0:
        return _generate_horizontal_text(
            text,
            font,
            text_color,
            font_size,
            space_width,
            character_spacing,
            fit,
            word_split,
            stroke_width,
            stroke_fill,
            fonts_wg,
        )
    elif orientation == 1:
        return _generate_vertical_text(
            text,
            font,
            text_color,
            font_size,
            space_width,
            character_spacing,
            fit,
            stroke_width,
            stroke_fill,
            fonts_wg,
        )
    else:
        raise ValueError("Unknown orientation " + str(orientation))


def _compute_character_width(image_font: ImageFont, character: str) -> int:
    if len(character) == 1 and (
        "{0:#x}".format(ord(character))
        in TH_TONE_MARKS + TH_UNDER_VOWELS + TH_UNDER_VOWELS + TH_UPPER_VOWELS
    ):
        return 0
    # Casting as int to preserve the old behavior
    return round(image_font.getlength(character))



def decide_font(font_path,chars):
    font_path=font_path
    font = TTFont(font_path)
    glyph_name = None
    founds=False
    for table in font['cmap'].tables:
        if ord(chars) in table.cmap.keys():
            founds = True
        glyph_name = table.cmap.get(ord(chars))
        if glyph_name is not None:
            break
    if glyph_name is not None:
        glyf = font['glyf']
        found = glyf.has_key(glyph_name) and glyf[glyph_name].numberOfContours > 0
    else:
        found = False

    return found



def _generate_horizontal_text(
    text: str,
    font: str,
    text_color: str,
    font_size: int,
    space_width: int,
    character_spacing: int,
    fit: bool,
    word_split: bool,
    stroke_width: int = 0,
    stroke_fill: str = "#282828",
    fonts_wg:int=0,
) -> Tuple:
    image_font = ImageFont.truetype(font=font, size=font_size)

    space_width = int(get_text_width(image_font, " ") * space_width)

    if word_split:
        splitted_text = []
        for w in text.split(" "):
            splitted_text.append(w)
            splitted_text.append(" ")
        splitted_text.pop()
    else:
        splitted_text = text

    piece_widths = [
        _compute_character_width(image_font, p) if p != " " else space_width
        for p in splitted_text
    ]
    text_width = sum(piece_widths)
    if not word_split:
        text_width += character_spacing * (len(text) - 1)

    text_height = max([get_text_height(image_font, p) for p in splitted_text])

    txt_img = Image.new("RGBA", (text_width, text_height), (0, 0, 0, 0))
    txt_mask = Image.new("RGB", (text_width, text_height), (0, 0, 0))

    txt_img_draw = ImageDraw.Draw(txt_img)
    txt_mask_draw = ImageDraw.Draw(txt_mask, mode="RGB")
    txt_mask_draw.fontmode = "1"

    colors = [ImageColor.getrgb(c) for c in text_color.split(",")]
    c1, c2 = colors[0], colors[-1]

    fill = (
        rnd.randint(min(c1[0], c2[0]), max(c1[0], c2[0])),
        rnd.randint(min(c1[1], c2[1]), max(c1[1], c2[1])),
        rnd.randint(min(c1[2], c2[2]), max(c1[2], c2[2])),
    )

    stroke_colors = [ImageColor.getrgb(c) for c in stroke_fill.split(",")]
    stroke_c1, stroke_c2 = stroke_colors[0], stroke_colors[-1]

    stroke_fill = (
        rnd.randint(min(stroke_c1[0], stroke_c2[0]), max(stroke_c1[0], stroke_c2[0])),
        rnd.randint(min(stroke_c1[1], stroke_c2[1]), max(stroke_c1[1], stroke_c2[1])),
        rnd.randint(min(stroke_c1[2], stroke_c2[2]), max(stroke_c1[2], stroke_c2[2])),
    )

    for i, p in enumerate(splitted_text):
        txt_img_draw.text(
            (sum(piece_widths[0:i]) + i * character_spacing * int(not word_split), 0),
            p,
            fill=fill,
            font=image_font,
            stroke_width=stroke_width,
            stroke_fill=stroke_fill,
        )
        txt_mask_draw.text(
            (sum(piece_widths[0:i]) + i * character_spacing * int(not word_split), 0),
            p,
            fill=((i + 1) // (255 * 255), (i + 1) // 255, (i + 1) % 255),
            font=image_font,
            stroke_width=stroke_width,
            stroke_fill=stroke_fill,
        )

    if fit:
        return txt_img.crop(txt_img.getbbox()), txt_mask.crop(txt_img.getbbox())
    else:
        return txt_img, txt_mask

list_char_bool= {}#对当前单字的字行是否在biaosong.ttf进行判断，如果在则为True，否则是False
list_char_bool1= {}#对当前单字的字行是否在cao.ttf进行判断，如果在则为True，否则是False
list_char_bool2= {}#对当前单字的字行是否在hang.TTF进行判断，如果在则为True，否则是False
list_char_bool3= {}#对当前单字的字行是否在kai.TTF进行判断，如果在则为True，否则是False
list_char_bool4= {}#对当前单字的字行是否在li.TTF进行判断，如果在则为True，否则是False
list_char_bool5= {}#对当前单字的字行是否在SourceHanSans-Normal.ttf进行判断，如果在则为True，否则是False
list_dict=[]
list_dict.append(list_char_bool)
list_dict.append(list_char_bool1)
list_dict.append(list_char_bool2)
list_dict.append(list_char_bool3)
list_dict.append(list_char_bool4)
list_dict.append(list_char_bool5)

strs='../trdg/fonts/cn/'
font_all = ['biaosong.ttf', 'cao.ttf', 'hang.TTF', 'kai.TTF',
            'li.TTF', 'SourceHanSans-Normal.ttf']

def _generate_vertical_text(
    text: str,
    font: str,
    text_color: str,
    font_size: int,
    space_width: int,
    character_spacing: int,
    fit: bool,
    stroke_width: int = 0,
    stroke_fill: str = "#282828",
    fonts_wg:int =0
) -> Tuple:
    list_font = []
    list_size = []

    for i in range(6):#对每一个单字的大小进行随机
        temps=random.randint(68, font_size)
        image_font = ImageFont.truetype(font=font, size=temps)
        list_font.append(image_font)
        list_size.append(temps)

    space_height = int(get_text_height(image_font, " ") * space_width)
    char_heights=[]
    random_height=[]
    temp_width = []

    for c in text:
        if c != " " :
            temp=random.randint(0,5)
            list_gj=[]
            temp_c = list_dict[0].__contains__(c)
            temp_c1 = list_dict[1].__contains__(c)
            temp_c2 = list_dict[2].__contains__(c)
            temp_c3 = list_dict[3].__contains__(c)
            temp_c4 = list_dict[4].__contains__(c)
            temp_c5 = list_dict[5].__contains__(c)
            list_gj.append(temp_c)
            list_gj.append(temp_c1)
            list_gj.append(temp_c2)
            list_gj.append(temp_c3)
            list_gj.append(temp_c4)
            list_gj.append(temp_c5)

            vgs = list_font[temp]
            for i in range(0,6):
                if list_gj[i]==True:
                    if list_dict[i][c]==True:
                        list_font[temp] = ImageFont.truetype(font=strs+font_all[i], size=list_size[temp])
                        break
                ggg=list_dict[i][c]=decide_font(strs + font_all[i], c)
                if ggg==True:
                    list_font[temp] = ImageFont.truetype(font=strs+font_all[i], size=list_size[temp])
                    #break
                else:
                    list_font[temp] = ImageFont.truetype(font='../trdg/fonts/SimSun-ExtB.ttf', size=list_size[temp])#如果上述6种字体都无法显示，则用SimSun-ExtB.ttf来显示

            random_height.append(temp)
            char_heights.append(get_text_height(list_font[temp], c))
            temp_width.append(get_text_width(list_font[temp], c))

            list_font[temp]=vgs
        else:
            char_heights.append(space_height)


    ran_height=random.randint(1, 10)
    for i in range(len(char_heights)):
        if ran_height>=0:
            twic_ran_height = random.randint(7, 9)
            char_heights[i]=round(char_heights[i]*((twic_ran_height+1.1)/10))#原来是0.9


    stroke_width=stroke_width
    text_width =90
    if len(temp_width)==0:
        text_width=90
    else:
        text_width = max(temp_width)


    text_height = sum(char_heights) + character_spacing * len(text)+10
    #text_height = sum(char_heights) + character_spacing * len(text) + 30

    txt_img = Image.new("RGBA", (text_width, text_height), (0, 0, 0, 0))
    txt_mask = Image.new("RGBA", (text_width, text_height), (0, 0, 0, 0))

    txt_img_draw = ImageDraw.Draw(txt_img)
    txt_mask_draw = ImageDraw.Draw(txt_mask)
    txt_mask_draw.fontmode = "1"

    colors = [ImageColor.getrgb(c) for c in text_color.split(",")]
    c1, c2 = colors[0], colors[-1]

    fill = (
        rnd.randint(c1[0], c2[0]),
        rnd.randint(c1[1], c2[1]),
        rnd.randint(c1[2], c2[2]),
    )

    stroke_colors = [ImageColor.getrgb(c) for c in stroke_fill.split(",")]
    stroke_c1, stroke_c2 = stroke_colors[0], stroke_colors[-1]

    stroke_fill = (
        rnd.randint(stroke_c1[0], stroke_c2[0]),
        rnd.randint(stroke_c1[1], stroke_c2[1]),
        rnd.randint(stroke_c1[2], stroke_c2[2]),
    )


    for i, c in enumerate(text):
        random_pro=0.95
        vgs = list_font[random_height[i]]
        if list_dict[fonts_wg][c]==False:
            for j in range(0, 6):
                if list_dict[j][c]==True:
                    list_font[random_height[i]] = ImageFont.truetype(font=strs+font_all[j], size=list_size[random_height[i]])
                    break
                list_font[random_height[i]] = ImageFont.truetype(font='../trdg/fonts/SimSun-ExtB.ttf',size=list_size[random_height[i]])

        txt_img_draw.text(
            (0, sum(char_heights[0:i])*random_pro + i * character_spacing),
            c,
            fill=fill,
            font=list_font[random_height[i]],
            stroke_width=stroke_width,
            stroke_fill=stroke_fill,
        )
        txt_mask_draw.text(
            (0, sum(char_heights[0:i])*random_pro + i * character_spacing),
            c,
            fill=((i + 1) // (255 * 255), (i + 1) // 255, (i + 1) % 255),
            font=list_font[random_height[i]],
            stroke_width=stroke_width,
            stroke_fill=stroke_fill,
        )
        list_font[random_height[i]]=vgs

    if fit:
        return txt_img.crop(txt_img.getbbox()), txt_mask.crop(txt_img.getbbox())
    else:
        return txt_img, txt_mask
