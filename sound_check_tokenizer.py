import sys
from nltk.tokenize import TreebankWordTokenizer
from collections import defaultdict

# Processing text messages with average < 500 words, therefore using dicts for tokens. Can
# later change to tries for larger samples.


def __main__():

    # check that a proper filename was given as an argument
    if len(sys.argv) < 2:
        print("No text file was inputted, please type the name of the file you wish to tokenize as the first command-line argument.")
    elif not sys.argv[1].endswith('.txt'):
        print("File is not a proper text file, please check your file name and try again.")
    else:
        # Create tokenizer based on Penn Treebank
        tokenizer = TreebankWordTokenizer()

        # Opening and reading a file
        filename = sys.argv[1]
        word_count = defaultdict(int)
        tokens = list()

        with open(filename, 'r', encoding="utf8") as input_text:
            for line in input_text:
                # Tokenize
                tokens = tokenizer.tokenize(line)

                for token in tokens:
                    word_count[token.lower()] += 1
        # sorting dict based on (inverted) values and then keys (alphabetically)
        output = sorted(word_count.items(), key=lambda pair: (-pair[1], pair[0]))
        for item in output:
            print('\t{} - {}'.format(item[0], item[1]))

        return tokens


def tone_analysis(file, tokens):

    pass


if __name__ == '__main__':
    __main__()
