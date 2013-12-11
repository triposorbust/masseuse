class _MockFile():
    def __init__(self, data=[]):
        self.__data = []
        for d in data:
            self.__data.append(d)
    def write(self, astring):
        data = map(float, astring.split()[1:])
        self.__data.append(data)
    def next(self):
        try: return self.__data.pop(0)
        except: raise StopIteration()
    def __iter__(self):
        return self
