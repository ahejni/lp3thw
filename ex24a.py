def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 1000
start_point = start_point / 10

#print("Who can also do that this way:")
formula = secret_formula(start_point)
#this is an easy way to apply a list to format string.
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
