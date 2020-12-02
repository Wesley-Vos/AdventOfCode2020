input_file = open("input.txt", "r")
data = input_file.read().splitlines()
input_file.close()

class Password:
    def __init__(self, password_string):
        data = password_string.split("-")[1].split(" ")
        self.password = data[2]
        self.first = int(password_string.split("-")[0])
        self.second = int(data[0])
        self.criteria = data[1][0]

    def test_password(self, part):
        if part == 1:
            counter = 0
            for letter in self.password:
                counter += (letter == self.criteria)
            return (self.first <= counter <= self.second)
        else:
            return bool(self.password[self.first - 1] == self.criteria) != bool(self.password[self.second - 1] == self.criteria)
        

data = map(lambda x: Password(x), data)

part = 2
counter = 0
for d in data:
    counter += d.test_password(part)
print(counter)
