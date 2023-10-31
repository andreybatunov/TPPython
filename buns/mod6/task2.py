class DoubleElement:
    def __init__(self, *lst):
        if len(lst) % 2 == 0:
            self.data = list(lst)
        else:
            self.data = list(lst)
            self.data.append(None)
        self.__counter = 0
        self.__limit = len(self.data)
            
    def __iter__(self):
        self.a = self.data[self.__counter]
        self.b = self.data[self.__counter + 1]
        return self
    
    def __next__(self):
        res = (self.a, self.b)
        current_pos = self.__counter + 2
        if self.__counter < self.__limit:
            if self.__limit - self.__counter != 2:
                self.a, self.b = self.data[current_pos], self.data[current_pos + 1]
            self.__counter += 2
        else:
            raise StopIteration
        return res

dL = DoubleElement(1,2,3,4)
for pair in dL:
    print(pair)
    
#     (1, 2)
#     (3, 4)

dL = DoubleElement(1,2,3,4,5)
for pair in dL:
    print(pair)
    
#     (1, 2)
#     (3, 4)
#     (5, None)
