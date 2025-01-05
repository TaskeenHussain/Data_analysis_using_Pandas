### Concatenation in Pandas  

#### Concatenation in Pandas allows combining DataFrames or Series along rows or columns, 
# enabling seamless data merging and # integration. 
# It supports various options for handling indices and data alignment.

# ### Concatenating Objects
import pandas as pd

one = pd.DataFrame({
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5'],
   'Marks_scored':[98,90,87,69,78]},
   index=[1,2,3,4,5])

two = pd.DataFrame({
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5'],
   'Marks_scored':[89,80,79,97,88]},
   index=[1,2,3,4,5])
print (pd.concat([one,two]))

one = pd.DataFrame({
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5'],
   'Marks_scored':[98,90,87,69,78]},
   index=[1,2,3,4,5])

two = pd.DataFrame({
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5'],
   'Marks_scored':[89,80,79,97,88]},
   index=[1,2,3,4,5])
print (pd.concat([one,two],keys=['x','y']))

one = pd.DataFrame({
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5'],
   'Marks_scored':[98,90,87,69,78]},
   index=[1,2,3,4,5])

two = pd.DataFrame({
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5'],
   'Marks_scored':[89,80,79,97,88]},
   index=[1,2,3,4,5])
print (pd.concat([one,two],keys=['x','y'],ignore_index=True))

one = pd.DataFrame({
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5'],
   'Marks_scored':[98,90,87,69,78]},
   index=[1,2,3,4,5])

two = pd.DataFrame({
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5'],
   'Marks_scored':[89,80,79,97,88]},
   index=[1,2,3,4,5])
print (pd.concat([one,two],axis=1))


import pandas as pd

# DataFrame one with updated data
one = pd.DataFrame({
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id': ['Math', 'Physics', 'Chemistry', 'Biology', 'History'],
   'Marks_scored': [98, 90, 87, 69, 78]},
   index=[1, 2, 3, 4, 5])

# DataFrame two with updated data
two = pd.DataFrame({
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id': ['Physics', 'Chemistry', 'Math', 'Biology', 'History'],
   'Marks_scored': [89, 80, 79, 97, 88]},
   index=[6, 7, 8, 9, 10])

# Concatenating using pd.concat
result = pd.concat([one, two], ignore_index=True)
print(result)

import pandas as pd

# DataFrame one
one = pd.DataFrame({
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id': ['sub1', 'sub2', 'sub4', 'sub6', 'sub5'],
   'Marks_scored': [98, 90, 87, 69, 78]},
   index=[1, 2, 3, 4, 5])

# DataFrame two
two = pd.DataFrame({
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id': ['sub2', 'sub4', 'sub3', 'sub6', 'sub5'],
   'Marks_scored': [89, 80, 79, 97, 88]},
   index=[1, 2, 3, 4, 5])

# Concatenating DataFrames using pd.concat()
result = pd.concat([one, two, one, two], ignore_index=True)
print(result)

print (pd.Timestamp('2017-03-01'))


 ### Create a TimeStamp

import pandas as pd

print (pd.Timestamp(1587687255,unit='s'))

import pandas as pd

print (pd.date_range("11:00", "13:30", freq="30min").time)

print (pd.date_range("11:00", "13:30", freq="H").time)


import pandas as pd

# Converting a Series with date strings and a None value
print(pd.to_datetime(pd.Series(['Jul 31, 2009', '2010-01-10', None]), errors='coerce'))

import pandas as pd

# Converting a Series with date strings and a None value
result = pd.to_datetime(pd.Series(['Jul 31, 2009', '2010-01-10', None]), errors='coerce', infer_datetime_format=True)

print(result)