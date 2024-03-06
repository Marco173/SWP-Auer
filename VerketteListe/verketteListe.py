import random as rd
import copy
import time


class ListElement:
    def __init__(self, obj):
        self.obj = obj
        # Beim erzeugen ist das nächste Element none und wird erst im nächsten Ablauf definiert
        self.next = None

    def __str__(self):
        return str(self.obj)


class VerketteteListe:
    def __init__(self, *args):
        self.first = None

    def __str__(self):
        if self.first == None:
            return "[]"
        else:
            current = self.first
            result = "["
            while current.next != None:
                result += str(current.obj) + ", "
                current = current.next
            result += str(current.obj) + "]"
            return result

    def getLength(self):
        if self.first == None:
            return 0
        else:
            current = self.first
            length = 1
            while current.next != None:
                length += 1
                current = current.next
            return length

    def append(self, newObject):
        new = ListElement(newObject)
        if self.first == None:
            self.first = new
        else:
            self.getLast().next = new

    def getLast(self):
        return self.getElementByIndex(self.getLength()-1)

    def findObjIndex(self, obj):
        if self.first == None:
            return None
        else:
            current = self.first
            index = 0
            while current.next != None:
                if current.obj == obj:
                    return {"cur": current, "i": index}
                current = current.next
                index += 1
            if current.obj == obj:
                return {"cur": current, "i": index}
            else:
                return None

    def findObj(self, obj):
        # Wenn das Objekt nicht gefunden wurde, wird None zurückgegeben
        return self.findObjIndex(obj)["cur"] if self.findObjIndex(obj) != None else None

    def clear(self):
        self.first = None

    def extend(self, *args):
        for arg in args:
            self.append(arg)

    def index(self, obj):
        # Wenn das Objekt nicht gefunden wurde, wird None zurückgegeben
        return self.findObjIndex(obj)["i"] if self.findObjIndex(obj) != None else None

    def pop(self):
        # Das vorletzte Element referenziert auf kein anderes mehr
        elem = self.getElementByIndex(self.getLength()-2)
        elem.next = None

    def reverse(self):
        newList = VerketteteListe()
        listcopy = copy.deepcopy(self)
        while listcopy.getLength() > 1 and listcopy.getLast() != None:
            newList.append(listcopy.getLast())
            listcopy.pop()
        newList.append(listcopy.first)
        return newList

    def getElementByIndex(self, index):
        if index >= self.getLength():
            raise IndexError("Index out of range")
        else:
            i = 0
            current = self.first
            while current.next != None and i < index:
                current = current.next
                i += 1
            return current

    def delete(self, index):
        # Man will das Element vor dem zu löschenden Element
        elem = self.getElementByIndex(index-1)

        if index == 0:
            self.first = self.first.next
            return
        # Wenn elem.next.next = None, dann wird elem.next = None, sprich nach dem element gibt es kein anderes mehr
        elem.next = elem.next.next

    def getSmallest(self):
        current = self.first
        smallest = current
        for i in range(self.getLength()):
            if current.obj < smallest.obj:
                smallest = current
            current = current.next
        return smallest

    def sort(self):
        list2 = VerketteteListe()
        listC = copy.deepcopy(self)
        while listC.getLength() > 0:
            smallest = listC.getSmallest()
            list2.append(smallest.obj)
            listC.delete(listC.index(smallest.obj))

        return list2


def main():
    # create a new list
    list = VerketteteListe()
    # add some elements
    list.append(rd.randint(0, 100))
    list.append(rd.randint(0, 100))
    list.append(rd.randint(0, 100))
    list.append(rd.randint(0, 100))
    list.append(rd.randint(0, 100))
    # print the list
    print(
        f"Befuellte Liste (Zufallszahlen): {list} mit der Laenge {list.getLength()}")
    print(f"Gibt es das Element 100 in der Liste? {list.findObj(100)}")
    print(f"Die Liste wird gelöscht !")
    # list.clear()
    print(f"Die Liste ist jetzt leer: {list}")
    print(f"Die Liste wird mit 10 Elementen befuellt !")
    list.extend(1, 2, 10,  3, 4, 5, 6, 7, 8, 9, 10)
    print(f"Die Liste ist jetzt befuellt: {list}")

    print(f"Gib den Index des Objekts 10 zurück: {list.index(10)}")

    print(
        f"Das letzte Element der Liste ist {list.getLast()} Nun wird es gelöscht !")
    list.pop()
    print(f"Das letzte Element der Liste ist {list.getLast()}")
    print(f"Die Liste wird umgedreht !")
    list2 = list.reverse()
    print(
        f"Die Liste ist jetzt umgedreht: {list2} und die alte Liste ist {list}")
    print(f"Das Element am Index 8 wird gelöscht !")
    print(list)
    list.delete(0)
    print(list)
    print(f"Das Element am Index 8 ist jetzt {list.getElementByIndex(8)}")
    print(f"Die neue Liste ist {list}")

    sorted = list.sort()
    print(sorted)

# define main
if __name__ == "__main__":
    main()