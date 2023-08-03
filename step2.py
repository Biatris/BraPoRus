import csv
from itertools import zip_longest

import pandas as pd
from conll_df import conll_df
from deeppavlov import build_model
from tqdm import tqdm

ud_model = build_model("ru_syntagrus_joint_parsing")

with open("sentence_tokens.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    lines = list(reader)

lines = pd.read_csv("sentence_tokens.csv", index_col=0)


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


res = []
for group in tqdm(grouper(lines, 2)):
    try:
        for x in group:
            res.append(ud_model([x])[0])
    except:
        pass

mega_df = []
for n, x in enumerate(res):
    file = open("temp/temp.win", "w")
    file.write(x)
    file.close()
    df = conll_df("temp/temp.win", file_index=False, v2=True)
    df = df.reset_index()
    df["s"] = n
    mega_df.append(df)

mega_df = pd.concat(mega_df, ignore_index=True)
mega_df.to_csv("ud_df.csv")
