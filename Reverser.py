item = [5,6,3,56,67,34]
msee = ["ian","mwangi","msee"]
test = ["ian","eyansky",254,345]

    
def checkintergers(items):
    # check if the list only contains integers
    for x in items:
        if type(x) != int:
            return "They are not all integers!!"
    else:
        items.reverse()
        return items

def checkstrings(items):
    # check if the list only contains strings
    for x in items:
        if type(x) != str:
            return "They are not all strings!!"
    else:
        item = []
        for x in items:
            up = x.upper()
            item.append(up) 
        return item

def checksatisfacton(items):
    if checkintergers(items) == "They are not all integers!!" and checkstrings(items) == "They are not all strings!!":
        return items
    else:
        pass

print(checkintergers(msee))
print(checkstrings(msee))
print(checksatisfacton(item))

        

