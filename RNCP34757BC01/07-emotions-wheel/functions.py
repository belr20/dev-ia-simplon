import numpy as np

from sklearn.feature_extraction.text import CountVectorizer


# Sub-sample the data to plot with the 100th firsts + 10th lasts
def subsample(x):
    return np.hstack((x[:100], x[len(x)-10:]))


def words_distribution(corpus):
    # Vectorization
    cv = CountVectorizer()
    X = cv.fit_transform(corpus)
    # Compute rank
    words = cv.get_feature_names()
    wsum = np.array(X.sum(0))[0]
    ix = wsum.argsort()[::-1]
    wrank = wsum[ix]
    classes = [words[i] for i in ix]
    freq = subsample(wrank)
    r = np.arange(len(freq))
    return r, freq, classes
