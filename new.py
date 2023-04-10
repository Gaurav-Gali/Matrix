from matrix import Matrix

m1 = Matrix("Name" , "Age")
m1.add_row(
    "PersonOne",
    17
)
m1.add_row(
    "PersonOne",
    17
)
m1.add_row(
    "PersonOne",
    17
)

m1.add_column("Srno")
m1.insert(17 , 2,3)

a = m1.search(17)

Matrix.pretty_print(a)

m1.printf("fancy")
