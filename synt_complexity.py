import pandas as pd
from tqdm import tqdm

tqdm.pandas()

PATH = "processed_data.csv"
df = pd.read_csv(PATH)

# Syntactic complexity metrics, can be applied to a pre-processed connlu df.
# METRIC 1: Computes maximum nesting depth.
def max_dep(g):
    s = g[["i", "g"]]
    depth = 0
    while s.shape[0] > 0:
        s = s[s["i"].isin(s["g"])]
        depth += 1
    return depth

max_depths = df.groupby("s").progress_apply(max_dep)

# METRIC 2: Computes mean sentence length.
msl = df.groupby("s").mean()

# METRIC 3: Computes # of clausal subjects, 
# i.e., where the subject is itself a clause.
def clausal_subject(g):
    return g[g["f"].isin(["csubj"])].shape[0]

cs = df.groupby("s").progress_apply(clausal_subject)

# METRIC 4: Computes # of clausal complements, i.e., where a clausal
# complement of a verb or adjective is a dependent clause.
def clausal_comp(g):
    return g[g["f"].isin(["ccomp"])].shape[0]

cc = df.groupby("s").progress_apply(clausal_comp)

# METRIC 5: Computes # of open clausal complements (xcomp), i.e., where
# a clausal complement of a verb or an adjective is a predicative or
# clausal complement without its own subject.
def clausal_open(g):
    return g[g["f"].isin(["xcomp"])].shape[0]

co = df.groupby("s").progress_apply(clausal_open)

# METRIC 6: Computes # of adverbial clause modifiers;
# i.e., where a clause modifies a verb or other predicate.
def adv_clause_pred(g):
    return g[g["f"].isin(["advcl"])].shape[0]

acp = df.groupby("s").progress_apply(adv_clause_pred)

# METRIC 7: Computes # of finite and non-finite clauses that modify a nominal.
def adv_clause_nom(g):
    return g[g["f"].isin(["acl"])].shape[0]

acn = df.groupby("s").progress_apply(adv_clause_nom)

# METRIC 8: Computes # of relative clauses.
def adv_clause_nom_rel(g):
    return g[g["f"].isin(["acl:relcl"])].shape[0]

acn_rel = df.groupby("s").progress_apply(adv_clause_nom_rel)

# METRIC 9: Computes # of passive voice constructions.
def count_pas(g):
    return g[g["Voice"] == "Pass"].shape[0]

pas = df.groupby("s").progress_apply(count_pas)

# METRIC 10: Computes # number of clauses (based on number of n-subjects).
def count_clauses(g):
    return g[g["f"] == "nsubj"].shape[0]

nsubj = df.groupby("s").progress_apply(count_clauses)

# METRIC 11: Computes # number of sentences that use complex coordination.
# Filters sentences containing at least two "nsubj" with none having
# "X" in the "x" column, no "mark", and at least one "cc".
coord = df.groupby("s").filter(
    lambda x: (x["f"] == "nsubj").sum() >= 2
    and (x["f"] == "mark").sum() == 0
    and (x["f"] == "cc").any()
    and ((x["f"] == "nsubj") & (x["x"] == "X")).sum() == 0
)

# METRIC 12: Computes # number of sentences that use complex subordination.
def count_subord(g):
    return g[g["f"].isin(["mark"])].shape[0]

subord = df.groupby("s").progress_apply(count_subord)
