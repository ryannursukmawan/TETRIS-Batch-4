from lib2to3.pgen2.token import PERCENT
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
import altair as alt

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
Analisa, Pendahuluan = st.tabs(["Analisa", "Pendahuluan"])

# Tampilkan konten di tab
with Analisa:
    st.write('Penulis: Ryan Nursukmawan')
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
        plt.title('Indeks Pembangunan Manusia Terbaik Jawa Barat 2010-2023')
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
        plt.title('Indeks Pembangunan Manusia Terburuk di Jawa Barat 2010-2023')
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
        plt.title('Indeks Pembangunan Manusia Terbaik Jawa Barat 2010-2023')
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
        plt.title('Indeks Pembangunan Manusia Terburuk di Jawa Barat 2010-2023')
        # Menambahkan label pada sumbu x dan y
        plt.xlabel('Nama Kota Kabupaten')
        plt.ylabel('Indeks Pembangunan Manusia')
        
        col1, col2 = st.columns(2)
        with col1:
            st.pyplot(fig_31)
        with col2 :
            st.pyplot(fig_41)    

    st.write("Berdasarkan data, Kota Bandung menduduki puncak dengan IPM tertinggi di Jawa Barat, yaitu 80,23. Diikuti oleh Kota Bekasi 80,23 dan Kota Depok 79,57. Ketiga kota ini menunjukkan pencapaian yang baik dalam pembangunan manusia. Secara keseluruhan, IPM di Jawa Barat menunjukkan tren positif. Mayoritas kota mengalami peningkatan nilai IPM dibandingkan tahun sebelumnya. Hal ini mencerminkan upaya pemerintah dalam meningkatkan kualitas hidup masyarakat di seluruh wilayah. Meskipun menunjukkan kemajuan, disparitas antar kota masih terlihat. Kabupaten Pangandaran masih tertinggal dengan nilai IPM 52,74. Hal ini menunjukkan perlunya fokus dan perhatian lebih untuk mendorong pembangunan di daerah tertinggal. memotret deretan daerah dengan Indeks Pembangunan Manusia (IPM) terendah. Data ini menjadi cerminan bagi upaya pembangunan yang perlu diintensifkan untuk mencapai kesejahteraan yang merata.")

    st.markdown('### Menelusuri Jejak IPM di Kota Depok')

    df_depok = pd.read_csv('lineplot_depok.csv')
    # Buat plot dengan Matplotlib
    plt.figure(figsize=(8, 5))
    plt.plot(df_depok['indeks_pembangunan_manusia'], df_depok['tahun'])
    plt.xlabel('Indeks Pembangunan Manusia')
    plt.ylabel('Tahun')
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

    st.write('karena p-value < 0,05 sebagai tingkat kepercayaan, maka kami menolak H Kesimpulan : setidaknya ada satu kelompok yang memiliki perbedaan angka IPM yang signifikan Kemungkinan penyebabnya : terdapat perbedaan faktor yang mempengaruhi IPM di setiap kota atau kabupaten di Jawa Barat')
    st.write('Insight : Berdasarkan Boxplot dibawah, bisa di terjemahkan ada perbedaan yang signifikan antara Kabupaten/Kota yang satu dan yang lainnya di wilayah Bodebek.')
    st.write('Possible Cause : Kemungkinan adanya penyebab perbedaan siginifikan Indeks Pembangunan Manusia di Bodebek perlu kita lakukan lebih lanjut mengenai faktor penyebabnya. Kita bisa mengira faktor tersebut antara lain: Korelasi Pendiidikan, Kepadatan Penduduk, Ekonomi, Kesenjangan Sosial.')
    
    st.markdown('### Faktor yang mempengaruhi Indeks Pembangunan Manusia')
    st.write('Berdasarkan Sumber Jurnal yang penulis dapatkan ada beberapa faktor yang mempengaruhi besar kecil nya Indeks Pembangunan Manusia di suatu daerah yaitu Pendidikan[[1]]( https://journal.ipb.ac.id/index.php/jekp/article/viewFile/19949/13741), Kesehatan[[2]]( https://ejurnalunsam.id/index.php/jse/article/view/2303), Ekonomi[[3]]( https://repository.ipb.ac.id/handle/123456789/88680), Pemerataan Pembangunan[[4]]( https://jimfeb.ub.ac.id/index.php/jimfeb/article/download/5339/4697)')

    st.markdown('### Apa yang bisa di tingkatkatkan untuk indeks pembangunan manusia di Bodebek maupun Jawa Barat?')
    st.write(' **Membangun Fondasi yang Kuat:**' )
    st.write('Berdasarkan data Indeks Pembangunan Manusia (IPM) di Bodebek (Kota/Kabupaten Bogor, Depok, Kota/KabupatenBekasi) dan Jawa Barat, terdapat beberapa aspek yang perlu ditingkatkan untuk mencapai kemajuan yang signifikan:')
    st.write('1. Pendidikan:')
    st.write ('-Meningkatkan akses pendidikan berkualitas di semua tingkatan, termasuk pendidikan anak usia dini.')
    st.write ('-Memperkuat program pelatihan dan pemagangan untuk meningkatkan keterampilan tenaga kerja.')
    st.write ('-Menyediakan beasiswa bagi siswa berprestasi dan kurang mampu.')
    st.write('2. Kesehatan')
    st.write('-Meningkatkan akses dan kualitas layanan kesehatan, termasuk di daerah pedesaan.')
    st.write('-Memperkuat program promotif dan preventif untuk menjaga kesehatan masyarakat.')
    st.write ('-Meningkatkan jumlah tenaga kesehatan dan fasilitas kesehatan.')
    st.write ('3. Ekonomi')
    st.write ('-Menciptakan lapangan kerja yang berkualitas dan berdaya saing.')
    st.write ('-Meningkatkan pendapatan masyarakat melalui program pemberdayaan ekonomi.')
    st.write('-Memperkuat infrastruktur ekonomi, seperti jalan, jembatan, dan pelabuhan.')
    st.write('4. Pemerataan pembangunan')
    st.write ('-Mengurangi kesenjangan pembangunan antar wilayah, terutama antara daerah urban dan rural.')
    st.write('-Memberikan perhatian khusus pada daerah tertinggal dalam hal pendidikan, kesehatan, dan ekonomi.')
    st.write('-Meningkatkan koordinasi dan sinergi antar pemangku kepentingan dalam pembangunan daerah.')
    st.write('**Langkah Strategis**')
    st.write('-Pemerintah: Merumuskan kebijakan dan program yang fokus pada peningkatan IPM, dengan memperhatikan kesenjangan antar wilayah.')
    st.write('-Masyarakat: Berpartisipasi aktif dalam program pembangunan dan meningkatkan kualitas hidup.')
    st.write('-Swasta: Bekerjasama dengan pemerintah dan masyarakat dalam program pembangunan, seperti melalui CSR dan program pemberdayaan masyarakat.')
    st.write('Dengan meningkatkan upaya di bidang-bidang tersebut, diharapkan IPM di Bodebek dan Jawa Barat dapat terus meningkat dan mencapai tingkat yang optimal. Hal ini akan mewujudkan masyarakat yang lebih sejahtera, adil, dan berdaya saing.')

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
