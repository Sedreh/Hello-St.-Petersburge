import sys

available_languages = ['afrikaans', 'albanian', 'amharic', 'arabic', 'aramaic', 'armenian', 'assamese', 'aymara', 'azerbaijani', 'balochi', 'bamanankan', 'bashkort', 'basque', 'belarusan', 'bengali', 'bhojpuri', 'bislama', 'bosnian', 'brahui', 'bulgarian', 'burmese', 'cantonese', 'catalan', 'cebuano', 'chechen', 'cherokee', 'croatian', 'czech', 'dakota', 'danish', 'dari', 'dholuo', 'dutch','english', 'esperanto', 'estonian', 'finnish', 'french', 'georgian', 'german', 'gikuyu', 'greek', 'guarani', 'gujarati', 'haitian', 'hausa', 'hawaiian', 'hawaiian', 'hebrew', 'hiligaynon', 'hindi', 'hungarian', 'icelandic', 'igbo', 'ilocano', 'indonesian', 'inuit', 'irish', 'italian', 'japanese', 'jarai', 'javanese', 'k\xe2\x80\x99iche\xe2\x80\x99', 'kabyle', 'kannada', 'kashmiri', 'kazakh', 'khmer', 'khoekhoekorean', 'kurdish', 'kyrgyz', 'lao', 'latin', 'latvian', 'lingala', 'lithuanian', 'macedonian', 'maithili', 'malagasy', 'malay', 'malayalam', 'mandarin', 'marathi', 'mende', 'mongolian', 'nahuatl', 'navajo', 'nepali', 'norwegian', 'ojibwa', 'oriya', 'oromo', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'quechua', 'romani', 'romanian', 'russian', 'rwanda', 'samoan', 'sanskrit', 'serbianshona', 'sindhi', 'sinhala', 'slovak', 'slovene', 'somali', 'spanish', 'swahili', 'swedish', 'tachelhit', 'tagalog', 'tajiki', 'tamil', 'tatar', 'telugu', 'thai', 'tibetic languages', 'tigrigna', 'tok pisinturkish', 'turkmen', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'warlpiri', 'welsh', 'wolof', 'xhosa', 'yakut', 'yiddish', 'yoruba', 'yucatec', 'zapotec', 'zulu']


def main(args):
    cmd = args[1]
    cmdargs = args[2:]

    error = False


    dictionary = []
    # This part is reading dictionary from the file
    with open("dict.tr", "r") as file:
        for line in file:
            words = []
            colon_separated = line.split(":")
            for colon_word in colon_separated:
                for word in colon_word.strip().split():
                    words.append(word)

            number_of_languages = int(len(words) / 2)
            word = {}
            for i in range(number_of_languages):
                language_index = i * 2
                word_index = (i * 2) + 1

                word[words[language_index].lower()] = words[word_index].lower()
            dictionary.append(word)
    if cmd == '+':
        # Each language will have one word, so if we divide the length of arguments for this command
        # it will shows the number of languages that we add to dictionary.
        number_of_languages = int(round(len(cmdargs) / 2.0))
        word = {}
        for i in range(number_of_languages):
            language_index = i * 2
            word_index = (i * 2) + 1
            if cmdargs[language_index].lower() not in available_languages:
                print('The language ' + cmdargs[language_index].lower() + ' is not supported')
                break
            if word_index >= len(cmdargs):
                error = True
                print('There is no word for language ' + cmdargs[language_index].lower())
            else:
                word[cmdargs[language_index].lower()] = cmdargs[word_index]

        if not error:
            dictionary.append(word)

        with open("dict.tr", "w") as file:
            for word in dictionary:
                file.write(" ".join([key + ':' + value for key, value in word.items()]) + "\n")
    elif cmd == '?':
        from_language = cmdargs[0].lower()
        to_language = cmdargs[1].lower()
        from_phrase = cmdargs[2:]
        to_phrase = []

        dictionary = [item for item in dictionary if from_language in item]

        if from_language not in available_languages:
            error = True
            print('The language ' + from_language + ' is not supported')

        if to_language not in available_languages:
            error = True
            print('The language ' + to_language + ' is not supported')
#check if word exsist from_language and its translation exists in to_language.
        for word in from_phrase:
            from_word_exists = False
            to_word_exists = False
            for item in dictionary:
                if item[from_language] == word.lower():
                    from_word_exists = True
                    if to_language in item:
                        to_word_exists = True
                        if word.isupper():
                            to_phrase.append(item[to_language].upper())
                        elif word.islower():
                            to_phrase.append(item[to_language].lower())
                        elif word[0].isupper():
                            to_phrase.append(item[to_language].capitalize())

            if not from_word_exists:
                error = True
#If one of the word from phrase is not present in froe_language print an error message.
                print("Word " + word + " does not exists for " + from_language)
            elif not to_word_exists:
                error = True
# If one of the words have no translation to to_language  print an error message.
                print("Word " + word + " does not exists for " + to_language)

        if not error:
# Otherwise you should print translated phrase to stdout.
            print(" ".join(to_phrase))
    else:
        print('Unknown command: {cmd}'.format(cmd=cmd))


if __name__ == '__main__':
    main(sys.argv)
