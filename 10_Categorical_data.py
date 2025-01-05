## Understanding Categorical Data in Pandas  

### Categorical data is a type of data that represents discrete categories or labels. In pandas, 
# it can be efficiently managed using the `Categorical` type, improving both performance and memory usage.

# ### Object Creation

import pandas as pd

s = pd.Series(["a","b","c","a"], dtype="category")
print (s)

# ### pd.Categorical
import pandas as pd

cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
print (cat)

import pandas as pd

cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'])
print (cat)



cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'],ordered=True)
print (cat)

### Description
import pandas as pd
import numpy as np

cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
df = pd.DataFrame({"cat":cat, "s":["a", "c", "c", np.nan]})

print (df.describe())
print (df["cat"].describe())

# ### Get the Properties of the Category
import pandas as pd
import numpy as np

s = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print (s.categories)

cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print (cat.ordered)

import pandas as pd

# Create a Series with categorical data
s = pd.Series(["a", "b", "c", "a"], dtype="category")

# Rename the categories
s = s.cat.rename_categories(["Group %s" % g for g in s.cat.categories])

# Print the updated categories
print(s.cat.categories)

 ### Appending New Categories
import pandas as pd

s = pd.Series(["a","b","c","a"], dtype="category")
s = s.cat.add_categories([4])
print (s.cat.categories)

# ### Removing Categories
import pandas as pd

s = pd.Series(["a","b","c","a"], dtype="category")
print ("Original object:")
print (s)

print ("After removal:")
print (s.cat.remove_categories("a"))
