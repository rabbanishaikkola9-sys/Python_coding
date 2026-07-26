dict={}
print(dict,type(dict))
dict={
    "rabbani":100,
    "rehaan":20,
    "king":"queen",
    "key":"value"
}
print(dict,"\n",type(dict))
# Using the key function()
print("yeah this is the printing of  the keys of the dictionary:\n")
print(dict.keys())
print("yeah this is the printing of  the values of the keys:\n")
print(dict.values())
print("Printing the key values of the dictionary:\n")
print(dict.items())
print("updating the dictionary:\n")
dict.update({"heck":"world"})
print(dict)
# get gives none and normally the output is syntax if get is not used 

# keys(),items(),values(),get(),update({}) are the methods used in dictionaries these are the primarily used methods or functions in Python

print("Hello world ")
print("End of the program!!")