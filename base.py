from googletrans import Translator
import pykakasi
import fugashi


def japanese_to_chinese(text):
    translator = Translator()
    translation = translator.translate(text, src='ja', dest='zh-cn')
    chinese_text = translation.text
    return chinese_text

def chinese_to_japanese(text):
    translator = Translator()
    translation = translator.translate(text, src='zh-cn', dest='ja')
    japanese_text = translation.text
    return japanese_text

def convert_to_hiragana_and_romaji(japanese_text):
    kks = pykakasi.kakasi()
    converted  = kks.convert(japanese_text)
    hiragana_text = ''.join([item['hira'] for item in converted])
    romaji_text = "".join([item["hepburn"] for item in converted])
    return hiragana_text, romaji_text

def exec(name, lyrics):
    with open("{}.txt".format(name), "w", encoding="utf-8") as file:
        for line in lyrics:
            file.write(japanese_to_chinese(line) + '\n')
            file.write(line + '\n')
            hiragana_text, romaji_text = convert_to_hiragana_and_romaji(line)
            file.write(hiragana_text + '\n')
            file.write(romaji_text + '\n')
            file.write('\n')