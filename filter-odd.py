sequence = list([int(x) for x in input('enter values: ')]);
print('Your enetered values: ', type(sequence))
even_ls = []
odd_ls = []
def function(sequence):
        if sequence%2:
            return True
        else:
            return False
filtered = filter(function,sequence)
print("The filtered elements are", filtered)
for s in filtered:
    print (s, end=",")
