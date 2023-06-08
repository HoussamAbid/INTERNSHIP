from translate import Translator

Languages = ['fr', 'it', 'es', 'ru', 'de']


text=input('Put the text u wanna translate :')
for language in Languages:
    translator = Translator(provider='libre', from_lang="en", to_lang=language)
    translation = translator.translate (text)
    print (f' (Language): {translation}')