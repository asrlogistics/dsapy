import stlpy as i

arr1 = [1,2,4,6]
num = 101010
arr2 = [3,5,7,8,9]
arr3 = [3,5,7,7,3,5,232,8,9]
print(i.array.addtoall(arr1,1))
print(i.number.factorial(5))
print(i.number.gcd(4,3))
print(i.dsa.binarysearch(arr1,0,4,3))
print(i.dsa.deletion(arr1,2))
print(i.number.bit.flip(num,1))
# print(i.number.bit.flip(num,))
print(i.dsa.mergeSort(arr1,arr2))
print(i.problem.josephus(50,29))
print(i.array.removeduplicates(arr3))
# print(i.array.permutations([1,2,3,4,5]))
print(len(list(i.array.permutations([1,2,3,4,5]))))

print(i.array.powerset([1,2,3]))

print(i.number.primearray(10))

print(i.number.sumtilln(10))
print(i.number.sumtilln(0))
# print(i.number.sumtilln("rbher"))

print(i.string.replaceallwith("pip","pi","3.14"))
print(i.array.matrix.transpose([[1,2],[4,5]]))

s = i.stack()
s.push(10)
s.push("yo")
s.push(eval("1+1"))
print(s)