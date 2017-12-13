
bigrams =[[0 for col in range(26)] for row in range(26)]
words = 'abcdefghijklmnopqrstuvwxyz'
total_pair = 0

for a in range(1,450):
    fp = open('english/%d.txt' % a, 'r')
    char = fp.read()

    for num in range(len(char)):
        for i in range(26):
            for j in range(26):
                if char[num] is not None:
                    if char[num] == words[i] and char[num+1] == words[j]:
                        bigrams[i][j] += 1
                        total_pair += 1
    fp.close()

print('the frequency of each bigram is:')
print('\t',end='')
for i in range(26):
    print(words[i] + '\t', end='')

for i in range(26):
    print()
    print(words[i] + '\t', end='')
    for j in range(26):
        print(str(bigrams[i][j]/total_pair*100) + '\t', end='')
