"""
Questions? Comments? Concerns?

Don't talk about 'em.
"""

print("This machine delivers onions. Please select how many onions you would like to receive.")
prompt = "One (1), or two (2)? "
numOnions = input(prompt)
if (numOnions == "1"):
    print("Ah, a traditionalist...")
elif (numOnions == "2"):
    print("Greedy girl, ain't ya?")
else:
    print(numOnions+"... but why?")
