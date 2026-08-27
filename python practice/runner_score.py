# score=[1,3,5,6,6]
# score.sort()
# print(score)
# sc.remove()
# maxm=max(score)
# print(maxm)
# for i in score:
# unique = set(score)
# unique.remove(max(unique))
# second=max(unique)
# print(second)
# total=sum(score)
# print(total)
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n - 1)

print(factorial(5))