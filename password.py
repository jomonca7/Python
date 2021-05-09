import hashlib
import multiprocessing
import time


class Password:
    """
    Class password to obtain the posible password
    """
    def __init__(self, hash, letters=[["a", "e"], ["f", "j"], ["l", "p"], ["q", "u"],
                                      ["v", "y"], ["z", "2"], ["3", "6"], ["7", "9"]], fin_pswd=""
                            ,char="abcdefghijklmnopqrstuvwxyz123456789"):
        self.hash = hash
        self.letters = letters
        self.fin_pswd = fin_pswd
        self.char = char

    # The different implementations to solve the password

    def passwd3(self, lett):
        """
        Solve the password with 3 characters
        42875 Possibilities
        :param lett: List with the letter to start
        """
        # Return Value
        value = 0
        # Boolean value if we have found it or not
        found = False
        first_let = lett[0]
        end_let = lett[1]
        # First letter string
        fr_letter = self.char[self.char.find(first_let):self.char.find(end_let) + 1]
        ind_1 = 0
        while not found and ind_1 < len(fr_letter):
            lt1 = fr_letter[ind_1]
            ind_1 += 1
            ind_2 = 0
            while not found and ind_2 < len(self.char):
                lt2 = self.char[ind_2]
                ind_3 = 0
                ind_2 += 1
                while not found and ind_3 < len(self.char):
                    lt3 = self.char[ind_3]
                    ind_3 += 1
                    psw = lt1 + lt2 + lt3 + self.fin_pswd
                    hash_aux = hashlib.sha3_256(psw.encode())
                    has_com = hash_aux.hexdigest()
                    if has_com == self.hash:
                        found = True
                        value = psw
        if value != 0:
            print("The password is:", value)
        return value

    def passwd4(self, lett):
        """
        Solve the password with 4 characters
        1500625 Possibilities
        :param lett: List with the letter to start
        """
        # Return Value
        value = 0
        # Boolean value if we have found it or not
        found = False
        first_let = lett[0]
        end_let = lett[1]
        # First letter string
        fr_letter = self.char[self.char.find(first_let):self.char.find(end_let) + 1]
        ind_1 = 0
        while not found and ind_1 < len(fr_letter):
            lt1 = fr_letter[ind_1]
            ind_1 += 1
            ind_2 = 0
            while not found and ind_2 < len(self.char):
                lt2 = self.char[ind_2]
                ind_3 = 0
                ind_2 += 1
                while not found and ind_3 < len(self.char):
                    lt3 = self.char[ind_3]
                    ind_3 += 1
                    ind_4 = 0
                    while not found and ind_4 < len(self.char):
                        lt4 = self.char[ind_4]
                        ind_4 += 1
                        psw = lt1 + lt2 + lt3 + lt4 + self.fin_pswd
                        hash_aux = hashlib.sha3_256(psw.encode())
                        has_com = hash_aux.hexdigest()
                        if has_com == self.hash:
                            found = True
                            value = psw
        if value != 0:
            print("The password is:", value)
        return value

    def passwd5(self, lett):
        """
        Solve the password with 5 characters
        52521875 Possibilities
        :param lett: List with the letter to start
        """
        # Return Value
        value = 0
        # Boolean value if we have found it or not
        found = False
        first_let = lett[0]
        end_let = lett[1]
        # First letter string
        fr_letter = self.char[self.char.find(first_let):self.char.find(end_let) + 1]
        ind_1 = 0
        while not found and ind_1 < len(fr_letter):
            lt1 = fr_letter[ind_1]
            ind_1 += 1
            ind_2 = 0
            while not found and ind_2 < len(self.char):
                lt2 = self.char[ind_2]
                ind_3 = 0
                ind_2 += 1
                while not found and ind_3 < len(self.char):
                    lt3 = self.char[ind_3]
                    ind_4 = 0
                    ind_3 += 1
                    while not found and ind_4 < len(self.char):
                        lt4 = self.char[ind_4]
                        ind_4 += 1
                        ind_5 = 0
                        while not found and ind_5 < len(self.char):
                            lt5 = self.char[ind_5]
                            ind_5 += 1
                            psw = lt1 + lt2 + lt3 + lt4 + lt5 + self.fin_pswd
                            hash_aux = hashlib.sha3_256(psw.encode())
                            has_com = hash_aux.hexdigest()
                            if has_com == self.hash:
                                found = True
                                value = psw
        if value != 0:
            print("The password is:", value)
        return value

    def passwd6(self, lett):
        """
        Solve the password with 6 characters
        1838265625 Possibilities
        :param lett: List with the letter to start
        """
        # Return Value
        value = 0
        # Boolean value if we have found it or not
        found = False
        first_let = lett[0]
        end_let = lett[1]
        # First letter string
        fr_letter = self.char[self.char.find(first_let):self.char.find(end_let) + 1]
        ind_1 = 0
        while not found and ind_1 < len(fr_letter):
            lt1 = fr_letter[ind_1]
            ind_1 += 1
            ind_2 = 0
            while not found and ind_2 < len(self.char):
                lt2 = self.char[ind_2]
                ind_3 = 0
                ind_2 += 1
                while not found and ind_3 < len(self.char):
                    lt3 = self.char[ind_3]
                    ind_4 = 0
                    ind_3 += 1
                    while not found and ind_4 < len(self.char):
                        lt4 = self.char[ind_4]
                        ind_4 += 1
                        ind_5 = 0
                        while not found and ind_5 < len(self.char):
                            lt5 = self.char[ind_5]
                            ind_5 += 1
                            ind_6 = 0
                            while not found and ind_6 < len(self.char):
                                lt6 = self.char[ind_6]
                                ind_6 += 1
                                psw = lt1 + lt2 + lt3 + lt4 + lt5 + lt6 + self.fin_pswd
                                hash_aux = hashlib.sha3_256(psw.encode())
                                has_com = hash_aux.hexdigest()
                                if has_com == self.hash:
                                    found = True
                                    value = psw
        if value != 0:
            print("The password is:", value)
        return value

    def solve(self, three=True, four=True, five=True, six=True):
        """
        Try to solve the password looking to all the possibilities between 2 and 6
        :param tree: If proves with 3 characters
        :param four: If proves with 3 characters
        :param five: If proves with 3 characters
        :param six: If proves with 3 characters
        :return:
        """
        n_p = len(self.letters)
        exit = False
        if three:
            t1 = time.time()
            print("With 3 characters")
            pool = multiprocessing.Pool(n_p)
            result = pool.map(self.passwd3, self.letters)
            t2 = time.time()
            print("Total time: ", t2 - t1)
            if any(result):
                exit = True
        if four and not exit:
            t1 = time.time()
            print("With 4 characters")
            pool = multiprocessing.Pool(n_p)
            result = pool.map(self.passwd4, self.letters)
            t2 = time.time()
            print("Total time: ", t2 - t1)
            if any(result):
                exit = True
        if five and not exit:
            t1 = time.time()
            print("With 5 characters")
            pool = multiprocessing.Pool(n_p)
            result = pool.map(self.passwd5, self.letters)
            t2 = time.time()
            print("Total time: ", t2 - t1)
            if any(result):
                exit = True
        if six and not exit:
            t1 = time.time()
            print("With 6 characters")
            pool = multiprocessing.Pool(n_p)
            pool.map(self.passwd6, self.letters)
            t2 = time.time()
            print("Total time: ", t2 - t1)
        return

