# Tugas 2 Pemrograman Berbasis Platform
**Nama    : Adrasa Cantya Salaka**

**NPM     : 2206829603**

**Kelas   : E**

## Aplikasi Adaptable dari Tugas 2: Inventory App dapat diakses melalui tautan [berikut](https://tugas-2-pbp-aca.adaptable.app/main/).

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   
     - [x]  Membuat sebuah proyek Django baru.
           
     Untuk bisa membuat sebuah proyek Django baru, saya perlu membuat virtual environment di dalam direktori proyek Inventory_App. Hal ini dilakukan dengan tujuan mengisolasi dependencies antara proyek-proyek yang berbeda.

     Di dalam virtual environment tersebut, saya perlu memasangkan dependencies (pada kasus ini, dependencies dituliskan di dalam sebuah file bernama `requirements.txt`) menggunakan perintah `pip install -r requirements.txt`. Selanjutnya, saya akan membuat proyek Django dengan perintah `django-admin startproject Inventory_App .` 

     - [x] Membuat aplikasi dengan nama main pada proyek tersebut.
           
     Di dalam proyek Inventory_App, perintah yang perlu dijalankan untuk membuat aplikasi dengan nama main adalah `python manage.py startapp main`. Perintah ini akan menciptakan direktori baru dengan nama `main` yang akan berisi struktur awal untuk aplikasi Inventory_App.
   
     - [x] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
           
     Agar aplikasi bernama `main` yang sudah dibuat tadi dapat dijalankan, saya perlu membuka file `settings.py` dan menambahkan `'main'` (nama aplikasi yang dibuat tadi) pada variabel `INSTALLED_APPS`.

     - [x] Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
           
     `name` sebagai nama item dengan tipe `CharField`.
   
     `amount` sebagai jumlah item dengan tipe `IntegerField`.

     `description` sebagai deskripsi item dengan tipe `TextField`.

     Untuk bisa memenuhi kriteria-kriteria di atas, saya mmemasukkan barisan kode berikut pada berkas `models.py` di aplikasi main.
   
   ```
     from django.db import models

     class Product(models.Model): # Membuat class Product sebagai nama model yang akan dibuat. models.Model untuk mendefinisikan model pada Django.
         # Assigning each attributes to their respective datatypes.
         name = models.CharField(max_length=255)
         amount = models.IntegerField()
         description = models.TextField()
   ```

     Langkah yang seharusnya saya lakukan adalah mengaplikasikan migrasi model dengan cara menjalankan perintah-perintah berikut secara berurutan pada command prompt.

   `python manage.py makemigrations` # Untuk mencari perbedaan pada model.

   `python manage.py migrate` # Mengaplikasikan perubahan yang ditemukan

     - [x] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

     Pada berkas `views.py` yang terletak di dalam berkas aplikasi main, tambahkan kode `from django.shortcuts import render` di line nomor 1 . Tujuan kode ini adalah mengimpor fungsi render dari modul `django.shortcuts` untuk me-render tampilan HTML dengan menggunakan data yang diberikan. Di bawahnya, kita perlu menambahkan barisan kode berikut.
     ```
      def show_main(request):
          context = {
              'app_name': 'Inventory App', 
              'name': 'Adrasa Cantya Salaka',
              'class': 'PBP E'
          }
      
          return render(request, "main.html", context)
     ```
     
     `def show_main(request)` merupakan deklarasi fungsi `show_main`, yang menerima parameter `request`. Fungsi ini akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai. `context` adalah dictionary yang berisi data yang akan dikirimkan ke tampilan. Pada konteks ini, tiga data disertakan, yaitu:

     - app_name: Data nama aplikasi.
     - name: Data nama.
     - class: Data kelas.
       
    `return render(request, "main.html", context)` berguna untuk me-render tampilan `main.html` dengan menggunakan fungsi render yang mengambil tiga argumen (`request`, `"main.html"`, dan `context`) sehingga tampilannya bisa dinamis.

     - [X] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

     Di dalam direktori main, saya akan membuat berkas berjudul `urls.py`. Berkas ini bertanggung jawab untuk mengonfigurasi routing URL aplikasi main.

     Isi dari berkas tersebut adalah sebagai berikut.
     ```
     from django.urls import path # Mendefinisikan pola URL
     from main.views import show_main # Tampilan yang akan ditampilkan saat URL diakses

     app_name = 'main' # Memberikan nama unik pada pola URL dalam aplikasi

     urlpatterns = [
        path('', show_main, name='show_main'),
     ]
     ```
     Selanjutnya yang perlu kita lakukan adalah menambahkan rute URL dalam `urls.py` tingkat proyek untuk menghubungkannya ke tampilan main. Hal ini dilakukan dengan cara mengimpor fungsi `include` untuk mengimpor rute URL dari aplikasi lain (dalam hal ini, dari aplikasi main) ke dalam berkas `urls.py` Inventory_App. Dilanjut dengan menambahkan rute URL `path('main/', include('main.urls'))` pada variabel `urlpatterns`, path URL `'main/'` akan diarahkan ke rute URL yang dibuat tadi pada file `urls.py` di aplikasi main. File `urls.py` pada aplikasi main bertugas untuk mengatur rute URL spesifik yang dibutuhkan oleh fitur-fitur aplikasi main sedangkan `urls.py` pada proyek Inventory_App bertugas untuk mengarahkan rute URL proyek dan akan mengimpor rute URL dari file `urls.py` aplikasi-aplikasi bila dibutuhkan.

     - [X] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

     Langkah pertama yang harus dilakukan adalah memastikan file proyek `Inventory_App` sudah memiliki repositori di GitHub dengan nama `Inventory_App`. Pada website Adaptable.io, pilih `Create New App` dan pilih opsi `Connect Git Repository`, kemudian pilih `repository Inventory_App` dan pilih `branch main`. Langkah selanjutnya adalah memilih `Python App Template` sebagai Deploy Template-nya, Gunakan Database Type `Postgre SQL` dan pilih `python version` sesuai dengan yang digunakan (3.11) dan mengisi start command dengan perintah `python manage.py migrate && gunicorn Inventory_App.wsgi`. Masukkan nama aplikasi, yaitu `tugas-2-pbp-aca`, dimana nama ini juga akan menjadi nama domainnya, terakhir centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses deployment.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas html.
   
   ![2.1 Gambar Bagan](https://github.com/acasalaka/Inventory_App/assets/124960259/9884e981-7c46-4f25-83f9-5af771d56693)
   Awalnya, `Client` akan mengirimkan HTTP request ke URL tertentu dan ditangkap oleh `urls.py`. `urls.py` mencocokkan URL yang diterima dari request dengan pola URL yang didefinisikan dalam file ini. Jika URL cocok dengan salah satu pola yang ada, `urls.py` mengarahkan request ke `views.py` yang sesuai. `views.py` dapat berinteraksi dengan `models.py` (jika diperlukan) untuk mengambil atau memanipulasi data dari database. `models.py` mengembalikan data dari database ke `views.py`. `views.py` akan mengolah berkas `main.html` dengan menggunakan data yang telah diperoleh dari `models.py`. Hasil olahan `main.html` oleh `views.py` akan menghasilkan response yang dikirim kembali ke `Client`

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
   
   Pada sebuah proyek yang menggunakan Django, kita perlu menggunakan virtual environment untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer. Apabila dianalogikan, virtual environment adalah sebuah kamar pribadi di dalam rumah yang sangat bebas untuk digunakan oleh seseorang tanpa mengganggu penghuni-penghuni yang lain. Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun pastinya akan rentan bermasalah disaat kita memiliki lebih dari satu proyek Django pada komputer kita.  

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

   Ketiganya merupakan jenis-jenis pola desain arsitektur. 
   
   **Model - View - Controller (MVC)**
   _Referensi: [https://www.geeksforgeeks.org/mvc-framework-introduction/](https://www.geeksforgeeks.org/mvc-framework-introduction/)_ 
   
   ![4.1 Gambar Bagan MVC](https://github.com/acasalaka/Inventory_App/assets/124960259/81e4e801-6b05-4138-b398-765742447796)
   
   - Model: komponen ini berisi tentang logika bisnis dan status data yang ada di dalam aplikasi. Ini dapat mewakili data yang ditransfer antara komponen View dan Controller atau data terkait logika bisnis lainnya.
   - View: komponen ini berhubungan dengan antarmuka pengguna yang terdiri dari HTML/CSS.XML. Komponen ini berkomunikasi dengan pengontrol dan terkadang berinteraksi dengan model. View berkerja sama dengan controller untuk menciptakan tampilan dinamis pada aplikasi yang dikembangkan. Selain bertugas untuk menangani antarmuka dan interaksi pengguna, komponen view juga memiliki tugas untuk menyajikan data yang sesuai untuk pengguna.
   - Controller: Controller adalah komponen yang mengintegrasikan View dan Model, perantara. Memproses semua logika bisnis dan permintaan masuk, memanipulasi data menggunakan komponen Model, dan berinteraksi dengan View untuk me-render tampilan akhir.
   
   Perbedaannya dengan yang lain adalah mempunyai batasan yang jelas antara logika bisnis, logika UI, dan logika input. Selain itu, perbedaan-perbedaan lainnya antara lain inputnya diarahkan pada Controller, relasi antara Controller dan View bersifat many-to-one, dan Controller menyerahkan Model ke View juga sehingga View paham tentang Controller. 
   
   **Model - View - Template (MVT)**
   _Referensi: [https://www.geeksforgeeks.org/django-project-mvt-structure/](https://www.geeksforgeeks.org/django-project-mvt-structure/)_ 
   
   ![4.2 Gambar Bagan MVT](https://github.com/acasalaka/Inventory_App/assets/124960259/2c981e8d-0834-4687-b8cc-1ec33a1d46be)

     Merupakan turunan dari MVC.
     
   - Model: bertindak sebagai interface data. objek yang mendefinisikan entitas pada database beserta konfigurasinya.
   - View: interface pengguna — apa yang dilihat di browser saat me-render situs web. Logika utama dari aplikasi yang akan melakukan pemrosesan terhadap permintaan yang masuk.
   - Template: komponen yang berfungsi untuk mengatur tampilan atau antarmuka pengguna. Template memisahkan kode HTML dari logika aplikasi. Dalam MVT, template digunakan untuk merancang tampilan yang akhirnya akan diisi dengan data dari Model melalui View.
  
   Perbedaannya dengan yang lain adalah alurnya. Berikut adalah alur pemrosesan sebuah request atau permintaan pada MVT. Yang pertama, permintaan yang masuk ke dalam server Django akan diproses melalui `urls` untuk diteruskan ke `views` yang didefinisikan oleh pengembang untuk memproses permintaan tersebut. Apabila terdapat proses yang membutuhkan keterlibatan database, maka nantinya `views` akan memanggil query ke `models` dan database akan mengembalikan hasil dari query tersebut ke `views`. Setelah permintaan telah selesai diproses, hasil proses tersebut akan dipetakan ke dalam HTML yang sudah didefinisikan sebelum akhirnya HTML tersebut dikembalikan ke pengguna sebagai respons.

   **Model - View - ViewModel (MVVM)**
   _Referensi: [https://www.geeksforgeeks.org/introduction-to-model-view-view-model-mvvm/](https://www.geeksforgeeks.org/introduction-to-model-view-view-model-mvvm/)_
   
   ![4.3 Gambar Bagan MVVM](https://github.com/acasalaka/Inventory_App/assets/124960259/b97b6af3-2fda-40f0-9c2f-d69127d4354e)

   - Model: objek bisnis yang merangkum data dan perilaku domain aplikasi, hanya menyimpan data.
   - View: memformat data sehingga mudah untuk dilihat oleh pengguna.
   - ViewModel: abstraksi dari View dan juga penyedia pembungkus data Model untuk ditautkan. ViewModel terdiri dari Model yang diubah menjadi View, dan berisi perintah yang dapat digunakan oleh View untuk mempengaruhi Model.
   
   Perbedaannya dengan yang lain adalah inputnya diawali pada Model, relasi antara ViewModel dengan View dan Model bersifat one-to-many, dan View tidak aware akan Model.
