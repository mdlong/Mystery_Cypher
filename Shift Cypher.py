import string

cypherdict = {}
shiftlist = []
decryptlist = []

outerlist = list(string.ascii_lowercase)

keyword = "something"

cypher = "g bfjw rnsr yju msf ej rngq! tfrtp rnt rnptt egigr mjet gf rngq jpetp: njw dsfy knsqtq gf qjmb'q tvgc kcsf? wnsr fudotp jh kjgfrq gq rnt ctrrtp m wjprn jf s qmpsooct rgct? rntpt gq sf gfvgqgoct fudotp ngeetf gf rnt qnjt qnjt iuget hjp qkgtq. wnsr gq gr?"


# Append the keyword to the front of the shiftlist
for key in keyword:
    shiftlist.append(key)

# Build a list of the alphabet left over after the keyword
for x in outerlist:
    if x not in keyword:
        shiftlist.append(x)

# print(outerlist)
# print(shiftlist)
# print(len(shiftlist))

count = 0
# Build a dictionary of the letter combos
for letter in shiftlist:
    cypherdict[letter] = outerlist[count]
    count += 1

# print(cypherdict)

# Decrypt the sentence by matching the list to the dictionary
for c in cypher:
    if c not in outerlist:
        decryptlist.append(c)
    else:
        decryptlist.append(cypherdict.get(c))

# print(decryptlist)

separator = ""
print(separator.join(item for item in decryptlist if item))


