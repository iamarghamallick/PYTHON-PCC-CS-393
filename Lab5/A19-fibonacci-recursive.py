# A19. Using recursion write a program to find Fibonacci serise of 1st n terms.


def fibo(first, sec, n):
    if n == 0:
        return
    print(first, end=" ")
    fibo(sec, first + sec, n - 1)


n = 10
fibo(0, 1, n)
