import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'detecht_backend.settings'
import django

django.setup()
import re
import string

'''
By Severn
'''


def cleanText(input):
    input = re.sub('\n+', " ", input).lower()  # Match line breaks with spaces to replace spaces
    input = re.sub('\[[0-9]*\]', "", input)  # Eliminate reference tags like [1]p
    input = re.sub(' +', " ", input)  # Replace consecutive spaces with one space
    # input = bytes(input)#.encode('utf-8') # Convert content to utf-8 format to eliminate escape characters
    # input = input.decode("ascii", "ignore")
    return input


def cleanInput(input):
    input = cleanText(input)
    cleanInput = []
    input = input.split(' ')  # Return the list with spaces as separators
    for item in input:
        item = item.strip(string.punctuation)  # string.punctuation gets all punctuation

        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):  # Find words, including i, a, etc.
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



