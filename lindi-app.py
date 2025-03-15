import streamlit as st
import pandas as pd

st.title("Hyjre ne te dhena")
Emri = st.text_input("Emri juaj: ")
Mosha = st.number_input("Mosha juaj eshte: ", min_value=0, max_value=100)
Shteti = st.selectbox("Shteti qe keni Zgjethur: ", ["Kosove", "Shqipri"])
if st.button("Dergo te dhena"):
    if Emri and Mosha and Shteti:
        st.write(f"Faleminderit, {Emri} qe keni zgjedhur te dhena te sakta!")
    data = {
        "Emri": [Emri],
        "Mosha": [Mosha],
        "Shteti": [Shteti]
    }
    df = pd.DataFrame(data)
    st.write(df)


else:
    st.error("Jep te dhena te sakta!")

st.title("Mirësevini në Aplikacionin tim Streamlit")
st.write("Ky është një shembull i thjeshtë i një aplikacioni Streamlit.")

name = st.text_input("Shkruani emrin tuaj:")
if name:
    st.write(f"Përshëndetje, {name}!")