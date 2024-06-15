import string
from collections import Counter
import matplotlib.pyplot as plt
import os
from docx import Document

def process_text(file_path):
    # Read text from the Word document
    document = Document(file_path)
    text = "\n".join([paragraph.text for paragraph in document.paragraphs])
    
    lowercase_text = text.lower()
    cleaned_text = lowercase_text.translate(str.maketrans('', '', string.punctuation))
    tokenized_words = cleaned_text.split()

    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                  "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                  "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
                  "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
                  "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                  "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                  "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
                  "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
                  "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
                  "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    final_words = [word for word in tokenized_words if word not in stop_words]

    emotion_list = []
    with open('emotions.txt', 'r') as file:
        for line in file:
            clear_line = line.replace("", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in final_words:
                emotion_list.append(emotion)
                
    return Counter(emotion_list)

def get_graph(w):
    fig, ax1 = plt.subplots()
    ax1.bar(w.keys(), w.values())
    fig.autofmt_xdate()
    plt.savefig('graph.png')
    return fig

if __name__ == "__main__":
    user_input = input("Please enter the text you want to analyze: ")

    with open('file.txt', 'w') as file:
        file.write(user_input)

    w = process_text('file.txt')
    print(w)
    get_graph(w)
    plt.show()
