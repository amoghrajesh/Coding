import inflect
inflect = inflect.engine()

english_words = ["hat", "hats",
                 "hero", "heroes",
                 "cherry", "cherries",
                 "dish", "dishes",
                 "stadium", "stadia", "stadiums",
                 "mitochondrion", "mitochondria",
                 "sheep", "a sheep", "the sheep",
                 "whjkjhkjh", "msipelling","half","halves"]

for en in english_words:
    if inflect.singular_noun(en) is False: #false means singular
        print (en, "is singular")
    else:
        print (en, "is plural")