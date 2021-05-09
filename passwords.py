# Libraries
import hashlib
import multiprocessing
import time

# There are 52.521.875 posibilitys (35^5)

# GLOBAL VARIABLES

# Hash
hash_c = hashlib.sha3_256("john2".encode())
HASH = hash_c.hexdigest()
# Possibility of adding if you know the end of the password
FIN_PSW = ""
# String with alphanumeric characters
ALFANUM = "abcdefghijklmnopqrstuvwxyz123456789"


def password(lett):
    """
    Try different combinations of alphanumeric passwords with 5 letters
      comparing with the hash code
    Parámetros:
        letras: list with two elements, the first element is the start letter, the second the end letter
    Return:
        0 if it has not found it, if it has found it returns the password
    """
    # Valor de retorno
    value = 0
    # Boolean value if we have found it or not
    found = False
    first_let = lett[0]
    end_let = lett[1]
    # First letter string
    fr_letter = ALFANUM[ALFANUM.find(first_let):ALFANUM.find(end_let)+1]
    ind_1 = 0
    while not found and ind_1 < len(fr_letter):
        lt1 = fr_letter[ind_1]
        ind_1 += 1
        ind_2 = 0
        while not found and ind_2 < len(ALFANUM):
            lt2 = ALFANUM[ind_2]
            ind_3 = 0
            ind_2 += 1
            while not found and ind_3 < len(ALFANUM):
                lt3 = ALFANUM[ind_3]
                ind_4 = 0
                ind_3 += 1
                while not found and ind_4 < len(ALFANUM):
                    lt4 = ALFANUM[ind_4]
                    ind_4 += 1
                    ind_5 = 0
                    while not found and ind_5 < len(ALFANUM):
                        lt5 = ALFANUM[ind_5]
                        ind_5 += 1
                        psw = lt1 + lt2 + lt3 + lt4 + lt5 + FIN_PSW
                        hash_aux = hashlib.sha3_256(psw.encode())
                        has_com = hash_aux.hexdigest()
                        if has_com == HASH:
                            found = True
                            value = psw
    if value != 0:
        print("The password is:", value)
    return value


def main():

    t1 = time.time()
    # The distribution of letters for the processors
    letters = [["a", "e"], ["f", "j"], ["l", "p"], ["q", "u"],
              ["v", "y"], ["z", "2"], ["3", "6"], ["7", "9"]]
    n_p = 8
    pool = multiprocessing.Pool(n_p)
    pool.map(password, letters)
    t2 = time.time()
    print("Total time: ", t2-t1)


if __name__ == "__main__":
    main()

