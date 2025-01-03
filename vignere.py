
global regex1
regex = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '&', '"', '#', "'", '-', '_', '@', '=', '+', '*', '/', ':', '!', '?', ';', '%', '$', '£', ',',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
]


def search(char,regex):
    for i in range(len(regex)):
        if regex[i] == char:
            return i
    return None

def vignere_cryptage(key,msg):
    crypted_msg = ""
    k = 0
    for m in range(len(msg)):
        key_index = search(key[k],regex)
        char2crypt = search(msg[m],regex)
        jump = (key_index + char2crypt) % len(regex)
        crypted_msg += regex[jump]
        k = (k + 1) % len(key)
    return crypted_msg

def decryptage_vignere(key,msg):
    decrypted_msg = ""
    k = 0
    for m in range(len(msg)):
        key_index = search(key[k],regex)
        decrypt_char = search(msg[m],regex)
        jump = decrypt_char - key_index
        if jump < 0:
            jump = len(regex) + jump
        decrypted_msg += regex[jump]
        k = (k + 1) % len(key)
    return decrypted_msg


