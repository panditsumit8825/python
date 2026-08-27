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
def tail_fact(n, acc=1):
    if n == 0:
        return acc
    else:
        return tail_fact(n-1, acc * n)

def nontail_fact(n):
    if n == 0:
        return 1
    else:
        return n * nontail_fact(n-1)
        
print(tail_fact(5))  
print(nontail_fact(5))