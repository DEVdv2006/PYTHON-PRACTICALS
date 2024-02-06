myset={'apple','banana','pineapple','grapes','watermelon'}
myset2={'apple','banana','greenapple','mango','melon'}
print(myset)
print(myset2)
myset.remove('banana')
myset2.add('sweetlemon')
print(myset)
print(myset2)

myset3=myset.union(myset2)
print(myset3)

myset4=myset.intersection(myset2)
print(myset4)

myset5=myset.symmetric_difference(myset2)
print(myset5)

myset6=myset.difference(myset2)
print(myset6)

print(myset.issubset(myset3))