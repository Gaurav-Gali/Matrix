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


m1.delete_column("Age")

m1.printf("fancy")
