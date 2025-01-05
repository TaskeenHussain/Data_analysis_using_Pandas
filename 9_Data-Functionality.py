### Data Functionality in Pandas  

# Pandas provides powerful data structures like DataFrames and Series to efficiently handle and manipulate structured data.
# It offers various functions for data cleaning, transformation, and analysis, making it an essential tool for data science.

 ### Create a Range of Dates
import pandas as pd

print (pd.date_range('1/1/2011', periods=5))


# ### Change the Date Frequency
print (pd.date_range('1/1/2011', periods=5,freq='M'))


# ### bdate_range

import pandas as pd

print (pd.date_range('1/1/2011', periods=5))

 ### String
import pandas as pd

print (pd.Timedelta('2 days 2 hours 15 minutes 30 seconds'))

### Integer
import pandas as pd

print (pd.Timedelta(6,unit='h'))

# ### Data Offsets
import pandas as pd

print (pd.Timedelta(days=2))

### to_timedelta()
import pandas as pd

print (pd.Timedelta(days=2))

### Operations

import pandas as pd

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))

print (df)


### Addition Operations
import pandas as pd

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
df['C']=df['A']+df['B']

print (df)

# ### Subtraction Operation
import pandas as pd

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
df['C']=df['A']+df['B']
df['D']=df['C']+df['B']

print (df)