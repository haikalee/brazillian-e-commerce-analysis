import pandas as pd
import numpy as np
from helpers import *

# load csv datas
all_df = pd.read_csv("./datas/all.csv")
order_items_df = pd.read_csv("./datas/order_items.csv")
order_reviews_df = pd.read_csv("./datas/order_reviews.csv")
orders_df = pd.read_csv("./datas/orders.csv")
products_df = pd.read_csv("./datas/products.csv")
sellers_df = pd.read_csv("./datas/sellers.csv")

# convert column to datetime
all_df_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]

all_df = to_datetime(all_df, all_df_columns)

orders_df_columns = ["order_purchase_timestamp", "order_approved_at"]

orders_df = to_datetime(orders_df, orders_df_columns)

# mencari selisih antara waktu persetujuan pesanan hingga pesanan diterima oleh  pelanggan
all_df["delivery_duration"] = (
    all_df.order_delivered_customer_date - all_df.order_approved_at
).dt.days

# merge dataframes
order_item_product = pd.merge(
    left=order_items_df,
    right=products_df,
    left_on="product_id",
    right_on="product_id",
)

order_product = pd.merge(
    left=order_items_df,
    right=products_df,
    how="inner",
    left_on="product_id",
    right_on="product_id",
)


# define function for get dataframe statistics of status order
def order_status_data():
    group_by_order_status = all_df.groupby(by="order_status").order_id.nunique()

    labels = group_by_order_status.index.tolist()
    values = group_by_order_status.values.tolist()

    order_status_df = pd.DataFrame({"total": values}, labels)
    order_status_df.sort_index(ascending=True)
    return order_status_df


# define function for analyze mean of delivery time
def delivery_time_mean_data():
    # mencari data delivery_duration yang tidak sesuai
    all_df.drop(all_df[all_df["delivery_duration"] < 0].index, inplace=True)

    # print("Rata - rata pengiriman: {} hari".format(all_df.delivery_duration.mean()))

    # visualisasi distribusi data menggunakan line plot
    delivery_duration_df = all_df.groupby(by="delivery_duration").order_id.nunique()
    return delivery_duration_df.values.tolist()


# define function for get data for get distribution of delivery duration and review score
def delivery_time_review_data():
    grouped_by_order_id = (
        all_df.groupby("order_id")
        .agg({"delivery_duration": "mean", "review_score": "mean"})
        .reset_index()
    )

    grouped_by_order_id["delivery_duration_bins"] = pd.cut(
        grouped_by_order_id["delivery_duration"], bins=range(0, 100, 5)
    )

    avg_score_by_duration = grouped_by_order_id.groupby("delivery_duration_bins")[
        "review_score"
    ].mean()
    return avg_score_by_duration


# define function for get product order by total order
def ordered_product(asc=False):
    return (
        order_item_product["product_category_name"]
        .value_counts()
        .sort_values(ascending=asc)
    )


# define function for get merged data of order and product
def order_product_data():
    return order_product


# define function for get RFM data
def rfm_data():
    rfm_df = (
        all_df[all_df["order_status"] == "delivered"]
        .groupby(by="customer_id", as_index=False)
        .agg({"order_purchase_timestamp": "max", "order_id": "nunique", "price": "sum"})
    )

    rfm_df.columns = ["customer_id", "max_order_timestamp", "frequency", "monetary"]
    # print(rfm_df["max_order_timestamp"].dt.date, "================================")

    rfm_df["max_order_timestamp"] = rfm_df["max_order_timestamp"].dt.date
    recent_date = orders_df["order_purchase_timestamp"].dt.date.max()
    rfm_df["recency"] = rfm_df["max_order_timestamp"].apply(
        lambda x: (recent_date - x).days
    )

    rfm_df.drop("max_order_timestamp", axis=1, inplace=True)

    return rfm_df
