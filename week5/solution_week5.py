# import modules we will need..
import requests
import os
from collections import Counter


# download the book file
url = "https://www.gutenberg.org/files/58267/58267-0.txt"  # set url


def download_book(url):
    book_data = requests.get(url_to_fetch)  # grab data from url
    return book_data    
        
# write the downloaded data to file
def save_book_file(fn, file_obj):
    if "bookfiles" not in os.listdir():
        os.makedirs("bookfiles")
    with open("bookfiles\\book1.txt", "wb") as book_fo_w:
        book_fo_w.write(file_obj.content)
    # create a directory to store our file
    # note checking to see if we already have this dir  - error if exists


# check whether book is already saved, - if not download it and save...
if "book1.txt" not in os.listdir("bookfiles"):
    book_data = download_book(url)
    save_book_file("bookfiles\\book1.txt", book_data)
    
book_text = ""

# read the data back in
with open("bookfiles\\book1.txt", "r", encoding = 'UTF-8') as book_fo_r:  
    book_line_list = book_fo_r.readlines() # read all the lines into a list

for l in book_line_list: # concat all lines into one string
    book_text += l 
    
print(book_text)
    # encoding is the character set used to save the file - this is essentially
    # a legacy issue, obviously different world languages have different 
    # symbols - compare Russian with English...   

# ---------------------
# get and print ten most common
# ---------------------
ctr = Counter() # use Counter object - could also implement with ordinary
                # dictionary

for l in book_line_list:
    for word in l.split():
        ctr[word] += 1  # see Counter in collections module

for w in ctr.most_common(10):
    print("Word count:", w[1], "=", w[0] )

# ---------------------
# find the longest word
# ---------------------
longest_word = ""
longest_word_list = []  # deal with case where long words are equal
    
for w in book_text.split():
    if w[:5] == "http:":  # ignore urls in text
        continue
    elif len(longest_word) < len(w):
        longest_word = w
        longest_word_list = [w]
    elif len(longest_word) == len(w):
        longest_word_list.append(w)
        
lwl_len = len(longest_word_list)

if lwl_len == 1:
    print("The longest word is", longest_word, "with length", str(len(longest_word)))
else:
    print("The longest words are", 
          longest_word_list, 
          "with length", 
          str(len(longest_word_list[0])))
    
# -----------------------
# words in longest sentence
# -----------------------

longest_sentence = ""
longest_sentence_list = []  # deal with case where long words are equal

for s in book_text.split("."):
    if len(s) > len(longest_sentence):
        longest_sentence = s
        longest_sentence_list = [s]
    elif len(s) == len(longest_sentence):
        longest_sentence_list.append(s)
    
lsl_len = len(longest_sentence_list)

if lsl_len == 1:
    print("The longest sentence is", longest_sentence, "with length", str(len(longest_sentence)))
else:
    print("The longest sentences are\n\n", 
          longest_sentence_list, 
          "\n\nwith length", 
          str(len(longest_sentence_list[0])))


