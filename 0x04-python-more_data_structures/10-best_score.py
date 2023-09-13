#!/usr/bin/python3
def best_score(a_dictionary):
    max_v = 0
    best = ""
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > max_v:
                max_v = value
                best = key
        return best
    else:
        return None
