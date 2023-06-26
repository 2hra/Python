n = int(input())
default = n
n_n = n+1
cnt = 0
while default!=n_n:
    n_one = n % 10
    n_ten = int(n / 10)
    n_n = (n_one*10)+((n_one+n_ten)%10)
    n = n_n
    cnt += 1
print(cnt)