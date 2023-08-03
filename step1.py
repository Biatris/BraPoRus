import csv
import re

import pandas as pd
import spacy
from spacy.lang.ru import Russian

with open("corpus/full_corpus.txt") as f:
    data = f.readlines()

speakers = (
    "AVM:",
    "EAB:",
    "IMK:",
    "NKP:",
    "SAP:",
    "SSN:",
    "TSL:",
    "VPK:",
    "ZPP:",
    "EKS:",
    "GAA:",
    "MVB:",
)

utterances = [u for u in data if u.startswith(speakers)]
utterances = str(utterances).strip().replace("\n", "")
utterances_cut = re.sub("\[(.*?)\]", "", utterances)
utterances_cut2 = re.sub("[A-Z]{3}\:", "", utterances_cut)
final_utterances = utterances_cut2.strip().replace("\\n", "")
final_utterances = final_utterances.lstrip()

nlp = Russian()
# nlp.add_pipe('sentencizer') # this needs to be done once for the sentence boundary detection
nlp.max_length = 500000000
config = {"punct_chars": None}
nlp.add_pipe("sentencizer", config=config)

doc = nlp(final_utterances)
sentence_tokens = [
    [token.text for token in sent if not token.is_punct and not token.is_space]
    for sent in doc.sents
]

with open("sentence_tokens.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerows(sentence_tokens)
