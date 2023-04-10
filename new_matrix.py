from tabulate import tabulate

class Matrix:
    def __init__(self, *args):
        self.matrix = [[]]
        
        for column in args:
            self.matrix[0].append(column)
    
    def printf(self, format="simple"):
        if format == "simple":
            self.format = "psql"
        elif format == "fancy":
            self.format = "fancy_grid"
        
        print(
            tabulate(
                self.matrix,
                headers="firstrow",
                tablefmt=self.format
            )
        )

    
m1 = Matrix("Name" , "Age")
m1.printf()

m2 = Matrix("Skills" , "Hobby")
m2.printf("fancy")