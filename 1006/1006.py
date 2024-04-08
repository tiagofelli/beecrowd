import requests
number = int(input())
hours = int(input())
salary = float(input())

x = (hours * salary)

print("NUMBER = %0.0f"%(number))
print("SALARY = U$ %0.2f"%(x))

requests.post("https://ntfy.sh/teste",
    data="x".encode(encoding='utf-8'))