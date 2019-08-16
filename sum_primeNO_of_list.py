def sumprimes(list):
  length_list=len(list)
  prime_list=[]
  for i in range(0,length_list):
    if(list[i]%2!=0):
      prime_list.append(list[i])
  length_prime_list=len(prime_list)
  for i in range(0,length_prime_list):
    sum=sum+prime_list[i]
  return sum
l=[]
n=int(input('enter number of elements in list'))
print('enter list elements')
for i in range(0,n):
  ele=int(input())
  l.append(ele)
s=sumprime(l)
print("sum of prime number: ")
print(s)
  
      
