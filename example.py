import matplotlib.pyplot as plt

def reverse_words(s):
    """
    Reverses order or words in string s.
    """
    words = s.split()
    words_reversed = words[::-1]
    return ' '.join(words_reversed)


def test_reverse_words():
    assert reverse_words('dogs hate cats') == 'cats hate dogs'
    assert reverse_words('dog eat dog') == 'dog eat dog'
    assert reverse_words('one two three four') == 'four three two one'


def get_word_lengths(s):
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    # uncomment next line in step 9
    return [len(word) for word in s.split()]
    return None


# uncomment this function in step 6
def test_get_word_lengths():
    text = "Three tomatoes are walking down the street"
    assert get_word_lengths(text) == [5, 8, 3, 7, 4, 3, 6]


def test_download():
    import os
    print(os.listdir('.'))
    print(os.listdir('samlpedata'))
    assert(os.path.isfile(os.path.join('samlpedata','camea2018n000495.hdf')))


def test_mpl():
    fig,ax = plt.subplots()
    ax.scatter([0,1,2,3,4],[1,1,1,1,1])

    fig.close()