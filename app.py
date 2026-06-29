import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="CSV Dashboard",
    page_icon="📊",
    layout="centered",
    menu_items={
        "Get help": "https://github.com/yourrepo",
        "Report a bug": "https://github.com/muecahitg/csv-dashboard/issues",
        "About": "A universal CSV dashboard that automatically visualizes any CSV file. Upload your data and instantly explore distributions, categories, missing values and more."
    }
)

st.title("csv dashboard")
#st.set_page_config("csv dashboard")

uploaded_file = st.file_uploader("load csv-file", type="csv")


if uploaded_file is not None:
	df = pd.read_csv(uploaded_file)
	st.subheader("preview")
	st.dataframe(df.head())
	st.write("---")
	st.subheader("summary")
	missing_vals = df.isnull().sum()

	st.write(f"rows: {df.shape[0]}")
	st.write(f"columns: {df.shape[1]}")
	st.write(missing_vals)
	st.write(df.describe())

	#l, r = st.columns(2)

	numeric_cols = df.select_dtypes(include="number").columns.tolist()

	#with l:
	st.subheader("diagrams")
	if len(numeric_cols) == 0:
		st.write("no columns found.")
	else:
		selected_col = st.selectbox("select column:", numeric_cols)
		fig, ax = plt.subplots()
		df[selected_col].hist(ax=ax, bins=20)
		ax.set_title(f"distribution: {selected_col}")
		ax.set_xlabel(selected_col)
		ax.set_ylabel("frequency")

		st.pyplot(fig)

	#with r:
	#st.write("---")
	categorical_cols = df.select_dtypes(include="object").columns.tolist()

	if len(categorical_cols) == 0:
		st.write("no categorical columns found.")
	else:
		bar_col1, bar_col2 = st.columns(2)

		with bar_col1:
			selected_cat_col = st.selectbox("select categorical column:", categorical_cols)
		with bar_col2:
			vals = st.number_input("number of values", min_value=1, max_value=20, value=5, key="bar_values")

		fig2, ax2 = plt.subplots()
		df[selected_cat_col].value_counts().head(vals).plot(kind="bar", ax=ax2)
		ax2.set_title(f"top {vals}: {selected_cat_col}")
		ax2.set_xlabel(selected_cat_col)
		ax2.set_ylabel("count")
		plt.xticks(rotation=45, ha="right")

		st.pyplot(fig2)

	st.write("---")
	st.subheader("pie chart")
	categorical_cols2 = df.select_dtypes(include="object").columns.tolist()
	pie_col1, pie_col2 = st.columns(2)

	with pie_col1:
		selected_pie_col = st.selectbox("select column for pie chart:", categorical_cols2)
	with pie_col2:
		vals = st.number_input("number of values", min_value=1, max_value=20, value=5, key="pie_values")

	fig3, ax3 = plt.subplots()
	df[selected_pie_col].value_counts().head(vals).plot(kind="pie", ax=ax3)
	ax3.set_ylabel("")

	st.pyplot(fig3)

