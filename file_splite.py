import re
import linecache


def file_splite():
    # inputfile = input('Input Source File:')
    fp = open('english.txt', 'r')

    number = []
    lineNumber = 0
    # keyword = input('Slice Keyword:')
    # outfileName = input('Outfile Name:')

    for eachLine in fp:
        m = re.search('text id=', eachLine)
        if m is not None:
            number.append(lineNumber)
        lineNumber += 1
    number.append(lineNumber)

    size = int(len(number))
    for i in range(1, size):
        start = number[i-1]
        end = number[i]
        destLines = linecache.getlines('english.txt')[start:end]
        fp_w = open('english/' + str(i) + '.txt', 'w')
        for key in destLines:
            fp_w.write(re.sub('<[A-Za-z\/][^>]*>', '', key))
        fp_w.close()


if __name__ == "__main__":
    file_splite()
