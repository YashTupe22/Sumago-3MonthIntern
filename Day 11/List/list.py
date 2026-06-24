# TASK ON LIST
n = [10,20,50,60,80,90,10,20,50]
n.sort(reverse=True)
print(n[2])
# Write a program to sort a list of integers in ascending order.
print(n.sort())
# Write a program to find the maximum value in a list of integers.
print(max(n))
# Write a program to find the average of a list of numbers.
print(sum(n)/(len(n)))
# Write a program to find remove all the duplicates from a list.
dup = []
for num in n:
    if num not in dup:
        dup.append(num)
print(dup)
# Write a program to find the second smallest element in a list.
for num in dup:
    if num > (min(dup)):
        print(num)
        break
# Write a program to reverse a list of integers.
dup.reverse()
print(dup)
dup.append(80)
# Write a program to find the sum of all the elements in a list.
print(sum(dup))
# Write a program to find the median of a list of numbers.
if len(dup)%2==0:
    median = (len(dup)-1)/2

    print(dup[int(median)],dup[int(median+1)])
else: 
    median =int((len(dup)-1)/2)
    print(dup[median])
    print(dup)

l = [1,2,3,4,5,6,7,8,9,10]
print(l[1:])
print(l[:9])
print(l[1:9:2])
print(l[::9])
