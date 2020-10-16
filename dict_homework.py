# 1
# sentence = input('Enter a sentence: ')
# splitted = sentence.split(' ')
# occurrence = {}
# for word in splitted:
#     if not (word in occurrence):
#         occurrence[word] = 1
#     else:
#         occurrence[word] += 1
# print('Result:')
# for word, times in occurrence.items():
#     print(word, times)

#2
# sentence = input('Enter a sentence: ')
# splitted = sentence.split(' ')
# occurrence = {}
# for word in splitted:
#     if not word.lower() in occurrence:
#         occurrence[word.lower()] = 1
#     else:
#         occurrence[word.lower()] += 1
# print('Result:')
# for word, times in occurrence.items():
#     print(word, times)

#3
# dictionary = {
#     "Programmer": "Someone Who Solves a Problem You Didn't Know You Had, in a Way You Don't Understand",
#     "Python": "a general-purpose interpreted, interactive, object-oriented, and high-level programming language"
# }
#
# while True:
#     print('Simple dictionary program, choose an option and press ENTER')
#     print('1 - Look up a word')
#     print('2 - Add a word')
#     print('0 - Exit')
#     choice = input('Your choice: ')
#     if choice == '1':
#         word = input('Enter the word you want to search: ')
#         if word in dictionary:
#             print(f'{word}: {dictionary[word]}')
#         else:
#             print(f'{word} does not exist')
#     elif choice == '2':
#         word = input('Enter the new word: ')
#         meaning = input(f"{word}'s definition: ")
#         dictionary[word] = meaning
#         print('Successfully added')
#     elif choice == '0':
#         print('Goodbye')
#         break
#     else:
#         print("I don't understand")

#4
dictionary = {
    "Argument": "a disagreement, or the process of disagreeing",
    "Comment": "something that you say or write that expresses your opinion"
}

while True:
    print('Simple dictionary program, choose an option and press ENTER')
    print('1 - Look up word')
    print('2 - Add a word')
    print('0 - Exit')
    choice = input('Your choice: ')
    if choice == '1':
        word = input('Enter the word you want to search: ')
        print('Result:')
        for w in dictionary:
            if word.lower() in w.lower():
                print(f'{w}: {dictionary[w]}')

    elif choice == '2':
        word = input('Enter the new word: ')
        meaning = input(f"{word}'s definition: ")
        dictionary[word] = meaning
        print('Successfully added')
    elif choice == '0':
        print('Goodbye')
        break
    else:
        print("I don't understand")
