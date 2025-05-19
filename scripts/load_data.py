import pandas as pd                              # import library pandas untuk manipulasi data
from sqlalchemy import create_engine             # import create_engine dari SQLAlchemy untuk koneksi database

# URL raw file CSV di GitHub
url = "https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv" 

# Baca langsung file CSV ke DataFrame
df = pd.read_csv(url, sep=';')   

# Hapus baris dengan nilai null pada kolom 'Status'
df = df.dropna(subset=['Status']).reset_index(drop=True)  

# Buat koneksi ke database PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:@localhost:5432/postgres') # sesuaikan user, password, host, port, dan nama database

# Muat DataFrame ke tabel 'student' di database
df.to_sql(
    'student',                                 # nama tabel target
    engine,                                      # engine/koneksi database
    if_exists='replace',                         # ganti tabel jika sudah ada
    index=False                                  # tidak menyertakan kolom indeks pandas sebagai kolom di SQL
)

print("✅ Data loaded to Postgres successfully") # konfirmasi keberhasilan proses ETL
