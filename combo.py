
import os
import shutil
path = os.getcwd()
"""
files = []
for file in os.listdir(path):
    if file.endswith('.txt'):
        files.append(file)
print(files)
"""
files = ['combined.txt', 'combined2.txt', 'combined3.txt', 'combined4.txt', 'combined5.txt', 'combined6.txt', 'combined7.txt', 'combined8.txt', 'combined9.txt', 'EKScombined.txt', 'GAAcombined.txt', 'MVBcombined.txt']



with open('full_corpus.txt','wb') as wfd:
    for f in files:
        with open(f,'rb') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write(b"\n")

KVAS
with open('full_corpus.txt', 'w') as outfile:
    for fname in files:
        with open(fname) as infile:
            outfile.write(infile.read())


    with open("full_corpus.txt", "a") as text_file:
        text_file.write(text)
