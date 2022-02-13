from turtle import width
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 超入門')
st.write('Dataframe')

st.checkbox('ShowImage')


st.line_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
     st.write("""
         The chart above shows some numbers I picked for you.
         I rolled actual dice for these, so they're *guaranteed* to
         be random.
     """)
     st.image("https://static.streamlit.io/examples/dice.jpg")

df= pd.DataFrame({
    '1列目':[1,2,3,2],
    '２列目':[1,10,20,40]
})

st.write(df)
st.dataframe(df,width=500, height=100)
st.dataframe(df.style.highlight_max(axis=0))
st.table(df.style.highlight_max(axis=0))


#マジックコマンドでマークダウンを利用できる
"""
# 章
## 節
### 項


```python
import streamlit as st
import numpy as np
import pandas as pd
```


"""

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a','b','c']
)

st.write(df)
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)

img = Image.open('test.jpg')
st.image(img, caption='test', use_column_width=True)