from difflib import SequenceMatcher

# TODO: Actually use these functions to implement automatic
# clustering / correction mechanism.

def get_normalized_keywords(answer):
    '''
    Returns a sorted list of keywords from the answer argument in a normalized
    form.
    '''
    return sorted(list(answer.lower().split(' ')))

def get_match_stats(kwlist1, kwlist2):
    '''
    Returns the confidence with which we can say that kwlist1 matches kwlist2.
    Usually, .60 is the threshold above which both can be said to be equal.
    '''
    
    return SequenceMatcher(None, kwlist1, kwlist2).ratio()
