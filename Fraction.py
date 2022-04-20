class Fraction:
    def __init__(self ,n,d,x,y) :
        self.sorat=n
        self.makhraj=d
        self.sorat1=x
        self.makhraj1=y
    def add(self):
        s1=(self.sorat/self.makhraj)+(self.sorat1/self.makhraj1)
        print=(s1)

    def sub(self)  :
        s1=(self.sorat/self.makhraj)-(self.sorat1/self.makhraj1)
        print=(s1)
    def mul(self)  :
        s1=(self.sorat/self.makhraj)*(self.sorat1/self.makhraj1)
        print=(s1) 
    def div(self)  :
        s1=(self.sorat/self.makhraj)/(self.sorat1/self.makhraj1)
        print=(s1)       
test=Fraction(8,2,6,3)
test.add()
test.sub()
test.mul()
test.div()
