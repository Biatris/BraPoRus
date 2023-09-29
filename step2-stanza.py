import csv

import pandas as pd
import stanza
from tqdm import tqdm

stanza.download("ru")

nlp = stanza.Pipeline("ru")  # initializes neural pipeline for Russian
# loads pre-tokenized sents
with open("sentence_tokens_test.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    lines = list(reader)
# Defines the list of all possible feature categories
feature_categories = [
    "PronType",
    "Gender",
    "VerbForm",
    "NumType",
    "Animacy",
    "Mood",
    "Poss",
    "NounClass",
    "Tense",
    "Reflex",
    "Number",
    "Aspect",
    "Foreign",
    "Case",
    "Voice",
    "Abbr",
    "Definite",
    "Evident",
    "Typo",
    "Degree",
    "Polarity",
    "Person",
    "Polite",
    "Clusivity",
]

# Initializes empty lists to store the extracted information
s_list, i_list, w_list, l_list, x_list, g_list, f_list = [], [], [], [], [], [], []

# Initializes lists for each feature category
feats_dict_list = {category: [] for category in feature_categories}

# Processes each sentence in the list
for s_num, sentence in enumerate(tqdm(lines, desc="Processing UD pipeline")):
    # Process the text
    doc = nlp(" ".join(sentence))

    # Initializes token index
    token_index = 1

    # Iterates through tokens in the sentence
    for sentence_info in doc.sentences:
        for token_info in sentence_info.words:
            # Appends information to respective lists
            s_list.append(s_num)  # Sentence number
            i_list.append(token_index)  # Token index
            w_list.append(token_info.text)  # Word text
            l_list.append(token_info.lemma)  # Lemma
            x_list.append(token_info.upos)  # UPOS
            g_list.append(token_info.head)  # Head
            f_list.append(token_info.deprel)  # Deprel

            # Unpacks feats into individual columns
            feats_info = token_info.feats
            for category in feature_categories:
                # Extracts the value for the category
                if feats_info:
                    category_value = "-"
                    for feature in feats_info.split("|"):
                        if feature.startswith(category + "="):
                            category_value = feature.split("=")[1]
                            break
                else:
                    category_value = "-"

                feats_dict_list[category].append(category_value)

            token_index += 1

# Creates a pandas DataFrame from the lists
df = pd.DataFrame(
    {
        "s": s_list,
        "i": i_list,
        "w": w_list,
        "l": l_list,
        "x": x_list,
        "g": g_list,
        "f": f_list,
        **feats_dict_list,
    }
)

# Saves the tagged df to a csv file
df.to_csv("ud_df.csv")
