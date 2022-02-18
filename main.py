def number1(A):
    perimeter = 0
    A = sorted(A,reverse=True)
    for i in range(len(A) - 2):
        if A[i] < A[i+1] + A[i+2] and A[i+1] < A[i] + A[i+2] and A[i+2] < A[i] + A[i+1]:
            perimeter = (A[i]+A[i+1]+A[i+2])
        return perimeter

print("Пример 1.1: ", number1([2, 1, 2]))
print("Пример 1.2: ", number1([1, 2, 1]))
print("Пример 1.3: ", number1([3, 2, 3, 4]))
print("Пример 1.4: ", number1([3,6,2,3]))


