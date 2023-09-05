class MySet:
    def __init__(self, iterable=None):
        self.data = {}  
        if iterable is not None:
            for item in iterable:
                self.add(item)

    def has(self, value):
        return value in self.data

    def add(self, value):
        self.data[value] = None

    def delete(self, value):
        if value in self.data:
            del self.data[value]

    def size(self):
        return len(self.data)

    def clear(self):
        self.data = {}  

    def __str__(self):
        return f"MySet: {{{', '.join(map(str, self.data.keys()))}}}"

if __name__ == "__main__":
    
    my_set = MySet([1, 2, 3, 3])
    print(my_set)  

    my_set.add(4)
    print(my_set)  

    my_set.delete(2)
    print(my_set)  

    print(my_set.has(3))  
    print(my_set.has(2))  

    print(my_set.size())  

    my_set.clear()
    print(my_set)  
