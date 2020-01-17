import pickle
from collections import Counter
from pathlib import Path

import scipy.stats
import sklearn_crfsuite
from sklearn.metrics import make_scorer
from sklearn.model_selection import RandomizedSearchCV
from sklearn_crfsuite import metrics

from ez_address_parser.features import tokens_to_instance, transform, load_data
from ez_address_parser.utils import tokenize

here = Path(__file__).parent.absolute()

with open(here / "ez_address_annotator/data/data.pkl", "rb") as f:
    data = pickle.load(f)

print(f"{len(data)} labelled addresses are used to create this pretrained model")

X, y = load_data(data)

crf = sklearn_crfsuite.CRF(
    algorithm="lbfgs", max_iterations=100, all_possible_transitions=True,
)
params_space = {
    "c1": scipy.stats.expon(scale=0.5),
    "c2": scipy.stats.expon(scale=0.05),
}
f1_scorer = make_scorer(metrics.flat_f1_score, average="weighted")

rs = RandomizedSearchCV(
    crf,
    params_space,
    cv=3,
    verbose=1,
    n_jobs=-1,
    n_iter=100,
    scoring=f1_scorer,
    random_state=2020,
)
rs.fit(X, y)

print(f"best params: {rs.best_params_}")
print(f"best CV score: {rs.best_score_}")
print("model size: {:0.2f}M".format(rs.best_estimator_.size_ / 1024 ** 2))

crf = rs.best_estimator_


def print_transitions(trans_features):
    for (label_from, label_to), weight in trans_features:
        print(f"{weight:.3f}: {label_from:20s} -> {label_to}")


top = 10
print("Top likely transitions:")
print_transitions(Counter(crf.transition_features_).most_common(top))

print("\nTop unlikely transitions:")
print_transitions(Counter(crf.transition_features_).most_common()[-top:])

with open(here / "ez_address_parser/model", "wb") as f:
    pickle.dump(crf, f)
print("pretrained model updated")
