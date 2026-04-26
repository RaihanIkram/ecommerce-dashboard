import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("dashboard/main_data.csv")

# =========================
# HANDLE DATE
# =========================
date_col = 'order_purchase_timestamp'

if date_col in df.columns:
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')

# =========================
# SIDEBAR
# =========================
st.sidebar.title("Filter")

segment_option = st.sidebar.selectbox(
    "Select Segment",
    ["All", "Low Value", "Mid Value", "High Value"]
)

# date filter
if date_col in df.columns:
    min_date = df[date_col].min()
    max_date = df[date_col].max()

    date_range = st.sidebar.date_input(
        "Select Date Range",
        [min_date, max_date]
    )
else:
    date_range = None

# =========================
# FILTER GLOBAL
# =========================
df_filtered = df.copy()

if segment_option != "All" and 'segment' in df.columns:
    df_filtered = df_filtered[df_filtered['segment'] == segment_option]


# =========================
# TITLE
# =========================
st.title("E-Commerce Customer Dashboard")

# =========================
# VISUAL 1: SEGMENT
# =========================
st.subheader("Customer Segmentation")

if 'segment' in df_filtered.columns and not df_filtered.empty:

    segment_order = ["Low Value", "Mid Value", "High Value"]

    segment_counts = (
        df_filtered['segment']
        .value_counts()
        .reindex(segment_order)
        .fillna(0)
    )

    fig1, ax1 = plt.subplots()
    ax1.bar(segment_counts.index, segment_counts.values)
    ax1.set_title("Customer Segmentation based on RFM")
    ax1.set_xlabel("Segment")
    ax1.set_ylabel("Number of Customers")

    st.pyplot(fig1)

else:
    st.warning("No data available for selected filters.")

# =========================
# VISUAL 2: REVENUE
# =========================
st.subheader("Top Revenue by Category")

if (
    'product_category_name' in df_filtered.columns and
    'revenue' in df_filtered.columns and
    not df_filtered.empty
):

    category_revenue = (
        df_filtered
        .groupby('product_category_name')['revenue']
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    if not category_revenue.empty:

        fig2, ax2 = plt.subplots()
        category_revenue.plot(kind='bar', ax=ax2)

        ax2.set_title("Top 10 Revenue by Category")
        ax2.set_xlabel("Product Category")
        ax2.set_ylabel("Total Revenue")

        ax2.yaxis.set_major_formatter(
            ticker.FuncFormatter(lambda x, _: f'{int(x):,}')
        )

        plt.xticks(rotation=45)

        st.pyplot(fig2)

    else:
        st.warning("No revenue data available.")

else:
    st.warning("Required columns not found or data is empty.")