def process_words():
    from words import word_string
    words = word_string.split(',')
    # handle first word
    words[0] = words[0][2:7] 
    # handle the rest of the words
    for i in range(1, len(words)):
        words[i] = words[i][1:6]

    words.sort(key  = lambda x: len(set(x)), reverse=True)
    return words

def guess_word(words, criteria):
    for word in words:
        if meets(word, criteria):
            return word
    return 'no match!'

def meets(word, criteria):
    for letter in criteria:
        for num in criteria[letter]:
            if num == 0:
                if letter in word:
                    return False
            elif num > 0:
                pos = num - 1
                if word[pos] != letter:
                    return False
            elif num < 0:
                if letter not in word:
                    return False
                pos = -num - 1
                if word[pos] == letter:
                    return False
    return True



if __name__ == "__main__":
    from collections import defaultdict

    info = defaultdict(list)
    words = process_words()

    guess = 'crane'

    while True:
        print(guess.upper())
        s = input().strip()
        s = list(s)
        assert len(s) == 5
        for i, code in enumerate(s):
            if code == '0':
                # corresponds to grey
                if not any(x > 0 or x < 0 for x in info[guess[i]]):
                    info[guess[i]].append(0)
            elif code == '1':
                # corresponds to yellow
                info[guess[i]].append(-(i+1))
            elif code == '2':
                # corresponds to green
                info[guess[i]] = [i+1]

        guess = guess_word(words, info)
