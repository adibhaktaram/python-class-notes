# Pass this function an iterable object.
def histogram(s):
    d =  dict()
    for item in s:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1

    return d

#swap the keys and the values to make a new dictionary
def invertDict(d):
    inverse = dict()

    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
if __name__ == "__main__":
    pets = {"cats": 5, "horses": 2, "pony": 1, "chickens": 14, "goats":3, "cats":2, "horses":4, "pony": 1}

    phrase = "i like my pets and feed them everyday"
    freq = histogram(phrase)
    invert  = invertDict(freq)
    print(freq)
    print(invert)
