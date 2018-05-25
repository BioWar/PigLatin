import time
t1 = time.time()


class PigLatin:

    def __init__(self, text: str):
        self.consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
        self.vowels = ['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y']
        self.vowels_ending = "yay"
        with open("words.txt", "r") as dictionary_src:
            self.dictionary = dictionary_src.read()
            self.dictionary = self.dictionary.split("\n")
            self.dictionary = [word.lower() for word in self.dictionary]
        self.text = text.lower()
        self.pig_latin_text = ""

    def __str__(self):
        return str(self.text)

    def pig_word(self, word):
        current = 0
        if word[0] in self.consonants:
            letter = ""
            for i in range(len(word)):
                if word[i] in self.consonants:
                    letter += word[i]
                    current = i+1
                else:
                    break
            pig = str(str(word[current:])+str(letter.lower()+"ay"))
        elif word[0] in self.vowels:
            pig = str(str(word) + self.vowels_ending)
        else:
            pig = word
        return pig

    def pig_latin_encr(self):
        ls = self.text.split(" ")
        result = list()
        for word in ls:
            result.append(self.pig_word(word))

        self.pig_latin_text = result = " ".join(result)
        return result


    def human_word(self, word):
        if len(word) >= 3:
            variant_1 = str(word[-3] + word[:len(word)-3])
            variant_2 = str(word[-4:-2] + word[:len(word)-4])
            variant_3 = str(word[-5:-2] + word[:len(word)-5])
            if word[-3:] == self.vowels_ending:
                return word[:len(word)-3]
            elif variant_1 in self.dictionary:
                return str(word[-3] + word[:len(word)-3])
            elif variant_2 in self.dictionary:
                return str(word[-4:-2] + word[:len(word)-4])
            elif variant_3 in self.dictionary:
                return str(word[-5:-2] + word[:len(word)-5])
            else:
                return word
        else:
            return word


    def pig_latin_decrypt(self):
        ls = [word for word in self.pig_latin_text.split(" ")]
        result = list()
        for word in ls:
            result.append(self.human_word(word))
        result = " ".join(result)
        return result


with open("Text.txt", "r") as file:
    text = file.read()

input_text = PigLatin(text)
pig_text = input_text.pig_latin_encr()
human_text = input_text.pig_latin_decrypt()

print("1 Input Text\n", input_text, "\n")
print("2 Pig Latin Text\n", pig_text, "\n")
print("3 Pig Text in Input Text\n", human_text, "\n")

print("Symbols: ", len(text))
print("Words: ", len([word for word in text.split(" ")]))
print("Time: ", time.time() - t1)