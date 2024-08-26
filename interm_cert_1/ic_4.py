class Funny_list(list):
    def append(self, value):
        self.insert(0, value)
funny_list = Funny_list()

funny_list.append(10)
funny_list.append(11)
funny_list.append(12)

print(*funny_list)