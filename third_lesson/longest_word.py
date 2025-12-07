def longest_word(string_of_words):
    words = string_of_words.split()
    max_word = words[0]
    for word in words:
        if len(word) >= len(max_word):
            max_word=word
    return(max_word)       

long = longest_word("hello and mello")
print(long)