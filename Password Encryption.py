from textwrap import wrap

'''Password dictionary to encrypt password'''
pswd_dict = {'a': 'dmn|', 'b': 'z4>p', 'c': 'D--j', 'd': '#~YW', 'e': 'Nw?m', 'f': 'QaOa', 'g': 'nhhz', 'h': '1Peq', 'i': '&1\\g', 'j': '10*`', 'k': '|u?&', 
             'l': 'kU-8', 'm': 'FO:9', 'n': 'f|y4', 'o': 'Sa.k', 'p': 'mCxR', 'q': '$!a8', 'r': 'z^-U', 's': '8NfT', 't': 'EMX`', 'u': 'sTVT', 'v': 'fOon', 
             'w': 'L^9!', 'x': 'p/~-', 'y': '_1CA', 'z': 'eqd+', 'A': '_t|0', 'B': 'g-ig', 'C': '_\\q&', 'D': 'WkgN', 'E': '0=_X', 'F': 'ac=N', 'G': 'f^_C', 
             'H': 'GRp<', 'I': 'bV1\\', 'J': 'YFk1', 'K': 'M>we', 'L': 'Ov.Z', 'M': 'N|Ce', 'N': 'Go21', 'O': 'YUGc', 'P': '&NG4', 'Q': 'k0Qm', 'R': '&n/y', 
             'S': '3<1d', 'T': '\\v4b', 'U': 'D:Gd', 'V': '*><O', 'W': 'U=8^', 'X': 'Sm7F', 'Y': '@jT6', 'Z': 'E/aO', '1': '>8dm', '2': 'SEUv', '3': ';5k3', 
             '4': 'seR^', '5': '<aa|', '6': 'oZWU', '7': 'dRod', '8': '&q&E', '9': 'ED;1', '0': ':<bp', '!': 'KjI:', '#': '9P99', '$': '*$7r', '%': '_dIn', 
             '^': 'x4?x', '&': '*vuI', '*': '|=P@', '@': 'h0Gt', '_': 'b9sl', '?': 'E4UP', '+': 'D:zH', '-': 'LH/+', '=': ':eM-', '|': 'bE!G', '\\': 'nLt.', 
             '.': '4>W#', ',': 'I.+R', '/': '%V,^', ';': '3Z7k', ':': 'FANa', '<': 'oR9b', '>': 'C;Gh', '`': 'OtmX', '~': 'kjCS',' ':'i5b@'}

'''Inversing password dictionary to decrypt the encrypted password'''
inv = {key: val for val, key in pswd_dict.items()}


def encrypt():
    '''This function will encrypt the password'''
    password = input("Enter Password:")
    print("Code:", end="")
    for x in password:
        print(pswd_dict[x], end="")


def decrypt():
    '''This function will decrypt the password'''
    code = input("\nEnter code:")
    code = wrap(code, 4)
    try:
        print("Password:", end="")
        for x in code:
            print(inv[x], end="")
    except Exception:
        print("Invalid code!!")


def main():
    '''This is main function which executes both encryption and decryption'''
    while True:
            encrypt()
            decrypt()
            user = input("\nDo you want to continue?(Y/N):").lower()
            if user == 'y':
                continue
            else:
                break
if __name__ == "__main__":
    main()
    
