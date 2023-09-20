# Tugas 3 Pemrograman Berbasis Platform
**Nama    : Adrasa Cantya Salaka**

**NPM     : 2206829603**

**Kelas   : E**

1. Apa perbedaan antara form POST dan form GET dalam Django?

   POST dan GET adalah satu-satunya metode HTTP yang digunakan saat menangani formulir. Akan tetapi, keduanya memiliki fungsi yang berbeda. Tabel di bawah ini menjelaskan perbedaan POST dan GET dalam Django. Berikut adalah [sumber](https://docs.djangoproject.com/en/4.2/topics/forms/#:~:text=GET%20and%20POST%20are%20typically,the%20state%20of%20the%20system) yang saya gunakan.
   
| POST | GET | 
| :-----------: | :---------: |
| POST digunakan saat ada permintaan untuk mengubah keadaan sistem | GET hanya boleh digunakan untuk permintaan yang tidak mempengaruhi keadaan sistem | 
| Formulir masuk Django dikembalikan menggunakan metode POST | GET menggabungkan data yang dikirimkan ke dalam string, dan menggunakannya untuk membuat URL | 
| Lebih aman, dapat digunakan untuk admin form dan menulis password | Lebih tidak aman, seluruh tulisan akan ditampilkan pada URL | 


2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

   [Sumber 1](https://www.deltaxml.com/blog/xml/whats-the-relationship-between-xml-json-html-and-the-internet/#:~:text=The%20differences%20between%20XML%2C%20JSON,how%20that%20data%20is%20displayed.), [Sumber 2](https://www.dicoding.com/blog/apa-itu-json/) & [Sumber 3](https://aws.amazon.com/id/compare/the-difference-between-json-xml/)
   
| XML (eXtensible Markup Language) | JSON (JavaScript Object Notation) | HTML (HyperText Markup Language) |
| :-----------: | :---------: | :----------: |
| XML memiliki data yang lebih terstruktur dan pengguna dapat menggunakannya untuk menambahkan catatan | JSON digunakan untuk mengirimkan data dengan cara data diuraikan dan dikirimkan melalui internet | HTML adalah bahasa markup yang digunakan untuk membuat dan menampilkan halaman web |
| XML merepresentasikan data dengan membentuk struktur seperti tree yang dimulai dari root, lalu branch, hingga berakhir pada leaves | JSON menggunakan pasangan kunci-nilai | HTML menggunakan tag untuk mendefinisikan elemen-elemen struktural di dalam halaman web |

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

   Karena format pertukaran datanya sangat ringan serta lebih mudah dibaca dan ditulis oleh manusia, sehingga mudah untuk diterjemahkan dan dibuat (generate) oleh komputer.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   
     - [x]  Membuat input form untuk menambahkan objek model pada app sebelumnya.
  
   Yang pertama harus dilakukan adalah membuat file di direktori `main` dengan nama `forms.py` lalu menambahkan Product dari models.py supaya isi dari form akan disimpan menjadi objek Product dengan meminta fields yang sesuai pada `models.py`. Untuk membuat sebuah input form pada aplikasi Django, kita perlu menggunakan `from django.forms import ModelForm` yang telah didesain khusus untuk mengubah model menjadi Django form. Berikut adalah barisan kode yang saya gunakan.
   
   ```
   from django.forms import ModelForm
   from main.models import Product

   class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "amount", "description"]
   ```
   `fields` sebaiknya dinyatakan secara eksplisit agar pengguna dapat menggunakan input forms tersebut dengan baik dan menghindari adanya kesalahan input. Value `__all__` dapat digunakan untuk menyatakan bahwa semua field pada model dapat digunakan.

   Setelah itu, saya perlu meng-import beberapa fungsi di dalam `views.py` di direktori main, menambahkan fungsi `create_product` dan mengubah fungsi `show_main`.

   ```
   from django.http import HttpResponseRedirect
   from main.forms import ProductForm
   from django.urls import reverse

   def show_main(request):
    products = Product.objects.all()
    count_products = Product.objects.count()
    context = {
        'app_name': 'Inventory App', 
        'name': 'Adrasa Cantya Salaka',
        'class': 'PBP E',
        'products': products,
        'count_products': count_products,
    }

    return render(request, "main.html", context)

   def create_product(request):
   form = ProductForm(request.POST or None)
   if form.is_valid() and request.method == "POST":
      form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
   
   context = {'form': form}
   return render(request, "create_product.html", context)
   ```

     - [x] Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

   a. HTML
      Agar bisa menampilkan objek yang sudah ditambahkan dalm format HTML, saya perlu membuat sebuah template dasar bernama `base.html` di dalam sebuah folder yang berada di root folder dengan nama `templates`. Isi dari `base.html` adalah sebagai berikut.

   ```
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
   </html>
   ```

   Kemudian, saya perlu mengubah file `settings.py` yang ada di subdirektori `Inventory_App` dan menambahkan kode `'DIRS': [BASE_DIR / 'templates']` di dalam variabel TEMPLATES. Hal ini perlu dilakukan agar kode pada `base.html` dapat dideteksi sebagai template.

   Tahapan selanjutnya adalah mengubah `main.html` di dalam subdirektori `templates` menjadi barisan kode di bawah.

   ```
   {% extends 'base.html' %}

   {% block content %}
      <h1>Inventory App Page</h1>

       <h5>App Name: </h5>
       <p>{{ app_name }}</p>

       <h5>Name: </h5>
       <p>{{ name }}</p> <!-- Ubahlah sesuai dengan nama kamu -->

       <h5>Class: </h5>
       <p>{{ class }}</p> <!-- Ubahlah sesuai dengan kelas kamu -->

       <p> Selamat datang di Inventory App! Anda telah memasukkan {{count_products}} barang ke dalam aplikasi ini. Selamat berbelanja! </p>
   {% endblock content %}
   ```

   Saya juga perlu membuat sebuah file baru dengan nama `create_product.html` di direktori main/templates. File tersebut diisi dengan kode sebagai berikut.

   ```
   {% extends 'base.html' %} 

   {% block content %}
   <h1>Add New Product</h1>

   <form method="POST"> // menandakan block mana yang digunakan untuk form dengan metode POST
    {% csrf_token %} // menjadi token untuk menjaga keamanan supaya tercegah dari serangan berbahaya
    <table>
        {{ form.as_table }} // menampilkan fields pada form yang sudah dibuat di file forms.py sebagai tabel
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/> // membuat sebuah tombol submit dengan tulisan Add Product untuk    mengirimkan request ke view create_product(request)
            </td>
        </tr>
    </table>
   </form>

   {% endblock %}
   ```
   Di dalam file `main.html`, tambahkan kode di bawah ke dalam `{% block content %}` supaya dapat menampilkan data produk dalam bentuk tabel sekaligus tombol "Add Product" yang akan me-redirect ke halaman form.

   ```
   <table>
            <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>

        {% for product in products %}
            <tr>
                <td>{{product.name}}</td>
                <td>{{product.amount}}</td>
                <td>{{product.description}}</td>
                <td>{{product.date_added}}</td>
            </tr>
        {% endfor %}
    </table>

    <br />

    <a href="{% url 'main:create_product' %}">
        <button>
            Add New Product
        </button>
    </a>
   {% endblock content %}
   ```

   b. XML, JSON, XML by ID, JSON by ID

   Pada file `views.py` yang ada pada folder main, tambahkan import `HttpResponse` dan `Serializer` pada bagian paling atas. `Serializers` digunakan untuk translate objek model menjadi format lain seperti XML dan JSON. Kemudian, membuat fungsi baru seperti pada barisan kode di bawah pada file `views.py` di `main`.

   ```
   from django.http import HttpResponse
   from django.core import serializers

   def show_xml(request):
      data = Product.objects.all()
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

   def show_json(request):
       data = Product.objects.all()
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")

   def show_xml_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

   def show_json_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```

   - [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
     
   a. HTML
   
   Untuk bisa mengakses view HTML, yang perlu kita lakukan cukup mengubah salah satu path yang telah kita tuliskan pada `urlpatterns` di dalam file `urls.py` yaitu `main/` menjadi `' '` sehingga dapat diakses pada Local Host HTML secara langsung, tanpa perlu menambahkan path `main/` di akhir URL.

   b. XML
   
   Menambahkan path baru ke dalam `urlpatterns` dalam file `urls.py` sehingga fungsi yang baru ditambahkan dapat diakses dengan menambahkan `xml/` pada tautan local host kita. Kodenya adalah sebagai berikut `path('xml/', show_xml, name='show_xml'),`

   c. JSON
   
   Menambahkan path baru ke dalam `urlpatterns` dalam file `urls.py` sehingga fungsi yang baru ditambahkan dapat diakses dengan menambahkan `json/` pada tautan local host kita. Kodenya adalah sebagai berikut `path('json/', show_json, name='show_json'),`

   d. XML by ID
   
   Menambahkan path url ke dalam `urlpatterns` menggunakan kode `path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),`.
   
   e. JSON by ID
   
   Menambahkan path url ke dalam `urlpatterns` menggunakan kode `path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),`.
     
5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
   
   a. HTML
   ![HTML](https://github.com/acasalaka/Inventory_App/assets/124960259/65cf14b5-01d0-48e5-bee5-d3b452256f01)

   b. XML
   ![XML](https://github.com/acasalaka/Inventory_App/assets/124960259/e64976ef-ed82-468a-9bb1-c1b9ec12f023)

   c. JSON
   ![JSON](https://github.com/acasalaka/Inventory_App/assets/124960259/ad5f657f-6aa0-414b-8462-f6d2022d517c)

   d. XML by ID (saya menggunakan ID = 3)
   ![XML by ID = 3](https://github.com/acasalaka/Inventory_App/assets/124960259/330b582f-f8f1-4324-b796-2733af1077b4)

   e. JSON by ID (saya menggunakan ID = 3)
   ![JSON by ID = 3](https://github.com/acasalaka/Inventory_App/assets/124960259/11b150b4-852d-476a-b63a-ba1a20812b80)
