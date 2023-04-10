from tabulate import tabulate

class Matrix:
    def __init__(self, *args):
        self.matrix = [[]]
        
        for column in args:
            self.matrix[0].append(column)

    def list(self):
        return self.matrix
    
    def add_row(self, *args):
        new_row = []
        for row_item in args:
            new_row.append(row_item)

        self.matrix.append(new_row)

    def add_column(self, column , location="last"):
        if location == "last":
            self.matrix[0].append(column)

            for rows in self.matrix[1:len(self.matrix)]:
                if len(rows) != len(self.matrix[0]):
                    rows.append(None)

        else:
            self.matrix[0].insert(location-1 , column)

            for rows in self.matrix[1:len(self.matrix)]:
                if len(rows) != len(self.matrix[0]):
                    rows.insert(location-1,None)

        

    def insert(self, value , row , column):
        row_no = self.matrix[row]
        row_no[column-1] = value
        
    def fetch(self , row , column):
        fetched = self.matrix[row][column-1]
        return fetched
    
    def remove(self, row , column):
        row_no = self.matrix[row]
        row_no[column-1] = None

    def delete_row(self, row):
        self.matrix.remove(self.matrix[row])
    
    def delete_column(self, column):
        column_index = self.matrix[0].index(column)

        row_count = 0

        for rows in self.matrix:
            rows.remove(self.matrix[row_count][column_index])
            row_count += 1

    def search(self , value):
        locations = [["row" , "column"]]

        row_count = 0
        column_count = 0

        for row in self.matrix:
            if value in row:
                for item in row:
                    column_count += 1
                    if item == value:
                        locations.append([row_count , column_count])
                
                column_count = 0

            row_count += 1


        return locations


    def printf(self, format="simple"):
        if format == "simple":
            self.format = "psql"
        elif format == "fancy":
            self.format = "fancy_grid"
        elif format == "raw":
            print(self.matrix)
            return
        
        print(
            tabulate(
                self.matrix,
                headers="firstrow",
                tablefmt=self.format
            )
        )

    def pretty_print(user_matrix , format="simple"):
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
            ["print_data" , "(matrix , format) : plain/fancy"],
            ["help" , "Get Information About Matrix"]
        ]    

        print(
            tabulate(help_data , headers="firstrow", tablefmt="fancy_grid")
        )
