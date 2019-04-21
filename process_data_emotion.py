import re

FOLDER = "C:\\Users\\rodri\\BeachHacks2019\\data"

EMOTIONS = [
    "anger",
    "fear",
    "joy",
    "sad",
]

FILE_LOCATION = [FOLDER + "\\" + name + "_label\\" + name + "_train.txt" for name in EMOTIONS]


def __main__():
    for index, location in enumerate(FILE_LOCATION):
        with open(location, 'r', encoding="utf8", errors="ignore") as file:
            count = 0
            file_name = FOLDER + "\\" + EMOTIONS[index] + "_label\\" + EMOTIONS[index] + "_"
            for line in file:
                # update count
                count += 1
                # removing first word and last two words to format data
                line = line.split('	', 1)[1]
                line = line.rsplit('	', 2)[0]
                # Remove unicode errors in data
                line = re.sub('(&#[0-9]*?;)', '', line)
                # Remove tweet mentions (@s)
                line = re.sub('(@[._]*? )', '', line)
                # Remove hashtags
                line = re.sub('(#[\\w]*[ ]?)', '', line)
                # Remove undefined characters (due to emoji's or different keyboard languages
                line = re.sub('([^A-Za-z\\w\\d\\s\'?!\".,-_@#*&^$%+=£()~])', '', line)

                file = open(file_name + str(count) + ".txt", 'w', encoding="utf8", errors="ignore")
                file.write(line)
                file.close()


if __name__ == '__main__':
    __main__()
