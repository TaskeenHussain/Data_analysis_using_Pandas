### Aggregation in Pandas  

# Aggregation in Pandas involves computing summary statistics like mean, sum, 
# or count for data grouped by categories or across an entire DataFrame.
# It simplifies data analysis by providing insights into trends and patterns efficiently.

# ### Applying Aggregations on DataFrame

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])

print (df)
r = df.rolling(window=3,min_periods=1)
print (r)

### Apply Aggregation on a Whole Dataframe

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df)
r = df.rolling(window=3,min_periods=1)
print (r.aggregate(np.sum))


 ### Apply Aggregation on a Single Column of a Dataframe

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df)
r = df.rolling(window=3,min_periods=1)
print (r['A'].aggregate(np.sum))

 ### Apply Aggregation on Multiple Columns of a DataFrame

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df)
r = df.rolling(window=3,min_periods=1)
print (r[['A','B']].aggregate(np.sum))

 ### Apply Multiple Functions on a Single Column of a DataFrame

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df)
r = df.rolling(window=3,min_periods=1)
print (r['A'].aggregate([np.sum,np.mean]))


# ### Apply Multiple Functions on Multiple Columns of a DataFrame

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df)
r = df.rolling(window=3,min_periods=1)
print (r[['A','B']].aggregate([np.sum,np.mean]))

#  ### Apply Different Functions to Different Columns of a Dataframe

import pandas as pd
import numpy as np
 
df = pd.DataFrame(np.random.randn(3, 4),
   index = pd.date_range('1/1/2000', periods=3),
   columns = ['A', 'B', 'C', 'D'])
print (df)
r = df.rolling(window=3,min_periods=1)
print (r.aggregate({'A' : np.sum,'B' : np.mean}))