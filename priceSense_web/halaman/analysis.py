import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


model = joblib.load("halaman/RF_model.pkl")

st.set_page_config(layout="wide")

st.markdown("""
    <style>
    .header-title {
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .subtitle {
        font-size: 18px;
        margin-bottom: 30px;
        color: #555;
    }
    .search-box {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }
    .search-box input {
        padding: 8px;
        border-radius: 8px;
        border: 1px solid #ccc;
        margin-right: 10px;
        width: 25%;
    }
    .label {
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 12px;
        color: white;
        font-weight: bold;
        display: inline-block;
        margin-top: 10px;
    }
    
    .murah { background-color: #4caf50; }
    .normal { background-color: #ffc107; }
    .mahal { background-color: #e53935; }

    .item-card {
        border: 1px solid #ddd;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="header-title">Harga Saat Ini</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Telusuri harga produk dan klasifikasi secara real-time</div>', unsafe_allow_html=True)

with st.container():
    col1, col2, col3, col4 = st.columns([1.5, 1.5, 1.5, 1])
    with col1:
        lokasi = st.text_input("Lokasi", "")
    with col2:
        produk = st.text_input("Produk", "")
    with col3:
        kategori = st.text_input("Kategori", "")

    search_button=st.button("Cari")
    st.markdown('</div>', unsafe_allow_html=True)

    # dummy for predict data
    combined_data = pd.DataFrame({
            'name': ['gula', 'beras', 'minyak', 'gula', 'beras', 'Susu UHT 250ml'],
            'price': [15000, 50000, 30000, 14000, 48000, 5500],
            'source': ['astro', 'indomart', 'astro', 'indomart', 'astro', 'indomart'],
            'gambar': ["https://c.alfagift.id/product/1/1_A7753140002167_20220328182324989_base.jpg",
                       "https://cdn.zyrosite.com/cdn-ecommerce/store_01HHCK9RDJG7N7V9XAJ14F4RMK%2Fassets%2F1732180858283-HarumasPremium_25.png",
                       "https://c.alfagift.id/product/1/1_A09350001879_20211001113946725_base.jpg",
                       "https://c.alfagift.id/product/1/1_A7753140002167_20220328182324989_base.jpg",
                       "https://cdn.zyrosite.com/cdn-ecommerce/store_01HHCK9RDJG7N7V9XAJ14F4RMK%2Fassets%2F1732180858283-HarumasPremium_25.png",
                       "https://image.astronauts.cloud/product-images/2024/4/UltraMilkMocca250mlSusuUHT1_7b9a2202-cb54-4d24-ba8f-453148481be6_900x900.png"]
    })

    if search_button:

        filtered_data = combined_data[combined_data['name'].str.contains(produk, case=False)]

        if not filtered_data.empty:
            # simpan original format
            filtered_data['original_price'] = filtered_data['price']
            filtered_data['original_source'] = filtered_data['source']

            # Preprocessing
            # encode
            filtered_data['source'] = filtered_data['source'].map({'astro': 0, 'indomart': 1})

            scaler = MinMaxScaler()
            filtered_data['price'] = scaler.fit_transform(filtered_data[['price']])

            # Prediksi category
            input_features = filtered_data[['price', 'source']]
            predictions = model.predict(input_features)
            # filtered_data['price_category'] = predictions
            filtered_data['status'] = predictions
           
            # Tampilkan hasil

            # call original price format
            filtered_data['price'] = filtered_data['original_price']
            filtered_data = filtered_data.drop(columns=['original_price'])

            # call original store name
            filtered_data['source'] = filtered_data['source'].map({0:'astro', 1:'indomart'})
            
            # st.write("Nilai price_category di filtered_data:")
            # st.write(filtered_data['price_category'].unique())
            combined_data = combined_data.merge(
                filtered_data[['name', 'status']],
                on='name',
                how='left'
            )
            # st.write("Hasil Prediksi:")
            # st.dataframe(filtered_data)
        else:
            st.write("Produk tidak ditemukan.")

# produk_list = [
#     {"nama": "Beras", "status": "Murah", "gambar": "https://cdn.zyrosite.com/cdn-ecommerce/store_01HHCK9RDJG7N7V9XAJ14F4RMK%2Fassets%2F1732180858283-HarumasPremium_25.png"},
#     {"nama": "Gula Pasir", "status": "Mahal", "gambar": "https://cdn.zyrosite.com/cdn-ecommerce/store_01HHCK9RDJG7N7V9XAJ14F4RMK%2Fassets%2F1732180858283-HarumasPremium_25.png"},
#     {"nama": "Minyak Goreng", "status": "Mahal", "gambar": "https://cdn.zyrosite.com/cdn-ecommerce/store_01HHCK9RDJG7N7V9XAJ14F4RMK%2Fassets%2F1732180858283-HarumasPremium_25.png"},
#     {"nama": "Daging", "status": "Mahal", "gambar": "https://cdn.zyrosite.com/cdn-ecommerce/store_01HHCK9RDJG7N7V9XAJ14F4RMK%2Fassets%2F1732180858283-HarumasPremium_25.png"},
#     {"nama": "Telur Ayam", "status": "Murah", "gambar": "https://cdn.zyrosite.com/cdn-ecommerce/store_01HHCK9RDJG7N7V9XAJ14F4RMK%2Fassets%2F1732180858283-HarumasPremium_25.png"},
#     {"nama": "Margarin", "status": "Normal", "gambar": "https://cdn.zyrosite.com/cdn-ecommerce/store_01HHCK9RDJG7N7V9XAJ14F4RMK%2Fassets%2F1732180858283-HarumasPremium_25.png"},
#     {"nama": "Kecap Manis", "status": "Murah", "gambar": "https://cdn.zyrosite.com/cdn-ecommerce/store_01HHCK9RDJG7N7V9XAJ14F4RMK%2Fassets%2F1732180858283-HarumasPremium_25.png"},
#     {"nama": "Penyedap Rasa", "status": "Normal", "gambar": "https://cdn.zyrosite.com/cdn-ecommerce/store_01HHCK9RDJG7N7V9XAJ14F4RMK%2Fassets%2F1732180858283-HarumasPremium_25.png"},
#     {"nama": "Garam", "status": "Murah", "gambar": "https://cdn.zyrosite.com/cdn-ecommerce/store_01HHCK9RDJG7N7V9XAJ14F4RMK%2Fassets%2F1732180858283-HarumasPremium_25.png"},
# ]

st.markdown("<h2 style='text-align: center;'>Bahan Pokok</h2>", unsafe_allow_html=True)
cols = st.columns(3)

if search_button and not filtered_data.empty:
    cols = st.columns(3)

    for idx, item in enumerate(filtered_data.to_dict(orient='records')):
        with cols[idx % 3]:

            st.markdown(
                f'<div style="text-align: center;">'
                f'<img src="{item["gambar"]}" width="100"/>'
                f'</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div style="text-align: center;"><strong>{item["name"]}</strong></div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div style="text-align: center;"><strong>{item["price"]}</strong></div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div style="text-align: center;">Toko: {item["source"]}</div>',
                unsafe_allow_html=True
            )

            label_class = item.get("status", "unknown") if item.get("status") else "unknown"

            st.markdown(
                f'<div style="text-align: center;"><span class="label {label_class}">{item.get("status", "Tidak Tersedia")}</span></div>',
                unsafe_allow_html=True
            )

            # st.image(item["gambar"], width=100)
            # st.markdown(f"**{item['name']}**", unsafe_allow_html=True)
            # st.markdown(f"**{item["price"]}**", unsafe_allow_html=True)
            # st.markdown(f"Toko: {item["source"]}", unsafe_allow_html=True)
            # st.markdown(f'<span class="label {label_class}">{item.get("status", "Tidak Tersedia")}</span>', unsafe_allow_html=True)

            st.markdown("<br><br>", unsafe_allow_html=True)

else:
    for idx, item in enumerate(combined_data.to_dict(orient='records')):
            with cols[idx % 3]:

                st.markdown(
                    f'<div style="text-align: center;">'
                    f'<img src="{item["gambar"]}" width="100"/>'
                    f'</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div style="text-align: center;"><strong>{item["name"]}</strong></div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div style="text-align: center;"><strong>Rp. {item["price"]}</strong></div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div style="text-align: center;">Toko: {item["source"]}</div>',
                    unsafe_allow_html=True
                )

                label_class = item.get("status", "unknown") if item.get("status") else "unknown"

                st.markdown(
                    f'<div style="text-align: center;"><span class="label {label_class}">{item.get("status", "Tidak Tersedia")}</span></div>',
                    unsafe_allow_html=True
                )

                # st.image(item["gambar"], width=100)
                # st.markdown(f"**{item['name']}**", unsafe_allow_html=True)
                # st.markdown(f"**{item["price"]}**", unsafe_allow_html=True)
                # st.markdown(f"Toko: {item["source"]}", unsafe_allow_html=True)
                # label_class = item["status"].lower()
                # st.markdown(f'<span class="label {label_class}">{item.get("status", "Tidak Tersedia")}</span>', unsafe_allow_html=True)

                st.markdown("<br><br>", unsafe_allow_html=True)



produk_list2 = [
    {"nama": "Susu UHT 250ml", "harga": "Rp. 5.500", "toko": "Indomart", "status": "Murah", "gambar": "https://cdn.zyrosite.com/cdn-ecommerce/store_01HHCK9RDJG7N7V9XAJ14F4RMK%2Fassets%2F1732180858283-HarumasPremium_25.png"},
    {"nama": "Sabun Mandi Refill 800ml", "harga": "Rp. 33.000", "toko": "Toko Serba Ada", "status": "Murah", "gambar": "https://cdn.zyrosite.com/cdn-ecommerce/store_01HHCK9RDJG7N7V9XAJ14F4RMK%2Fassets%2F1732180858283-HarumasPremium_25.png"},
    {"nama": "Pasta Gigi", "harga": "Rp. 15.000", "toko": "Alfamart", "status": "Murah", "gambar": "https://cdn.zyrosite.com/cdn-ecommerce/store_01HHCK9RDJG7N7V9XAJ14F4RMK%2Fassets%2F1732180858283-HarumasPremium_25.png"},
    {"nama": "Tisu Kering", "harga": "Rp. 22.000", "toko": "Indomart", "status": "Normal", "gambar": "https://cdn.zyrosite.com/cdn-ecommerce/store_01HHCK9RDJG7N7V9XAJ14F4RMK%2Fassets%2F1732180858283-HarumasPremium_25.png"},
    {"nama": "Saos Sambal", "harga": "Rp. 12.500", "toko": "Indomart", "status": "Normal", "gambar": "https://cdn.zyrosite.com/cdn-ecommerce/store_01HHCK9RDJG7N7V9XAJ14F4RMK%2Fassets%2F1732180858283-HarumasPremium_25.png"},
    {"nama": "Telur 10 pcs", "harga": "Rp. 21.900", "toko": "Alfamart", "status": "Mahal", "gambar": "https://cdn.zyrosite.com/cdn-ecommerce/store_01HHCK9RDJG7N7V9XAJ14F4RMK%2Fassets%2F1732180858283-HarumasPremium_25.png"},
]

st.markdown("<h2 style='text-align: center;'>Toko Terdekat</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Rekomendasi harga termurah di wilayah anda</p>", unsafe_allow_html=True)
if "status_filter" not in st.session_state:
    st.session_state["status_filter"] = "Murah"

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("Murah"):  st.session_state["status_filter"] = "Murah"
with c2:
    if st.button("Normal"): st.session_state["status_filter"] = "Normal"
with c3:
    if st.button("Mahal"):  st.session_state["status_filter"] = "Mahal"

warna = {"Murah":"#4caf50","Normal":"#ffc107","Mahal":"#e53935"}
sf = st.session_state["status_filter"]
st.markdown(
    f"<h3 style='text-align:center;'>Menampilkan kategori: "
    f"<span style='color:{warna[sf]}'>{sf}</span></h3>",
    unsafe_allow_html=True
)

toko = [
    {"nama":"Susu UHT 200ml",     "toko":"Indomart","harga":7900,  "status":"Normal", "gambar":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvsx-xeiefTduE0-OglA37C6voQbKdHzA5BQ&s"},
    {"nama":"Sabun Cuci Piring",  "toko":"FamilyMart","harga":23000,"status":"Mahal","gambar":"https://www.static-src.com/wcsstore/Indraprastha/images/catalog/full//101/MTA-3390895/sunlight_-sunlight-jeruk-nipis-sabun-cuci-piring--755-ml-_full02.jpg"},
    {"nama":"Shampoo",            "toko":"Indomart","harga":25000, "status":"Murah", "gambar":"https://guardianindonesia.co.id/media/catalog/product/3/0/3042325.jpg?optimize=high&bg-color=255%2C255%2C255&fit=cover&height=375&width=840&auto=webp&format=pjpg"},
    {"nama":"Quaker 100g",        "toko":"Lawson","harga":75000,   "status":"Mahal", "gambar":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTE3faN8Ir9eQ8zwxJ0bLGURAQOTuMO7ODPDw&s"},
    {"nama":"Hand Sanitizer",     "toko":"Indomart","harga":18500, "status":"Normal", "gambar":"https://i0.wp.com/raisa.aeonstore.id/wp-content/uploads/2023/08/1253931.png?fit=1080%2C1080&ssl=1"},
    {"nama":"Baygon",             "toko":"Alfamart","harga":33700, "status":"Normal", "gambar":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1LuMLa2ipJvXH-JEL6b1PUyUODWDe5FdVow&s"},
]

filtered = [p for p in toko if p["status"] == sf]
cols = st.columns(3)
for i, p in enumerate(filtered):
    with cols[i % 3]:
        # st.markdown('<div class="item-card">', unsafe_allow_html=True)
        st.image(p["gambar"], width=100)
        # st.image("https://cdn.zyrosite.com/cdn-ecommerce/store_01HHCK9RDJG7N7V9XAJ14F4RMK%2Fassets%2F1732180858283-HarumasPremium_25.png", use_container_width=True)
        st.markdown(f"**{p['nama']}**", unsafe_allow_html=True)
        st.write(f"{p['toko']} : Rp. {p['harga']:,}")
        label_class = p["status"].lower()
        st.markdown(f'<span class="label {label_class}">{p["status"]}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>Lainnya</h2>", unsafe_allow_html=True)
cols = st.columns(3)

for idx, item in enumerate(produk_list2):
    with cols[idx % 3]:

        # st.markdown('<div class="item-card">', unsafe_allow_html=True)
        st.image(item["gambar"], width=100)
        st.markdown(f"**{item['nama']}**", unsafe_allow_html=True)
        label_class = item["status"].lower()
        st.markdown(f'<span class="label {label_class}">{item["status"]}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)