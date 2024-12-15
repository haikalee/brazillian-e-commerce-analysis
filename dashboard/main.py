# import packages
import streamlit as st
import matplotlib.pyplot as plt
import datetime

# import local functions
from data import *
from plot import *


def delivery_time():
    # delivery time section
    st.subheader("Durasi Pengiriman")
    st.pyplot(fig=render_delivery_time())
    # end delivery time section


def delivery_time_review():
    # delivery time review section
    st.pyplot(fig=render_delivery_time_review())
    # end delivery time review section


def top_5_product():
    # top 5 product section
    st.subheader("5 Produk populer dan tidak populer")
    st.pyplot(fig=render_top_5_product())
    # end top 5 product section


def corr_price_freight():
    # correlation price freight section
    st.subheader("Harga Barang dan Biaya Pengiriman")
    st.pyplot(fig=render_corr_price_freight())
    # end correlation price freight section


def corr_product_weight_freight():
    # correlation price freight section
    st.pyplot(fig=render_corr_product_weight_freight())
    # end correlation price freight section


def rfm_analysis():
    # rfm analysis section
    st.subheader("Analisis RFM")
    st.pyplot(fig=render_rfm_analysis())
    # end rfm analysis


pg = st.navigation(
    [
        st.Page(page=delivery_time, title="Durasi Pengiriman"),
        st.Page(page=delivery_time_review, title="Review Durasi Pengiriman"),
        st.Page(page=top_5_product, title="Top 5 Produk"),
        st.Page(page=corr_price_freight, title="Korelasi Harga dan Biaya Pengiriman"),
        st.Page(
            page=corr_product_weight_freight,
            title="Korelasi Berat Produk dan Biaya Pengiriman",
        ),
        st.Page(page=rfm_analysis, title="Analisis RFM"),
    ]
)
pg.run()
