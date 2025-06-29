# -*- coding: utf-8 -*-
"""ads_recommender_system.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Pgr48m_7W2QFyElBVNas3nVXS4yFK-zP

Tahap-tahap berikut dilakukan mulai dari impor library, membaca dataset, mengeksplorasi data, memeriksa informasi, hingga pembersihan.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Concatenate, Dense, Dropout
from tensorflow.keras.regularizers import l2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Concatenate

articlesDF = pd.read_csv('/content/AdvertisemetRecommenderSystem-with-ArticleDatasets/Dataset/Articles.csv')
usersDF = pd.read_csv('/content/AdvertisemetRecommenderSystem-with-ArticleDatasets/Dataset/Users.csv')

articlesDF.shape

usersDF.head()

articlesDF.info()

usersDF.info()

articlesDF = articlesDF.drop(columns = ['body'], axis=1)

articlesDF.head()

usersDF = usersDF.drop(columns = ['Daily Internet Usage', 'Ad Topic Line', 'City', 'Male', 'Country',
       'Timestamp', 'Clicked on Ad'], axis=1)

"""Menghilangkan beberapa kolom dari DataFrame `usersDF` dilakukan dengan menggunakan fungsi `.drop()`. Parameter `columns` digunakan untuk menentukan nama-nama kolom yang ingin dihapus, yaitu: 'Daily Internet Usage', 'Ad Topic Line', 'City', 'Male', 'Country', 'Timestamp', dan 'Clicked on Ad'."""

usersDF.head()

articlesDF['category'].value_counts()

articlesDF = articlesDF.groupby('category', group_keys=False).apply(lambda x: x.sample(min(len(x), 300)))

"""Memastikan bahwa jumlah baris untuk setiap kategori dalam kolom 'category' tidak melebihi 300."""

articlesDF['category'].value_counts()

usersDF['userId'] = [i for i in range(1, len(usersDF) + 1)]

"""Menyisipkan kolom `userID` guna mempermudah proses identifikasi atau pelacakan data."""

usersDF

articlesDF['articleId'] = ['article_' + str(i) for i in range(1, len(articlesDF) + 1)]

"""Menambahkan kolom `articleID` untuk mempermudah proses pelacakan."""

articlesDF

dummy_data = []

for user in usersDF["userId"]:
    chosen_articles = np.random.choice(articlesDF["articleId"], 30, replace=False)
    for article in chosen_articles:
        dummy_data.append({"userId": user, "articleId": article})

"""Membuat data dummy yang merepresentasikan interaksi pengguna dengan dataset iklan (artikel)."""

user_article_df = pd.DataFrame(dummy_data)

unique_counts = user_article_df.value_counts().unique()

print("Unique counts of userId and articleId combinations:", unique_counts)

if len(unique_counts) == 1 and unique_counts[0] == 1:
    print("Validation passed: No duplicate user-article combinations.")
else:
    print("Validation failed: Duplicate combinations found!")

user_article_df.head(12)

articlesDF.head(12)

usersDF.head(12)

interactions_df = user_article_df.merge(articlesDF, on='articleId')
interactions_df.head(5)

user_category_matrix = interactions_df.groupby(["userId", "category"]).size().unstack(fill_value=0)

user_category_matrix

num_categories = len(user_category_matrix.columns)

user_input = Input(shape=(num_categories,), name='user_input')
category_input = Input(shape=(num_categories,), name='category_input')

merged = Concatenate()([user_input, category_input])

hidden_1 = Dense(64, activation='relu')(merged)
hidden_2 = Dense(32, activation='relu')(hidden_1)
output = Dense(1, activation='sigmoid', name='output')(hidden_2)

model = Model(inputs=[user_input, category_input], outputs=output)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.summary()

"""Model neural network ini digunakan untuk memprediksi output biner (0 atau 1). Model memiliki dua input, yaitu `user_input` dan `category_input`, yang masing-masing memiliki panjang sama dengan jumlah kategori pada `user_category_matrix`. Kedua input tersebut digabungkan melalui layer Concatenate. Selanjutnya, terdapat dua lapisan tersembunyi dengan 64 dan 32 neuron yang menggunakan fungsi aktivasi ReLU untuk pemrosesan lebih lanjut. Output model berupa satu neuron dengan aktivasi sigmoid, yang menghasilkan prediksi biner. Model ini dikompilasi menggunakan optimizer Adam dan fungsi loss `binary_crossentropy` khusus untuk klasifikasi biner."""

user_preferences = user_category_matrix.values

articles = pd.get_dummies(articlesDF['category'])

user_ids = interactions_df['userId'].unique()
categories = articles.columns

num_categories = len(categories)
X_user = []
X_category = []
y = []

for user in user_ids:
    for category in categories:
        X_user.append(user_category_matrix.loc[user].values if user in user_category_matrix.index else [0] * num_categories)

        category_vector = np.zeros(num_categories)
        category_index = list(categories).index(category)
        category_vector[category_index] = 1
        X_category.append(category_vector)

        interacted = interactions_df[
            (interactions_df['userId'] == user) & (interactions_df['category'] == category)
        ]
        y.append(1 if not interacted.empty else 0)



X_user = np.array(X_user)
X_category = np.array(X_category)
y = np.array(y)

"""Mempersiapkan data untuk melatih model yang memprediksi interaksi antara pengguna dan kategori artikel. Untuk setiap kombinasi pengguna (`userId`) dan kategori artikel, dibuat dua input: `X_user`, yaitu vektor preferensi pengguna terhadap kategori, dan `X_category`, berupa vektor one-hot encoding kategori artikel tersebut. Target `y` menunjukkan ada atau tidaknya interaksi pengguna dengan artikel di kategori tersebut (1 jika berinteraksi, 0 jika tidak). Semua data untuk tiap pasangan pengguna dan kategori dikumpulkan ke dalam array NumPy (`X_user`, `X_category`, dan `y`) yang siap dipakai untuk pelatihan model prediksi interaksi."""

model.fit([X_user, X_category], y, epochs=5, batch_size=32)

new_user_articles = ['article_1021', 'article_2364', 'article_271', 'article_1741', 'article_3485']

new_user_vector = np.zeros(num_categories)

for article_id in new_user_articles:
    article_category = articlesDF.loc[articlesDF['articleId'] == article_id, 'category'].values[0]
    category_index = list(categories).index(article_category)
    new_user_vector[category_index] += 1

new_user_vector = new_user_vector / len(new_user_articles)
print("New user preference vector:", new_user_vector)

preferred_categories = [categories[i] for i in range(num_categories) if new_user_vector[i] > 0]

potential_recommendations = articlesDF[articlesDF['category'].isin(preferred_categories)]
print(potential_recommendations)

"""Di bagian ini, dibuat sebuah vektor kosong dengan panjang sesuai jumlah kategori. Kemudian, untuk setiap artikel yang dibaca oleh pengguna baru (`new_user_articles`), kategori artikel tersebut diidentifikasi, dan nilai pada posisi kategori yang bersangkutan di dalam vektor preferensi diperbarui. Vektor ini kemudian dinormalisasi dengan membagi setiap nilainya dengan total artikel yang telah dibaca. Selanjutnya, kategori dengan nilai lebih dari nol diambil dari vektor preferensi dan digunakan untuk menyaring artikel-artikel yang masuk dalam kategori tersebut sebagai rekomendasi potensial bagi pengguna baru."""

recommendations = []

for _, article in potential_recommendations.iterrows():
    article_category_vector = np.zeros(num_categories)
    article_index = list(categories).index(article['category'])
    article_category_vector[article_index] = 1

    probability = model.predict([np.array([new_user_vector]), np.array([article_category_vector])], verbose = 0)[0][0]

    recommendations.append((article['articleId'], article['title'], probability))

recommendations = sorted(recommendations, key=lambda x: x[2], reverse=True)

"""**Top N (5) Recommendation For Content-Based Filtering**"""

top_n = 5
print("Top recommendations:")
for article_id, title, prob in recommendations[:top_n]:
    print(f"Article: {title} (ID: {article_id}, PROB: {prob:.2f})")

"""Membuat rekomendasi artikel untuk pengguna baru dengan menggunakan prediksi dari model. Setiap artikel dalam `potential_recommendations` diproses secara individual untuk membentuk vektor kategori dalam format one-hot encoding."""

scaler = MinMaxScaler()
usersDF[['Daily Time Spent on Site', 'Age', 'Area Income']] = scaler.fit_transform(
    usersDF[['Daily Time Spent on Site', 'Age', 'Area Income']]
)

article_ids = interactions_df['articleId'].unique()
article_to_idx = {article: idx for idx, article in enumerate(article_ids)}
interactions_df['article_idx'] = interactions_df['articleId'].map(article_to_idx)

num_users = len(usersDF)
num_articles = len(article_ids)
interactions_matrix = np.zeros((num_users, num_articles))

for _, row in interactions_df.iterrows():
    interactions_matrix[row['userId'] - 1, row['article_idx']] = 1

embedding_dim = 50

user_input = Input(shape=(3,), name='user_features')  # [Age, Income, Time Spent]

user_id_input = Input(shape=(1,), name='user_id')
user_embedding = Embedding(input_dim=num_users, output_dim=embedding_dim, name='user_embedding')(user_id_input)
user_embedding = Flatten()(user_embedding)

article_input = Input(shape=(1,), name='article_id')
article_embedding = Embedding(input_dim=num_articles, output_dim=embedding_dim, name='article_embedding')(article_input)
article_embedding = Flatten()(article_embedding)

merged = Concatenate()([user_embedding, article_embedding, user_input])

hidden = Dense(32, activation='relu')(merged)
hidden = Dense(16, activation='relu')(hidden)
output = Dense(1, activation='sigmoid', name='output')(hidden)

model = Model(inputs=[user_id_input, article_input, user_input], outputs=output)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.summary()

"""Model neural network dibangun untuk memprediksi interaksi antara pengguna dan artikel dengan memadukan embedding dan fitur tambahan pengguna. Data pengguna (`usersDF`) dinormalisasi pada fitur seperti durasi waktu, usia, dan pendapatan menggunakan MinMaxScaler. Setiap artikel diberikan indeks unik, dan interaksi antara pengguna dan artikel direpresentasikan dalam bentuk matriks biner (`interactions_matrix`). Model menerima tiga input: ID pengguna (`user_id_input`), ID artikel (`article_input`), dan fitur tambahan pengguna (`user_features`). Embedding dipakai untuk merepresentasikan pengguna dan artikel dalam ruang berdimensi rendah (50 dimensi). Hasil embedding diratakan lalu digabungkan dengan fitur tambahan pengguna melalui layer Concatenate. Data kemudian diproses oleh dua lapisan tersembunyi dengan 32 dan 16 neuron sebelum menghasilkan output probabilitas interaksi lewat layer akhir dengan aktivasi sigmoid. Model ini dikompilasi menggunakan optimizer Adam dan fungsi loss `binary_crossentropy` untuk klasifikasi biner."""

positive_samples = interactions_df[['userId', 'article_idx']]
positive_samples['label'] = 1

all_user_ids = np.arange(num_users)
all_article_ids = np.arange(num_articles)

all_pairs = pd.MultiIndex.from_product([all_user_ids, all_article_ids], names=["userId", "article_idx"]).to_frame(index=False)

negative_samples = all_pairs.merge(positive_samples, on=['userId', 'article_idx'], how='left', indicator=True)
negative_samples = negative_samples[negative_samples['_merge'] == 'left_only'].drop(columns=['_merge'])
negative_samples['label'] = 0

training_data = pd.concat([positive_samples, negative_samples.sample(len(positive_samples))])  # Balance classes

X_user_id = training_data['userId'].values -1
X_article_id = training_data['article_idx'].values
X_user_features = usersDF[['Age', 'Area Income', 'Daily Time Spent on Site']].values[X_user_id]
y = training_data['label'].values

model.fit(
    [X_user_id, X_article_id, X_user_features],
    y,
    epochs=5,
    batch_size=32
)

"""Model dilatih menggunakan data positif dan negatif untuk memprediksi interaksi antara pengguna dan artikel. Data positif (`positive_samples`) berisi pasangan pengguna-artikel dari `interactions_df` dengan label 1. Data negatif (`negative_samples`) dibuat dengan terlebih dahulu menghasilkan semua kemungkinan pasangan pengguna-artikel, kemudian menghapus pasangan yang sudah ada di data positif. Pasangan negatif ini diberi label 0, dan jumlahnya disesuaikan agar seimbang dengan data positif. Fitur input meliputi ID pengguna (`X_user_id`), ID artikel (`X_article_id`), dan fitur tambahan pengguna (`X_user_features`) yang diambil dari DataFrame `usersDF` berdasarkan ID pengguna. Target (`y`) merupakan label interaksi biner (1 atau 0). Model kemudian dilatih selama 5 epoch dengan batch size 32 menggunakan fungsi `model.fit()`.

**Top N (5) Recommendations Collaborative Filtering**
"""

def recommend_articles_for_new_user(user_features, interacted_articles, top_n=5):
    normalized_features = scaler.transform([user_features])

    user_input = np.array([normalized_features[0]] * num_articles)
    article_input = np.arange(num_articles)

    probabilities = model.predict([np.zeros(len(article_input)), article_input, user_input])

    excluded_articles = set(interacted_articles)
    article_probabilities = [
        (article_ids[idx], prob)
        for idx, prob in enumerate(probabilities.flatten())
        if article_ids[idx] not in excluded_articles
    ]

    article_probabilities.sort(key=lambda x: x[1], reverse=True)

    recommended_articles = article_probabilities[:top_n]

    recommendations_with_titles = [
        {
            "article_id": article_id,
            "title": articlesDF.loc[articlesDF["articleId"] == article_id, "title"].values[0],
            "probability": prob,
        }
        for article_id, prob in recommended_articles
    ]

    return recommendations_with_titles


new_user_features = [20, 50000, 70]
interacted_articles = ['article_251', 'article_999', 'article_78']

recommendations = recommend_articles_for_new_user(new_user_features, interacted_articles, top_n=5)

print("Recommended articles for the new user:")
for recommendation in recommendations:
    print(f"Article ID: {recommendation['article_id']}, Title: {recommendation['title']}")

"""Memberikan rekomendasi artikel kepada pengguna baru berdasarkan fitur mereka dan riwayat artikel yang telah dibaca. Pertama, fitur pengguna (`user_features`) dinormalisasi menggunakan scaler yang telah dipelajari sebelumnya. Seluruh artikel yang tersedia dijadikan kandidat dengan membuat input pengguna (`user_input`) berupa penggandaan fitur yang sudah dinormalisasi, serta input artikel (`article_input`) berupa indeks semua artikel. Model kemudian memprediksi probabilitas interaksi untuk setiap artikel. Artikel yang sudah pernah dilihat oleh pengguna (`interacted_articles`) dikeluarkan dari daftar rekomendasi. Artikel yang tersisa disusun berdasarkan probabilitas interaksi dari yang tertinggi ke terendah, lalu sejumlah `top_n` artikel terbaik dikembalikan sebagai rekomendasi. Hasil rekomendasi ditampilkan dengan mencetak ID artikel yang dipilih."""