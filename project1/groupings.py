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

def count_occurences(matches, ):
    occurrences = {}
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


def graph_occurences(ax, data, title, n=5):
    #getting the top n words
    top_n = list(data.keys())[:n]

    #getting the occurences of the top n words
    occurences = list(data.values())[:n]

    #creating the graph
    ax.set_title(title)
    ax.set_ylabel('# Occurrences')
    ax.bar(top_n, occurences)


