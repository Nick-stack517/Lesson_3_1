calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(str_):
    count_calls()
    # len_ =len(str_)
    # string_up = str_.upper()
    # string_low = str_.lower()
    #tuple_ = (len_, string_up, string_low)
    # return tuple_
    return (len(str_), str_.upper(), str_.lower())


def is_contains(string, list_to_search):
    count_calls()
    str_ = string.upper()

    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].upper()

    flag = str_ in list_to_search
    return flag


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
