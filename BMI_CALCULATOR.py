"""
---------------------------------------------------------------------------
Project Title      : Body Mass Index (BMI) Calculator
Organization       : Oasis Infobyte
Domain             : Python Programming Internship
Author             : Aman
Date               : June 2026
Description        : A clean, mobile-optimized BMI Calculator project 
                     structured using standard Python OOP design.
---------------------------------------------------------------------------
"""

import sys

class BMICalculator:
    def __init__(self):
        self.weight = 0.0
        self.height = 0.0
        self.bmi = 0.0

    def display_header(self):
        print("\n" + "="*40)
        print("      BMI CALCULATOR - INTERNSHIP      ")
        print("="*40)

    def get_valid_input(self, prompt, min_val, max_val):
        while True:
            try:
                val = float(input(prompt))
                if min_val <= val <= max_val:
                    return val
                else:
                    print(f"Error: Enter a value between {min_val} and {max_val}")
            except ValueError:
                print("Error: Please enter numbers only.")

    def collect_data(self):
        print("\n[System]: Enter your measurements below:")
        self.weight = self.get_valid_input("Weight in kg (e.g. 65): ", 10.0, 300.0)
        self.height = self.get_valid_input("Height in meters (e.g. 1.7): ", 0.5, 2.5)

    def calculate(self):
        # BMI standard calculation formula
        self.bmi = round(self.weight / (self.height ** 2), 2)

    def get_results(self):
        # Shortened text strings to prevent mobile formatting issues
        if self.bmi < 18.5:
            cat = "Underweight"
            rec = "Advice: Consider eating a more calorie-dense diet."
        elif 18.5 <= self.bmi < 24.9:
            cat = "Normal Weight"
            rec = "Advice: Great job! Maintain your current healthy lifestyle."
        elif 25.0 <= self.bmi < 29.9:
            cat = "Overweight"
            rec = "Advice: Consider incorporating regular physical activity."
        else:
            cat = "Obese"
            rec = "Advice: Highly advised to seek fitness or dietary guidance."
            
        return cat, rec

    def display_results(self):
        category, recommendation = self.get_results()
        print("\n" + "-"*40)
        print("            DIAGNOSTIC REPORT           ")
        print("-"*40)
        print(f" Your BMI        : {self.bmi}")
        print(f" Classification  : {category}")
        print("-"*40)
        print(recommendation)
        print("="*40 + "\n")


if __name__ == "__main__":
    try:
        app = BMICalculator()
        while True:
            app.display_header()
            app.collect_data()
            app.calculate()
            app.display_results()
            
            retry = input("Calculate again? (yes/no): ").lower().strip()
            if retry not in ['yes', 'y']:
                print("\n[System]: Closing app. Thank you!")
                break
    except KeyboardInterrupt:
        print("\n\n[System]: Program exited.")
        sys.exit(0)
