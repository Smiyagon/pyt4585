#.set() => c# ' dan görmediğiiniz hattta merak edip bakmayacağınız nesnemiz  içerisinde uniq değer tutar. yani aynı elemandan en fazla 1 tane bulunabilir. 

mySet  = set()

print(mySet)

mySet.add(1)
mySet.add(2)
mySet.add(3)
print(len(mySet))
mySet.add(1)
mySet.add(2)
mySet.add(3)
print(len(mySet))
print(mySet)