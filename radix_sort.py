import random



def pancake_sort(a):
    
    max_index = lambda x: x.index(max(x))
    for i in reversed(range(len(a))):
        reverese(a,0,max_index(a[:i+1]))
        reverse(a,0,i)

def reverse(a,low,high):

    while low < high:
        a[low],a[high] = a[high],a[low]
        high -=1 
        low += 1

def counting_sort(a,digit,base=10):

    values = [[] for _ in range(base)]
    
    for num in a:
        v = (num // (base**digit)) % len(values)
        values[v].append(num)

    result = []

    for bucket in values:
        result.extend(bucket)

    return result




def radix_sort(a,digits=3):

    for i in range(digits):
        a = counting_sort(a,i)
    
    return a


if __name__ == "__main__":
    

    a = [random.randint(1,500) for i in range(100)]

    print(a)

    sorted_a = radix_sort(a)
    print(sorted_a)
