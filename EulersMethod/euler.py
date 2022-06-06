class EulersMethod:
    def __init__(self, equation, x0, y0):
        try:
            self.equation = equation.strip().split("=")[1]
        except:
            raise Exception("Equation is not in the correct form, d.h. y'=f(x, y)")
        self.x0 = x0
        self.y0 = y0
    
    def __str__(self) -> str:
        return "Equation: " + self.equation + " || Initial values: x0=" + str(self.x0) + " & y0=" + str(self.y0)
    
    def __calculate(self, x0, y0, step_size):
        f = eval(self.equation.replace("x", str(x0)).replace("y", str(y0)))
        y1 = y0 + f * step_size
        return y1

    def execute(self, x_stop, step_size = 0.1, iterations = 1000):
        values = []
        x_cond = "larger"
        if (self.x0 > x_stop):
            x_cond = "smaller"
            step_size = (-1) * step_size
        x_curr = self.x0
        y_curr = self.y0
        i = 1
        while (i <= iterations):
            
            values.append([x_curr, y_curr])
            if (x_stop != False and (x_cond == "smaller" and x_curr <= x_stop) or (x_cond == "larger" and x_curr >= x_stop)):
                break
            y_curr = self.__calculate(x_curr, y_curr, step_size)
            x_curr += step_size
            i += 1

        return {"y": y_curr, "x": x_curr, "values": values}