# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

#def read_file_content("./story.txt"):
    # [assignment] Add your code here 
    
   # return "Hello World"


#def count_words():
   # text = read_file_content("C:\Users\richa\Desktop\Reading-Text-Files")
    # [assignment] Add your code here
 #return {"as": 10, "would": 20}

#Samples
list_of_samples = ['with', 'a', 'smile', 'on', 'her', 'face']
dict_generated_from_story = {}
def no_of_appearance(sample):
    word_counter = 0
    content = text 
    splitted_word = content.split()
    for particular in splitted_word:
        if particular == sample:
            word_counter = word_counter + 1
            return word_counter

for list_sample in list_of_samples:
    dict_generated_from_story[list_sample] = no_of_appearance(list_sample)
    return dict_generated_from_story



   