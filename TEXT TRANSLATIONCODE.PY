from googletrans import Translator

def translate_text(text, src_language, dest_language):
    translator = Translator()
    try:
        translation = translator.translate(text, src=src_language, dest=dest_language)
        return translation.text
    except Exception as e:
        return f"Error during translation: {e}"

if __name__ == "__main__":
    # Example usage
    source_text = "Hello, how are you?"
    source_lang = "en"  # English
    target_lang = "es"  # Spanish

    translated_text = translate_text(source_text, source_lang, target_lang)
    print(f"Original ({source_lang}): {source_text}")
    print(f"Translated ({target_lang}): {translated_text}")