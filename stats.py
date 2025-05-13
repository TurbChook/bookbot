def word_counter(book_text):
    return len(book_text.split())
def character_counter(text):
    text = text.lower()
    words_dict = {}
    for word in text:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return words_dict
def sort_on(dict):
    return dict["num"]
def character_list(letters):
    sorted_characters = list()
    for letter in letters:
        sorted_characters.append({"char": letter,"num":letters[letter]})
    sorted_characters.sort(reverse=True,key=sort_on)
    return sorted_characters
