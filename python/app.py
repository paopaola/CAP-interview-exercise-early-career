import re

seen_strings = {}

# remove whitespaces and punctuation
# keep only alpha num chars
def format_input(input_string):
    return re.sub(r"[^a-zA-Z0-9]","",input_string)

# get all dict keys having max_value as a value
def get_dict_key(my_dict, max_value):
    char_list = []
    for key, value in my_dict.items():
         if max_value == value:
            char_list.append(key)
    return ', '.join(char_list)

# get chars frequency of a given input
# returns a tuple where the first element is the freq and the second element - all chars having that freq
def get_freq_char(input):
    formatted_input = format_input(input)
    char_freq = {}
    for char in formatted_input:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    max_freq = max(char_freq.values())
    chars = get_dict_key(char_freq, max_freq)
    print(f'Highest frequency of chars in the given string is: {max_freq}\nChars with high frequency: {chars}')
    return (max_freq, chars)

def quit_func():
    print('Exiting...\n')

def get_stats(my_dict):
    if my_dict:
        # get most popular value
        input_list = []
        popular_freq = max(input['freq'] for input in my_dict.values())
        for key, value in my_dict.items():
            if popular_freq == value['freq']:
                input_list.append(key)
        input_list = ', '.join(input_list)
        # get longest string. Only one string it is shown if there are 2 or more strings with same length
        longest_input = max(my_dict, key=lambda input:my_dict[input]['len'])
        print(f'\nStats:\n {my_dict}\n\nMost popular: {input_list}\n\nLongest input received: {longest_input}\n')
    else:
        print('No inputs given.')

#check if given input is palindrome
def is_palindrome(input):
    return input == input[::-1]

def stringinate():
    while True:
        inputResult = input('Enter an input string (\'stats\' to see statistics, \'quit\' to exit): ')
        inputResult = inputResult.strip()
        if inputResult:
            if (inputResult.lower() == "quit"):
                quit_func()
                break
            elif (inputResult.lower() == "stats"):
                get_stats(seen_strings)
            else:
                print('\nInput = %s' % inputResult)
                print('Length = %s' % len(inputResult))
                if inputResult in seen_strings:
                    seen_strings[inputResult]['freq'] += 1
                else:
                    seen_strings[inputResult] = {}
                    seen_strings[inputResult]['freq'] = 1
                    seen_strings[inputResult]['len'] = len(inputResult)
                    seen_strings[inputResult]['char_freq'] = get_freq_char(inputResult.lower())
                    seen_strings[inputResult]['is_palindrome'] = is_palindrome(inputResult)
        else:
            print('No input given.')

if __name__ == '__main__':
    stringinate()