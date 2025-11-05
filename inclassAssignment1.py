#Write a function that calculates the below: ( Mathematics - Geometry) 
# Area of the Circle
# Circumference of the Circle
# Volume and Surface area of a Cylinder
# Area of the rectangle
# Perimeter of the rectangle
# Area of the Square

# Area of the Circle
radius = float(input('radius = '))
area = 3.14 * radius * radius 
print('area of circle = ', area )
circum = 2 * 3.14 * radius 
print('circumfrence = ',circum)
 

height = float(input('height ='))
volume = 3.14 * (radius ** 2) * height 
print('volume of cylinder =', volume)

s_area = (2 * 3.14 * radius * height) + (2 * 3.14 * radius ** 2)
print('surface area of cylinder =', s_area)

length = float(input('length ='))
breadth = float(input('breadth ='))
a_rec = length * breadth 
print('area of rectangle =', a_rec)

peri = 2 * (length + breadth)
print('perimeter of rectangle =', peri)

side = float(input('side ='))
a_sq = side ** 2
print('area of square =', a_sq)