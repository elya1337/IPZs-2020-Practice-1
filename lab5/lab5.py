import platform
import ipaddress
import pytest


def prime_num_generator():
    for n in range(2, 1000):  # n starts from 2 to end
        for x in range(2, n):  # check if x can be divided by n
            if n % x == 0:  # if true then n is not prime
                break
        else:  # if x is found after exhausting all values of x
            yield n
        n += 1


a = prime_num_generator()
b = prime_num_generator()
i = 0;
needed_num = 0;
while (i <= 101):
    needed_num = next(b)
    print(needed_num)
    i = i + 1


# task 1


@pytest.mark.parametrize("expected_result", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
def test_prime_num_generator(expected_result):
    assert next(a) == expected_result


@pytest.mark.parametrize("expected_result", [557])
def test_prime_num_generator_2(expected_result):
    assert needed_num == expected_result


def palindrome(text):
    # put the words from input to word list

    word_list = []
    temp = ''
    for i, v in enumerate(text):
        if v.isalpha():  # checking is it every character is from alphabet
            temp += v
            if i == len(text) - 1 and temp.isalpha():
                word_list.append(temp)  # add to the temporary variable
        else:  # if it's not the character is alphabet, add our word to wordlist, and clear the temp variable
            word_list.append(temp)
            temp = ''

    # checking is the word is palindrome

    pal_words = []
    for i in word_list:
        reversed_word = i[::-1]  # making words reversed
        if len(i) < 3:
            break
        if reversed_word == i:  # checking is it read same as the original word,if yes add to pal_words
            pal_words.append(i)
    return pal_words


# task 2


@pytest.mark.parametrize("palindrome_func_arg, result", [("add", []), ("adda", ["adda"]), ("ada", ["ada"]), (5, [])])
def test_palindrome(palindrome_func_arg, result):
    try:
        assert palindrome_func_arg != ''
        assert palindrome(palindrome_func_arg) == result
    except TypeError:
        print()
        print()
        print("Неправильний аргумент: int - недійсний тип аргументу")


def validate_ip(ip_address):
    ip_validate = False
    try:
        ip = ipaddress.ip_address(ip_address)
        ip_validate = True
    except ValueError:
        ip_validate = False

    return ip_validate


# task 3


@pytest.mark.parametrize("validate_ip_func_arg, result", [("192.168", False), ("-1.168.1.42", False),
                                                          ("192.400.1.40", False),
                                                          ("192.168.-44.42", False),
                                                          ("192.168.1.420", False)])
def test_validate_ip(validate_ip_func_arg, result):
    assert validate_ip_func_arg != ''
    assert validate_ip(validate_ip_func_arg) == result


def get_os():
    return platform.system()


# task 4

def test_get_os():
    assert get_os() == "Windows"
