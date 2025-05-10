import streamlit as st

st.set_page_config(
    page_title="PriceSense",
    layout="wide",
)

st.markdown("""
    <style>
        .main-header {
            background-image: linear-gradient(rgba(255,255,255,0.7), rgba(255,255,255,0.7)),
                              url('https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSeKNe-085myhu5sfZYXe7IG83D0PsAag3ZtgAns8DhYS3phkiHpxizq-CdAoE8bH9_sMEvfk4sdVGMA4zDid2UqDTUbsrkHvZJicJOCw');
            background-size: cover;
            padding: 80px 40px;
            border-top-left-radius: 80px;
            border-top-right-radius: 80px;
            border-bottom-left-radius: 80px;
            border-bottom-right-radius: 80px;
        }
        .main-title {
            font-size: 48px;
            font-weight: bold;
            color: #000000;
        }
        .subtitle {
            font-size: 20px;
            margin-top: 10px;
            color: #000000;
        }
        .cta-button {
            background-color: #fbc02d;
            color: #000000;
            font-weight: bold;
            padding: 12px 24px;
            border-radius: 8px;
            text-decoration: none;
            display: inline-block;
            margin-top: 30px;
        }
            
        .cta-button:hover {
            background-color: #fbc02d;
            color: white;
        }
            
        h1, h3 {
            color: #0f172a;
        }

        .feature-title {
            font-size: 24px;
            font-weight: 700;
            color: #0f172a;
        }

        .feature-desc {
            font-size: 16px;
            color: #6b7280;
            margin-bottom: 10px;
        }

        .try-button {
            background-color: #10b981;
            color: white;
            padding: 0.4rem 1.2rem;
            border-radius: 10px;
            font-weight: 600;
            border: none;
            text-decoration: none;
            display: inline-block;
            transition: 0.3s ease;
        }

        .try-button:hover {
            background-color: #059669;
            color: white;
        }

        img {
            border-radius: 10px;
            width: 80%;
            height: auto;
            opacity: 0.60;
        }
            
        .container-manfaat {
            display: flex;
            background-color: #4CAF84;
            border-radius: 12px;
            padding: 20px;
            color: white;
            margin-bottom: 20px;
        }
            
        .container-info {
            display: flex;
            background-color: #4CAF84;
            border-radius: 12px;
            padding: 20px;
            color: white;
            margin-bottom: 20px;
        }
        
        .text-box {
            flex: 1;
            padding-right: 20px;
        }
            
        .image-box {
        flex: 1;
        }
        
        .contact-section {
            text-align: center;
            margin-top: 40px;
        }
        .contact-button {
            background-color: #2E7D32;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="main-header">
        <div class="main-title">Ketahui Harga Produk<br>Secara Real-Time!</div>
        <div class="subtitle">Dapatkan informasi harga beras, minyak, telur, dan kebutuhan pokok lainnya setiap hari!</div>
        <a href="#fitur" class="cta-button">Telusuri Harga</a>
    </div>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Fitur Utama</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6b7280;'>Strategi penetapan harga dan mengoptimalkan keputusan bisnis.</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="feature-title">Klasifikasi Harga</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature-desc">Rincian regional harga produk yang diklasifikasikan sebagai relatif murah, reguler, atau mahal menggunakan data historis.</div>', unsafe_allow_html=True)
    st.markdown('<a href="#" class="try-button">🔍 Coba</a>', unsafe_allow_html=True)

with col2:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2L4abXLLjw3nG8heLPYvUtfpXMTiIknp9bg&s", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.image("https://expertindo-training.com/wp-content/uploads/2023/05/Screenshot-2023-05-11-095742.jpg", use_container_width=True)

with col4:
    st.markdown('<div class="feature-title">Analisis Kompetitor</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature-desc">Dapatkan wawasan tentang strategi harga pesaing untuk tetap unggul di pasar.</div>', unsafe_allow_html=True)
    st.markdown('<a href="#" class="try-button">🔍 Coba</a>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="container-manfaat">
    <div class="text-box">
        <h2><b>Manfaat Pengguna</b></h2>
        <p>1. Atur Pengeluaran dengan Bijak.</p>
        <p>2. Lacak Tren Harga</p>
        <p>3. Peringatan Harga</p>
        <p>4. Menghemat Waktu dan Usaha.</p>
    </div>
    <div class="image-box">
        <img src="https://www.beritabethel.com/img/berita/waktu&uang.jpg" width="100%" style="border-radius: 10px;">
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="container-info">
    <div class="text-box">
        <h2><b>Tentang Kami</b></h2>
        <p>Kami adalah platform informasi harga sembako yang bertujuan membantu masyarakat Indonesia memantau dan membandingkan harga kebutuhan pokok di berbagai daerah.</p>
        <p>Pengguna dapat melihat harga beras, minyak goreng, telur, dan bahan pokok lainnya lengkap dengan status harga (mahal, murah, atau standar).</p>
        <p>Kami percaya dengan adanya akses informasi harga yang transparan dan mudah dipahami akan membantu konsumen dalam menghemat waktu dan usaha.</p>
    </div>
    <div class="image-box">
        <img src="https://thumb.viva.co.id/media/frontend/thumbs3/2022/09/21/632b0b83608da-ilustrasi-orang-sedang-menggunakan-laptop_665_374.jpg" width="100%" style="border-radius: 10px;">
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="contact-section">
    <h3>Info lebih lanjut<br>Hubungi Kami :</h3>
    <button class="contact-button">Kontak</button>
</div>
""", unsafe_allow_html=True)