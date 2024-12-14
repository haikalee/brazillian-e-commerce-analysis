# import packages
import streamlit as st
import matplotlib.pyplot as plt

# import local functions
from data import *
from plot import *

st.header("Brazillian E-Commerce Analysis 👍")

# delivery time section
st.subheader("Durasi Pengiriman")
fig, ax = plt.subplots(figsize=(16, 8))
st.pyplot(fig=render_delivery_time())
# end delivery time section

# delivery time review section
fig, ax = plt.subplots(figsize=(16, 8))
st.pyplot(fig=render_delivery_time_review())
# end delivery time review section

# top 5 product section
st.subheader("5 Produk populer dan tidak populer")
fig, ax = plt.subplots(figsize=(16, 8))
st.pyplot(fig=render_top_5_product())
# end top 5 product section

# correlation price freight section
st.subheader("Harga Barang dan Biaya Pengiriman")
fig, ax = plt.subplots(figsize=(16, 8))
st.pyplot(fig=render_corr_price_freight())
# end correlation price freight section

# correlation price freight section
fig, ax = plt.subplots(figsize=(16, 8))
st.pyplot(fig=render_corr_product_weight_freight())
# end correlation price freight section

# rfm analysis section
st.subheader("Analisis RFM")
fig, ax = plt.subplots()
st.pyplot(fig=render_rfm_analysis())
# end rfm analysis
