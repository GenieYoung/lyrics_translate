import base

def main():
    chinese_text = input("chinese_text : ")
    japanese_text = base.chinese_to_japanese(chinese_text)
    hiragana_text, romaji_text = base.convert_to_hiragana_and_romaji(japanese_text)
    print(f"japanese_text: {japanese_text}")
    print(f"hiragana_text: {hiragana_text}")
    print(f"romaji_text  : {romaji_text}")


if __name__ == "__main__":
    main()