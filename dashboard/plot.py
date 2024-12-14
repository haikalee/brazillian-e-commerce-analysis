import matplotlib.pyplot as plt
from data import *
import seaborn as sns


def render_delivery_time():
    fig, ax = plt.subplots()
    ax.plot(delivery_time_mean_data())
    ax.set_xlabel("Jumlah Order")
    ax.set_ylabel("Rata-rata Durasi Pengiriman (hari)")
    ax.set_title(
        "Rata-rata Skor Ulasan Berdasarkan Rentang Durasi Pengiriman (Per Order)"
    )

    return fig


def render_delivery_time_review():
    fig, ax = plt.subplots()

    ax.plot(delivery_time_review_data().values, marker="o")
    ax.set_xlabel("Rentang Durasi Pengiriman (hari)")
    ax.set_ylabel("Rata-rata Skor Ulasan")
    ax.set_title(
        "Rata-rata Skor Ulasan Berdasarkan Rentang Durasi Pengiriman (Per Order)"
    )

    return fig


def render_top_5_product():
    fig, ax = plt.subplots(ncols=2, figsize=(16, 8))

    ax[0].bar(
        ordered_product(asc=False).head(5).index,
        ordered_product(asc=False).head(5).values,
    )
    ax[0].set_xlabel("Nama Produk")
    ax[0].set_ylabel("Total Order")
    ax[0].set_title("Top 5 Produk yang Paling Banyak Dipesan")
    ax[0].tick_params(axis="x", labelsize=9, rotation=45)
    ax[1].bar(
        ordered_product(asc=True).head(5).index,
        ordered_product(asc=True).head(5).values,
    )
    ax[1].set_xlabel("Nama Produk")
    ax[1].set_ylabel("Total Order")
    ax[1].set_title("Top 5 Produk yang Paling Banyak Dipesan")
    ax[1].tick_params(axis="x", labelsize=9, rotation=45)

    return fig


def render_corr_price_freight():
    data = order_product_data()

    fig, ax = plt.subplots()
    ax.scatter(data["price"], data["freight_value"], alpha=0.3)
    ax.set_xlabel("Harga")
    ax.set_ylabel("Biaya Pengiriman")
    ax.set_title("Korelasi Harga dan Biaya Pengiriman")

    return fig


def render_corr_product_weight_freight():
    data = order_product_data()

    fig, ax = plt.subplots()
    ax.scatter(data["product_weight_g"], data["freight_value"], alpha=0.3)
    ax.set_xlabel("Berat Produk")
    ax.set_ylabel("Biaya Pengiriman")
    ax.set_title("Korelasi Berat Produk dan Biaya Pengiriman")

    return fig


def render_rfm_analysis():
    rfm_df = rfm_data()

    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(30, 6))

    colors = ["#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4"]

    sns.barplot(
        y="recency",
        x="customer_id",
        data=rfm_df.sort_values(by="recency", ascending=True).head(5),
        palette=colors,
        ax=ax[0],
    )
    ax[0].set_ylabel(None)
    ax[0].set_xlabel(None)
    ax[0].set_title("By Recency (days)", loc="center", fontsize=18)
    ax[0].tick_params(axis="x", labelsize=9, rotation=45)

    sns.barplot(
        y="frequency",
        x="customer_id",
        data=rfm_df.sort_values(by="frequency", ascending=False).head(5),
        palette=colors,
        ax=ax[1],
    )
    ax[1].set_ylabel(None)
    ax[1].set_xlabel(None)
    ax[1].set_title("By Frequency", loc="center", fontsize=18)
    ax[1].tick_params(axis="x", labelsize=9, rotation=45)

    sns.barplot(
        y="monetary",
        x="customer_id",
        data=rfm_df.sort_values(by="monetary", ascending=False).head(5),
        palette=colors,
        ax=ax[2],
    )
    ax[2].set_ylabel(None)
    ax[2].set_xlabel(None)
    ax[2].set_title("By Monetary", loc="center", fontsize=18)
    ax[2].tick_params(axis="x", labelsize=9, rotation=45)

    return fig
