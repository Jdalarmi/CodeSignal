class IP:
    def __init__(self, inputString):
        lista = inputString.split(".")
        self.is_ip = True
        self.number_1 = self.validate_number(lista[0])
        self.number_2 = self.validate_number(lista[1])
        self.number_3 = self.validate_number(lista[2])
        self.number_4 = self.validate_number(lista[3])
        

    def validate_number(self, numberInput):
        try:
            number = int(numberInput)
            if str(number) == numberInput:
                if self.is_ip:
                    if not 0 <= number < 256:
                        self.is_ip = False
            else:
                self.is_ip = False
        except:
            self.is_ip = False

def solution(inputString):
    if len(inputString.split(".")) == 4:
        ip = IP(inputString)
        return ip.is_ip
    else:
        return False