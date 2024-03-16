import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
import altair as alt
import squarify
import random

st.set_page_config(
     page_title = 'Indeks Pembangunan Manusia'
     ,layout='wide'
)

st.markdown("<h1 style='text-align: center;'>Indeks Pembangunan Manusia Jawa Barat Tahun 2010-2023 </h1>", unsafe_allow_html=True)

# Sidebar Content
modeWarna = st.sidebar.selectbox(
    "Mode warna grafik",
    ("JAWA BARAT","KOTA DEPOK")
)
    
stringInfo1 = '''
            ### Dataset 
            
            Dataset yang digunakan dalam artikel ini bersumber dari :
            
            1. https://opendata.jabarprov.go.id/id/dataset/indeks-pembangunan-manusia-berdasarkan-kabupatenkota-di-jawa-barat 
            
            2. https://jabar.bps.go.id/subject/26/indeks-pembangunan-manusia.html#subjekViewTab1
            '''
st.sidebar.info(stringInfo1)
    
# Buat pilihan tab
Pendahuluan, Jawa_Barat, Analisa, Kesimpulan   = st.tabs(["Pendahuluan","Jawa Barat", "Analisa", "Kesimpulan" ])

# Tampilkan konten di tab
with Analisa:
    st.header("Menelusuri Indeks Pembangunan Manusia Terbaik dan Terbawah Jawa Barat")
     
    if modeWarna =='JAWA BARAT':
        ##ipm chart
        df_ipm = pd.read_csv("ipm_jabar.csv")
        # Buat plot
        fig_11, ax_11 = plt.subplots(figsize=(10, 6))
        nama_kabupaten_kota = df_ipm['nama_kabupaten_kota'].tolist()
        ipm = df_ipm['indeks_pembangunan_manusia'].tolist()
        ax_11.barh(nama_kabupaten_kota, ipm)
        # Menambahkan judul
        plt.title('Indeks Pembangunan Manusia Terbaik Jawa Barat Berdasarkan Ranking')
        # Menambahkan label pada sumbu x dan y
        plt.xlabel('Indeks Pembangunan Manusia')
        plt.ylabel('Nama Kabupaten Kota')
        
        df_ipm = pd.read_csv("ipm_jabar_terbawah.csv")
        # Buat plot
        fig_21, ax_21 = plt.subplots(figsize=(10, 6))
        nama_kabupaten_kota = df_ipm['nama_kabupaten_kota'].tolist()
        ipm = df_ipm['indeks_pembangunan_manusia'].tolist()
        ax_21.barh(nama_kabupaten_kota, ipm)
        # Menambahkan judul
        plt.title('Indeks Pembangunan Manusia Terburuk di Jawa Barat Berdasarkan Ranking')
        # Menambahkan label pada sumbu x dan y
        plt.xlabel('Indeks Pembangunan Manusia')
        plt.ylabel('Nama Kabupaten Kota')

        col1, col2 = st.columns(2)
        with col1:
            st.pyplot(fig_11)
        with col2:
            st.pyplot(fig_21)

    elif modeWarna == 'KOTA DEPOK':
        ##ipm chart
        df_ipm = pd.read_csv("ipm_jabar.csv")
        # Buat plot
        fig_31, ax_31 = plt.subplots(figsize=(10, 6))
        nama_kabupaten_kota = df_ipm['nama_kabupaten_kota'].tolist()
        ipm = df_ipm['indeks_pembangunan_manusia'].tolist()
        ax_31.barh(df_ipm["nama_kabupaten_kota"], df_ipm["indeks_pembangunan_manusia"], color=["#808080", "#808080", "#3366cc", "#808080", "#808080"])
        # Menambahkan judul
        plt.title('Indeks Pembangunan Manusia Terbaik Jawa Barat')
        # Menambahkan label pada sumbu x dan y
        plt.xlabel('Nama Kota Kabupaten')
        plt.ylabel('Indeks Pembangunan Manusia')
        
        df_ipm = pd.read_csv("ipm_jabar_terbawah.csv")
        # Buat plot
        fig_41, ax_41 = plt.subplots(figsize=(10, 6))
        nama_kabupaten_kota = df_ipm['nama_kabupaten_kota'].tolist()
        ipm = df_ipm['indeks_pembangunan_manusia'].tolist()
        ax_41.barh(nama_kabupaten_kota, ipm)
        # Menambahkan judul
        plt.figure(figsize=(8, 5))
        plt.title('Indeks Pembangunan Manusia Terburuk di Jawa Barat')
        # Menambahkan label pada sumbu x dan y
        plt.xlabel('Nama Kota Kabupaten')
        plt.ylabel('Indeks Pembangunan Manusia')
        
        col1, col2 = st.columns(2)
        with col1:
            st.pyplot(fig_31)
        with col2 :
            st.pyplot(fig_41)    

    st.write("Berdasarkan Grafik Aggregasi diatas, Kota Bandung menduduki puncak dengan IPM tertinggi di Jawa Barat, yaitu 80,23. Diikuti oleh Kota Bekasi 80,06 dan Kota Depok 79,57. Ketiga kota ini menunjukkan pencapaian yang baik dalam pembangunan manusia. Secara keseluruhan, IPM di Jawa Barat menunjukkan tren positif. Mayoritas kota mengalami peningkatan nilai IPM dibandingkan tahun sebelumnya. Hal ini mencerminkan upaya pemerintah dalam meningkatkan kualitas hidup masyarakat di seluruh wilayah. Meskipun menunjukkan kemajuan, disparitas antar kota masih terlihat. Kabupaten Pangandaran masih tertinggal dengan nilai IPM 52,74. Hal ini menunjukkan perlunya fokus dan perhatian lebih untuk mendorong pembangunan di daerah tertinggal. memotret deretan daerah dengan Indeks Pembangunan Manusia (IPM) terendah. Data ini menjadi cerminan bagi upaya pembangunan yang perlu diintensifkan untuk mencapai kesejahteraan yang merata.")

    st.header('Menelusuri IPM Kota Bandung')
    
    df_bandung = pd.read_csv('lineplot_kota_bandung.csv')
    #Buat Plot untuk Kota Bandung dengan Matplotlib
    plt.figure(figsize=(8, 5))
    plt.plot(df_bandung['tahun'], df_bandung['indeks_pembangunan_manusia'])
    plt.xlabel('Tahun')
    plt.ylabel('Indeks Pembangunan Manusia')
    plt.title('Line Plot Indeks Pembangunan Manusia Kota Bandung Tahun 2010-2023')
    # Tampilkan plot di Streamlit
    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(plt)
    
    st.write('Secara umum, IPM Kota Bandung mengalami tren kenaikan yang stabil, dari tahun 2010 hingga 2023.'
             'Kenaikan IPM ini menunjukkan bahwa pembangunan manusia di Kota Bandung terus meningkat'
             'Pada tahun 2010, IPM Kota Bandung berada pada angka 77,49.'
             'Pada tahun 2023, IPM Kota Bandung mencapai angka 83,04.'
             'Kenaikan IPM ini menunjukkan bahwa Kota Bandung telah mencapai kategori "Sangat Tinggi" dalam pembangunan manusia.')
    
    st.header('Menelusuri IPM Kabupaten Pangandaran')
    
    df_pangandaran = pd.read_csv('lineplot_kab_pangandaran.csv')
    #Buat Plot untuk Kabupaten Pangandaran menggunakan Matplotlib
    plt.figure(figsize=(8, 5))
    plt.plot(df_pangandaran['tahun'], df_pangandaran['indeks_pembangunan_manusia'])
    plt.xlabel('Tahun')
    plt.ylabel('Indeks Pembangunan Manusia')
    plt.title('Line Plot Indeks Pembangunan Manusia Kabupaten Pangandaran Tahun 2010-2023')
    # Tampilkan plot di Streamlit
    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(plt)
        
    st.write('Secara umum, IPM Kabupaten Pangandaran mengalami tren kenaikan yang stabil dari tahun 2010 hingga 2023.'
             'Kenaikan IPM ini menunjukkan bahwa pembangunan manusia di Kabupaten Pangandaran terus meningkat.'
             'Pada tahun 2013, Mengapa data awal Kabupaten Pangandaran 2013? karena Kabupaten ini beridiri pada tanggal 25 Oktober 2012. IPM Kabupaten Pangandaran berada pada angka 64,73.'
             'Pada tahun 2023, IPM Kabupaten Pangandaran mencapai angka 69,38.'
             'Walaupun tergolong belum lama berdiri menunjukkan bahwa Kabupaten Pangandaran telah mencapai kategori "Tinggi" dalam pembangunan manusia.')
    
    st.header(' Menelusuri Jejak IPM di Kota Depok')

    df_depok = pd.read_csv('lineplot_depok.csv')
    # Buat plot untuk Kota Depok dengan Matplotlib
    plt.figure(figsize=(8, 5))
    plt.plot(df_depok['tahun'], df_depok['indeks_pembangunan_manusia'])
    plt.xlabel('Tahun')
    plt.ylabel('Indeks Pembangunan Manusia')
    plt.title('Line Plot Indeks Pembangunan Manusia Kota Depok 2010-2023')
    # Tampilkan plot di Streamlit
    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(plt)

    st.write("Disini Penulis akan mengulas kota tempat tinggal penulis yaitu Kota Depok. Gambar line plot di atas adalah indeks pembangunan manusia di Kota Depok selama 13 tahun, terhitung dari tahun 2010 hingga 2023. Indeks Pembangunan Manusia (IPM) menjadi acuan yang mengarahkan kita pada tingkat kesejahteraan masyarakat, mengukur akses terhadap pendidikan, kesehatan, dan taraf hidup yang layak.Pada tahun 2010, IPM Kota Depok berada di angka 76,66. Angka ini menunjukkan bahwa pembangunan manusia masih memiliki ruang untuk berkembang.Sepanjang 13 tahun berikutnya, Depok menunjukkan geliat kemajuan yang menggembirakan. IPM secara konsisten meningkat, mencapai 82,38 pada tahun 2023. Kenaikan ini mencerminkan upaya pemerintah dalam meningkatkan kualitas hidup masyarakat.Meskipun menunjukkan tren positif, terdapat fluktuasi kecil pada IPM Depok di beberapa tahun. Fluktuasi ini dapat disebabkan oleh berbagai faktor, seperti perubahan kebijakan pemerintah, kondisi ekonomi, dan bencana alam.Data IPM menjadi peta jalan untuk pembangunan manusia yang lebih merata dan berkeadilan. Upaya meningkatkan kualitas pendidikan, kesehatan, dan taraf hidup masyarakat perlu terus digalakkan.")
    df_ipm_bodebek = pd.read_csv('indeks_pembangunan_manusia.csv')

    st.markdown('### Menelusuri Jejak Kemajuan Bodebek(Kota/Kabupaten Bogor, Kota Depok, Kota/Kabuapaten Bekasi)')

    kota_depok = df_ipm_bodebek[df_ipm_bodebek['nama_kabupaten_kota']=='KOTA DEPOK']
    kota_bogor = df_ipm_bodebek[df_ipm_bodebek['nama_kabupaten_kota']=='KOTA BOGOR']
    kota_bekasi = df_ipm_bodebek[df_ipm_bodebek['nama_kabupaten_kota']=='KOTA BEKASI']
    kab_bogor = df_ipm_bodebek[df_ipm_bodebek['nama_kabupaten_kota']=='KABUPATEN BOGOR']
    kab_bekasi = df_ipm_bodebek[df_ipm_bodebek['nama_kabupaten_kota']=='KABUPATEN BEKASI']

    x = df_ipm_bodebek['tahun'].unique()
    y1 = kota_depok['indeks_pembangunan_manusia']
    y2 = kota_bogor['indeks_pembangunan_manusia']
    y3 = kota_bekasi['indeks_pembangunan_manusia']
    y4 = kab_bogor['indeks_pembangunan_manusia']
    y5 = kab_bekasi['indeks_pembangunan_manusia']

    data = {
        "x" :np.array(x),
        "y1":np.array(y1),
        "y2":np.array(y2),
        "y3":np.array(y3),
        "y4":np.array(y4),
        "y5":np.array(y5)
    }
    df = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(df['x'], df['y1'], label='Kota Depok', color='blue')
    ax.plot(df['x'], df['y2'], label='Kota Bogor', color='red')
    ax.plot(df['x'], df['y3'], label='Kota Bekasi', color='green')
    ax.plot(df['x'], df['y4'], label='Kabupaten Bogor', color='grey')
    ax.plot(df['x'], df['y5'], label='Kabupaten Bekasi', color='grey')
    ax.set_xlabel('tahun')
    ax.set_ylabel('indeks pembangunan manusia')
    ax.legend()
    plt.show()

    ##ipm chart
    df_ipm_bodebek = pd.read_csv("ipm_bodebek_2023.csv")
    # Buat plot
    fig_22, ax = plt.subplots()
    nama_kabupaten_kota = df_ipm_bodebek['nama_kabupaten_kota'].tolist()
    ipm = df_ipm_bodebek['indeks_pembangunan_manusia'].tolist()
    ax.barh(nama_kabupaten_kota, ipm)
    # Menambahkan judul
    plt.title('Indeks Pembangunan Manusia Bodebek 2023')
    # Menambahkan label pada sumbu x dan y
    plt.xlabel('Nama Kota Kabupaten')
    plt.ylabel('Indeks Pembangunan Manusia')

    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(fig)
    with col2:
        st.pyplot(fig_22)
        
    st.write('Gambar multiline plot dan barplot diatas adalah pembangunan manusia di Bodebek selama 13 tahun, terhitung dari tahun 2010 hingga 2023. Indeks Pembangunan Manusia (IPM) menjadi kompas yang mengarahkan kita pada tingkat kesejahteraan masyarakat, mengukur akses terhadap pendidikan, kesehatan, dan taraf hidup yang layak.Pada tahun 2010, IPM di Bodebek  menunjukkan variasi, dengan Kota Bekasi sebagai yang terdepan (83,03) dan Kabupaten Bogor sebagai yang tertinggal (71,78).Sepanjang 13 tahun berikutnya, Bodebek menunjukkan geliat kemajuan yang menggembirakan. IPM secara konsisten meningkat di semua wilayah, dengan Kota Depok dan Kota Bekasi mengalami kenaikan paling signifikan. Data IPM menjadi tolak ukur untuk pembangunan manusia yang lebih merata dan berkeadilan. Upaya meningkatkan kualitas pendidikan, kesehatan, dan taraf hidup masyarakat perlu terus digalakkan di semua wilayah. Line plot Bodebek 2010-2023 memberikan gambaran kemajuan dan tantangan dalam pembangunan manusia. Data ini menjadi landasan untuk melangkah maju, menuju Bodebek khusunya dan Jawa Barat umumnya yang lebih sejahtera dan berkeadilan.')

    st.header('Boxplot Indeks Pembangunan Manusia Bodebek')
    
    #Boxplot IPM
    fig, ax = plt.subplots(figsize=(10, 6))
    col1, col2 = st.columns(2)
    with col1 :
        ax.boxplot([y1,y2,y3,y4,y5], labels=['Kota Depok', 'Kota Bogor', 'Kota Bekasi', 'Kab Bogor', 'Kab Bekasi'], showmeans=True)
        ax.set_title("Boxplot IPM")
        ax.set_xlabel("Kota")
        ax.set_ylabel("IPM")
        st.pyplot(fig)

    st.write('Insight : Berdasarkan Boxplot dibawah, bisa di terjemahkan ada perbedaan yang signifikan antara Kabupaten/Kota yang satu dan yang lainnya di wilayah Bodebek.')
    st.write('Possible Cause : Kemungkinan adanya penyebab perbedaan siginifikan Indeks Pembangunan Manusia di Bodebek perlu kita lakukan lebih lanjut mengenai faktor penyebabnya. Kita bisa mengira faktor tersebut antara lain: Korelasi Pendiidikan, Kepadatan Penduduk, Ekonomi, Kesenjangan Sosial.')

# Tampilkan konten di tab
with Pendahuluan:
    st.write('Penulis: Ryan Nursukmawan')
    st.header('Latar Belakang')
    st.write('Mengutip isi Human Development Report (HDR) pertama tahun 1990, pembangunan manusia adalah suatu proses untuk memperbanyak pilihan-pilihan yang dimiliki oleh manusia. Diantara banyak pilihan tersebut, pilihan yang terpenting adalah untuk berumur panjang dan sehat, untuk berilmu pengetahuan, dan untuk mempunyai akses terhadap sumber daya yang dibutuhkan agar dapat hidup secara layak. Indeks Pembangunan Manusia (IPM) mengukur capaian pembangunan manusia berbasis sejumlah komponen dasar kualitas hidup. Sebagai ukuran kualitas hidup, IPM dibangun melalui pendekatan tiga dimensi dasar. Dimensi tersebut mencakup umur panjang dan sehat; pengetahuan, dan kehidupan yang layak. Ketiga dimensi tersebut memiliki pengertian sangat luas karena terkait banyak faktor. ')
    st.header('Batasan Masalah')
    st.write('1. Data ini diambil melalui Open Data Jabar yaitu Portal Data resmi Pemerintah Provinsi Jawa Barat dan juga Badan Pusat Statistik yaitu Portal Data resmi Pemerintah Pusat.')
    st.write ('2. Analisis ini hanya membahas seputar Indeks Pembangunan Manusia di Jawa Barat dan Bodebek Tahun 2010-2023.')    
    st.header('Tujuan Analisis')
    st.write('1. Mengukur Keberhasilan Pembangunan Manusia')
    st.write('Dengan melihat nilai Indeks Pembangunan Manusia (IPM), kita dapat mengetahui tingkat kemajuan pembangunan manusia di suatu wilayah dibandingkan dengan wilayah lain atau dibandingkan dengan waktu sebelumnya.')
    st.write('2. Membandingkan Pembangunan Manusia Antar Wilayah')
    st.write('IPM dapat digunakan untuk membandingkan tingkat pembangunan manusia antar wilayah, baik antar provinsi, kabupaten/kota, maupun negara.Informasi ini dapat membantu pemerintah dalam menentukan kebijakan pembangunan yang tepat dan prioritas pembangunan di wilayah mana yang perlu ditingkatkan.')
    st.write('3. Mengevaluasi Efektivitas Kebijakan Pembangunan')
    st.write('IPM dapat digunakan untuk mengevaluasi efektivitas kebijakan pembangunan yang telah dijalankan oleh pemerintah.Dengan melihat tren nilai IPM dari waktu ke waktu, pemerintah dapat mengetahui apakah kebijakan yang dijalankan telah memberikan dampak positif terhadap pembangunan manusia.')
    st.write('4. Menentukan Target Pembangunan')
    st.write('Nilai IPM dapat digunakan sebagai acuan dalam menentukan target pembangunan manusia di masa depan.Pemerintah dapat menetapkan target peningkatan nilai IPM dalam jangka pendek, menengah, dan panjang.')
    st.write('5. Meningkatkan Kesadaran Masyarakat')
    st.write('Analisis IPM dapat meningkatkan kesadaran masyarakat tentang pentingnya pembangunan manusia.Informasi ini dapat mendorong masyarakat untuk terlibat aktif dalam proses pembangunan manusia di wilayahnya.')
    st.header('Harapan Analisis')
    st.write('Informasi ini dapat digunakan oleh pemerintah Jawa Barat untuk:')
    st.write('1.Menentukan kebijakan pembangunan yang tepat untuk meningkatkan IPM di wilayah yang masih rendah.')
    st.write('2.Mengevaluasi efektivitas kebijakan pembangunan yang telah dijalankan.')
    st.write('3.Menentukan target peningkatan IPM di masa depan.')
    st.write('4.Meningkatkan kesadaran masyarakat tentang pentingnya pembangunan manusia.')
    
with Jawa_Barat:

     # Memuat data
    pivot_table_path = 'pivot_table_jabar.csv'
    data = pd.read_csv('pivot_table_jabar.csv')

    # Aplikasi Streamlit
    st.title('Tren IPM Kabupaten/Kota di Jawa Barat 2010-2023')

    # Memilih kabupaten/kota untuk ditampilkan
    selected_kabupaten_kota = st.multiselect('Pilih Kabupaten/Kota:', options=data['nama_kabupaten_kota'].unique())

    # Menyiapkan data untuk plotting
    filtered_data = data[data['nama_kabupaten_kota'].isin(selected_kabupaten_kota)]

    # Membuat plot jika ada kabupaten/kota yang dipilih
    if not filtered_data.empty:
        plt.figure(figsize=(10, 4))
        for _, row in filtered_data.iterrows():
            plt.plot(row.index[1:], row.values[1:], marker='o', label=row['nama_kabupaten_kota'])
        
        plt.title('Tren IPM dari Tahun ke Tahun')
        plt.xlabel('Tahun')
        plt.ylabel('IPM')
        plt.xticks(rotation=30)
        plt.legend()
        plt.grid(True)
        
        st.pyplot(plt)
    else:
        st.write("Silakan pilih satu atau lebih kabupaten/kota untuk menampilkan tren IPM.")

    st.write('Grafik diatas berisi Lineplot Tren Kabupaten Kota di Jawa Barat 2010-2023.')
     
    st.markdown('### Indeks Pembangunan Manusia Jawa Barat berdasarkan Kabupaten dan Kota Tahun 2013-2023')
    #Buat Pivot Table Jabar
    df_jabar = pd.read_csv("pivot_table_jabar.csv")
    # Sidebar Content
    tahun = st.selectbox(
        "Tahun",
        ("2023","2022","2021","2020","2019","2018","2017","2016","2015","2014","2013")
    )
    #2023
    if tahun == "2023":
        # # AWAL Membuat TREEMAP
        nama_kab_kota = df_jabar['nama_kabupaten_kota']
        data_2023 = df_jabar['2023']
        data_2023, nama_kab_kota = zip(*sorted(zip(data_2023, nama_kab_kota), reverse=False))
        result = list(map(lambda x: (x[0], x[1]), zip(nama_kab_kota, data_2023)))
        # Membuat warna acak untuk setiap label
        color_map = {}
        for kab_kota in nama_kab_kota:
            color_map[kab_kota] = f"#{random.randint(0, 0xFFFFFF):06x}"

        # Membuat treemap
        plt.figure(figsize=(8, 6))
        squarify.plot(sizes=data_2023, label=result,color=[color_map[kab_kota] for kab_kota in nama_kab_kota], alpha=0.7,  text_kwargs={'fontsize':3})
        # Menambahkan label
        plt.title("Indeks Pembangunan Manusia per Tahun 2023", fontsize = 8)
        plt.axis('off')
        # Menampilkan plot
        st.pyplot(plt)
    
    
    #2022
    elif tahun == "2022":
        # # AWAL Membuat TREEMAP
        nama_kab_kota = df_jabar['nama_kabupaten_kota']
        data_2022 = df_jabar['2022']
        data_2022, nama_kab_kota = zip(*sorted(zip(data_2022, nama_kab_kota), reverse=False))
        result = list(map(lambda x: (x[0], x[1]), zip(nama_kab_kota, data_2022)))
        # Membuat warna acak untuk setiap label
        color_map = {}
        for kab_kota in nama_kab_kota:
            color_map[kab_kota] = f"#{random.randint(0, 0xFFFFFF):06x}"

        # Membuat treemap
        plt.figure(figsize=(8, 6))
        squarify.plot(sizes=data_2022, label=result,color=[color_map[kab_kota] for kab_kota in nama_kab_kota], alpha=0.7,  text_kwargs={'fontsize':3})
        # Menambahkan label
        plt.title("Indeks Pembangunan Manusia per Tahun 2022", fontsize = 8)
        plt.axis('off')
        # Menampilkan plot
        st.pyplot(plt)    
    
    #2021
    elif tahun == "2021":
        # # AWAL Membuat TREEMAP
        nama_kab_kota = df_jabar['nama_kabupaten_kota']
        data_2021 = df_jabar['2021']
        data_2021, nama_kab_kota = zip(*sorted(zip(data_2021, nama_kab_kota), reverse=False))
        result = list(map(lambda x: (x[0], x[1]), zip(nama_kab_kota, data_2021)))
        # Membuat warna acak untuk setiap label
        color_map = {}
        for kab_kota in nama_kab_kota:
            color_map[kab_kota] = f"#{random.randint(0, 0xFFFFFF):06x}"

        # Membuat treemap
        plt.figure(figsize=(8, 6))
        squarify.plot(sizes=data_2021, label=result,color=[color_map[kab_kota] for kab_kota in nama_kab_kota], alpha=0.7,  text_kwargs={'fontsize':3})
        # Menambahkan label
        plt.title("Indeks Pembangunan Manusia per Tahun 2021", fontsize = 8)
        plt.axis('off')
        # Menampilkan plot
        st.pyplot(plt)    
        
    #2020
    elif tahun == "2020":
        # # AWAL Membuat TREEMAP
        nama_kab_kota = df_jabar['nama_kabupaten_kota']
        data_2020 = df_jabar['2020']
        data_2020, nama_kab_kota = zip(*sorted(zip(data_2020, nama_kab_kota), reverse=False))
        result = list(map(lambda x: (x[0], x[1]), zip(nama_kab_kota, data_2020)))
        # Membuat warna acak untuk setiap label
        color_map = {}
        for kab_kota in nama_kab_kota:
            color_map[kab_kota] = f"#{random.randint(0, 0xFFFFFF):06x}"

        # Membuat treemap
        plt.figure(figsize=(8, 6))
        squarify.plot(sizes=data_2020, label=result,color=[color_map[kab_kota] for kab_kota in nama_kab_kota], alpha=0.7,  text_kwargs={'fontsize':3})
        # Menambahkan label
        plt.title("Indeks Pembangunan Manusia per Tahun 2020", fontsize = 8)
        plt.axis('off')
        # Menampilkan plot
        st.pyplot(plt) 
        
    #2019
    elif tahun == "2019":
        # # AWAL Membuat TREEMAP
        nama_kab_kota = df_jabar['nama_kabupaten_kota']
        data_2019 = df_jabar['2019']
        data_2019, nama_kab_kota = zip(*sorted(zip(data_2019, nama_kab_kota), reverse=False))
        result = list(map(lambda x: (x[0], x[1]), zip(nama_kab_kota, data_2019)))
        # Membuat warna acak untuk setiap label
        color_map = {}
        for kab_kota in nama_kab_kota:
            color_map[kab_kota] = f"#{random.randint(0, 0xFFFFFF):06x}"

        # Membuat treemap
        plt.figure(figsize=(8, 6))
        squarify.plot(sizes=data_2019, label=result,color=[color_map[kab_kota] for kab_kota in nama_kab_kota], alpha=0.7,  text_kwargs={'fontsize':3})
        # Menambahkan label
        plt.title("Indeks Pembangunan Manusia per Tahun 2019", fontsize = 8)
        plt.axis('off')
        # Menampilkan plot
        st.pyplot(plt)
        
    #2018
    elif tahun == "2018":
        # # AWAL Membuat TREEMAP
        nama_kab_kota = df_jabar['nama_kabupaten_kota']
        data_2018 = df_jabar['2018']
        data_2018 , nama_kab_kota = zip(*sorted(zip(data_2018, nama_kab_kota), reverse=False))
        result = list(map(lambda x: (x[0], x[1]), zip(nama_kab_kota, data_2018)))
        # Membuat warna acak untuk setiap label
        color_map = {}
        for kab_kota in nama_kab_kota:
            color_map[kab_kota] = f"#{random.randint(0, 0xFFFFFF):06x}"

        # Membuat treemap
        plt.figure(figsize=(8, 6))
        squarify.plot(sizes=data_2018, label=result,color=[color_map[kab_kota] for kab_kota in nama_kab_kota], alpha=0.7,  text_kwargs={'fontsize':3})
        # Menambahkan label
        plt.title("Indeks Pembangunan Manusia per Tahun 2018", fontsize = 8)
        plt.axis('off')
        # Menampilkan plot
        st.pyplot(plt)     
    
    #2017
    elif tahun == "2017":
        # # AWAL Membuat TREEMAP
        nama_kab_kota = df_jabar['nama_kabupaten_kota']
        data_2017 = df_jabar['2017']
        data_2017 , nama_kab_kota = zip(*sorted(zip(data_2017, nama_kab_kota), reverse=False))
        result = list(map(lambda x: (x[0], x[1]), zip(nama_kab_kota, data_2017)))
        # Membuat warna acak untuk setiap label
        color_map = {}
        for kab_kota in nama_kab_kota:
            color_map[kab_kota] = f"#{random.randint(0, 0xFFFFFF):06x}"

        # Membuat treemap
        plt.figure(figsize=(8, 6))
        squarify.plot(sizes=data_2017, label=result,color=[color_map[kab_kota] for kab_kota in nama_kab_kota], alpha=0.7,  text_kwargs={'fontsize':3})
        # Menambahkan label
        plt.title("Indeks Pembangunan Manusia per Tahun 2017", fontsize = 8)
        plt.axis('off')
        # Menampilkan plot
        st.pyplot(plt)     
    
    #2016
    elif tahun == "2016":
        # # AWAL Membuat TREEMAP
        nama_kab_kota = df_jabar['nama_kabupaten_kota']
        data_2016 = df_jabar['2016']
        data_2016 , nama_kab_kota = zip(*sorted(zip(data_2016, nama_kab_kota), reverse=False))
        result = list(map(lambda x: (x[0], x[1]), zip(nama_kab_kota, data_2016)))
        # Membuat warna acak untuk setiap label
        color_map = {}
        for kab_kota in nama_kab_kota:
            color_map[kab_kota] = f"#{random.randint(0, 0xFFFFFF):06x}"

        # Membuat treemap
        plt.figure(figsize=(8, 6))
        squarify.plot(sizes=data_2016, label=result,color=[color_map[kab_kota] for kab_kota in nama_kab_kota], alpha=0.7,  text_kwargs={'fontsize':3})
        # Menambahkan label
        plt.title("Indeks Pembangunan Manusia per Tahun 2016", fontsize = 8)
        plt.axis('off')
        # Menampilkan plot
        st.pyplot(plt)     
    
    #2015
    elif tahun == "2015":
        # # AWAL Membuat TREEMAP
        nama_kab_kota = df_jabar['nama_kabupaten_kota']
        data_2015 = df_jabar['2015']
        data_2015 , nama_kab_kota = zip(*sorted(zip(data_2015, nama_kab_kota), reverse=False))
        result = list(map(lambda x: (x[0], x[1]), zip(nama_kab_kota, data_2015)))
        # Membuat warna acak untuk setiap label
        color_map = {}
        for kab_kota in nama_kab_kota:
            color_map[kab_kota] = f"#{random.randint(0, 0xFFFFFF):06x}"

        # Membuat treemap
        plt.figure(figsize=(8, 6))
        squarify.plot(sizes=data_2015, label=result,color=[color_map[kab_kota] for kab_kota in nama_kab_kota], alpha=0.7,  text_kwargs={'fontsize':3})
        # Menambahkan label
        plt.title("Indeks Pembangunan Manusia per Tahun 2015", fontsize = 8)
        plt.axis('off')
        # Menampilkan plot
        st.pyplot(plt)     
    
    #2014
    elif tahun == "2014":
        # # AWAL Membuat TREEMAP
        nama_kab_kota = df_jabar['nama_kabupaten_kota']
        data_2014 = df_jabar['2014']
        data_2014 , nama_kab_kota = zip(*sorted(zip(data_2014, nama_kab_kota), reverse=False))
        result = list(map(lambda x: (x[0], x[1]), zip(nama_kab_kota, data_2014)))
        # Membuat warna acak untuk setiap label
        color_map = {}
        for kab_kota in nama_kab_kota:
            color_map[kab_kota] = f"#{random.randint(0, 0xFFFFFF):06x}"

        # Membuat treemap
        plt.figure(figsize=(8, 6))
        squarify.plot(sizes=data_2014, label=result,color=[color_map[kab_kota] for kab_kota in nama_kab_kota], alpha=0.7,  text_kwargs={'fontsize':3})
        # Menambahkan label
        plt.title("Indeks Pembangunan Manusia per Tahun 2014", fontsize = 8)
        plt.axis('off')
        # Menampilkan plot
        st.pyplot(plt)     
    
    #2013
    elif tahun == "2013":
        # # AWAL Membuat TREEMAP
        nama_kab_kota = df_jabar['nama_kabupaten_kota']
        data_2013 = df_jabar['2013']
        data_2013 , nama_kab_kota = zip(*sorted(zip(data_2013, nama_kab_kota), reverse=False))
        result = list(map(lambda x: (x[0], x[1]), zip(nama_kab_kota, data_2013)))
        # Membuat warna acak untuk setiap label
        color_map = {}
        for kab_kota in nama_kab_kota:
            color_map[kab_kota] = f"#{random.randint(0, 0xFFFFFF):06x}"

        # Membuat treemap
        plt.figure(figsize=(8, 6))
        squarify.plot(sizes=data_2013, label=result,color=[color_map[kab_kota] for kab_kota in nama_kab_kota], alpha=0.7,  text_kwargs={'fontsize':3})
        # Menambahkan label
        plt.title("Indeks Pembangunan Manusia per Tahun 2013", fontsize = 8)
        plt.axis('off')
        # Menampilkan plot
        st.pyplot(plt) 
        
        
    st.write("Grafik diatas menggunakan Treemap dimana menyajikan poin Indeks Pembangunan Manusia Jawa Barat Tahun 2013-2023. Dikarenakan Kabupaten Pangandara baru berdiri di Tahun 2012 jadi data nya tidak ada dan penulis memulai dari tahun 2013 agar semua Kabupaten dan Kota tersedia data nya")
    
    with Kesimpulan:
        
        st.header('Kesimpulan IPM Jawa Barat 2010-2023')
        st.write('Secara Nasional, IPM Jawa Barat mengalami peningkatan yang signifikan dari tahun 2010 ke 2023. Menurut Sumber Badan Pusat Statistik (BPS), pada tahun 2010, IPM Jawa Barat adalah 66,15, dan pada tahun 2023 mencapai 73,12. Hal ini menunjukkan bahwa pembangunan manusia di Jawa Barat telah berjalan dengan baik. Meskipun IPM Jawa Barat meningkat, masih terdapat ketimpangan antar wilayah. Kota-kota besar seperti Bandung, Bekasi, dan Depok memiliki IPM yang lebih tinggi dibandingkan dengan Kota Kabupaten lain di Jawa Barat. Terutama di wilayah Jawa Barat bagian Selatan yang mana mayoritas memiliki IPM yang relatif rendah dibandingkan Kota Kabuapten yang lain di Jawa Barat. Semoga Pemerintah Provinsi Jawa Barat umumnya dan Pemerintah Daerah setempat khusunya Jawa Barat bagian Selatan bisa lebih memperhatikan wilayah Kota Kabupaten nya, agar bisa menyamai Kota dan Kabupaten lain di Jawa Barat. Sehingga harapannya ke depan Provinsi Jawa Barat bisa menjadi Provinsi dengan IPM Tertinggi di Indonesia')
        st.image("ipm_jabar_2010_2012.png", caption="Indeks Pembangunan Manusia menurut Provinsi, 2010-2012", use_column_width=True)
        st.image("ipm_jabar_2022_2023.png", caption="Indeks Pembangunan Manusia menurut Provinsi, 2022-2023", use_column_width=True)
       
       
