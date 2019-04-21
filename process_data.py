import re

FILELOCATION = [
    "C:\\Users\\rodri\\BeachHacks2019\\data\\hate_speech_label\\hate_speech_label.txt",
    "C:\\Users\\rodri\\BeachHacks2019\\data\\not_hate_speech_label\\not_hate_speech_label.txt",
]


def __main__():

    with open(FILELOCATION[0], 'r') as hate_speech_file:
        count = 0
        file_name = "C:\\Users\\rodri\\BeachHacks2019\\data\\hate_speech_label\\hate_speech_"
        for line in hate_speech_file:
            # update count
            count += 1
            # Remove unicode errors in data
            line = re.sub('(&#[0-9]*?;)', '', line)
            # Remove tweet mentions (@s)
            line = re.sub('(@.*? )', '', line)

            file = open(file_name + str(count) + ".txt", 'w')
            file.write(line)
            file.close()


    with open(FILELOCATION[1], 'r') as not_hate_speech_file:
        count = 0
        file_name = "C:\\Users\\rodri\\BeachHacks2019\\data\\not_hate_speech_label\\not_hate_speech_"
        for line in not_hate_speech_file:
            # update count
            count += 1
            # Remove unicode errors in data
            line = re.sub('(&#[0-9]*?;)', '', line)
            # Remove tweet mentions (@s)
            line = re.sub('(@.*? )', '', line)

            file = open(file_name + str(count) + ".txt", 'w')
            file.write(line)
            file.close()


if __name__ == '__main__':
    __main__()
