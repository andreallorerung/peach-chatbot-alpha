import preprocess.stemmer_factory

def test_stemword():
    # set up
    words = ["apple","application","maximum","maximally","horsing","lady",
            "depression","femininity","painful","breathing","responsibilities",
            "responsiblities","obliged","financial","graduate","homeless",
            "housekeeping","boyfriend","sibling","mother","moth","plans",
            "disappointment","horrible"]

    expected_stems = ["appl","apply","maxim","maxim","hors","lady","depress",
                     "feminin","pain","breath","respons","respons","oblig","fin"
                     ,"gradu","homeless","housekeep","boyfriend","sibl","moth",
                     "moth","plan","disappoint","horr"]

    stemmer = preprocess.stemmer_factory.get_stemmer()

    # verify
    for expected, actual in zip(expected_stems, [stemmer.stem(word) for word in words]):
        assert expected == actual
