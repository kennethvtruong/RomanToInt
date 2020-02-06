class Roman:
    def __init__(self, numeral, raw_lst, lst, ans):
        self.numeral = numeral
        self.raw_lst = raw_lst
        self.lst = lst
        self.ans = ans

    def get_input(self):
        self.numeral = input("What Roman numeral do you want converted? ")
        for i in self.numeral:
            self.raw_lst.append(i)
        print(self.raw_lst)

    def numeral_to_integer(self):
        for i in self.raw_lst:
            if i == "I":
                i = 1
                self.lst.append(i)
            elif i == "V":
                i = 5
                self.lst.append(i)
            elif i == "X":
                i = 10
                self.lst.append(i)
            elif i == "L":
                i = 50
                self.lst.append(i)
            elif i == "C":
                i = 100
                self.lst.append(i)
            elif i == "D":
                i = 500
                self.lst.append(i)
            elif i == "M":
                i = 1000
                self.lst.append(i)
        print(self.lst)

    def calculate_numeral(self):
        self.ans = 0
        for i in range(len(self.lst) - 1):
            if self.lst[i] < self.lst[i+1]:
                self.ans -= self.lst[i]
            else:
                self.ans += self.lst[i]
        self.ans += self.lst[len(self.lst) - 1]
        print(self.ans)
        return self.ans


my_sol = Roman("", [], [], 1)
my_sol.get_input()
my_sol.numeral_to_integer()
my_sol.calculate_numeral()
