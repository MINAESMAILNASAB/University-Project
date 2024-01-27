input = input().split()

sentence = 'Formatted Text: '
for i in input:
    sentence += i
    sentence += ' '

sentence = list(sentence)
count = 0
for ozv in sentence:
    if ozv == '@':
        for i in range(count, len(sentence)):
            if sentence[i] == '#':
                sentence[i] = ''
                break
    count +=1


sentence = ''.join(sentence)
sentence = sentence.split('\\n')
for element in sentence:
    print(element)