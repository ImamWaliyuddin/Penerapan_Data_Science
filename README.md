# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
- Nama Institusi: Jaya Jaya Institut (Fiktif) 
- Tahun Berdiri: 2000 
- Reputasi: Telah mencetak banyak lulusan dengan reputasi yang sangat baik. 
- Kondisi Saat Ini: Meskipun memiliki reputasi baik, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.  Jumlah dropout yang tinggi menjadi salah satu masalah besar bagi institusi. 
- Tujuan Proyek dari Sisi Institusi: Jaya Jaya Institut ingin mendeteksi sedini mungkin siswa yang berpotensi dropout sehingga dapat diberi bimbingan khusus.  Selain itu, mereka meminta Anda membuat dashboard agar mudah dalam memahami data dan memonitor performa siswa. 

### Permasalahan Bisnis
Berdasarkan latar belakang, permasalahan bisnis utama yang akan diselesaikan adalah:
1. Tingginya Angka Mahasiswa Dropout: Mengidentifikasi faktor-faktor utama yang menyebabkan mahasiswa di Jaya Jaya Institut mengalami dropout.
2. Kesulitan Deteksi Dini Mahasiswa Berisiko: Institusi memerlukan sistem untuk mendeteksi secara dini mahasiswa yang memiliki potensi dropout agar dapat diberikan intervensi yang tepat.
3. Pemantauan Performa Mahasiswa yang Kurang Efektif: Kebutuhan akan alat bantu visual (dashboard) untuk mempermudah pemantauan dan pemahaman terhadap data performa mahasiswa secara keseluruhan.

### Cakupan Proyek
Untuk menyelesaikan permasalahan bisnis di atas, cakupan proyek ini meliputi:
1. Analisis Data Eksploratif (EDA): Memahami karakteristik data mahasiswa, mengidentifikasi pola, dan menemukan insight awal terkait faktor-faktor yang mungkin berpengaruh terhadap status kelulusan mahasiswa.
2. Persiapan Data: Melakukan pembersihan data, transformasi, dan feature engineering yang diperlukan untuk mempersiapkan data sebelum proses pemodelan.
3. Pengembangan Model Machine Learning: Membangun model klasifikasi untuk memprediksi status mahasiswa (Dropout, Graduate, Enrolled) berdasarkan data historis.
4. Evaluasi Model: Mengevaluasi performa model yang telah dibangun menggunakan metrik yang sesuai untuk memastikan keandalan prediksi.
5. Pembuatan Dashboard Bisnis: Mengembangkan dashboard interaktif (menggunakan Metabase atau alternatif lain) untuk visualisasi data performa mahasiswa dan tren dropout.
6. Deployment Model (Prototipe): Membuat prototipe sistem machine learning yang dapat diakses secara remote (menggunakan Streamlit Cloud) untuk memprediksi status mahasiswa.
7. Penyusunan Rekomendasi: Memberikan rekomendasi tindak lanjut (action items) kepada Jaya Jaya Institut berdasarkan temuan analisis dan hasil model.

### Persiapan

Data yang digunakan dalam proyek ini berasal dari dataset **Student Performance** yang tersedia secara publik di:  
[https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv)

Dataset ini berisi informasi tentang performa mahasiswa, termasuk fitur demografi, akademik, dan status kelulusan (Dropout, Graduate, Enrolled), yang akan digunakan untuk analisis dan pembuatan model prediksi.

1. Setup environment:
  - Buka terminal.
  - Buat Environment virtual: `python -m venv venv`
  - Aktifkan:
    - Windows: `venv\Scripts\activate`
    - Mac/Linux: `source venv/bin/activate`
  - Instal dependensi: `pip install -r requirements.txt`
  - Load Data: `python scripts/load_data.py`

## Business Dashboard
Business Dashboard yang ditampilkan pada gambar terakhir dirancang untuk memberikan Jaya Jaya Institut alat yang komprehensif dan interaktif untuk memantau performa mahasiswa dan tren dropout. Visualisasi utama meliputi:
1. Donut Chart (Kiri Atas): Menunjukkan distribusi status mahasiswa. Dari total 4.424 mahasiswa, 49% (2.169) lulus, 32% (1.418) dropout, dan 17% (837) masih terdaftar. Ini memberikan gambaran cepat tentang hasil pendidikan mahasiswa.
2. Bar Chart (Kanan Atas): Membandingkan jumlah penerima beasiswa dan non-beasiswa berdasarkan status. Ada 1.787 penerima beasiswa (835 lulus, 1.574 dropout) dan 2.637 non-beasiswa (1.334 lulus, 1.787 dropout). Ini menunjukkan non-beasiswa memiliki jumlah dropout lebih tinggi, menandakan dukungan finansial berpengaruh pada retensi.
3. Horizontal Bar Chart (Kiri Tengah): Menampilkan jumlah dropout per program studi. Manajemen (Kelas Malam) memiliki jumlah dropout tertinggi dengan 136, diikuti Keperawatan dengan 118, sementara Teknologi Produksi Biofuel terendah dengan 8. Ini membantu mengidentifikasi program berisiko tinggi untuk intervensi.
4. Bar Chart (Kanan Tengah): Membandingkan nilai rata-rata mahasiswa berdasarkan status dan status pembayaran kuliah (lunas vs. belum lunas). Lulusan memiliki nilai rata-rata tertinggi (128.79), diikuti Terdaftar (125.53) dan Dropout (124.96). Ini menunjukkan performa akademik sebagai faktor potensial dalam risiko dropout.
5. Grouped Bar Chart (Kanan Tengah): Memecah status pembayaran berdasarkan status kelulusan. Dari yang lunas, 2.209 lulus, 794 terdaftar, dan 1.421 dropout. Dari yang belum lunas, 209 lulus, 794 terdaftar, dan 1.421 dropout. Ini menunjukkan korelasi antara tunggakan biaya dengan tingkat dropout.
6. Histogram (Kiri Bawah): Menggambarkan persentase dropout per program studi. Equiculture memiliki persentase dropout tertinggi, sementara Teknologi Produksi Biofuel terendah, sesuai dengan data jumlah dropout sebelumnya.
7. Line Graph (Kanan Bawah): Menunjukkan tren usia pendaftaran mahasiswa untuk Lulusan dan Dropout. Keduanya puncak pada usia muda (sekitar 20), tetapi Dropout menurun lebih tajam, menunjukkan mahasiswa muda lebih rentan dropout.
Dashboard ini memungkinkan Jaya Jaya Institut dengan cepat mengenali tren, seperti tingkat dropout tinggi di program tertentu, dampak faktor finansial, dan pengaruh usia serta performa akademik terhadap hasil mahasiswa.

**Akses**:
- URL: `http://localhost:3000`
- Login: `root@mail.com / root123`
- Screenshot: `imamwaliyuddin-dashboard.png`
- Video Singkat Penjelasan Dashboard: `imamwaliyuddin-video.mp4`

## Menjalankan Sistem Machine Learning
Prototipe ini dikembangkan menggunakan Streamlit dan di-deploy melalui Streamlit Cloud. Berikut langkah-langkahnya:

### Langkah 1: Persiapkan Environment (Jika Menjalankan Secara Lokal)
1. **Pastikan Python Terinstal**: Unduh Python (versi 3.7+) dari [python.org](https://www.python.org/downloads/).
2. **Instal Dependensi**:
   - Buka terminal.
   - Buat Environment virtual: `python -m venv venv`
   - Aktifkan:
     - Windows: `venv\Scripts\activate`
     - Mac/Linux: `source venv/bin/activate`
   - Instal dependensi: `pip install -r requirements.txt`
3. **Unduh File Proyek**: Pastikan `app.py` dan `student_status_predictor.joblib` ada di direktori yang sama.
4. **Jalankan Aplikasi**: Di terminal, ketik: `streamlit run app.py` Aplikasi akan terbuka di browser (`http://localhost:8501`).

### Langkah 2: Akses Prototipe yang Sudah Di-Deploy
1. **Kunjungi Link Prototipe**:  
[https://jaya-jaya-institut-predictor.streamlit.app/](https://jaya-jaya-institut-predictor.streamlit.app/)
2. **Masukkan Data Mahasiswa**: Di sidebar, masukkan data seperti status pernikahan, jenis kelamin, usia pendaftaran, status beasiswa, dll.
3. **Lakukan Prediksi**: Klik "Prediksi Status Mahasiswa" untuk melihat hasil dan probabilitas.
4. **Tindak Lanjuti Hasil**: Jika diprediksi "Dropout", berikan dukungan tambahan.

## Link untuk Mengakses Prototipe

Prototipe dapat diakses melalui:  
[https://jaya-jaya-institut-predictor.streamlit.app/](https://jaya-jaya-institut-predictor.streamlit.app/)

## Conclusion
Proyek ini berhasil mengatasi tantangan Jaya Jaya Institut terkait tingginya angka dropout melalui pendekatan berlapis:
1. Analisis Data Eksploratif (EDA): EDA mengungkapkan wawasan penting, seperti korelasi antara tunggakan biaya kuliah, performa akademik rendah, dan tingkat dropout tinggi. Program seperti Manajemen (Kelas Malam) dan Keperawatan menunjukkan jumlah dropout lebih banyak, sementara mahasiswa muda dan non-beasiswa lebih berisiko.
2. Model Machine Learning: Model Logistic Regression dikembangkan dengan F1-score 0.7442, menunjukkan performa baik dalam memprediksi status mahasiswa (Dropout, Lulus, Terdaftar). Model ini efektif mengidentifikasi mahasiswa berisiko berdasarkan fitur demografi, akademik, dan finansial.
3. Pengembangan Dashboard: Dashboard interaktif menyediakan visualisasi data yang jelas, memungkinkan institusi memantau performa dan tren dropout dari berbagai dimensi seperti program studi, status finansial, dan usia.
4. Penyebaran Prototipe: Aplikasi Streamlit memungkinkan prediksi status mahasiswa secara real-time, membantu institusi mengidentifikasi mahasiswa berisiko dropout secara proaktif.
Secara keseluruhan, proyek ini memberikan Jaya Jaya Institut alat yang dapat ditindaklanjuti untuk mengurangi angka dropout dan meningkatkan hasil mahasiswa.

### Rekomendasi Action Items
Berdasarkan temuan, berikut adalah rekomendasi tindakan untuk Jaya Jaya Institut:
1. Intervensi Terarah untuk Program Berisiko Tinggi: Fokus pada program dengan tingkat dropout tinggi seperti Manajemen (Kelas Malam) dan Keperawatan. Laksanakan program mentor, dukungan akademik tambahan, atau jadwal fleksibel untuk mahasiswa kelas malam.
2. Inisiatif Dukungan Finansial: Karena non-beasiswa dan mahasiswa dengan tunggakan biaya kuliah memiliki tingkat dropout lebih tinggi, perluas program beasiswa dan tawarkan rencana pembayaran untuk mengurangi beban finansial.
3. Sistem Peringatan Dini: Gunakan model machine learning untuk mendeteksi mahasiswa berisiko sejak dini. Siapkan peringatan otomatis untuk mahasiswa yang diprediksi "Dropout" dan tugaskan konselor untuk memberikan dukungan personal.
4. Dukungan Akademik untuk Mahasiswa Muda: Mahasiswa muda (sekitar usia 20) menunjukkan kecenderungan dropout lebih tinggi. Buat program orientasi, kelompok dukungan sejawat, dan workshop akademik untuk membantu mereka menyesuaikan diri dengan tuntutan pendidikan tinggi.
5. Pemantauan Berkelanjutan via Dashboard: Gunakan dashboard secara rutin untuk melacak tren performa mahasiswa dan tingkat dropout. Latih staf untuk menginterpretasikan visualisasi dan membuat keputusan berbasis data.
6. Peningkatan Model: Terus perbarui model machine learning dengan data mahasiswa baru untuk meningkatkan akurasinya. Eksplorasi fitur tambahan, seperti catatan kehadiran atau keterlibatan ekstrakurikuler, untuk memperkaya prediksi.
