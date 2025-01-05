# # Pandas - Series

# Create an Empty Series

#import the pandas library and aliasing as pd
import pandas as pd
s = pd.Series()
print (s)

# #### Create a Series from ndarray

# #import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print (s)

# #import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print (s)


 # ### Create a Series from dict


# #import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print (s)

# #import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print (s)

# # ### Create a Series from Scalar

#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
s = pd.Series(5, index=[0, 1, 2, 3])
print (s)


# # ### Accessing Data from Series with Position


import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first element
print (s[0])

import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first three element
print (s[:3])


import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the last three element
print (s[-3:])


# ### Retrieve Data Using Label (Index)


import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve a single element
print (s['a'])

import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])


# #retrieve multiple elements
print (s[['a','c','d']])

import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])


#retrieve multiple elements

import pandas as pd

# Sample series
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# Use get() to avoid KeyError for missing keys
print(s.get('f', 'Key not found'))  # Will print 'Key not found'
# print (s['f']) # Will raise KeyError


print (s['f']) # Will raise KeyError