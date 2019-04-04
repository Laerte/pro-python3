tax = .07  # make a variable named tax that is floating point
print(id(tax))  # shows identity number of tax
print("Tax now changing value and identity number")
tax = .08  # create a new variable, in a different location in memory and mask the first one we created
print(id(tax))  # shows identity of tax
print("Now we switch tax back...")
tax = .07  # change tax back to .07 (mask the second one and reuse first
print(id(tax))  # now we see the original identity of tax
