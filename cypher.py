alphabet = "abcdefghijklmnopqrstuvwxyz"
MAJ_alpha = alphabet.upper()

def cipher_decrypt(msg, offset):
    decrypted_msg = ""
    for letter in msg:
        index = alphabet.find(letter)
        index_MAj = MAJ_alpha.find(letter)
        if (index != -1 or index_MAj != -1):
            if (index_MAj != -1):
                decrypted_msg += MAJ_alpha[(index_MAj + offset) % 26]
            else:
                decrypted_msg += alphabet[(index + offset) % 26]
        else:
            decrypted_msg += letter
    return (decrypted_msg)

def cipher_crypt(msg, offset):
    crypted_msg = ""
    for letter in msg:
        index = alphabet.find(letter)
        index_MAj = MAJ_alpha.find(letter)
        if (index != -1 or index_MAj != -1):
            if (index_MAj != -1):
                crypted_msg += MAJ_alpha[(index_MAj - offset) % 26]
            else:
                crypted_msg += alphabet[(index - offset) % 26]
        else:
            crypted_msg += letter
    return (crypted_msg)

def cipher_decrypt_bruteforce(msg):
    offset = 1
    while (offset < 27):
        print(offset, cipher_decrypt(msg, offset))
        offset += 1

def duplicate_keyword(keyword, msg):
    string = ""
    num = 0
    for letter in msg:
        index = alphabet.find(letter)
        index_MAj = MAJ_alpha.find(letter)
        if (index != -1):
            string += keyword[num % (len(keyword))]
            num += 1
        elif (index_MAj != -1):
            string += keyword[num % (len(keyword))]
            num += 1
        else:
            string += letter
    return string

def vigenere_ciper_decrypt(msg, keyword):
    keyword_msg = duplicate_keyword(keyword, msg)
    decrypted_msg = ""
    i = 0
    while (i < len(msg)):
        index_MAj = MAJ_alpha.find(msg[i])
        index = alphabet.find(msg[i])
        if (index != -1 or index_MAj != -1):
            if (index != -1):
                keyword_index = alphabet.find(keyword_msg[i])
                decrypted_msg += alphabet[(index - keyword_index) % 26]
            elif (index_MAj != -1):
                keyword_index = MAJ_alpha.find(keyword_msg[i])
                decrypted_msg += MAJ_alpha[(index_MAj - keyword_index) % 26]
        else:
            decrypted_msg += msg[i]
        i += 1
    return decrypted_msg

def vigenere_ciper_crypt(msg, keyword):
    keyword_msg = duplicate_keyword(keyword, msg)
    crypted_msg = ""
    i = 0
    while (i < len(msg)):
        index_MAj = MAJ_alpha.find(msg[i])
        index = alphabet.find(msg[i])
        if (index != -1 or index_MAj != -1):
            if (index != -1):
                keyword_index = alphabet.find(keyword_msg[i])
                crypted_msg += alphabet[(index + keyword_index) % 26]
            elif (index_MAj != -1):
                keyword_index = MAJ_alpha.find(keyword_msg[i])
                crypted_msg += MAJ_alpha[(index_MAj + keyword_index) % 26]
        else:
            crypted_msg += msg[i]
        i += 1
    return crypted_msg
