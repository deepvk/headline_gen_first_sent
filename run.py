from nltk.tokenize import sent_tokenize

with open('/input.txt') as f:
    texts = [line.strip() for line in f]

firsts = [sent_tokenize(text)[0] for text in texts]

with open('/output.txt', "wt") as f:
    for s in firsts:
        f.write(s + "\n")
