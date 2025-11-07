def manipulating():
    # Manipulating Words:
    # Given the string info = "Python is fun. Fun is good. Good is subjective.",
    info = "Python is fun. Fun is good. Good is subjective."
    # a. Extract the word 'subjective' without knowing its exact position.
    print(info.split()[-1])
    # b. Extract every third word.
    print(info.split()[::3])
    # c. Reverse the positions of the words, but keep the characters in each word in the same order.
    ' '.join(info.split()[::-1])