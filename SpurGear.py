class SpurGear():
    def __init__(self, N=3, d=42):
        self.N = N
        self.d = d

    def getTeethAmount(self):
        return self.N

    def getPitchDiameter(self):
        return self.d

    def getDiametralPitch(self):
        return self.N/self.d

    def getModule(self):
        return self.d/self.N

    def getCircularPitch(self):
        return 3.1416 * self.d/self.N

    def __str__(self):
        return 'Spur Gear\n N: {} teeths\n d: {:.2f} mm\n P: {:.2f} teeths/mm\n m: {:.2f} mm\n p: {:.2f} mm'.format(self.N, self.d, self.getDiametralPitch(), self.getModule(), self.getCircularPitch())

gear = SpurGear();
print(gear)
