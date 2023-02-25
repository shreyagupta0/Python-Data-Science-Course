class calc:

    result = 0

    def show(self):
        return self.result

    def add(self , n1, n2):
        self.result = n1+n2
    def sub(self , n1,n2):
        self.result = n1 - n2
    def mult(self , n1 , n2):
        self.result = n1 * n2

    def sq(self , n ):
        self.result = n*n    
c = calc()
c.add(10,20)
print(c.show())
c.sub(12,3)   
print(c.show())
c.sq(20)
print(c.show())
c.mult(67,88)
print(c.show())