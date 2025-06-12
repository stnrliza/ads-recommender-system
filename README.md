# 1. Project Overview

Perkembangan pesat dalam teknologi pembelajaran mesin telah membuka peluang besar dalam bidang sistem rekomendasi, khususnya menggunakan metode content-based filtering dan collaborative filtering. Metode-metode ini terbukti efektif dalam menganalisis data dalam jumlah besar dengan tingkat akurasi yang tinggi, sehingga mampu memahami preferensi dan perilaku pengguna secara mendalam. Studi oleh Konapure dan Lobo (2021) menunjukkan bahwa pendekatan content-based filtering dapat meningkatkan relevansi rekomendasi iklan berdasarkan karakteristik konten yang diminati pengguna. Sementara itu, Ekstrand, Riedl, dan Konstan (2011) menegaskan keunggulan collaborative filtering dalam mengidentifikasi pola kesamaan antar pengguna untuk menyajikan rekomendasi yang lebih personal.

Proyek ini penting untuk diselesaikan karena sistem rekomendasi iklan yang efektif memberikan manfaat ganda, baik bagi pengguna maupun pelaku bisnis. Dari sisi pengguna, rekomendasi yang tepat membantu mereka menemukan informasi atau produk yang sesuai tanpa harus mencari secara manual, sehingga meningkatkan pengalaman yang lebih personal dan efisien. Bagi bisnis, sistem ini dapat meningkatkan tingkat konversi dan keterlibatan pengguna, mengoptimalkan strategi pemasaran, dan pada akhirnya meningkatkan pendapatan. Di era digital saat ini, di mana volume informasi sangat besar, sistem rekomendasi berperan penting dalam mengatasi masalah kelebihan informasi (information overload) dan memastikan iklan yang disajikan tepat sasaran. Dengan mengintegrasikan metode content-based dan collaborative filtering, proyek ini bertujuan untuk memanfaatkan data secara cerdas demi menghadirkan solusi rekomendasi yang optimal dan berdampak signifikan.

### **Referensi**:

[1] Konapure, R. C., & Lobo, L. M. R. J. (2021). Video content-based advertisement recommendation system using classification technique of machine learning. *Journal of Physics: Conference Series, 1854*(1), 012025. [https://doi.org/10.1088/1742-6596/1854/1/012025](https://doi.org/10.1088/1742-6596/1854/1/012025)

[2] Ekstrand, M. D., Riedl, J. T., & Konstan, J. A. (2011). Collaborative filtering recommender systems. *Foundations and Trends in Human–Computer Interaction, 4*(2), 81–173. [http://dx.doi.org/10.1561/1100000009](http://dx.doi.org/10.1561/1100000009)


# 2. Business Understanding
### 2.1 Problem Statements
Permasalahan yang ingin diselesaikan pada proyek ini adalah:
1. Bagaimana cara merekomendasikan iklan yang sesuai dan relevan kepada pengguna dengan memperhatikan preferensi individu mereka?
2. Bagaimana memberikan rekomendasi yang efektif untuk pengguna baru yang belum memiliki data interaksi historis?
3. Bagaimana mengelola kelebihan informasi agar hanya iklan yang relevan yang muncul dan tidak membebani pengguna?

### 2.2 Goals
Tujuan utama proyek ini adalah:
1. Membangun sistem rekomendasi iklan yang mampu menampilkan konten relevan dan menarik berdasarkan preferensi pengguna.
2. Menyediakan solusi rekomendasi yang efektif untuk pengguna baru meskipun tanpa data klik atau interaksi sebelumnya.
3. Meningkatkan pengalaman pengguna dengan mengurangi jumlah iklan yang tidak relevan melalui penyaringan informasi yang cermat.

### 2.3 Solution Approach
Untuk mencapai tujuan di atas, dua pendekatan solusi utama diusulkan:
1. **Content-Based Filtering**  
Pendekatan ini memanfaatkan informasi kategori artikel atau iklan yang telah diakses pengguna sebelumnya untuk memberikan rekomendasi konten serupa. Contohnya, jika seorang pengguna sering membaca artikel di kategori "Teknologi", sistem akan merekomendasikan artikel lain dari kategori "Teknologi" atau kategori yang memiliki keterkaitan serupa, sehingga menghasilkan rekomendasi yang relevan dan personal.

2. **Collaborative Filtering**  
Pendekatan ini didasarkan pada pola interaksi pengguna lain yang memiliki kemiripan dengan pengguna target. Terdapat dua metode utama:  
   - *User-Based Collaborative Filtering:* Mencari pengguna lain dengan karakteristik serupa, seperti usia, pendapatan, atau durasi penggunaan platform. Sistem kemudian merekomendasikan iklan yang disukai atau diklik oleh pengguna-pengguna tersebut.  
   - *Item-Based Collaborative Filtering:* Mengidentifikasi kemiripan antar iklan berdasarkan pola klik dan interaksi pengguna. Jika dua pengguna menunjukkan preferensi yang mirip, sistem akan merekomendasikan iklan yang relevan dan belum pernah dilihat oleh pengguna target berdasarkan kesamaan pola klik tersebut.


# 3. Data Understanding
Dataset yang digunakan dalam proyek ini mencakup data iklan dan data pengguna. Dataset iklan yang dipakai merupakan data artikel yang juga mengsimulasikan iklan, termasuk kategori, judul, dan ID unik setiap artikel. Dataset pengguna mencakup atribut demografi dan perilaku pengguna, seperti usia, pendapatan, dan waktu harian yang dihabiskan di situs. Terdapat data dummy juga yang dibuat untuk mengsimulasikan iklan yang di klik oleh pengguna. Dataset artikel berita memiliki 14 kategori dengan jumlah artikel bervariasi (lihat tabel di bawah), yang kemudian akan dinormalisasi pada tahap persiapan data. Dataset pengguna mencakup 1.000 pengguna yang secara acak memilih 30 artikel sebagai klik mereka. 

SUMBER DATA:

[Advertisement - Click on Ad dataset](https://www.kaggle.com/datasets/gabrielsantello/advertisement-click-on-ad).

[News Article Category Dataset](https://www.kaggle.com/datasets/timilsinabimal/newsarticlecategories)

Variabel-variabel dalam dataset

---

### 3.1. Dataset Artikel Berita (`(6877, 3)`)

| **Kolom** | **Deskripsi** | **Tipe Data Awal** 
| :--------- | :------------------------------------------------------- | :----------------- | 
| `category` | Kategori artikel (misalnya: Politik, Olahraga, dll.)    | `object`           | 
| `title`    | Judul artikel berita.                                    | `object`           |
| `body`     | Isi lengkap artikel berita.                              | `object`           | 



#### Rincian Jumlah Artikel per Kategori:

| **Kategori**     | **Jumlah Artikel** |
| ---------------- | ------------------ |
| ARTS AND CULTURE | 1002               |
| BUSINESS         | 501                |
| COMEDY           | 380                |
| CRIME            | 300                |
| EDUCATION        | 490                |
| ENTERTAINMENT    | 501                |
| ENVIRONMENT      | 501                |
| MEDIA            | 347                |
| POLITICS         | 501                |
| RELIGION         | 501                |
| SCIENCE          | 350                |
| SPORTS           | 501                |
| TECH             | 501                |
| WOMEN            | 501                |

---

### 3.2. Dataset Pengguna (`(1000, 10)`)

| **Kolom**                  | **Deskripsi**                                                       |
| -------------------------- | ------------------------------------------------------------------- |
| `Daily Time Spent on Site` | Waktu harian (menit) yang dihabiskan pengguna di situs              |
| `Age`                      | Usia pengguna dalam tahun                                           |
| `Area Income`              | Rata-rata pendapatan wilayah geografis pengguna                     |
| `Daily Internet Usage`     | Rata-rata menit penggunaan internet harian pengguna                 |
| `Ad Topic Line`            | Judul atau headline dari iklan                                      |
| `City`                     | Kota tempat tinggal pengguna                                        |
| `Male`                     | Apakah pengguna berjenis kelamin laki-laki (1 = ya, 0 = tidak)      |
| `Country`                  | Negara asal pengguna                                                |
| `Timestamp`                | Waktu ketika pengguna mengklik iklan atau menutup jendela           |
| `Clicked on Ad`            | Indikator apakah pengguna mengklik iklan (1 = klik, 0 = tidak klik) |

---

![image](https://raw.githubusercontent.com/stnrliza/system-recommender/main/image.png?raw=true)

Dataset articlesDF memiliki 6,877 entri dengan 3 kolom (category, title, dan body), di mana kolom body memiliki 5 nilai kosong yang perlu ditangani, sementara kolom lainnya lengkap dan siap digunakan. Dataset ini menggunakan memori sebesar 161.3 KB, dan jika ada ketidakseimbangan jumlah artikel antar kategori, normalisasi data dapat diterapkan. Dataset usersDF berisi 1,000 entri dengan 10 kolom, di mana beberapa kolom seperti Ad Topic Line, City, Country, dan Timestamp kemungkinan tidak relevan untuk sistem rekomendasi sehingga dapat dihapus, sementara kolom numerik seperti Daily Time Spent on Site, Age, dan Area Income dapat dinormalisasi untuk meningkatkan performa model. Dengan semua kolom lengkap tanpa nilai kosong dan ukuran dataset yang kecil (78.2 KB), kedua dataset cukup ringan dan siap diproses setelah dilakukan pembersihan dan normalisasi.

 


# 4. Data Preparation

Tahap ini adalah langkah krusial dalam menyiapkan data mentah menjadi format yang siap untuk digunakan oleh model rekomendasi. Proses ini mencakup pembersihan data, rekayasa fitur, dan transformasi data untuk memastikan kualitas dan kompatibilitas dengan arsitektur model yang akan dibangun.

### 4.1. Dataset Artikel (`articlesDF`)

Dataset awal artikel (`news-article-categories.csv`) berisi informasi mengenai judul, kategori, dan isi (`body`) artikel.

* **Pembersihan Data: Penghapusan Kolom `body`**
    Kolom `body` dihapus dari `articlesDF` karena untuk kebutuhan sistem rekomendasi ini, fokus utama adalah pada kategori dan judul artikel. Kolom `body` yang berupa teks panjang dapat menambah kompleksitas dan mungkin tidak memberikan nilai tambah signifikan dibandingkan dengan `category` dan `title` dalam konteks rekomendasi berbasis kategori.

    ```python
    articlesDF = articlesDF.drop(columns=['body'], axis=1)
    ```

* **Distribusi Kategori Data: Pembatasan Jumlah Artikel per Kategori**
    Analisis awal menunjukkan distribusi jumlah artikel per kategori yang tidak seimbang. Untuk memastikan setiap kategori memiliki representasi yang merata dan menghindari bias model terhadap kategori mayoritas, jumlah artikel per kategori dibatasi hingga **maksimal 300 artikel**. Teknik ini membantu menyeimbangkan dataset, sehingga model tidak terlalu condong pada kategori dengan jumlah data yang sangat besar.

    ```python
    articlesDF = articlesDF.groupby('category', group_keys=False).apply(lambda x: x.sample(min(len(x), 300)))
    ```

* **Penambahan ID Unik (`articleId`)**
    Setiap artikel dalam `articlesDF` diberikan ID unik dalam format `article_X` (misalnya, `article_1`, `article_2`, dst.). Penambahan `articleId` ini sangat penting untuk mempermudah identifikasi, pelacakan, dan penggabungan artikel dengan data interaksi pengguna di tahap selanjutnya.

    ```python
    articlesDF['articleId'] = ['article_' + str(i) for i in range(1, len(articlesDF) + 1)]
    ```

* **Encoding Kategori Artikel**
    Untuk keperluan model **Content-Based Filtering**, kolom `category` pada `articlesDF` diubah menjadi format numerik menggunakan *one-hot encoding* (`pd.get_dummies`). Proses ini mengubah setiap kategori unik menjadi kolom biner baru (1 jika kategori tersebut ada, 0 jika tidak), memungkinkan model untuk memprosesnya sebagai fitur.

    ```python
    articles = pd.get_dummies(articlesDF['category'])
    ```
Output dari proses ini digunakan untuk membentuk articles\_encoded dan user\_category\_matrix:

* articles\_encoded adalah dataframe artikel dengan representasi one-hot kategori.
* user\_category\_matrix merepresentasikan preferensi pengguna terhadap masing-masing kategori artikel, dihitung berdasarkan interaksi mereka dengan artikel sebelumnya.
Matrix user\_category\_matrix inilah yang digunakan sebagai input utama untuk model Content-Based Filtering.


### 4.2. Dataset Pengguna (`usersDF`)

Dataset `usersDF` (`advertising.csv`) awalnya berisi berbagai atribut demografi dan perilaku pengguna.

* **Pembersihan Data: Penghapusan Kolom Tidak Relevan**
    Beberapa kolom dari `usersDF` dihapus karena dianggap tidak relevan untuk pembangunan sistem rekomendasi artikel ini. Kolom-kolom yang dihapus meliputi `Daily Internet Usage`, `Ad Topic Line`, `City`, `Male`, `Country`, `Timestamp`, dan `Clicked on Ad`. Penghapusan ini menyederhanakan dataset dan fokus pada fitur-fitur yang lebih esensial untuk memodelkan preferensi pengguna.

    ```python
    usersDF = usersDF.drop(columns=['Daily Internet Usage', 'Ad Topic Line', 'City', 'Male', 'Country',
           'Timestamp', 'Clicked on Ad'], axis=1)
    ```

* **Penambahan ID Unik (`userId`)**
    Setiap pengguna dalam `usersDF` diberikan ID unik dalam format angka berurutan. Penambahan `userId` ini krusial untuk mengidentifikasi dan melacak setiap pengguna secara unik dalam sistem rekomendasi, serta untuk membangun profil interaksi mereka.

    ```python
    usersDF['userId'] = [i for i in range(1, len(usersDF) + 1)]
    ```

* **Normalisasi Fitur Numerik Pengguna**
    Untuk model **Collaborative Filtering** (terutama bagian _hybrid_), fitur-fitur numerik seperti `Daily Time Spent on Site`, `Age`, dan `Area Income` dinormalisasi menggunakan `MinMaxScaler`. Normalisasi ini menskalakan nilai-nilai fitur ke dalam rentang tertentu (biasanya 0-1), yang membantu menjaga stabilitas dan mempercepat konvergensi pelatihan model _neural network_.

    ```python
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    usersDF[['Daily Time Spent on Site', 'Age', 'Area Income']] = scaler.fit_transform(
        usersDF[['Daily Time Spent on Site', 'Age', 'Area Income']]
    )
    ```

---

### 4.3. Data Dummy: Interaksi Pengguna dengan Artikel (`user_article_df`)

Karena dataset asli tidak menyediakan data interaksi langsung antara pengguna dan artikel, data *dummy* dibuat untuk mensimulasikan riwayat interaksi pengguna.

* **Pembuatan Data Dummy Interaksi**
    Untuk mensimulasikan interaksi, setiap pengguna secara acak "memilih" atau "berinteraksi" dengan **30 artikel** yang berbeda dari `articlesDF` (tanpa pengulangan). Interaksi ini disusun dalam format pasangan `userId` dan `articleId`, membentuk dataset `user_article_df`. Data ini berfungsi sebagai dasar untuk membangun profil minat pengguna.

    ```python
    dummy_data = []
    for user in usersDF["userId"]:
        chosen_articles = np.random.choice(articlesDF["articleId"], 30, replace=False)
        for article in chosen_articles:
            dummy_data.append({"userId": user, "articleId": article})
    user_article_df = pd.DataFrame(dummy_data)
    ```

* **Validasi Data Dummy**
    Validasi dilakukan untuk memastikan bahwa tidak ada kombinasi `userId` dan `articleId` yang duplikat dalam `user_article_df`. Validasi ini memastikan bahwa setiap interaksi yang disimulasikan adalah unik, yang penting untuk integritas data.

    ```python
    unique_counts = user_article_df.value_counts().unique()
    if len(unique_counts) == 1 and unique_counts[0] == 1:
        print("Validation passed: No duplicate user-article combinations.")
    ```


### 4.4. Membuat Matriks Interaksi dan Indeks untuk Model

Tahap ini berfokus pada transformasi data interaksi menjadi format yang spesifik untuk *input* model, terutama untuk model _collaborative filtering_.

* **Gabungan Data Interaksi dengan Informasi Artikel**
    Data interaksi pengguna-artikel (`user_article_df`) digabungkan (`merge`) dengan dataset artikel (`articlesDF`) berdasarkan kolom `articleId`. Penggabungan ini menambahkan informasi kategori dan judul artikel ke setiap entri interaksi, yang penting untuk menganalisis dan memodelkan preferensi kategori pengguna.

    ```python
    interactions_df = user_article_df.merge(articlesDF, on='articleId')
    ```

* **Pemetaan `articleId` ke Indeks Numerik (`article_idx`)**
    Setiap `articleId` unik dipetakan ke indeks numerik (`article_idx`). Pemetaan ini sangat penting karena *embedding layer* dalam model _neural network_ membutuhkan _input_ berupa integer (indeks) daripada string ID. Kolom `article_idx` baru ditambahkan ke `interactions_df`.

    ```python
    article_ids = interactions_df['articleId'].unique()
    article_to_idx = {article: idx for idx, article in enumerate(article_ids)}
    interactions_df['article_idx'] = interactions_df['articleId'].map(article_to_idx)
    ```

* **Pembuatan Matriks Interaksi Kategori Pengguna (`user_category_matrix`)**
    Matriks ini dibuat menggunakan teknik pengelompokan (`groupby`) berdasarkan `userId` dan `category`, kemudian di-_unstack_ (`unstack(fill_value=0)`). Setiap sel pada matriks merepresentasikan jumlah artikel yang diakses oleh seorang pengguna dalam kategori tertentu. Matriks diisi dengan nilai 0 jika tidak ada interaksi pada kategori tersebut, memberikan representasi numerik yang padat dari preferensi kategori setiap pengguna.

    ```python
    user_category_matrix = interactions_df.groupby(["userId", "category"]).size().unstack(fill_value=0)
    ```
### 4.5. Pembentukan Data Pelatihan Positif dan Negatif

Untuk melatih model rekomendasi, terutama pada pendekatan *collaborative filtering*, diperlukan set data yang terdiri dari contoh interaksi positif (pengguna berinteraksi dengan item) dan negatif (pengguna tidak berinteraksi dengan item). Langkah ini memastikan model belajar membedakan antara interaksi yang diminati dan yang tidak.

* **Identifikasi Sampel Positif**: Interaksi yang telah terjadi (dari `interactions_df`) diberi label `1`, menunjukkan adanya minat atau interaksi pengguna terhadap artikel.

    ```python
    positive_samples = interactions_df[['userId', 'article_idx']]
    positive_samples['label'] = 1
    ```

* **Generasi Sampel Negatif**: Semua kemungkinan pasangan pengguna dan artikel dibuat. Dari daftar ini, pasangan yang sudah ada dalam `positive_samples` (yaitu, yang sudah berinteraksi) dieliminasi. Pasangan yang tersisa diasumsikan sebagai interaksi negatif dan diberi label `0`.

    ```python
    all_user_ids = np.arange(num_users)
    all_article_ids = np.arange(num_articles)
    all_pairs = pd.MultiIndex.from_product([all_user_ids, all_article_ids], names=["userId", "article_idx"]).to_frame(index=False)
    negative_samples = all_pairs.merge(positive_samples, on=['userId', 'article_idx'], how='left', indicator=True)
    negative_samples = negative_samples[negative_samples['_merge'] == 'left_only'].drop(columns=['_merge'])
    negative_samples['label'] = 0
    ```

* **Penyeimbangan Kelas**: Untuk mencegah model bias terhadap kelas mayoritas (non-interaksi), jumlah sampel negatif diseimbangkan agar setara dengan jumlah sampel positif.

    ```python
    training_data = pd.concat([positive_samples, negative_samples.sample(len(positive_samples))])
    ```

* **Pemecahan Data untuk Model Input**: Data pelatihan kemudian dipecah menjadi tiga _input_ terpisah (`X_user_id`, `X_article_id`, `X_user_features`) dan satu _output_ target (`y`), sesuai dengan kebutuhan arsitektur model _hybrid_.

    ```python
    X_user_id = training_data['userId'].values - 1
    X_article_id = training_data['article_idx'].values
    X_user_features = usersDF[['Age', 'Area Income', 'Daily Time Spent on Site']].values[X_user_id]
    y = training_data['label'].values
    ```



# 5. Modeling and Result

Tahapan pemodelan ini fokus pada pengembangan sistem rekomendasi yang menyajikan rekomendasi top-N artikel untuk pengguna. Dua pendekatan berbeda digunakan: **Content-Based Filtering** dan **Collaborative Filtering**. Berikut penjelasan terperinci, hasilnya, serta kelebihan dan kekurangan masing-masing metode.

### 5.1 Content-Based Filtering

#### 1. Cara Kerja

Content-Based Filtering memprediksi kemungkinan interaksi antara pengguna dan kategori artikel tertentu dengan output biner (0 atau 1). Model ini memanfaatkan:

1. **Preferensi Pengguna (X\_user)**: Representasi historis interaksi pengguna dengan berbagai kategori.
2. **Vektor Kategori (X\_category)**: One-hot encoding dari kategori artikel yang sedang diproses.

Kedua input digabung menggunakan **layer Concatenate** sehingga model belajar memetakan hubungan preferensi pengguna terhadap kemungkinan interaksi.

#### 2. Arsitektur Model

* **Input Layers**:
  `user_input` dan `category_input`, masing-masing berdimensi `num_categories`, berisi preferensi pengguna dan vektor kategori.
* **Concatenate Layer**:
  Menggabungkan input menjadi vektor panjang `2 * num_categories`.
* **Hidden Layers**:

  * `Dense(64, activation='relu')`: Mengekstraksi hubungan non-linear.
  * `Dense(32, activation='relu')`: Menyaring informasi lebih lanjut.
* **Output Layer**:
  `Dense(1, activation='sigmoid')` untuk memprediksi probabilitas interaksi.
* **Model Compilation**:
  Optimizer `adam`, loss function `binary_crossentropy`, metric `accuracy`.

#### 3. Hasil Top-N Recommendations

* Article: **Anderson Cooper Shreds Trump** (ID: article\_2101, PROB: 0.57)
* Article: **How Many Times Can Wolf Blitzer Avoid Saying 'Shithole'?** (ID: article\_2102, PROB: 0.57)
* Article: **Parents Of Slain DNC Staffer Seth Rich Sue Fox News Over Fake News Story** (ID: article\_2103, PROB: 0.57)
* Article: **Media Euphemisms For 'Racist' Are Stupidly Tinged** (ID: article\_2104, PROB: 0.57)
* Article: **Ted Cruz Makes It Too Easy To Point Out The Hypocrisy Of His Latest Campaign Ad** (ID: article\_2105, PROB: 0.57)

### 5.2 Collaborative Filtering

#### 1. Cara Kerja
Collaborative Filtering memanfaatkan pola interaksi historis antara pengguna dan artikel. Model ini menggunakan:
- **Embedding Layer**: Mengubah ID pengguna dan artikel ke representasi vektor berdimensi rendah.
- **Fitur Tambahan**: Usia, pendapatan, dan waktu yang dihabiskan di situs memperkaya representasi pengguna.

#### 2. Arsitektur Model
* **Normalisasi Fitur Tambahan**:
  Menggunakan `MinMaxScaler` agar berada dalam rentang \[0, 1].
* **Representasi Data**:
  * Artikel dan pengguna direpresentasikan dengan indeks unik.
  * Matriks interaksi biner menandakan ada/tidaknya interaksi.
* **Embedding Layers**:
  * `user_embedding` dan `article_embedding` dengan `embedding_dim=50`, kemudian diratakan.
* **Fitur Tambahan**:
  `user_features` (usia, pendapatan, waktu di situs) digabungkan ke embedding.
* **Hidden Layers**:
  * `Dense(32, activation='relu')` dan `Dense(16, activation='relu')`.
* **Output Layer**:
  `Dense(1, activation='sigmoid')`.
* **Model Compilation**:
  Optimizer `adam`, loss function `binary_crossentropy`, metric `accuracy`.

#### 3. Hasil Top-N Recommendations
* Article: **UN Climate Talks May Only Bring Moderate Progress As Rich Nations Worry About Economy** (ID: article\_1889)
* Article: **Tucker Carlson Turns On Trump: 'Imagine If Barack Obama Had Said That'** (ID: article\_2306)
* Article: **When Patriotism Becomes Idolatry** (ID: article\_2888)
* Article: **Cops Explain How To Pull Off A Good Halloween Prank Without Getting Arrested** (ID: article\_1049)
* Article: **'Late Night' Writer's Breathless Royal Wedding Recap Is The Only One You Need** (ID: article\_815)

### 5.3. Kelebihan dan Kekurangan

| Aspek                       | Content-Based Filtering                        | Collaborative Filtering                      |
| --------------------------- | ---------------------------------------------- | -------------------------------------------- |
| **Cold-Start**              | Baik untuk artikel baru                        | Tidak efektif untuk artikel/pengguna baru    |
| **Eksplorasi Artikel Baru** | Cenderung hanya merekomendasikan konten serupa | Lebih beragam karena melihat pola interaksi  |
| **Ketergantungan Fitur**    | Sangat bergantung pada fitur artikel           | Tidak bergantung pada fitur, hanya interaksi |
| **Data Interaksi**          | Tidak memerlukan data interaksi langsung       | Sangat bergantung pada data interaksi        |
| **Kompleksitas Model**      | Lebih sederhana dan cepat di-train             | Lebih kompleks dan memerlukan data besar     |

Kedua pendekatan disusun dan dijelaskan sesuai urutan yang diterapkan di notebook untuk menjaga konsistensi. Sistem rekomendasi ini diharapkan mampu membantu pengguna menemukan artikel yang sesuai minat dan relevan dengan kebiasaan mereka.



# 6. Evaluation

### 6.1 Metrik Evaluasi
Model dievaluasi menggunakan dua metrik utama: **accuracy** dan **loss**. Keduanya diukur sepanjang proses pelatihan untuk menilai kinerja model.

- **Accuracy**: Mengukur persentase prediksi yang benar dibandingkan total data. Metrik ini memberikan gambaran seberapa efektif model dalam menghasilkan rekomendasi yang relevan.
- **Loss**: Mengukur seberapa besar kesalahan model dalam memprediksi nilai target. Loss yang lebih rendah menunjukkan bahwa model berhasil menyesuaikan diri lebih baik dengan data.

Metrik ini dipilih karena:
- Sesuai dengan konteks data dan permasalahan, yaitu untuk mengevaluasi relevansi rekomendasi yang dihasilkan.
- Sesuai dengan solusi yang diinginkan, di mana akurasi tinggi dan loss rendah menjadi indikator bahwa model bekerja dengan baik dalam memprediksi interaksi pengguna.

### 6.2 Hasil Evaluasi

#### 1. Content-Based Filtering
| Epoch | Accuracy | Loss   |
|-------|----------|--------|
| 1     | 88.88%   | 0.3464 |
| 2     | 89.05%   | 0.3347 |
| 3     | 89.81%   | 0.3073 |
| 4     | 89.56%   | 0.2955 |
| 5     | 89.25%   | 0.2786 |

- Model content-based filtering menunjukkan stabilitas yang baik dengan akurasi akhir sebesar **89.25%**.
- Loss terus menurun hingga **0.2786**, menunjukkan bahwa model berhasil mempelajari pola preferensi pengguna secara efektif.

#### 2. Collaborative Filtering
| Epoch | Accuracy | Loss   |
|-------|----------|--------|
| 1     | 49.43%   | 0.6938 |
| 2     | 55.28%   | 0.6868 |
| 3     | 62.80%   | 0.6490 |
| 4     | 70.66%   | 0.5723 |
| 5     | 76.89%   | 0.4889 |

- Model collaborative filtering menunjukkan peningkatan signifikan dalam akurasi, dari **49.43%** menjadi **76.89%** pada akhir pelatihan.
- Penurunan loss hingga **0.4889** mencerminkan kemampuan model untuk menangkap pola interaksi kompleks antara pengguna dan artikel.

### 6.3. Penjelasan Metrik Evaluasi

- Accuracy
Mengukur rasio prediksi benar terhadap total prediksi yang dibuat. Metrik ini digunakan untuk memberikan gambaran umum tentang seberapa akurat model dalam memprediksi interaksi.

$$
\text{Accuracy} = \frac{\text{Jumlah Prediksi Benar}}{\text{Total Data}}
$$

- Loss (Binary Crossentropy)
Menghitung kesalahan antara prediksi probabilitas dengan nilai target aktual. Formula binary crossentropy digunakan karena ini adalah masalah klasifikasi biner (0 atau 1).   Semakin kecil nilai loss, semakin baik model dalam menyesuaikan output-nya terhadap target yang diinginkan.


$$
\text{Loss} = -\frac{1}{N} \sum_{i=1}^N \left( y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right)
$$
