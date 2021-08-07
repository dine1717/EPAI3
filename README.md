# Session 13 - Generators and Iteration tools 

## Goal 1

Create a lazy iterator that will return a named tuple of the data in each row. The data types should be appropriate - i.e. if the column is a date, you should be storing dates in the named tuple, if the field is an integer, then it should be stored as an integer, etc.

## Goal 2

Calculate the number of violations by car make.


github link : https://github.com/dine1717/EPAI3/blob/Session13/session13.ipynb


### For goal one, We have implemented following function-
  - 1. Function cast_row: Function takes input as string for line of file and typecast the integer and date type objects from string to respective types.
  - 2. read_ticket_lazy: Generator object which takes input as file name. Creates a named tuple type of the header of file. reads the lines for file and yields the file rows and named tuple one at a time.
  - 3. We have implemented and tested the generator object in the session15.pynb file

### For goal two, We have implemented following function-
  - 1. Function get_voilations_by_car_make: Function takes make_name (example 'BMW') as input and returns the number of violations by this specific car make. We create a generator object with vehicle makes as elements. we use the collections counter object to count the violations.
