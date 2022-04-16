def get_text_info(filepath):
    word_counter = {}
    with open(filepath, "r") as file:
        word_list = []
        temp = ''
        b = file.read().lower()
        for i, v in enumerate(b):
            if v.isalpha():  # checking is it every character is from alphabet
                temp += v
            else:  # if it's not the character is alphabet, add our word to wordlist, and clear the temp variable
                if temp == '':
                    continue
                else:
                    word_list.append(temp)
                    temp = ''

        for word in word_list:
            if word not in word_counter:
                word_counter[word] = 1
            else:
                word_counter[word] = word_counter[word] + 1
        print('{:16}{:3}'.format('Word', 'Count'))
        print('-' * 19)
    for (word, occurance) in word_counter.items():
        print('{:16}{:3}'.format(word, occurance))


get_text_info("article.txt")


import requests

CSV_URL = "https://support.staffbase.com/hc/en-us/article_attachments/360009197031/username.csv"


def download_csv(urlpath):
    with requests.Session() as s:
        download = s.get(urlpath)
        open('source_data/data.csv', 'wb').write(download.content)
        print("Downloaded completed!\n")
    f = open('source_data/data.csv', "r")
    lines = f.readlines()
    lines.pop()
    lines.pop()
    f = open('source_data/data.csv', "w")
    f.writelines(lines)


download_csv(CSV_URL)