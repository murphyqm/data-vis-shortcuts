import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide", page_title="Gridded Plot", page_icon="🌠")

# with open( ".streamlit/style.css" ) as css:
#     st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.title('Gridded plot template for Matplotlib/Python')

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

desc_01 = """
This app was created by Maeve Murphy Quinlan as part of the teaching materials for the *Introduction to Data Visualisation with Python* course run by Research Computing at the University of Leeds.

© Maeve Murphy Quinlan, University of Leeds, 2024
"""

with st.sidebar:
    st.header("Create multi-panelled plots quickly")
    st.markdown(desc_01)

desc_02 = """
Select the number of rows and columns you want in your subplot, and choose whether you want x- and y-axes shared across panels or not. The preview and code snippet will update to match.

"""

st.markdown(desc_02)


col1, col2 = st.columns(2)

with col1:
    nrows = st.number_input("Number of rows", min_value=1, max_value=None)
    ncols = st.number_input("Number of columns", min_value=1, max_value=None)

    sharex = st.checkbox("Share x values on all subplots")
    sharey = st.checkbox("Share y values on all subplots")

    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)
    fig, axs = plt.subplots()
    fig, axs = plt.subplots(nrows, ncols, constrained_layout=True, sharex=sharex, sharey=sharey)
    for row in range(nrows):
        for col in range(ncols):
            axs[row, col].plot(x, y, 'tab:pink')
            axs[row, col].set_title(f'Axis [{row}, {col}]')
            axs[row, col].set(xlabel=f'{row}, {col} x-label', ylabel=f'{row}, {col} y-label')
    st.pyplot(fig)

markdown_str = f"""
# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Some example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

# Set up figure with {nrows} rows and {ncols} columns
"""

markdown_str = markdown_str + f"fig, axs = plt.subplots({nrows}, {ncols}, constrained_layout=True, sharex={sharex}, sharey={sharey})" + "\n"
for row in range(nrows):
    for col in range(ncols):
        markdown_str = markdown_str + "\n" + f"axs[{row}, {col}].plot(x, y, 'tab:pink')"
        markdown_str = markdown_str + "\n" + f"axs[{row}, {col}].set_title('Axis [{row}, {col}]')"
        markdown_str = markdown_str + "\n" + f"axs[{row}, {col}].set(xlabel='{row}, {col} x-label', ylabel='{row}, {col} y-label')"
        markdown_str = markdown_str + "\n"

markdown_str = markdown_str + "\n" + "plt.savefig('example_figure.png')"

with col2:
    st.code(markdown_str, language="python")