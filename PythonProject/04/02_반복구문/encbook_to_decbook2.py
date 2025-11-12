#!/usr/bin/python3


def make_book():
    # input : ?
    # output : dict(encbook), dict(decbook)
    # function :
    encbook = {'a': '#', 'p': 's', 'l': '?', 'e': 'k'}
    decbook = {}

    for k, v in encbook.items():
        decbook[v] = k

    return encbook, decbook


def encrypt_str(msgs, encbook):
    # input : str(msgs), dict(encbook)
    # output : str(enc_msgs)
    # function :
    enc_list = []
    for i in msgs:
        enc_list.append(encbook[i])
    enc_msgs = ''.join(enc_list)

    return enc_msgs


def decrypt_str(encrypted_msgs, decbook):
    # input : str(encrypted_msgs), dict(decbook)
    # output : str(plaintext)
    # function :
    plaintext = ''
    for i in encrypted_msgs:
        plaintext += decbook[i]

    return plaintext


def main():
    plaintext = 'apple'
    enc_table, dec_table = make_book()
    encrypted_msgs = encrypt_str(plaintext, enc_table)
    decrypted_msgs = decrypt_str(encrypted_msgs, dec_table)

    print("Original  : |%s|" % plaintext)
    print("Encrypted : |%s|" % encrypted_msgs)
    print("Decrypted : |%s|" % decrypted_msgs)


if __name__ == '__main__':
    main()