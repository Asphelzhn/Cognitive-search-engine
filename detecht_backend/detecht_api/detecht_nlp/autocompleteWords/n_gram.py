import re
import string
import operator
import time

# from detecht_api import models
# from detecht_backend.detecht_api import models
'''
By Severn
'''


def cleanText(input):
    input = re.sub('\n+', " ", input).lower()  # Match line breaks
    # with spaces to replace spaces
    input = re.sub('[[0-9]*]', "", input)  # Eliminate reference
    # tags like [1]p
    input = re.sub(' +', " ", input)  # Replace consecutive spaces
    # with one space
    # input = bytes(input)#.encode('utf-8') # Convert content to utf-8
    # format to eliminate escape characters
    # input = input.decode("ascii", "ignore")
    return input


def cleanInput(input):
    input = cleanText(input)
    cleanInput = []
    input = input.split(' ')  # Return the list with spaces as separators
    for item in input:
        item = item.strip(string.punctuation)  # string.punctuation
        # gets all punctuation

        if len(item) > 1 or (
                item.lower() == 'a' or item.lower() == 'i'):  # Find words,
            # including i, a, etc.
            cleanInput.append(item)
    return cleanInput


def getNgrams(input, n):
    input = cleanInput(input)

    output = {}
    for j in range(2, n):
        for i in range(len(input) - j + 1):
            ngramTemp = " ".join(input[i:i + j])  # .encode('utf-8')
            if ngramTemp not in output:  # Word frequency statistics
                output[ngramTemp] = 0  # Typical dictionary operation
            output[ngramTemp] += 1
    return output


def get_result(query):
    lines = open("result_1.txt").readlines()
    suggestions = []
    pattern = '.*'.join(query)
    regex = re.compile(pattern)
    i = 0
    q = query.split()
    length = len(q)
    for line in lines:
        s = line.split()
        s_sub = []
        w = ""
        for m in range(length):
            s_sub.append(s[m])
        w.join(s_sub)
        if w == query:
            suggestions.append(re.sub('\n+', " ", line))
            i += 1
        if i > 7:
            break
    return suggestions


if __name__ == '__main__':
    t1 = time.clock()
    content = open("big.txt").read()
    ngrams = getNgrams(content, 5)
    sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1),
                          reverse=True)  # =True descending sort
    '''
    with open("result.txt","w") as f:
        for key, value in ngrams.items():
            f.write(key+":"+str(value))
            f.write('\n')
    '''

    with open("result_1.txt", "w") as f:
        for s in sortedNGrams:
            if s[1] > 1:
                f.write(str(s[0]))
                f.write('\n')
    t2 = time.clock()
    print(t2 - t1)
    '''
    for s in sortedNGrams:
        if s[1] > 1:
            models.Search_Autocomplete.add_row(str(s[0]), int(s[1]))
    # print(sortedNGrams)
    '''
