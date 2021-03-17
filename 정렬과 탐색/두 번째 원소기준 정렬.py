array = [('홍길동', 50), ('이순신', 32), ('동동동', 3)]
print(sorted(array, key=lambda x:x[1]))
print(sorted(array, key=lambda x:x[1], reverse=True))