import streamlit as st
import numpy as np
import pandas as pd

# st.write('Bem vinda')

# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)


# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))

# st.dataframe(dataframe.style.highlight_max(axis=0))


# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))
# st.table(dataframe)


# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)



# st.title('My first app')

# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))


# """
# # My first app
# Here's our first attempt at using data to create a table:
# """

# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# df

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)


# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)




import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'