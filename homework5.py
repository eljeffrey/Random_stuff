
class Rat:
    num = 0
    dem = 0
    def __init__(self, *inp):
        if len(inp) == 2:
            self.num,dem = self.two_args(inp)

    def two_args(self,args):
        x = 0
        y = 0
        if args[1] != 0:
            x = args[0]
            y = args[1]
        else:
            x = args[0]
            y = 1
        return x,y

    def get_num():
        return self.num
    def get_d():
        return self.dem

    def set_n(n):
        self.num = n
    def set_d(d):
        self.dem = d

    def rat_operator_plus(Rat):
        t = Rat()
        t.num = self.num * Rat.dem + dem * Rat.num
        t.dem = self.dem * Rat.dem
        return t

    def __str__(self):
        return self.num+'/'+self.dem
        
def main():
    print ("hello")
if __name__ == "__main__":
    main()
