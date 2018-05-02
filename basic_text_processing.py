import pandas as pd
import nltk


def word_count(text):
    words = []
    # tokenize
    for elem in text:
        words += elem.split(" ")
    unique_words = list(set(words))
    mapping = {}.fromkeys(unique_words, 0)
    for word in words:
        mapping[word] += 1
    word_counts = [(key, mapping[key]) for key in mapping]
    return sorted(word_counts, key=lambda t: t[1], reverse=True)
    
    
def analyze_word_count(word_counts):
    print("Most Frequently occurring words")
    for elem in word_counts[:11]:
        print("Word:",elem[0],",count",elem[1])
    counts = [elem[1] for elem in word_counts]
    least_common_words = [elem for elem in word_counts if elem[1] == min(counts)]
    print("There were ",len(least_common_words), "words that occurred", min(counts))
    print("Which is ",len(least_common_words)/sum(counts), "of the total words")
    
df = pd.read_csv("sampled_data.csv")
cols = df.columns.tolist()
cols = [elem for elem in cols if "Unnamed" not in elem]
df = df[cols]

# Let's start with word count
word_count_body = word_count(df["body"])
word_count_headline = word_count(df["headline"])
print("For body count")
analyze_word_count(word_count_body)
print("For headline count")
analyze_word_count(word_count_headline)
