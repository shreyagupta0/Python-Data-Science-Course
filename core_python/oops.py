class dog:
    def __init__(self, breed , age,color):
        self.breed = breed
        self.age = age
        self.color = color

class cat:
    def __init__(self , name , gender , is_wild):
        self.name = name
        self.gender = gender
        self.is_wild = is_wild 
    

class burger:
    def __init__(self , bread , topping , filling , is_veg , price): #dunder methods 
        self.bread = bread
        self.topping = topping
        self.filling = filling
        self.is_veg = is_veg
        self.price = price
# use the classes to create object        
tiger = dog('german shepherd', 2 , 'golden')
sheru = dog('pug' , 3 , 'brown')
tommy = dog('labrador' , 4 , 'white')
mao = cat('mao' , 'f' , False)
oreo = cat('oero' , 'f' , False)
mimi = cat('mimi','f' ,True)
max = cat('max','f',False)
burger1 = burger('brown' , 'chees' , 'chicken' , False, 100) 
burger2 = burger('brown' , 'lettuce' , 'veg' , False , 150)

print("tiger is a " , tiger.breed, "dog")
