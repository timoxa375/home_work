message = 'Hello!Anthony!Have!A!Good!Day!'
message = message.upper()
words = message.split('!')
words.remove('')
words.sort()
for word in words:
    print(word)