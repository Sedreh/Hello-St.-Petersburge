import sys


def main(args):
    cmd = args[1]
    cmdargs = args[2:]

    dictionary = []
    # This part is reading dictionary from the file
    with open("dict.tr", "r") as file:
        for line in file:
            # spliting line to each type of languages
            languages = line.split()
            word = {}
            # here I seperate each language from word with colon.
            for language in languages:
                language = language.split(":")
                word[language[0].lower()] = language[1]
            dictionary.append(word)
            # This part add new words to dictionary
    if cmd == '+':
        # Each language will have one word, so if we divide the length of arguments for this command
        # it will shows the number of languages that we add to dictionary.
        number_of_languages = int(len(cmdargs) / 2)
        word = {}
        for i in range(number_of_languages):
            language_index = i * 2
            word_index = (i * 2) + 1
            word[cmdargs[language_index].lower()] = cmdargs[word_index]
        dictionary.append(word)
        with open("dict.tr", "w") as file:
            for word in dictionary:
                file.write(" ".join([key + ':' + value for key, value in word.items()]) + "\n")
    elif cmd == '?':
        from_language = cmdargs[0].lower()
        to_language = cmdargs[1].lower()
        from_phrase = cmdargs[2:]
        to_phrase = []
        error = False
        dictionary = [item for item in dictionary if from_language in item]
#check if word exsist from_language and its translation exists in to_language.
        for word in from_phrase:
            from_word_exists = False
            to_word_exists = False
            for item in dictionary:
                if item[from_language] == word:
                    from_word_exists = True
                    if to_language in item:
                        to_word_exists = True
                        to_phrase.append(item[to_language])

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
