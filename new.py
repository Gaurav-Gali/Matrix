from matrix import Matrix

m1 = Matrix.create("Name" , "Age")
Matrix.add_row(m1 , "Gaurav" , 17)
Matrix.add_row(m1 , "Rachna" , 12)

Matrix.add_column(m1 , "Sex")

Matrix.store(m1 , "Male" , 1 , 4)
Matrix.store(m1 , "Female" , 2 , 4)


Matrix.printf(m1 , "fancy")
# Matrix.help()