# Tugas 4 Pemrograman Berbasis Platform
**Nama    : Adrasa Cantya Salaka**

**NPM     : 2206829603**

**Kelas   : E**

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
