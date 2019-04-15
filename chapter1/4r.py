n=10
func=lambda x: print (x) if x>n else x*x
print(sum(list(map(func,range(1,4)))))
