def reverse_words(text):
    words = text.split(" ")
    concatenate_word = ""
    for i in range(len(words)):
        if(i == len(words) - 1):
            concatenate_word += words[i][::-1]
        else:
            concatenate_word += words[i][::-1] + " "
            

    return concatenate_word

print(reverse_words("teste pote"))