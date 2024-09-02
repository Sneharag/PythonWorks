#program to calculate monthly emi
#loan_amount
#tenure(years)=>months
#interest_rate=(p.a)->(p.m)
#emi=p*r*(1+r)**n/(1+r)**n-1

loan_amount=int(input("\nEnter the loan amount: "))

interest_rate=int(input("\nEnter interest rate: "))

monthly_interest_rate=interest_rate/12/100

tenure=int(input("\nEnter the tenure: "))

tenure_in_months=tenure*12

emi=loan_amount*monthly_interest_rate*((1+monthly_interest_rate)**tenure_in_months/(((1+monthly_interest_rate)**tenure_in_months)-1))

print(f"emi={emi}")

total_amount_payable=emi*tenure_in_months

print(f"Total amount payable={total_amount_payable}")

total_interest_payable=loan_amount-total_amount_payable

print(f"Total interest payable={total_interest_payable}")


