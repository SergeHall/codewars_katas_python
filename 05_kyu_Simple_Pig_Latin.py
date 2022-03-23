#  Move the first letter of each word to the end of it, then add "ay" to the
#  end of the word. Leave punctuation marks untouched.
#
# Examples
#
# pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
# pigIt('Hello world !');     // elloHay orldway !

def pig_it(text):
    words = text.split(" ")
    new_w = []

    for word in words:
        if word.isalpha():
            cur_new_word = word[1:] + word[0] + "ay"
            new_w.append(cur_new_word)
        else:
            new_w.append(word)

    return " ".join(new_w)
