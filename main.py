# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
def read_file_content(filename):
    # [assignment] Add your code here 
    f = open(filename, 'r')
    reader = f.read()
    f.close()
    return(reader)
   
read_file_content("./story.txt")


def count_words():
    text = read_file_content("./story.txt")
    tofind = text.split()
    result = {}
    for items in tofind:
        if items in tofind:
            result[items] = result.get(items, 0) +1
    for k, v in result.items():
        return result





    