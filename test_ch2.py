#create a function that derives the shortest and the longest word from a string

def short_long(string):
    words=string.split()
    long=words[0]
    long_list=[]
    short=words[0]
    short_list=[]
    for word in words:
        if len(word)<len(short):
            short_list.clear()
            short=word
            short_list.append(word)
        elif len(word)==len(short):
            short_list.append(word)
    for word in words:
        if len(word) > len(long):
            long_list.clear()
            long = word
            long_list.append(word)
        elif len(word) == len(long):
            long_list.append(word)

    if len(short_list)>1 and len(long_list)>1:
        return short_list, long_list
    elif len(short_list)>1 and len(long_list)==1:
        return short_list, long
    elif len(long_list)>1 and len(short_list)==1:
        return short, long_list
    else:
        return short, long

def test_short_long():
    assert short_long('hiiiiii how is life')==('is','hiiiiii')

def test_multiple_short_long():
    assert short_long('did you disturb plonsky')==(['did','you'],['disturb','plonsky'])

def test_returning_list_strings():
    assert short_long('did you disturb')==(['did','you'],'disturb')