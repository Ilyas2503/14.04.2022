result = []

class Name:

    def __init__(self, name):
        self.name = name

    def save(self):
        result.append(self.name)

class name2(Name):
    def __init__(self, name2):
        super().__init__(name2)

    def save(self):
        self.name = "Bakyt"
        return super().save()

save = name2("Adiko")
save.save()
print (result)
save1 = Name('adiko')
save1.save()
print(result)
