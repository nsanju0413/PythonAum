class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        return 703 * self.weight / (self.height ** 2)

    def bmi_description(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Healthy"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"