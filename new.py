from matrix import Matrix

new = [
    ["A" , "B"],
    [21 , 31],
    [32 , 33]
]

m1 = Matrix()
# m1.import_csv("new.csv")
m1.import_matrix(new)


m1.printf("fancy")
