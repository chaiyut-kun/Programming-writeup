def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

def generate_primes(limit):
    return [num for num in range(2, limit+1) if is_prime(num)]

# ตัวอย่างการใช้งาน
limit = int(input())
if limit <= 0 :
  print("ไม่สามารถหาได้")
else:
  primes = generate_primes(limit)
  print(f"จำนวนเฉพาะในช่วง 0 ถึง {limit}")
  print(f"มีอยู่ {len(primes)} จำนวน")

