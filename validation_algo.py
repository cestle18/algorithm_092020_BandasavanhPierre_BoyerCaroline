from algorithm_092020_BandasavanhPierre_BoyerCaroline import FibonacciHeap

f_heap = FibonacciHeap()
f_heap.insert(5)
f_heap.insert(1)
f_heap.insert(10)
f_heap.insert(0)
f_heap.insert(42)
f_heap.insert(15)
f_heap.insert(7)
f_heap.insert(19)
f_heap.insert(20)
f_heap.insert(2)
f_heap.insert(84)
f_heap.insert(50)
print("\n\n==========\n\n")

expected=[]
while (node := f_heap.delete_min()) is not None:
	print(node)
	expected.append(node)

success = str(expected) == "[0, 1, 2, 5, 7, 10, 15, 19, 20, 42, 50, 84]"

if success:
	print("OK tout marche bien")
else:
	print("L'algorithme est cassé")

