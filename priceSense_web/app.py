import streamlit as st

main_page = st.Page(
    "halaman/home.py",
    title="Beranda",
    icon=":material/home:",
    default=True,
)
analysis_page = st.Page(
    "halaman/analysis.py",
    title="Analisis Harga",
    icon=":material/article:",
)
other_page = st.Page(
    "halaman/other.py",
    title="Lainnya",
    icon=":material/info:",
)

pg = st.navigation(pages=[main_page, analysis_page, other_page])

pg.run()