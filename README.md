**Nama    : Adrasa Cantya Salaka**

**NPM     : 2206829603**

**Kelas   : E**

<details>
<summary> Tugas 4 Pemrograman Berbasis Platform</summary>

# Tugas 4 Pemrograman Berbasis Platform

1. Apa itu `Django UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
   
   `Django UserCreationForm` adalah impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web. Dengan formulir ini, pengguna baru dapat mendaftar dengan mudah di situs web Anda tanpa harus menulis kode dari awal.

| KELEBIHAN | KEKURANGAN | 
| :-----------: | :---------: |
| Mudah digunakan karena formulirnya sudah jadi, kita hanya cukup meng-import | Tidak menyediakan pendaftaran eksternal, misalkan menggunakan Google Account, dll. | 
| Telah terintegrasi dengan Django's authentication system | Tampilannya perlu disesuaikan dengan layout web kita | 
| Proses validasi otomatis | Data bawaan yang diautentikasi hanya username dan password, sehingga jika ingin menambahkan kolom lain perlu dikerjakan secara manual |

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

   Autentikasi adalah proses menentukan identitas pengguna. Dalam Django, autentikasi biasanya melibatkan pengguna untuk memasukkan kredensial mereka (seperti nama pengguna dan kata sandi) untuk masuk ke akun mereka. Django menyediakan sistem autentikasi bawaan yang mencakup model pengguna (django.contrib.auth.models.User), formulir autentikasi, dan pustaka otentikasi yang memudahkan pengembang untuk mengimplementasikan proses autentikasi.

   Otorisasi adalah proses untuk menentukan apakah pengguna yang meminta izin masuk tersebut sudah memiliki akses dari sumber daya yang berwenang. Dalam Django, otorisasi biasanya diimplementasikan menggunakan sistem otorisasi berdasarkan peran (role-based) dan izin (permission-based). Anda dapat menetapkan peran kepada pengguna (misalnya, pengguna biasa, admin, atau moderator) dan kemudian memberikan izin kepada peran tersebut untuk melakukan tindakan tertentu di dalam aplikasi.

   Keduanya penting karena merupakan salah satu bentuk sistem keamanan website. Hal ini perlu dilakukan agar mencegah akses yang tidak sah atau tidak diinginkan ke sumber daya atau informasi sensitif.

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

   Cookie (sering dikenal sebagai cookie internet) adalah file teks dengan potongan kecil data — seperti nama pengguna dan kata sandi — yang digunakan untuk mengidentifikasi komputer user saat user menggunakan jaringan. Dengan kata lain, cookie adalah istilah untuk kumpulan informasi yang berisi rekam jejak dan aktivitas ketika menelusuri sebuah website. Secara sederhana pengertian cookies adalah kumpulan data yang diterima komputer dari sebuah situs dan mengirimkan kembali ke situs yang dikunjungi. Cookie khusus digunakan untuk mengidentifikasi pengguna tertentu dan meningkatkan pengalaman penelusuran web mereka. Data yang disimpan dalam cookie dibuat oleh server pada koneksi user. Data ini diberi label dengan ID unik untuk user dan komputer user. Ketika cookie dipertukarkan antara komputer user dan server jaringan, server membaca ID dan mengetahui informasi apa yang secara khusus disajikan kepada user.

   Django menggunakan cookies untuk mengelola data sesi pengguna dengan menggunakan mekanisme yang disebut "Django Sessions." Django Sessions memungkinkan user untuk menyimpan data sesi pengguna secara aman pada sisi server, tetapi tetap mengidentifikasi pengguna dengan bantuan cookie yang dikirim ke peramban pengguna.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

   Django secara default mengenkripsi cookies sesi pengguna, sehingga keamanan data sensitif pengguna dapat dipastikan aman. Akan tetapi, cookie dapat menimbulkan risiko keamanan bila digunakan secara tidak benar. Informasi sensitif yang disimpan dalam cookie dapat rentan terhadap akses tidak sah, terutama jika dikirimkan melalui koneksi HTTP yang tidak aman. Selain itu, cookie dapat menjadi vektor untuk serangan cross-site scripting (XSS) dan cross-site request forgery (CSRF), di mana aktivitas jahat dapat dijalankan pada browser pengguna dengan mengeksploitasi kelemahan kode situs web.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   
   - [X] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
  
   Semuanya dikerjakan di dalam virtual environment (env).

   a. Registrasi
   
Pada file `views.py` yang ada pada subdirektori `main`, saya akan membuat fungsi `registrasi` yang menerima parameter `request` dengan kode sebagai berikut.

```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

`form = UserCreationForm(request.POST)` digunakan untuk membuat variabel `form` baru yang merupakan `UserCreationForm`. Kemudian memasukkan `QueryDict` berdasarkan input dari user pada `request.POST`. `form.is_valid()` digunakan untuk memvalidasi isi input form, `form.save()` digunakan untuk membuat dan menyimpan data dari form, `messages.success(request, 'Your account has been successfully created!')` digunakan untuk menampilkan pesan kepada pengguna apabila ia berhasil melakukan registrasi. `return redirect('main:show_main')` digunakan untuk redirect user setelah data form berhasil disimpan.

Selain itu saya juga akan menambahkan `import redirect, UserCreationForm,` dan `messages` pada bagian paling atas untuk mendukung `UserCreationForm`.

```
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```

Langkah selanjutnya adalah membuat berkas `register.html` pada folder `main/templates` dan mengisinya dengan barisan kode di bawah.

```
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

Seperti tugas03. kita perlu mengubungkan file ini dengan main dengan cara mengimpor fungsi ini kedalam `views.py` menggunakan `from main.views import register`. Setelah itu kita juga perlu menambahkan path url ini ke dalam `urlspattern` di `urls.py` dengan kode `path('register/', register, name='register'),`.


   b. Login

Pada file `views.py` yang ada pada subdirektori `main`, saya akan membuat fungsi `login_user` yang menerima parameter `request` dengan kode sebagai berikut.

```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

Sedikit berbeda dengan registrasi, pada barisan kode di atas terdapat `uthenticate(request, username=username, password=password` yang digunakan untuk melakukan autentikasi pengguna berdasarkan username dan password yang diterima dari permintaan (request) yang dikirim oleh pengguna saat login.

Selain itu saya juga perlu menambahkan `import authenticate, login` pada bagian paling atas dengan kode `from django.contrib.auth import authenticate, login`

Langkah selanjutnya adalah membuat berkas `login.html` pada folder `main/templates` dan mengisinya dengan barisan kode di bawah.

```
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```

Seperti registrasi. saya perlu mengubungkan file ini dengan main dengan cara mengimpor fungsi ini kedalam `views.py` menggunakan `from main.views import login_user`. Setelah itu kita juga perlu menambahkan path url ini ke dalam `urlspattern` di `urls.py` dengan kode `path('login/', login_user, name='login'),`.

   c. Logout

Pada file `views.py` yang ada pada subdirektori `main`, saya akan membuat fungsi `logout_user` yang menerima parameter `request` dengan kode sebagai berikut.

```
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

Selain itu saya juga perlu menambahkan `import logout` pada bagian paling atas dengan kode `from django.contrib.auth import logout`

Setelah itu, saya perlu menambahkan barisan kode berikut pada file `main.html` dan diletakkan setelah tag Add New Product.

```
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
```

Seperti registrasi dan login. saya perlu mengubungkan file ini dengan main dengan cara mengimpor fungsi ini kedalam `views.py` menggunakan `from main.views import logout_user`. Setelah itu kita juga perlu menambahkan path url ini ke dalam `urlspattern` di `urls.py` dengan kode `path('logout/', logout_user, name='logout'),`.


   - [X] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

<img width="960" alt="Screenshot 2023-09-27 113303" src="https://github.com/acasalaka/Inventory_App/assets/124960259/dc9ceb0d-8c7a-4a28-bdf7-d2ee4baf2a89">

<img width="960" alt="Screenshot 2023-09-27 113321" src="https://github.com/acasalaka/Inventory_App/assets/124960259/068f8421-0b28-40ae-9c9a-3f95dc674b52">

Disini terlihat bahwa kedua user masih memiliki barang-barang yang sama di inventori mereka. Selain ini, saya juga masih mengalami error saat ingin melakukan `python manage.py runserver` di dalam virtual environment.

   - [X] Menghubungkan model Item dengan User.

   Buka models.py yang ada di direktori main lalu impor `User` dari `django.contrib.auth.models`. Pada model Product yang ada, saya perlu menambahkan kode berikut.

```
class Product(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   ...
```

Hal ini dilakukan supaya kita menghubungkan satu produk dengan satu user menggunakan relationship, sehingga sebuah produk pasti terasosiasi dengan user. Pada file `views.py` yang ada di direktori main, saya perlu memodifikasi fungsi `create_product` menjadi sebagai berikut.

```
def create_product(request):
form = ProductForm(request.POST or None)

if form.is_valid() and request.method == "POST":
  product = form.save(commit=False)
  product.user = request.user
  product.save()
  return HttpResponseRedirect(reverse('main:show_main'))
...
```

`commit=False` berfungsi supaya Django tidak langsung menyimpan objek yang dibuat dari form ke database sehingga objek dapat dimodifikasi tersebut dahulu. Kita mengisi field user dengan objek User dari return nilai `request.user` yang sudah terautentikasi untuk menandakan bahwa objek tersebut milik pengguna yang sedang login.

Selanjutnya, saya perlu mengubah fungsi `show_main` menjadi sebagai berikut.
```
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
    ...
    }
...
```

Langkah terakhir adalah melakukan migrasi karena saya telah melakukan perubahan pada Model products. Saat ada error yang muncul pada proses migrasi, kita perlu menulis `1` untuk menetapkan default value untuk field user pada semua row yang telah dibuat pada basis data.
  
   - [X] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.   

Pada file `views.py` yang ada pada subdirektori `main`, saya perlu menambahkan `import HttpResponseRedirect, reverse, dan datetime` pada bagian paling atas. Selanjutnya, saya perlu menambahkan cookie pada fungsi `login_user` yang bernama `last_login` supaya bisa menentukan kapan waktu terakhir user tersebut melakukan login. Hal ini dilakukan dengan mengganti kode pada blok `if user is not None:` dengan kode sebagai berikut.

```
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```

`login(request, user)` berfungsi agar web melakukan login terlebih dahulu. Selanjutnya program akan membuat sebuah variabel baru bernama `response` yang berisikan `HttpResponseRedirect(reverse("main:show_main"))`. Nantinya, response akan ditambahkan dengan cookie last_login.

Langkah selanjutnya adalah menambahkan kode `'last_login': request.COOKIES['last_login']` pada variable `context` di fungsi `show_main`.

Saya juga perlu mengubah fungsi `logout_user` menjadi sebagai berikut sehingga cookie `last_login` dihapus saat pengguna melakukan logout.

```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

Agar perubahan dan juga sesi terakhir login dapat dilihat secara langsung oleh user, saya perlu menambahkan `<h5>Sesi terakhir login: {{ last_login }}</h5>` pada barisan kode yang terletak di `main.html`.

</details>

<details>
<summary>Tugas 5 Pemrograman Berbasis Platform</summary>


# Tugas 5 Pemrograman Berbasis Platform

<b> 1. Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework </b>

-  Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.

Pada tugas ini, saya menggunakan CSS from scratch. Saya juga banyak menggunakan icon yang diperoleh dari fontawesome.com. Untuk itu, saya perlu menambahkan barisan kode ini setelah {% block meta %} untuk meng-import icon yang diinginkan.

```
<script src="https://kit.fontawesome.com/54f81dee97.js" crossorigin="anonymous"></script>
```

Selanjutnya saya akan menambahkan block `<style>` di bawah block script untuk meletakkan pengaturan style yang saya inginkan dari halaman login, register, dan tambah inventori. Pada block ini, saya banyak menggunakan element selector, class selector, dan juga [attribute="value"] selector. Berikut adalah styles yang saya gunakan untuk menciptakan halaman login yang menarik. 

```
body {
    font-family: "Poppins", sans-serif;
    text-align: center;
    max-width: fit-content;
    max-height: fit-content;
    background-image: url('https://images.unsplash.com/photo-1513672494107-cd9d848a383e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2069&q=80');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
.container {
    display: inline-block;
    width: 220px;
    height: 300px;
    position: absolute;
    top: 48%;
    left: 50%;
    transform: translate(-50%, -50%);
    margin: 0 auto;
    padding: 40px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}
.register_message {
    font-family: "Poppins", sans-serif;
    font-size: smaller;
    position: absolute;
    top: 71%;
    left: 50%;
    transform: translate(-50%, -50%);
    max-width: 400px;
    margin: 0 auto;
    padding: auto;
}
i {
    font-size: 60px;
    padding-bottom: 17px;
}
table {
    display: inline-block;
    margin-bottom: 5px;
}
input[type="text"],
input[type="password"] {
    width: 80%; 
    padding: 10px;
    margin-top: 5px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 8px;
}
input[type="submit"] {
    background-color: #0070e8;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 8px;
    cursor: pointer;
    position: absolute;
    left: 37%;
}
input[type="submit"]:hover {
    background-color: #024995;
}
```
Di bawah ini adalah kode untuk styling halaman register.
```
body {
    font-family: "Poppins", sans-serif;
    text-align: center;
    max-width: auto;
    max-height: auto;
    background-image: url('https://images.unsplash.com/photo-1513672494107-cd9d848a383e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2069&q=80');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
.register {
    display: inline-block;
    width: auto;
    height: auto;
    position: absolute;
    top: 48%;
    left: 50%;
    transform: translate(-50%, -50%);
    margin: 0 auto;
    padding-left: 30px;
    padding-right: 30px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}
table {
    margin-bottom: 3px;
    text-align: left;
}
input[type="text"],
input[type="password"] {
    width: 80%; 
    padding: 10px;
    margin-top: 5px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 8px;
    text-align: left;
}
input[type="submit"] {
    background-color: #0070e8;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 8px;
    cursor: pointer;
    position: relative;
    margin-top: 10px;
    margin-bottom: 10px;
    transform: translateX(-90%);
}
input[type="submit"]:hover {
    background-color: #024995;
}
span[class="helptext"] {
    font-size: smaller;
}
ul {
    text-align: left;
}
th {
    text-align: left;
}
tr {
    text-align: center;
}
```
Terakhir, barisan kode di bawah ini digunakan untuk styling halaman create_product.
```
* {
    margin: 0;
    padding: 0;
    font-family: "Poppins", sans-serif;
    text-align: center;
}
body {
    font-family: "Poppins", sans-serif;
    text-align: center;
    max-width: auto;
    max-height: auto;
    background-color: blanchedalmond;
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
h2 {
    margin-bottom: 10px;
}
.add-product {
    display: inline-block;
    width: auto;
    height: auto;
    position: absolute;
    top: 48%;
    left: 50%;
    transform: translate(-50%, -50%);
    margin: 0 auto;
    padding: 30px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}
table {
    margin-bottom: 3px;
    text-align: left;
}
input[type="text"],
input[type="number"], textarea {
    width: 80%; 
    padding: 10px;
    margin-top: 5px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 8px;
    text-align: left;
}
input[type="submit"] {
    background-color: #0070e8;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 8px;
    cursor: pointer;
    position: relative;
    margin-top: 10px;
    transform: translateX(-30%);
}
input[type="submit"]:hover {
    background-color: #024995;
}
ul {
    text-align: left;
}
td {
    border-radius: 8px;
}
th {
    text-align: left;
}
```

- Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.

Pada tugas ini, saya menggunakan CSS from scratch. Saya juga banyak menggunakan icon yang diperoleh dari fontawesome.com. Untuk itu, saya perlu menambahkan barisan kode ini setelah {% block meta %} untuk meng-import icon yang diinginkan.

```
<script src="https://kit.fontawesome.com/54f81dee97.js" crossorigin="anonymous"></script>
```

Selanjutnya saya akan menambahkan block `<style>` di bawah block script untuk meletakkan pengaturan style yang saya inginkan dari halaman login, register, dan tambah inventori. Pada block ini, saya banyak menggunakan element selector, class selector, [attribute="value"] selector, dan juga menggunakan pseudo-class selector `:visited`, `:hover`, `:last-child`, dan lain sebagainya. Action selection `:last-child` secara spesifik akan saya gunakan untuk mengerjakan tugas bonus, yaitu memberikan warna yang berbeda pada produk terakhir di tabel.

Untuk bisa membuat sebuah navbar, saya meletakan barisan kode berikut setelah {% block content %} dimulai.

```
<div class="navbar">
    <a class="logo"><i class="fa-solid fa-box" style="color: #0070e8;" width="20px"></i>&nbsp; &nbsp; &nbsp;Inventory App</a>
    <a class="logout-btn" href="{% url 'main:logout' %}">Logout</a>
</div>
``` 
Nantinya, di block style saya akan mengatur sehingga logo akan terletak di paling kiri dan tombol logout di paling kanan. 
```
.navbar {
    background-color: white;
    overflow: hidden;
}
.navbar a {
    color: black;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}
.navbar .logo {
    float: left;
}
.logout-btn {
    float: right;
    padding: 14px 16px;
    background-color: rgb(232, 232, 232);
    color: white;
    border: none;
    cursor: pointer;
}
.logout-btn:hover {
            background-color: rgb(198, 197, 197);
}
```
Menggunakan block style itu juga, saya mengubah tampilan dari tabel berisi produk menggunakan element selector `table`, `th`, `tr`, dan `td`.
```
table {
    margin: auto;
    margin-top: 50px;
    margin-bottom: 20px;
    width: 80%;
}
th {
    background-color: #0070e8;
    color: white;
    padding: 10px;
    font-size: 16px;
    text-align: center;
}
td {
    padding: 10px;
    font-size: 14px;
    text-align: center;
}
tr {
    border: 1px;
    text-align: justify;
    font-size: 14px;
    background-color: white;
    margin: 10px;
}
tr:last-child {
    background-color: rgb(198, 197, 197);
} 
```
Untuk mempercantik tampilan button Add product dan Logout, saya menggunakan style berikut.
```
button {
    background-color: white; 
    color: black; 
    padding: 10px 20px;
    border: none; 
    border-radius: 8px; 
    cursor: pointer; 
    margin-right: 20px;
}
button:hover{
    background-color: #bababa;
}
button:visited { <!-- Diperlukan sehingga warna tombol tidak berubah setelah ditekan -->
    color: black;
}
```
Terakhir, pada tugas ini saya juga menambahkan 2 kolom tambahan pada tabel yang ditujukan untuk mengubah dan menghapus produk. Seperti tugas-tugas sebelumnya, yang perlu saya lakukan adalah menambahkan fungsi baru di `views.py`, meng-import method-nya ke dalam `urls.py` dan menambahkannya ke dalam `urlspattern`, dan juga menghubungkan tombol dengan method yang terkait. Berikut adalah barisan kode yang dituliskan di `views.py`.

```
def edit_product(request, id):
    product = Product.objects.get(pk = id)

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```

Karena edit_product akan menampilkan sebuah layar html baru, maka saya akan membuat sebuah file baru bernama `edit_product.html` di dalam main/templates.

``` 
{% extends 'base.html' %}
    <title>Inventory App Register</title>
{% block content %}

<div class="edit-product">
    <h2>Edit Product</h2>
    
    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Edit Product"/>
                </td>
            </tr>
        </table>
    </form>

</div>

{% endblock content %}
```
Untuk menambahkan mereka sebagai kolom baru di tabel, saya menambahkan kode di bawah ini.
```
<tr>                
    ...
    <td>
        <a href="{% url 'main:edit_product' product.pk %}">
            <i class="fa-regular fa-pen-to-square"></i>
        </a>
    </td>
    <td>
        <a href="{% url 'main:delete_product' product.pk %}">
            <i class="fa-solid fa-trash"></i>
        </a>
    </td>
</tr>
```
Karena saya tidak ingin kedua kolom tersebut berisikan tulisan, saya menggunakan tag `<i>`. `<i class="">` digunakan agar kolom tersebut berisi icon yang saya pilih.

Nantinya, laman edit_product akan mendapatkan style yang kurang lebih sama dengan laman add_product.

<b> 2. Menjawab beberapa pertanyaan berikut pada README.md </b>

- [X]  Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

    a. Universal selector

    Memilih seluruh elemen HTML di halaman. Biasanya digunakan untuk memberikan style dasar pada setiap elemen HTML. Untuk bisa menggunakan universal selector, kita perlu menuliskan '*' seperti di bawah ini.

    ```
    * {
    text-align: center;
    color: blue;
    }
    ```

    b. Element selector

    Memilih elemen yang spesifik. Untuk bisa memilih sebuah elemen, kita perlu menuliskan nama elemen. Contohnya seperti berikut.

    ```
    p {
    text-align: center;
    color: red;
    }
    ```

    c. ID selector

    Memilih atribut ID yang spesifik dari sebuah elemen. Biasanya ID dinyatakan secara eksplisit menggunakan kode 'id="..."'. Untuk bisa memilih sebuah ID, kita perlu meletakkan '#' di depannya.

    ```
    contohnya kita memiliki sebuah elemen dengan id="firstname", maka:

    #firstname {
    text-align: center;
    color: red;
    }
    ```

    d. Class selector

    Memilih kelas yang spesifik. Biasanya kelas dinyatakan secara eksplisit menggunakan kode 'class="..."'. Untuk bisa memilih sebuah kelas, kita perlu meletakkan titik di depannya. Bisa juga digunakan untuk menyatakan kelas yang spesifik bagi sebuah elemen. Contohnya sebagai berikut.

    ```
    p.center {
        text-align: center;
        color: red;
    }
    ```

    e. Pseudo-class selector

   Mendefinisikan keadaan khusus suatu elemen. Contohnya adalah saat elemen tersebut dikunjungi, atau di-hover mengugnakan mouse. Sintaksnya adalah sebagai berikut.

   ```
    p:hover {
        color: grey;
        font-variant: small-caps;
    }

   ```

    f. Pseudo-element selector

    Mendefinisikan bagian tertentu dari suatu elemen. Contohnya untuk styling huruf pertama atau baris pertama dari sebuah elemen. Sintaksnya adalah sebagai berikut.

    ```
    p::first-line {
        color: #ff0000;
        font-variant: small-caps;
    }

```

    e. Grouping selector

    Digunakan saat semua element yang ingin diubah memiliki style yang sama.

    Contoh:

    ```
    h1 {
        text-align: center;
        color: red;
    }

    h2 {
        text-align: center;
        color: red;
    }

    p {
        text-align: center;
        color: red;
    }
    ```
    Karena setiap elements memiliki style yang sama, kode tersebut dapat diubah menjadi sebagai berikut.
        
    ```
    h1, h2, p {
        text-align: center;
        color: red;
    }
    ```


- [X] Jelaskan HTML5 Tag yang kamu ketahui.

    | HTML5 Tag | Kegunaan | 
    | :-----------: | :---------: |
    | !--...-- | Mendefinisikan sebuah komentar. |
    | !DOCTYPE | Mendefinisikan jenis dokumen HTML yang digunakan. |
    | html | Menandai root dari keseluruhan dokumen HTML. |
    | head | Berisi informasi terkait dokumen HTML, seperti metadata dan tautan ke stylesheet. |
    | title | Menentukan judul dokumen yang akan ditampilkan di tab browser. |
    | body | Menandai badan dokumen, merupakan area utama dokumen yang berisi konten yang ditampilkan kepada pengguna. |
    | h1 - h6 | Menandai heading pada HTML, diurutkan berdasarkan tingkat kepentingan. Semakin kecil, semakin besar ukuran font header |
    | p | Menandai paragraf dalam dokumen. |
    | a | Membuat hyperlink. |
    | b | Membuat tulisan cetak tebal. |
    | i | Meletakkan icon atau membuat tulisan bercetak miring. |
    | img | Menampilkan gambar dalam dokumen HTML. |
    | button | Membuat tombol yang dapat di-klik oleh pengguna. |
    | div | Menandai sebagian dokumen yang dapat digunakan untuk mengelompokkan dan mengatur elemen-elemen HTML. |
    | input | Mendefinisikan sebuah input. |
    | label | Mendefinisikan sebuah label bagi elemen input. |
    | form | Mendefinisikan sebuah HTML form bagi user input. |

- [X] Jelaskan perbedaan antara margin dan padding.

    | Margin | Padding | 
    | :-----------: | :---------: |
    | Margin merupakan ruang di luar batas elemen | Padding adalah ruang di dalam batas elemen |
    | Margin berguna untuk mengatur jarak antar elemen | Padding berguna untuk menambah ruang internal sebuah elemen
    | Margin tidak meliputi background dan background color | Padding memisahkan konten dari batas |
    | Margin memisahkan blok dari blok yang berdekatan | Padding meliputi gambar dan warna background yang diterapkan di sekitar content  |

- [X] Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

    | Bootstrap | Tailwind |
    | :-----------: | :---------: |
    | Kerangka kerja berbasis komponen ditambah kelas utilitas | Kerangka kerja CSS yang mengutamakan utilitas |
    | Kelas yang telah ditentukan sebelumnya untuk setiap komponen | Semua styles ditentukan di utility class | 
    | Bootstrap memiliki komponen bawaan yang mempercepat pengembangan Anda dan memberi Anda elemen desain yang dapat diulang dan responsif dengan cepat dan mudah | Tailwind CSS tidak komponen bawaan, tapi menawarkan kit UI tambahan yang berbayar yang disebut TailwindUI |

    Persamaan dari keduanya adalah mereka telah memiliki responsive styles. Jadi, kapan kita sebaiknya menggunakan Bootstrap dan kapan kita perlu menggunakan Tailwind?

    Kita bisa menggunakan Bootstrap disaat kita ingin menggunakan komponen CSS bawaan yang disediakan, sehingga kita bisa meminimalisasi effort dalam men-design. Sebaliknya, Tailwind akan lebih baik digunakan disaat kita ingin mementingkan design dari website. Jika kita ingin membuat sebuah website yang unik, Tailwind bisa digunakan.


</details>