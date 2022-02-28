class Income():

    def __init__(self,Rental_Income=1000, Personal_Income=2000):
        self.Rental_Income = int(Rental_Income)
        self.Personal_Income = int(Personal_Income)



    def calcIncome(self):
        self.income = self.Rental_Income + self.Personal_Income
        return self.income

class Expenses():
    # def __init__(self, tax, insurance, utilities, HOA, yardcare, vacancy, repairs, CapEx, management, mortgage):
    #     self.tax = int(tax)
    #     self.insurance = int(insurance)
    #     self.utilities = int(utilities)
    #     self.HOA = int(HOA)
    #     self.yardcare = int(yardcare)
    #     self.vacancy = int(vacancy)
    #     self.repairs = int(repairs)
    #     self.CapEx = int(CapEx)
    #     self.management = int(management)
    #     self.mortgage = int(mortgage)

    def expenses(self):
        self.tax = int(input('What is your tax?'))
        self.insurance = int(input('How much will insurance cost?'))
        self.utilities = int(input('How much will utilities cost?'))
        self.HOA = int(input('How much will you have to pay for HOA?'))
        self.yardCare = int(input('How much will yard care cost?'))
        self.vacancy = int(input('How much will you set aside for vacancy?'))
        self.repairs = int(input('How much will you set aside for repairs?'))
        self.CapEx = int(input('How much will you set aside for capital expenses?'))
        self.management = int(input('How much will you pay for property management?'))
        self.mortgage = int(input('How much will you pay for mortgage?'))




    def TotalExpenses(self):
        self.expenses = self.tax + self.insurance + self.utilities + self.HOA + self.yardCare+ self.vacancy + self.repairs + self.CapEx + self.management +self.mortgage
        return self.expenses

class PropertyCost():
    def __init__(self, cost):
        self.cost = int(cost)

class ROI():
    def __init__(self, downPay, closingCost): #takes in all the varaibles you will need to calculate the return on investment
        self.downPay = int(downPay)
        self.closingCost = int(closingCost)
       

    def calcCashFlow(self, income, expenses): #calculates cash flow
        self.cashFlow = income - expenses
        return self.cashFlow    

    def totalInvestment(self): #calculates total amount spent on property 
        self.totalDown = self.downPay + self.closingCost 
        return self.totalDown
    
    def annualCashFlow(self): #calcluates yearly cashflow from property
        self.annualCash = self.cashFlow * 12
        return self.annualCash

    def totalROI(self): #calculates ROI
        self.totalROI = self.annualCash / self.totalDown
        return '{0:.2%}'.format(self.totalROI)

def run():
    income = Income()
    propertycost = PropertyCost()
    roi= ROI ()
    expenses= Expenses()

    ans = input("Welcome! Please answer the following prompts accordingly, type (Yes) to continue")

    if ans == "Yes":
        propertycost.cost = int(input('How much will the Property Cost?'))
        
        roi.downPay = int(input('How much will you put down as a down payment?'))

        income.Rental_Income = int(input('How much will you charge for rent?'))

        income.Personal_Income = int(input('How much do you make?'))

        expenses.tax = int(input('How much tax do you pay?'))

        expenses.insurance = 1


        roi.calcCashFlow(income.calcIncome(),expenses.TotalExpenses())


run()



#i dont know how to put everything together