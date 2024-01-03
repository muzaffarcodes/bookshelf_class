class bookShelf:
	"""It can open left door or right one."""
	def __init__(self,color,height,width,depth,material,location):
		self.s = color
		self.v = height
		self.sh = width
		self.d = depth
		self.m = material
		self.l = location
    def __str__(self):
        return f""" The attributes of bookshelf
Color : {self.s}
Height: {self.v}
Width: {self.sh}
Depth : {self.d}
Material: {self.m}
Location: {self.l}
"""
       
    def openLeftDoor(self,doorOpenL):
        print("Left door is opened!")
        self.lDoor = doorOpenL

    def openRightDoor(self,doorOpenR):
        print("Right door is opened!")
        self.rDoor = doorOpenR    
        
shkaf = bookShelf('red', 120, 25, 30, "steel", 'living room')
print(shkaf)
