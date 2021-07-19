
class Rat:
    num = 0
    dem = 0
    def __init__(self, num = None,dem = None):
       if num and dem:
            self.num = num
            self.dem = dem
       elif num and not dem:
            self.num = num
            self.dem = 1
       else:
            self.num = 0
            self.dem = 1

    def get_num():
        return self.num
    def get_d():
        return self.dem

    def set_n(n):
        self.num = n
    def set_d(d):
        self.dem = d

    def __add__(self,next_rat):
        t = Rat()
        t.num = self.num * next_rat.dem + self.dem * next_rat.num
        t.dem = self.dem * next_rat.dem
        return t

    def __str__(self):
        return str(self.num)+'/'+str(self.dem)
        
def main():
    print ("hello")
    X = Rat(3 ,4)
    print(X)
    Y = Rat(3)
    print(Y)
    Z = Rat()
    print(Z)
    print ( Y + X)
if __name__ == "__main__":
    main()
