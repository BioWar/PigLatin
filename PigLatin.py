import random


class PigLatin:

    def __init__(self, text: str):
        self.first = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
        self.second = ['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y']
        self.text = text

    def pig_word(self, word):
        pig = ""
        curr = 0
        if word[0] in self.first:
            lett = ""
            for i in range(len(word)):
                if word[i] in self.first:
                    lett += word[i]
                    curr = i+1
                else:
                    break
            pig = str(str(word[curr:])+str(lett.lower()+"ay"))
        elif word[0] in self.second:
            pig = str(str(word) + random.choice(["way", "yay", "hay", "ay"]))
        return pig

    def pig_latin_encr(self):
        ls = self.text.split(" ")
        result = list()
        for word in ls:
            result.append(self.pig_word(word))

        result = " ".join(result)
        return result

    # def pig_latin_decr(text:str) -> str:
    #     first = "B C D F G H J K L M N P Q R S T V W X Z".split(" ")
    #     first_l = [i.lower() for i in first]
    #     first += first_l
    #
    #     second = "A E I O U Y".split(" ")
    #     second_l = [i.lower() for i in second]
    #     second += second_l
    #
    #     ls = text.split(" ")
    #     print(ls)
    #     result = list()
    #
    #     for word in ls:
    #         pass

with open("Text.txt", "r") as file:
    text = file.read()
piggy = PigLatin(text)
print(piggy.pig_latin_encr())

# text = "DdpDog"
# print(pig_latin_encr(text))
