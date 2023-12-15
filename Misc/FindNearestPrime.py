total_primes = []
f = open("C:/Users/blake/Documents/VSCode/Python/ProjectEuler/primes.txt", "r")
for line in f:
  total_primes.append(int(line))
f.close()

def is_prime2(num):
  if num == 2:
    return True
  if num%2 ==0 or num == 1:
    return False
  n = 0
  while total_primes[n]**2<=num:
    if num%total_primes[n]==0:
      return False
    n+=1
  return True

num = int(input('Find Nearest Prime to: '))
if is_prime2(num):
    print(num)
else:
    i = 1
    while True:
        if is_prime2(num+i):
            print(num+i)
            break
        elif is_prime2(num-i):
            print(num-i)
            break
        i += 1