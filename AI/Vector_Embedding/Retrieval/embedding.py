from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
import numpy as np
def cosine_similiarity(a,b):
    return np.dot(a=a,b=b)/(np.linalg.norm(a)*np.linalg.norm(b))
model = SentenceTransformer("all-MiniLM-L6-v2")
contents = []
grammar_words = ["a", "about", "above", "across", "after", "against", "all", "along", "although", "am", "an", "and", "any", "anybody", "anyone", "anything", "are", "around", "as", "at", "be", "because", "been", "before", "behind", "below", "beside", "besides", "between", "both", "but", "by", "can", "cannot", "can't", "could", "couldn't", "dare", "did", "didn't", "do", "does", "doesn't", "doing", "done", "don't", "down", "each", "either", "enough", "even", "every", "everybody", "everyone", "everything", "except", "few", "fewer", "fewest", "first", "for", "from", "had", "hadn't", "has", "hasn't", "have", "haven't", "he", "her", "hers", "herself", "him", "himself", "his", "how", "however", "i", "if", "in", "inside", "into", "is", "isn't", "it", "its", "itself", "least", "less", "like", "little", "many", "me", "might", "mine", "more", "most", "much", "my", "myself", "near", "neither", "no", "nobody", "none", "nor", "not", "nothing", "now", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "our", "ours", "ourselves", "out", "outside", "over", "own", "per", "please", "rather", "really", "same", "several", "shall", "shan't", "she", "should", "shouldn't", "since", "so", "some", "somebody", "someone", "something", "still", "such", "than", "that", "the", "their", "theirs", "them", "themselves", "then", "there", "therefore", "these", "they", "this", "those", "though", "through", "till", "to", "too", "under", "until", "up", "upon", "us", "very", "want", "was", "wasn't", "we", "were", "weren't", "what", "whatever", "when", "where", "whereas", "wherever", "whether", "which", "whichever", "while", "who", "whoever", "whom", "whose", "why", "will", "with", "within", "without", "won't", "would", "wouldn't", "yet", "you", "your", "yours", "yourself", "yourselves", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[","]", "^", "_", "`", "{", "|", "}", "~" ]
embeddings = [] 
with open("document.txt","r") as file:
    for line in file:
        contents.append(line)
for content in contents:
    embeddings.append(model.encode(content))
prompt = input("Enter the prompt:")
embedded_prompt = model.encode(prompt)
count = 0
matches = []
for embedding in embeddings:
    similiarity = cosine_similiarity(embedding,embedded_prompt)
    util_similarity = cos_sim(embedded_prompt,embedding)
    print("similiarity:",similiarity)
    print("util similiarity:",util_similarity)
    count +=1
    if similiarity >0.7:
        matches.append(count)
with open("document.txt","r") as file:
    line_count = 0
    for line in file:
        line_count += 1
        if line_count in matches:
            print("semantic search match:",line)
print("match count:",matches)
extracts = []
for word in prompt.split(" "):
    if word not in grammar_words:
        extracts.append(word)
with open("document.txt") as file:
    for line in file:
        extract_match = 0
        for extract in extracts:
            if extract in line:
                extract_match += 1
        if extract_match > int(len(extracts)/2):
            print("keyword search match:",line)