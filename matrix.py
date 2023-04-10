from tabulate import tabulate

class Matrix:
    new_matrix = []

    def create(*args):
        row_matrix = []

        row_matrix.append("Sr_No")
        for column_header in args:
            row_matrix.append(column_header)

        Matrix.new_matrix.append(row_matrix)

        return Matrix.new_matrix
    
    def add_row(matrix,*args):
        row_matrix = []
        no_of_rows = len(matrix)-1
        row_matrix.append(no_of_rows+1)

        for items in args:
            row_matrix.append(items)

        matrix.append(row_matrix)
    
    def add_rows(matrix , values):
        for item in values:
            no_of_rows = len(matrix)-1
            matrix.append([no_of_rows + 1]+item)


    
    def add_column(matrix,header):
        matrix[0].append(header)
        
        for rows in matrix[1:len(matrix)]:
            if len(rows) != len(matrix[0]):
                rows.append(None)

    def store(matrix , value , row , column):
        if row == 0 or column == 0:
            return None

        row_matrix = matrix[row]
        row_matrix[column-1] = value

    def get(matrix , row , column):
        if row == 0 or column == 0:
            return None

        row_matrix = matrix[row]
        return row_matrix[column-1]

    def delete_row(matrix , row_no):
        row = matrix[row_no]
        matrix.remove(row)

    def printf(matrix , format):
        options = ["psql" , "fancy_grid"]
        chosen = ""

        if format == "plain":
            chosen = options[0]
        elif format == "fancy":
            chosen = options[1]
        else:
            chosen = options[0]

        print(
            tabulate(matrix , headers="firstrow" , tablefmt=chosen)
        )

    def help():
        
        print(
            tabulate([
                ["Matrix  " , "Faster Way To Formulate Data."]
            ] , headers="firstrow" , tablefmt="fancy_grid")
        )

        help_data = [
            ["Method" , "Functionality"],
            ["create" , "(*args) : headers"],
            ["add_row" , "(matrix , *args) : items"],
            ["add_rows" , "(matrix , values) : [items]"],
            ["add_column" , "(matrix , header) : header"],
            ["store" , "(matrix , value , row , column)"],
            ["get" , "(matrix , row , column)"],
            ["delete_row" , "(matrix , row)"],
            ["printf" , "(matrix , format) : plain/fancy"],
            ["help" , "Get Information About Matrix"]
        ]    

        print(
            tabulate(help_data , headers="firstrow", tablefmt="fancy_grid")
        )

