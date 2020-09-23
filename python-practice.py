phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

phone_book["Godzilla"] = 46394  # New entry
print(phone_book)

phone_book["Godzilla"] = 9000  # updating
print(phone_book)



cersei = phone_book.pop("Cersei")
print(phone_book)
print(cersei)
#removing last
lastAdded = phone_book.popitem()
print(lastAdded)
print(len(phone_book))

list1=[1,2,3,"hi",2.3]
print(len(list1))

tuple=(2,3,4,"hi",'ok',8.9)
print(tuple)
print(len(tuple))


second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}

# Adding secondphone_book to phone_book
phone_book.update(second_phone_book)
print(phone_book)