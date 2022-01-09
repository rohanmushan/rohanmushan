tuples = ("java","python","c","cpp","visual basic","javascript","c#","pascal","fortran","c")

# Extract all list
print ("All list",tuples)

# Extract index number 2 to 5
print ("Index number 2 to 5",tuples[2:5])

#reverse elements
print ("Reverse elements",tuples[::-1])

#Index function
a = tuples.index("c#")
print ("Index function",a)

# Count function
b = tuples.count("c")
print ("Count function",b)