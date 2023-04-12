from tabulate import tabulate
import csv

class Matrix:
    def __init__(self, *args):
        self.matrix = [[]]
        self.locked = False
        
        if len(args) == 1 and type(args[0]) == list:
            for column in args[0]:
                self.matrix[0].append(column)
        else:
            for column in args:
                self.matrix[0].append(column)
    
    def reset(self):
        self.matrix = [[]]
    
    def lock(self):
        self.locked = True
    
    def unlock(self):
        self.locked = False

    def export_matrix(self):
        return self.matrix
    
    def export_html(self , path , theme="light"):
        file = open(path , 'w')

        syntax_top = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

</head>
<body> 

        """

        table = tabulate(
            self.matrix,
            headers="firstrow",
            tablefmt="html"
        )

        if theme == "light":
            syntax_table = '<table class="table table-striped table-hover">' + table[7:len(table)]
        elif theme == "dark":
            syntax_table = '<table class="table table-dark table-striped table-hover">' + table[7:len(table)]

        syntax_bottom = """
        
</body>
</html>
        """

        file_data = syntax_top + syntax_table + syntax_bottom

        file.write(file_data)

        file.close()
    
    def raw_matrix(self):
        self.matrix = self.matrix[1:len(self.matrix)]
    
    def add_row(self, *args):
        if self.locked:
            return
        
        new_row = []
        if len(args) == 1 and type(args[0]) == list:
            for row_item in args[0]:
                new_row.append(row_item)
        else:
            for row_item in args:
                new_row.append(row_item)

        self.matrix.append(new_row)

    def add_column(self, column , location="last" , filler=None):
        if self.locked:
            return
        
        if location == "last":
            self.matrix[0].append(column)

            for rows in self.matrix[1:len(self.matrix)]:
                if len(rows) != len(self.matrix[0]):
                    rows.append(filler)

        else:
            self.matrix[0].insert(location-1 , column)

            for rows in self.matrix[1:len(self.matrix)]:
                if len(rows) != len(self.matrix[0]):
                    rows.insert(location-1,None)

    def row_result(self , row_no , operation="+"):
        if self.locked:
            return
        
        row = self.row_data(row_no)
        result = 0

        if operation == "+":
            for item in row:
                if item != None and type(item) != str:
                    result += eval(str(item))
        elif operation == "-":
            for item in row:
                if item != None and type(item) != str:
                    result -= eval(str(item))
        elif operation == "*":
            result = 1
            for item in row:
                if item != None and type(item) != str:
                    result *= eval(str(item))
        elif operation == "/":
            result = 1
            for item in row:
                if item != None and type(item) != str:
                    result /= eval(str(item))
        else:
            pass

        
        return result
    
    def column_result(self , column_name , operation = "+"):
        column = self.column_data(column_name)

        result = 0

        if operation == "+":
            for item in column:
                if item != None and type(item) != str:
                    result += eval(str(item))
        elif operation == "-":
            for item in column:
                if item != None and type(item) != str:
                    result -= eval(str(item))
        elif operation == "*":
            result = 1
            for item in column:
                if item != None and type(item) != str:
                    result *= eval(str(item))
        elif operation == "/":
            result = 1
            for item in column:
                if item != None and type(item) != str:
                    result /= eval(str(item))
        else:
            pass

        
        return result

    
    def len(self):
        return len(self.matrix)-1

    def row_data(self, row):
        row_count = 1
        for rows in self.matrix:
            if row_count == row:
                return self.matrix[row]
            row_count += 1

    def column_data(self, column):
        column_data = []
        column_index = self.matrix[0].index(column)

        for row in self.matrix:
            column_data.append(
                row[column_index]
            )

        return column_data


    def insert(self, value , row , column):
        if self.locked:
            return
        
        row_no = self.matrix[row]
        row_no[column-1] = value
        
    def fetch(self , row , column):
        fetched = self.matrix[row][column-1]
        return fetched
    
    def remove(self, row , column):
        if self.locked:
            return
        
        row_no = self.matrix[row]
        row_no[column-1] = None

    def delete_row(self, row):
        if self.locked:
            return
        
        self.matrix.remove(self.matrix[row])
    
    def delete_column(self, column):
        if self.locked:
            return
        
        column_index = self.matrix[0].index(column)

        row_count = 0

        for rows in self.matrix:
            rows.remove(self.matrix[row_count][column_index])
            row_count += 1

    def serialize(self):
        if self.locked:
            return
        
        self.add_column("Srno" , 1)
        row_count = 0
        for rows in self.matrix:
            if row_count == 0:
                row_count = 1
            else:
                rows[0] = row_count
                row_count += 1
    
    def count(self , value):
        locations = self.search(value)
        return len(locations) - 1

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
    

    
    def export_csv(self , path):
        file = open(path, 'w')
        writer_obj = csv.writer(file)
        writer_obj.writerows(self.matrix)
        file.close()

    def import_csv(self , path):
        csv_matrix = []
        file = open(path, 'r')
        reader = csv.reader(file)
        for row in reader:
            csv_matrix.append(row)
        file.close()

        self.matrix = csv_matrix

    def import_matrix(self , matrix):
        self.matrix = matrix
        
    def gen_table(self , rng , num):
        self.matrix.append([i for i in range(1,num+1)])

        for i in range(2,rng+1):
            row = []
            for j in range(1,num+1):
                row.append(j*i)
            
            self.matrix.append(row)

        


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
                ["Matrix        " , "Faster Way To Formulate Data.              " , "★  Important"]] , 
                headers="firstrow" , tablefmt="fancy_grid")
        )

        help_data = [
            ["Method" , "Functionality"],
            ["★  add_row" , "(*args) : items"],
            ["★  add_column" , "(header) : header"],
            ["★  insert" , "(value , row , column)"],
            ["★  fetch" , "(row , column)"],
            ["len" , "() : returns length of matrix"],
            ["remove" , "(row , column)"],
            ["reset" , "() : resets the matrix"],
            ["★  search" , "(search item)"],
            ["★  lock" , "() : locks the matrix"],
            ["★  unlock" , "() : unlocks the matrix"],
            ["row_result" , "(row_no , operation) : returns result of row operation"],
            ["column_result" , "(column_name , operation) : returns result of column operation"],
            ["★  printf" , "(format) : plain/fancy"],
            ["pretty_print" , "(matrix , format) : plain/fancy"],
            ["delete_row" , "(row)"],
            ["delete_column" , "(column)"],
            ["★  serialize" , "() : adds serial column"],
            ["count" , "() : counts the occurance"],
            ["★  row_data" , "(row) : returns row data"],
            ["★  column_data" , "(column_name) : returns column data"],
            ["export_csv" , "(path) : exports the matrix as csv "],
            ["export_matrix" , "() : exports the matrix as 2d list "],
            ["import_csv" , "(path) : imports csv as matrix "],
            ["★  import_matrix" , "() : imports a 2d list as matrix "],
            ["★  export_html" , "(path) : exports matrix as html tabe"],
            ["★  help" , "Get Information About Matrix"]
        ]    

        print(
            tabulate(help_data , headers="firstrow", tablefmt="fancy_grid")
        )
