import re
import matplotlib.pyplot as plt

def find_groupings(data, target):
    #using regex (?:[a-zA-Z]+[^a-zA-Z]+){0,3}target(?:[^a-zA-Z]+[a-zA-Z]+){0,3}
    #to find what words are before and after the target word

    regex = re.compile(r'(?:[a-zA-Z]+[^a-zA-Z]+){0,3}' + target + r'(?:[^a-zA-Z]+[a-zA-Z]+){0,3}', re.M)

    matches = re.findall(regex, data)

    #removing the target word from the matches
    for i in range(len(matches)):
        matches[i] = matches[i].replace(target, '')


    return matches

def count_occurences(matches, occurrences = {}):
    #break matches into words
    for match in matches:
        words = match.split()

        #count occurrences of each word
        for word in words:
            if word in occurrences:
                occurrences[word] += 1
            else:
                occurrences[word] = 1

    #sort occurrences
    occurrences = dict(sorted(occurrences.items(), key=lambda item: item[1], reverse=True))
    
    return occurrences


def graph_occurences(data):
    #using matplotlib to graph the occurences of the words given in the dictionary
    #graphing the top 20 words

    #getting the top 20 words
    top_20 = list(data.keys())[:30]

    #getting the occurences of the top 20 words
    occurences = list(data.values())[:30]

    #creating the graph
    plt.bar(top_20, occurences)
    plt.xticks(rotation=90)
    plt.show()


if __name__ == '__main__':

    ##testing code
    with open('data.txt', 'r') as f:
        data = f.read()
    
    data = data.lower()
    ###testing code
    

    occurences = find_groupings(data, 'bee')
    dict = count_occurences(occurences)

    graph_occurences(dict)
