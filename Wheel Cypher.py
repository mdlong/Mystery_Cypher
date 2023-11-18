import string

def decrypt(keyletter, encsentence):

    cypherdict = {}
    outerlist = list(string.ascii_lowercase)

    innerlist = ['a', 'd', 'g', 'j', 'l', 'z', 'c', 'b', 'm', 'w', 'r', 'y', 'i', 'p', 's', 'f', 'h', 'k', 'x', 'v', 'n', 'q', 'e', 't', 'u', 'o']

    # Find the index of the Key letter
    keyindex = innerlist.index(keyletter)
    # print(keyindex)

    # Build dictionary from the key letter
    count = 0
    for letter in innerlist[keyindex:]:
        # print(letter)
        cypherdict[letter] = outerlist[count]
        count += 1

    # build the dictionary to the key letter
    for letter in innerlist[:keyindex]:
        # print(letter)
        cypherdict[letter] = outerlist[count]
        count += 1

    decsentence = []

    for item in encsentence:
        if item not in outerlist:
            decsentence.append(item)
        else:
            decsentence.append(cypherdict.get(item))

    separator = ""
    return separator.join(decsentence)

# Enter you key letter
keyletter = "b"

# Type your encrypted sentence
print(decrypt(keyletter, "zqd vdoa ifnr sfpsaqe myiquy osy ifnro obuwbovq fi asyz buy jqukfnp aqpyasyu asy jw fo xqoa asy wqry ndvmyu fo idn osqy rqqu"))

# print(decrypt(keyletter, "gr vrrw bcmhaq. s mcvo xchr opr mckk. opsu qkcmr su yakk ny mnxqaort pcmhrtu cvw opr qpnvru ctr ckk baiirw. uql pnoksvr mnwr su psiponq'u osmhro vaxbrt "
#                          "xsvau cwxsuusnv qtsmr."))

# print(decrypt(keyletter, "ddolobh"))


# print(decrypt(keyletter, "this is my message"))

# print(decrypt(keyletter, "rkgi gi cf cqiiuwq"))
