from ssl import _PasswordType


class Time:
    def __init__(self,h,m,s) :
       self.hour=h
       self.minute=m
       self.second=s

    def add(self):
        if m+s>60 :
            print(" error bishtar az 60 min ")
    def sub(self):
        if m-s <0 :
            print(" error kamtar az 0 ")
    def s_to_h(self):
       h= s/3600
       m=s/60
    def h_to_s(self):
        s=h*3600
        s=m*60
test=Time(5,33,20)
test.add()
test.sub()
test.s_to_h()
test.h_to_s()
    
    
