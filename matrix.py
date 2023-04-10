from tabulate import tabulate

class Matrix:
    def __init__(self, *args):
        self.matrix = [[]]
        
        for column in args:
            self.matrix[0].append(column)
    
    def add_row(self, *args):
        new_row = []
        for row_item in args:
            new_row.append(row_item)

        self.matrix.append(new_row)

    def add_column(self, column):
        self.matrix[0].append(column)

        for rows in self.matrix[1:len(self.matrix)]:
            if len(rows) != len(self.matrix[0]):
                rows.append(None)

    def insert(self, value , row , column):
        row_no = self.matrix[row]
        row_no[column-1] = value
        
    def fetch(self , row , column):
        fetched = self.matrix[row][column-1]
        return fetched
    
    def remove(self, row , column):
        row_no = self.matrix[row]
        row_no[column-1] = None

    def search(self , value):
        locations = [["row" , "column"]]

        for row in range(1 , len(self.matrix)):
            if value in self.matrix[row]:
                for item in range(row):
                    if self.matrix[row][item] == value:
                        column =  item
                        locations.append([row,column])
        
        return locations


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

    def print_data(user_matrix , format="simple"):
        if format == "simple":
            formated = "psql"
        elif format == "fancy":
            formated = "fancy_grid"
        
        print(
            tabulate(
                user_matrix,
                headers="firstrow",
                tablefmt=formated
            )
        )

    def help():
        
        print(
            tabulate([
                ["Matrix  " , "Faster Way To Formulate Data."]
            ] , headers="firstrow" , tablefmt="fancy_grid")
        )

        help_data = [
            ["Method" , "Functionality"],
            ["add_row" , "(*args) : items"],
            ["add_column" , "(header) : header"],
            ["insert" , "(value , row , column)"],
            ["fetch" , "(row , column)"],
            ["remove" , "(row , column)"],
            ["search" , "(search item)"],
            ["printf" , "(format) : plain/fancy"],
            ["print_data" , "(matrix , format) : plain/fancy"]
            ["help" , "Get Information About Matrix"]
        ]    

        print(
            tabulate(help_data , headers="firstrow", tablefmt="fancy_grid")
        )
