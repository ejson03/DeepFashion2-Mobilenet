import pandas as pd 
import json
import os
from os.path import splitext
import time

st = []
print(len(os.listdir('annos')))
for f in os.listdir('annos'):
    fname, _ = splitext(f)
    with open(os.path.join("annos", f)) as stuff:
        data = json.load(stuff)
        if('item1' in data.keys() and 'item2' in data.keys()):
            st.append([f"{fname}.jpg", 
                        data['source'], 
                        f"{data['item1']['category_name']}, {data['item2']['category_name']}",
                      f"{data['item1']['category_id']}, {data['item2']['category_id']}"
                    ])
        elif ('item1' not in data.keys()):
            st.append([f"{fname}.jpg", 
                        data['source'], 
                        data['item2']['category_name'],
                        data['item2']['category_id']
            ])
        else: 
            st.append([f"{fname}.jpg", 
                        data['source'], 
                        data['item1']['category_name'],
                    data['item1']['category_id']
            ])

print(st)
df =  pd.DataFrame(st, columns = ['image', 'source', 'category', 'id'])
df.to_csv('val.csv', index=False)