# Libraries
import hashlib
import multiprocessing
import time
from password import Password

# GLOBAL VARIABLES
# Hash
hash_c = hashlib.sha3_256("john4".encode())
HASH = hash_c.hexdigest()
# Possibility of adding if you know the end of the password
FIN_PSW = ""
# String with alphanumeric characters
CHAR = "abcdefghijklmnopqrstuvwxyz123456789"
# CHAR2 = "abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRTSUVWXYZ"
# The distribution of letters for the processors
LETTERS = [["a", "e"], ["f", "j"], ["l", "p"], ["q", "u"],
           ["v", "y"], ["z", "2"], ["3", "6"], ["7", "/"]]

# LETTERS2 = [["a", "j"], ["k", "p"], ["p", "v"], ["w", "3"],
#           ["4", "B"], ["C", "I"], ["J", "O"], ["P", "Z"]]


def main():
    passw = Password(hash=HASH, char=CHAR, letters=LETTERS)
    # Without looking for passwords that have more than 5 letters
    passw.solve(six=False)


if __name__ == "__main__":
    main()

