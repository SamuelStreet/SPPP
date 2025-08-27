import plotly.express as px
import pandas as pd

df = pd.DataFrame(dict(
    x =[]  
))
fig = px.line(x=[[1,2,3],[1,2,3]], y = [[1,2,3],[2,4,6]], color=['red'])
#fig.update_xaxes(type='category')
fig.show()