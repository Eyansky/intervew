items = [5,6,3,56,"56",67,34]
for x in items:
    if type(x) != int:
        print("they are not all intergers")
        break
    
def SwitchReverser(items):
    if type(items) == list:
        # check if the list only contains integers
        for x in items:
            if type(x) != int:
                print("They are not all integers!!")
                return False
        else:
            item = reversed(items)
            return item
        
        # check if the list only contains strings
        for x in items:
            if type(x) != string:
                print("They are not all strings!!")
        else:
            item = []
            for x in items:
                up = x.upper()
                item.append(up) 
                return item
    else:
        return items