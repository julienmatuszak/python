# [x] create words after "G" following the Assignment requirements use of functions, menhods and kwyowrds
# sample quote "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)
# [x] copy and paste in edX assignment page

def words_after_g(quote):
    a = ""
    result = ""
    start = 0
    space_index = quote.find(" ")
    while space_index != -1:
        word = quote[start:space_index]
        if word[0].lower() <= "g":
            result += ""
        else:
            for x in word:
                if x.isalpha() is False:
                    result += ""
                result += x
            result += "\n"
        start = space_index+1
        space_index = quote.find(" ",start)
    result += quote[start:]
    print(result.upper())

quote = input("enter a 1 sentence quote, non-alpha separate words : ")
words_after_g(quote)
