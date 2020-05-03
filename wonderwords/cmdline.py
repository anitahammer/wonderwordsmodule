import argparse
import random_word
import random_sentence

def main():
    random_word_class = random_word.random_word()
    random_sentence_class = random_sentence.random_sentence()

    # Create the parser
    my_parser = argparse.ArgumentParser(prog='wonderwords',
                                        description='Random word and sentence generation')

    # Add the arguments
    my_parser.add_argument('Mode',
                           metavar='mode',
                           type=str,
                           help='the mode of the generation: rw (random word), rl (random words list), rs (random sentence)')

    my_parser.add_argument('-n',
                           action='store_true',
                           help='include nouns (rw or rl)')

    my_parser.add_argument('-v',
                           action='store_true',
                           help='include verbs (rw or rl)')

    my_parser.add_argument('-a',
                           action='store_true',
                           help='include adjectives (rw or rl)')

    my_parser.add_argument('-min',
                           action='store',
                           type=int,
                           help='minimum word length (rw or rl)')

    my_parser.add_argument('-max',
                           action='store',
                           type=int,
                           help='maximum word length  (rw or rl)')

    my_parser.add_argument('-amount',
                           action='store',
                           type=int,
                           help='length of the random words list (rl)')

    my_parser.add_argument('-sw',
                           action='store',
                           type=str,
                           help='what letter you want the word to start with (rw)')

    my_parser.add_argument('-stype',
                           action='store',
                           type=str,
                           help='sentence type: bb (bare bone), ss (simple sentence), bba (bare bone with adjective), s (sentence)')

    # Execute parse_args()
    args = vars(my_parser.parse_args())

    # Now for the logic
    if args['Mode'] == 'rw':
        pos_options = {'n': 'noun', 'v': 'verb', 'a': 'adjective'}

        pos_str = ''

        for key, value in pos_options.items():
            if args[key]:
                pos_str += f" {value}"

        if args['min'] is not None:
            len_min = args['min']
        else:
            len_min = 0

        if args['max'] is not None:
            len_max = args['max']
        else:
            len_max = 0

        if args['sw'] is None:
            print(random_word_class.word(include_parts_of_speech=pos_str, word_min_length=len_min, word_max_length=len_max))
        else:
            if len['sw'] != 1:
                print('Please choose ONE letter for the -sw parameter')
                quit()
            else:
                print(random_word_class.starts_with(letter=args['sw'], include_parts_of_speech=pos_str, word_min_length=len_min, word_max_length=len_max))
    elif args['Mode'] == 'rl':
        if args['amount'] is not None:
            list_len = args['amount']
        else:
            list_len = 1

        pos_options = {'n': 'noun', 'v': 'verb', 'a': 'adjective'}

        pos_str = ''

        for key, value in pos_options.items():
            if args[key]:
                pos_str += f" {value}"

        if args['min'] is not None:
            len_min = args['min']
        else:
            len_min = 0

        if args['max'] is not None:
            len_max = args['max']
        else:
            len_max = 0

        print(random_word_class.words_list(amount=list_len, include_parts_of_speech=pos_str, word_min_length=len_min, word_max_length=len_max))


    elif args['Mode'] == 'rs':
        sentence_type_options = ['bb', 'ss', 'bba', 's']

        if args['stype'] is None:
            sentence_type = sentence_type_options[3]
        else:
            if args['stype'] not in sentence_type_options:
                print('Please choose a valid sentence type (bb, ss, bba, s). Type "wonderwords -h" for help')
                quit()
            else:
                sentence_type = args['stype']

        if sentence_type == 'bb':
            print(random_sentence_class.bare_bone_sentence())
        elif sentence_type == 'ss':
            print(random_sentence_class.simple_sentence())
        elif sentence_type == 'bba':
            print(random_sentence_class.bare_bone_with_adjective())
        else:
            print(random_sentence_class.sentence())
    else:
        print(f"The mode '{args['Mode']}' is invalid\nPlease choose a valid mode or type 'wonderwords -h' for help")
        quit()

if __name__ == '__main__':
    main()
