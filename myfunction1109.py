def say_hello():
    print('hello')
    
def say_bye():
    print('bye')

a = 3

def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            print("소수가 아닙니다.")
            return 0
    print("소수입니다.")