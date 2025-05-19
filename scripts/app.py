import streamlit as st  # import Streamlit untuk membuat antarmuka web interaktif
import pandas as pd     # import pandas untuk manipulasi data
import joblib            # import joblib untuk memuat model yang disimpan
import numpy as np      # import numpy untuk operasi numerik (jika diperlukan)
import os               # import os untuk operasi sistem (path, file)

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Prediksi Status Mahasiswa - Jaya Jaya Institut",  # judul aplikasi di tab browser
    layout="wide"                                              # tata letak halaman (lebar penuh)
)

# Judul dan deskripsi aplikasi
st.title("🤖 Sistem Prediksi Status Mahasiswa")
st.write("""
Aplikasi ini memprediksi status kelulusan mahasiswa (Dropout, Terdaftar, atau Lulus)
berdasarkan data akademik dan demografi. Ini adalah prototipe untuk membantu
Jaya Jaya Institut dalam mengidentifikasi mahasiswa yang berpotensi memerlukan dukungan lebih.
""")

@st.cache_resource  # men-cache resource agar model tidak dimuat ulang berulang kali
def load_model(model_path):
    """
    Memuat pipeline model dari file .joblib.
    Mengembalikan objek pipeline atau None jika gagal.
    """
    try:
        pipeline = joblib.load(model_path)  # muat model pipeline dari path
        return pipeline
    except FileNotFoundError:
        # tampilkan error jika file model tidak ditemukan
        st.error(f"Error: File model '{model_path}' tidak ditemukan. Pastikan file ada di direktori yang benar.")
        return None
    except Exception as e:
        # tampilkan error lain yang terjadi saat memuat model
        st.error(f"Error saat memuat model: {e}")
        return None

# Tentukan path model relatif terhadap direktori kerja
model_path = os.path.join('model', 'student_status_predictor.joblib')
# Panggil fungsi untuk memuat model
pipeline_model = load_model(model_path)

# Sidebar untuk input data mahasiswa
st.sidebar.header("Masukkan Data Mahasiswa:")

def user_input_features():
    """
    Mengumpulkan input pengguna dari sidebar dan mengembalikannya sebagai DataFrame.
    """
    # Pilihan status pernikahan dengan mapping angka ke label
    marital_status_options = {
        1: 'Single', 2: 'Married', 3: 'Widower',
        4: 'Divorced', 5: 'Facto Union', 6: 'Legally Separated'
    }
    marital_status_label = st.sidebar.selectbox(
        'Status Pernikahan', list(marital_status_options.values())
    )
    # cari key berdasarkan label yang dipilih
    marital_status = [key for key, value in marital_status_options.items() if value == marital_status_label][0]

    # Pilihan jenis kelamin
    gender_options = {1: 'Male', 0: 'Female'}
    gender_label = st.sidebar.selectbox('Jenis Kelamin', list(gender_options.values()))
    gender = [key for key, value in gender_options.items() if value == gender_label][0]

    # Slider untuk usia
    age_at_enrollment = st.sidebar.slider('Usia saat Pendaftaran', 17, 70, 20)

    # Pilihan penerima beasiswa
    scholarship_holder_options = {1: 'Ya', 0: 'Tidak'}
    scholarship_holder_label = st.sidebar.selectbox(
        'Penerima Beasiswa?', list(scholarship_holder_options.values())
    )
    scholarship_holder = [key for key, value in scholarship_holder_options.items() if value == scholarship_holder_label][0]

    # Pilihan status hutang
    debtor_options = {1: 'Ya', 0: 'Tidak'}
    debtor_label = st.sidebar.selectbox('Memiliki Hutang?', list(debtor_options.values()))
    debtor = [key for key, value in debtor_options.items() if value == debtor_label][0]

    # Pilihan status pembayaran kuliah
    tuition_fees_up_to_date_options = {1: 'Ya', 0: 'Tidak'}
    tuition_fees_up_to_date_label = st.sidebar.selectbox(
        'Uang Kuliah Lunas?', list(tuition_fees_up_to_date_options.values())
    )
    tuition_fees_up_to_date = [
        key for key, value in tuition_fees_up_to_date_options.items()
        if value == tuition_fees_up_to_date_label
    ][0]

    # Pilihan kualifikasi sebelumnya
    prev_qual_options = {
        1: 'SMA/Sederajat', 2: 'Sarjana (S1/Bachelor)',
        3: 'Gelar (D3/Associate)', 39: 'Kursus Spesialisasi Teknologi'
    }
    prev_qual_label = st.sidebar.selectbox(
        'Kualifikasi Sebelumnya', list(prev_qual_options.values())
    )
    previous_qualification = [
        key for key, value in prev_qual_options.items() if value == prev_qual_label
    ][0]

    # Slider untuk nilai kualifikasi sebelumnya dan nilai penerimaan
    previous_qualification_grade = st.sidebar.slider(
        'Nilai Kualifikasi Sebelumnya', 0.0, 200.0, 120.0, step=0.1
    )
    admission_grade = st.sidebar.slider(
        'Nilai Penerimaan', 0.0, 200.0, 120.0, step=0.1
    )

    # Slider untuk SKS dan nilai semester 1
    curricular_units_1st_sem_approved = st.sidebar.slider(
        'SKS Lulus Semester 1', 0, 26, 5
    )
    curricular_units_1st_sem_grade = st.sidebar.slider(
        'Rata-rata Nilai Semester 1', 0.0, 20.0, 12.0, step=0.01
    )

    # Slider untuk SKS dan nilai semester 2
    curricular_units_2nd_sem_approved = st.sidebar.slider(
        'SKS Lulus Semester 2', 0, 25, 5
    )
    curricular_units_2nd_sem_grade = st.sidebar.slider(
        'Rata-rata Nilai Semester 2', 0.0, 20.0, 12.0, step=0.01
    )

    # Daftar kolom yang diharapkan oleh model
    expected_cols = [
        'Marital_status', 'Application_mode', 'Application_order',
        'Course', 'Daytime_evening_attendance', 'Previous_qualification',
        'Previous_qualification_grade', 'Nacionality', 'Mothers_qualification',
        'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation',
        'Admission_grade', 'Displaced', 'Educational_special_needs', 'Debtor',
        'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder',
        'Age_at_enrollment', 'International',
        'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled',
        'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_approved',
        'Curricular_units_1st_sem_grade',
        'Curricular_units_1st_sem_without_evaluations',
        'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled',
        'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved',
        'Curricular_units_2nd_sem_grade',
        'Curricular_units_2nd_sem_without_evaluations',
        'Unemployment_rate', 'Inflation_rate', 'GDP'
    ]

    # Membangun dict data berdasarkan input pengguna
    data = {
        'Marital_status': marital_status,
        'Application_mode': 1,  # default fixed jika tidak diinput
        'Application_order': 1,
        'Course': 9238,
        'Daytime_evening_attendance': 1,
        'Previous_qualification': previous_qualification,
        'Previous_qualification_grade': previous_qualification_grade,
        'Nacionality': 1,
        'Mothers_qualification': 1,
        'Fathers_qualification': 1,
        'Mothers_occupation': 5,
        'Fathers_occupation': 9,
        'Admission_grade': admission_grade,
        'Displaced': 0,
        'Educational_special_needs': 0,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition_fees_up_to_date,
        'Gender': gender,
        'Scholarship_holder': scholarship_holder,
        'Age_at_enrollment': age_at_enrollment,
        'International': 0,
        'Curricular_units_1st_sem_credited': 0,
        'Curricular_units_1st_sem_enrolled': 6,
        'Curricular_units_1st_sem_evaluations': 8,
        'Curricular_units_1st_sem_approved': curricular_units_1st_sem_approved,
        'Curricular_units_1st_sem_grade': curricular_units_1st_sem_grade,
        'Curricular_units_1st_sem_without_evaluations': 0,
        'Curricular_units_2nd_sem_credited': 0,
        'Curricular_units_2nd_sem_enrolled': 6,
        'Curricular_units_2nd_sem_evaluations': 8,
        'Curricular_units_2nd_sem_approved': curricular_units_2nd_sem_approved,
        'Curricular_units_2nd_sem_grade': curricular_units_2nd_sem_grade,
        'Curricular_units_2nd_sem_without_evaluations': 0,
        'Unemployment_rate': 10.8,
        'Inflation_rate': 1.4,
        'GDP': 1.74
    }

    # Pastikan semua kolom expected terisi, tambahkan default 0 jika tidak ada
    for col in expected_cols:
        if col not in data:
            data[col] = 0

    # Buat DataFrame dan susun kolom sesuai urutan yang diharapkan model
    features = pd.DataFrame(data, index=[0])
    features = features[expected_cols]
    return features

# Ambil input fitur dari fungsi
input_df = user_input_features()

# Tampilkan DataFrame input pengguna
st.subheader('Data Mahasiswa yang Dimasukkan:')
st.dataframe(input_df, hide_index=True, use_container_width=True)

# Tombol untuk menjalankan prediksi
if st.sidebar.button('Prediksi Status Mahasiswa'):
    if pipeline_model is not None:
        try:
            # Prediksi kelas status mahasiswa
            prediction = pipeline_model.predict(input_df)
            # Prediksi probabilitas untuk setiap kelas
            prediction_proba = pipeline_model.predict_proba(input_df)
            # Mapping angka ke label status
            status_labels = {0: 'Dropout', 1: 'Terdaftar (Enrolled)', 2: 'Lulus (Graduate)'}
            predicted_status = status_labels[prediction[0]]

            # Tampilkan hasil prediksi
            st.subheader('Hasil Prediksi:')
            st.success(f"Mahasiswa diprediksi akan: **{predicted_status}**")

            # Tampilkan probabilitas prediksi
            st.subheader('Probabilitas Prediksi:')
            proba_df = pd.DataFrame(
                prediction_proba,
                columns=[status_labels[i] for i in range(len(status_labels))]
            )
            st.dataframe(proba_df, hide_index=True, use_container_width=True)

            # Pesan tambahan berdasarkan hasil
            if predicted_status == 'Dropout':
                st.warning(
                    "Perhatian: Mahasiswa ini memiliki risiko tinggi untuk dropout. Pertimbangkan untuk memberikan dukungan atau intervensi."
                )
            elif predicted_status == 'Terdaftar (Enrolled)':
                st.info(
                    "Mahasiswa ini diprediksi masih akan terdaftar. Pantau terus perkembangannya."
                )
            else:
                # Animasi jika lulus
                st.balloons()
                st.success(
                    "Selamat! Mahasiswa ini diprediksi akan Lulus."
                )
        except Exception as e:
            # Tangani error prediksi
            st.error(f"Terjadi error saat melakukan prediksi: {e}")
            st.error("Pastikan semua input fitur sudah benar dan model telah dimuat dengan sukses.")
    else:
        # Jika model gagal dimuat
        st.error("Model tidak dapat dimuat. Prediksi tidak dapat dilakukan.")
else:
    # Instruksi awal jika tombol belum ditekan
    st.info("Masukkan data mahasiswa di sidebar dan klik tombol 'Prediksi Status Mahasiswa'.")

# Garis pemisah dan disclaimer
st.markdown("---")
st.markdown("""
**Disclaimer:** Ini adalah sistem prototipe dan hasil prediksi bersifat indikatif.
Keputusan akhir tetap harus mempertimbangkan berbagai faktor lain dan penilaian profesional.
""")