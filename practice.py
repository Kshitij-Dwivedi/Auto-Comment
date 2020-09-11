import pandas as pd
df = pd.read_csv("./videos_id/3rmeiTJX3mw.csv",index_col=0)
comments_id =["1","2","3"]
y = pd.DataFrame(comments_id,columns=["id"])
x = pd.concat([df,y],ignore_index=True)
x.to_csv("./videos_id/3rmeiTJX3mw.csv")