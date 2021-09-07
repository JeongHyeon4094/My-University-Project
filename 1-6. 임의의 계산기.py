#20214094 박정현

result = 0
class calculator():
    def formula(self, first, second):
        self.first = first
        self.second = second

    def ad(self):
        result = self.first + self.second
        return result

    def su(self):
        result = self.first - self.second
        return result

    def mu(self):
        result = self.first * self.second
        return result

    def di(self):
        result = self.first / self.second
        return result

class square(calculator):
    def sq(self):
        result = self.first ** self.second
        return result

cal = square()
cal_fist = int(input("num1: "))
cal_seco = int(input("num2: "))
four_cal = input("사칙 선택(+, -, *, /, ^): ")
cal.formula(cal_fist, cal_seco)
if four_cal == "+":
    print(cal.first, "+", cal.second, "=",cal.ad())
elif four_cal == "-":
    print(cal.first, "-", cal.second, "=",cal.su())
elif four_cal == "*":
    print(cal.first, "x", cal.second, "=",cal.mu())
elif four_cal == "/":
    print(cal.first, "÷", cal.second, "=",cal.di())
elif four_cal == "^":
    print(cal.first, "^", cal.second, "=",cal.sq())

