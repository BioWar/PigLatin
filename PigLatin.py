def pig_latin_eng(text:str) -> str:
    first = "B C D F G H J K L M N P Q R S T V W X Z".split(" ")
    first_l = [i.lower() for i in first]
    first += first_l
    second = "A E I O U Y".split(" ")
    second_l = [i.lower() for i in second]
    second += second_l
    ls = text.split(" ")
    result = list()
    for word in ls:
        if word[0] in first:
            print(str(word[1:])+str(word[0])+"ay")
            result.append(str(str(word[1:])+str(word[0])+"ay"))
        elif word[0] in second:
            result.append(str(str(word) + "way"))
        else:
            print("NotLatinWordError")

    result = " ".join(result)
    return result

with open("Text.txt", "r") as file:
    text = file.read()
print(pig_latin_eng(text))
