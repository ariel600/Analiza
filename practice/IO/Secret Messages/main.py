class Secret_Messages:
    def __init__(self, name_file = "message.txt"):
        self.name_file = name_file
        self.message = input()
    
    def encryption(self):
        mass = ""
        encry = {"a":"z", "b":"y", "c":"x", "d":"w", "e":"v", "f":"u", "g":"t", "h":"s", "i":"r", "j":"q", "k":"p", "l":"o", "m":"n",
                "n":"m", "o":"l", "p":"k", "q":"j", "r":"i", "s":"h", "t":"g", "u":"f", "v":"e", "w":"d", "x":"c", "y":"b", "z":"a",
                "A":"Z", "B":"Y", "C":"X", "D":"W", "E":"V", "F":"U", "G":"T", "H":"S", "I":"R", "J":"Q", "K":"P", "L":"O", "M":"N",
                "N":"M", "O":"L", "P":"K", "Q":"J", "R":"I", "S":"H", "T":"G", "U":"F", "V":"E", "W":"D", "X":"C", "Y":"B", "Z":"A" }
        for line in self.message:
            if line in encry:
                mass += encry[line]
            else:
                mass += line
        return mass
    
    def seving(self):
        with open(self.name_file, "w") as mess:
            return mess.write(self.encryption())

    def print_mess(self):
        print(self.message)