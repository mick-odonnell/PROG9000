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
    # create a directory to store our file
    # note checking to see if we already have this dir  - error if exists
    if "bookfiles" not in os.listdir():
        os.makedirs("bookfiles")
    with open("bookfiles\\book1.txt", "wb") as book_fo_w:
        book_fo_w.write(file_obj.content)

# check whether book is already saved, - if not download it and save...
if "book1.txt" not in os.listdir("bookfiles"):
    book_data = download_book(url)
    save_book_file("bookfiles\\book1.txt", book_data)

# read the data back in
with open("bookfiles\\book1.txt", "r", encoding = 'UTF-8') as book_fo_r:  
    # encoding is the character set used to save the file - this is essentially
    # a legacy issue, obviously different world languages have different 
    # symbols - compare Russian with English...   
    book_line_list = book_fo_r.readlines() # read all the lines into a list

ctr = Counter() # use Counter object - could also implement with ordinary
                # dictionary

for l in book_line_list:
    for word in l.split():
        ctr[word] += 1

print(ctr.most_common(10))
