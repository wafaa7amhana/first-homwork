def test(lst, char):
    result = [i for i in lst if i.startswith(char)]
    return result
L=["Network","Math","Programming","Physics","Music"]
print("\nOriginal list:")
print(L)
char = "P"
print("\nItems start with",char,"from the said list:")
print(test(L, char))
