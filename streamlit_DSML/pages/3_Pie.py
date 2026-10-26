import streamlit as st
import pandas as pd
from pathlib import Path

st.title("🥧 Pie Chart")

# data/pie_demo.csv sits next to the pages folder
CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "pie_demo.csv"
sales = pd.read_csv(CSV_PATH)

st.markdown("#### Sales by Category")
st.vega_lite_chart(sales, {
    "mark": {"type": "arc", "tooltip": True},
    "encoding": {
        "theta": {"field": "Sales", "type": "quantitative"},
        "color": {"field": "Category", "type": "nominal"},
    },
}, use_container_width=True)

with st.expander("Show the data"):
    st.dataframe(sales, hide_index=True)

st.divider()
st.caption("Data loaded from `data/pie_demo.csv`. Edit `pages/3_Pie.py` to customize this page.")
