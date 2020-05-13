# 1
# http://www.pythonchallenge.com/pc/def/map.html

def cypher(sentence, step):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    new_sentence = ''
    for letter in sentence.lower():
        if letter in alphabet:
            letter_idx = alphabet.index(letter) + step if alphabet.index(letter) + step <= len(alphabet) - 1 else alphabet.index(letter) - len(alphabet) + step
            new_sentence += alphabet[letter_idx]
        else:
            new_sentence +=letter
    return new_sentence


sentence = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr''q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
step = 2
print(cypher(sentence, step))

print(cypher('map',step))