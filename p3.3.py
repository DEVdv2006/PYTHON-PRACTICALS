p=int(input("Enter principal amount: "))
r=int(input("Enter interest rate"))
t=int(input("Enter time period"))

simple_intrest=(p*r*t)/100
print(f"Simple Intrest:{simple_intrest}")

n=int(input("enter no of times intrest is applied per time period"))
compound_intrest=p*pow(base=(1+(r/(100*n))),exp=(n*t))
print(f"Compound intrest:{compound_intrest}")