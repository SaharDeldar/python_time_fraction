from ssl import _PasswordType


class Time:
    def __init__(self,h,m,s) :
       self.hour=h
       self.minute=m
       self.second=s

    def add(self):
        if self.minute +self.second:
            print(" error bishtar az 60 min ")
    def sub(self):
        if self.minute -self.second <0 :
            print(" error kamtar az 0 ")
    def s_to_h(self):
      self.hour= self.second/3600
      self.minute=self.second/60
    def h_to_s(self):
        s= self.hour*3600
        s=self.minute*60
test=Time(5,33,20)
test.add()
test.sub()
test.s_to_h()
test.h_to_s()
    
    
