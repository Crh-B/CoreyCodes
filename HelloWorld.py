# print("HelloWorld!")

# Make a short story about yourself with the information stored as each of the different variable types we talked about. Use at least 5.
# Source information
name = "Corey"
age = 27
ff = "sushi"
fn =  69.69
poland = [ 'Aro', 'Iwo', 'Beata', 'Bogdan', '& Julia' ]
tinydict = {'fibre': 'toast', 'protein': 'beans', 'calcium': 'cheese', 'spice': 'sriracha'}

# Short story
print(f"Hello! My name is {name}, I'm {age} years old, and my favourite food is {ff}.")
print(f"Sometimes people ask me what my favourite number is, and I never really know the answer so I just go with {fn}")
print(f"Soon I'll be traveling to Poland with Lidia where we'll see {poland}!")
print(f"but that's far away, so today I'll just focus on my lunch of {tinydict.values()}")

# Make a list of at least 10 elements long, print out the list, then print out the first 3 elements of the list
# List

numbers = [0,1,2,3,4,5,6,7,8,9]
print(numbers)
print(numbers[0:3])

# Make a variable integer then use it in an if statement to find if it is odd or even.
# I Googled this, but I think I understand it!
# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#     print("{0} is Even".format(num))
# else:
#     print("{0} is Odd".format(num))

# Do the same thing as in ex 1 but use a dictionary instead of variables.

# There has to be a better way to do this, but I can't figure it out
finaldict ={
    "brand": "Honda",
    "model": "Jazz",
    "year": 2006,
    "colour": "Blue",
    "miles": 65000
}
print("My car brand is a ")
print(finaldict["brand"])
print(finaldict["model"])
print("made in the year")
print(finaldict["year"])
print("and it's colour is")
print(finaldict["colour"])
print("and it has driven roughly")
print(finaldict["miles"])
print("miles")