* Tugas 3 *

1. Apa perbedaan antara form POST dan form GET dalam Django?
a. POST akan mengirimkan data atau nilai langsung ke action untuk ditampung, tanpa menampilkan pada url. Method POST cocok untuk data-data yang bersifat private, seperti username dan password. Sedangkan GET akan menampilkan data atau nilai pada url, kemudian akan ditampung oleh action.
b. POST digunakan untuk form yang bertujuan untuk menambah data atau sebuah proses yang akan mengubah database. Sedangkan GET berfungsi untuk menampilkan data dari database.
c. POST menggunakan variable $_POST untuk menampung data atau nilai. Sedangkan GET menggunakan variable $_GET untuk menampung data atau nilai.
d. Data yang dikirim oleh POST tidak terbatas. Sedangkan pada GET, data tidak boleh lebih dari 2047 karakter.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
- XML adalah bahasa markup yang menyimpan data dalam elemen yang terstruktur dan mudah dibaca oleh manusia dan mesin, tetapi kurang efisien dan lebih sulit diurai daripada JSON.
- JSON adalah bahasa meta yang menyimpan data dalam objek JavaScript yang efisien dan ringan, tetapi tidak rapi untuk dilihat. JSON mendukung semua browser dan framework JavaScript, serta sebagian besar teknologi backend.
- HTML adalah bahasa markup yang menyajikan data dalam halaman web dengan menggunakan tag dan atribut. HTML tidak memisahkan data dari presentasi, sehingga tidak cocok untuk pertukaran data antar aplikasi.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
: JSON lebih sering digunakan dalam pertukaran data antara aplikasi web modern karena file JSON mudah dibaca dan lebih cepat untuk parsing data. Selain itu, JSON memiliki struktur data yang sederhana, mudah dipahami, dan tidak terpengaruh oleh platform. JSON mudah diterjemahkan oleh komputer dan berfungsi baik dalam komunikasi antara server dan klien dalam aplikasi web. JSON juga digunakan sebagai format penyimpanan data sederhana.

---STEP-BY-STEP---

1. Membuat input form untuk menambahkan objek model pada app sebelumnya.
a. Saya membuat Skeleton yang berfungsi sebagai kerangka views situs website saya. Pada root folder saya membuat templates > base.html. Berkas base.html ini berperan sebagai template dasar atau kerangka umum untuk halaman web lainnya dalam proyek saya. Lalu, saya menghubungkan folder yang berisi base.html di settings.py agar template ini terdeteksi. Terakhir, saya mengubah secara total isi main.html saya dengan menggunakan base.html sebagai main template.
b. Pada step ini, saya akan membuat form untuk menginput data commision literature pada aplikasi writer’s archive saya untuk user yang ingin request essay tentang genre fiksi apapun. Data komisi baru akan diterima di main > forms.py. Model yang saya gunakan adalah Item— sehingga ketika data dari form disimpan, form berisi objek Item. Fields saya berisi nama/ judul komisi, jumlah komisi (1 jika berupa standalone), deskripsi komisi, jumlah kata per/komisi, genre komisi, dan asal karakter dalam komisi tersebut.
c. Pada views.py, saya membuat fungsi baru create_item yang menerima request dari user untuk menghasilkan formulir yang dapat menambahkan data komisi ketika form di submit. Variabel form membuat ProductForm baru dengan memasukkan QueryDict berdasarkan request user. Setelah request di validasi, data dari form akan disimpan dan komisi di redirect.
d. Pada fungsi show_main, fungsi Item.objects.all() akan mengambil objek-objek Item yang tersimpan di database. Hal yang tak kalah penting untuk dilakukan, adalah mengimpor fungsi create_item tadi di main > urls.py dan menambahkan path url ke dalam variabel urlpatterns, dua hal ini penting agar halaman form dapat diakses dan terkoneksi dengan halaman utama web saya.
e. Pada main > templates, saya membuat berkas create_item.html yang akan menampilkan fields form sebagai tabel, dan mengirimkan request ke View. Pada main.html, data komisi akan ditampilkan dalam bentuk tabel serta tombol “Request Commision” yang akan redirect user ke halaman form.

2. Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
[Poin-poin berikut untuk menjawab kedua nomor, nomor (2) dan nomor (3)]
a. Fungsi views dalam format HTML telah ditambahkan pada poin pertama saya dalam fungsi create_item.
b. Selanjutnya, fungsi views XML akan menerima request dengan nama show_xml yang akan menyimpan hasil query dari seluruh data komisi yang ada pada Item. Fungsi ini akan mengembalikan HttpResponse yang berisi data hasil query yang sudah di-convert menjadi format XML dan tipe konten berupa application/xml. Tidak lupa saya untuk mengimpor fungsi show_xml pada urls.py dan menambah pathnya pada urlpatterns agar dapat diakses.
c. Fungsi views JSON akan menerima request dengan nama show_json yang akan menyimpan hasil query dari seluruh data komisi yang ada pada Item. Fungsi ini akan mengembalikan HttpResponse yang berisi data hasil query yang sudah di-convert menjadi format XML dan tipe konten berupa application/json. Tidak lupa saya untuk mengimpor fungsi show_json pada urls.py dan menambah pathnya pada urlpatterns agar dapat diakses.
d. 2 fungsi views XML dan JSON berdasarkan id akan menerima request dan id (urutan data komisi masuk) dengan nama show_xml_by_id dan show_json_by_id yang akan menyimpan hasil query dari seluruh data komisi yang ada pada Item. Fungsi ini akan mengembalikan HttpResponse yang berisi data hasil query yang sudah di-convert menjadi format XML dan tipe konten berupa application/xml, dan format JSON dan tipe konten berupa application/json. Tidak lupa saya untuk melakukan routing dengan mengimpor kedua fungsi show_xml_by_id dan show_json_by_id pada urls.py dan menambah pathnya pada urlpatterns agar dapat diakses.

***Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman.
![Screenshot (48)](https://github.com/nadyaaysha/archive_of_ours/assets/124881541/84e39417-7b53-4e88-9f54-80fff13b0648)
![Screenshot (47)](https://github.com/nadyaaysha/archive_of_ours/assets/124881541/59a48754-94c2-46e5-8b88-3829d9ba3dcd)
![Screenshot (49)](https://github.com/nadyaaysha/archive_of_ours/assets/124881541/57f4dc0c-66d7-4f22-8354-21cc4b8cf749)
![Screenshot (50)](https://github.com/nadyaaysha/archive_of_ours/assets/124881541/174e4bcd-947d-480d-b74a-88ea37da0936)
![Screenshot (51)](https://github.com/nadyaaysha/archive_of_ours/assets/124881541/4dd3a21d-b2ef-4df0-8085-fdd0740cd4b3)

***

* Tugas 2 *

Link to AoO => https://archiveofours.adaptable.app/main

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    a. Membuat sebuah proyek Django baru.
      : Pertama-tama, saya membuat direktori utama ‘archive_of_ours’ dan mengaktifkan Virtual Environment di dalamnya. Lalu, saya menambahkan beberapa dependencies di berkas requirements.txt dan memasangnya sebelum membuat proyek Django dengan nama yang sama dengan direktori utama saya. Setelah proyek saya konfigurasi, saya kemudian mengunggah proyek ke Repositori GH yang public.
    b. Membuat aplikasi dengan nama main pada proyek tersebut.
      : Karena saya belum mematikan VE, saya lanjut ke tahap berikutnya yakni membuat aplikasi ‘main’ dalam proyek ‘archive_of_ours’ dan mendaftarkannya ke berkas settings.py. Di dalam direktori proyek ‘main’ saya membuat subdirektori lagi ‘templates’ yang memuat berkas main.html, tujuan dari step ini hanya sekedar untuk checking tampilan dasar HTML kita, belum terhubung django.
    c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
      : Untuk menjalankan aplikasi web dengan pola MVT, pertama, kita harus mendefinisikan pola URL untuk setiap tampilan atau fitur dalam aplikasi milik kita, yang kemudian akan dihubungkan dengan tampilan yang sesuai untuk mengelola logika bisnis. Kemudian, tampilan tersebut harus diimplementasikan untuk mengambil data dari model dan merender tampilan menggunakan template HTML. Akhirnya, kita perlu mengaktifkan sistem routing agar dapat menentukan tampilan yang harus dijalankan berdasarkan URL yang diakses oleh pengguna.
    d. Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
    - name sebagai nama item dengan tipe CharField.
    - amount sebagai jumlah item dengan tipe IntegerField.
    - description sebagai deskripsi item dengan tipe TextField.
      : Saya membuat main class untuk mendefinisikan model saya yang bernama Item, class ini memiliki tiga atribut yakni name (CharField), amount (atau di aplikasi saya menunjukkan word count dari literatur saya) yang bertipe Integer, serta description (TextField). Setelah itu saya memigrasi model saya ke basis data.
    e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
      : Pertama, kita perlu mendefinisikan fungsi di dalam file `views.py`, di mana akan dingambil data yang diperlukan. Setelah itu, saya mengatur data tersebut dalam konteks (context) yang akan digunakan dalam template HTML. Selanjutnya, saya membuat atau memodifikasi template HTML. Terakhir, tinggal menambahkan URL pattern di file `urls.py` agar user dapat mengakses halaman tersebut melalui URL tertentu.
    f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
      : Untuk membuat routing pada `urls.py` dalam aplikasi 'main' yang memetakan fungsi `views.py`, saya akan menentukan URL pattern yang sesuai. Saya menambahkan entri URL pattern ke dalam file `urls.py`. Saya misalkan dengan fungsi bernama `show_main` di `views.py` yang ingin dihubungkan dengan URL '/main/'. Dengan ini, ketika user mengakses URL 'http://alamat-website-saya/main/', fungsi `show_main` dalam `views.py` akan dipanggil, dan data yang dihasilkan oleh fungsi tersebut akan ditampilkan melalui template HTML yang sesuai.
    g. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
      : Ketika kita add, commit, dan push Repositori kita, maka Adaptable akan otomatis men-deploy ulang berdasarkan commit terbaru. Dengan ini, website saya akan dapat diakses melalui domain website saya.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![ALIN - MindMap SPL - Frame 1](https://github.com/nadyaaysha/archive_of_ours/assets/124881541/80dde040-8560-4814-9c6d-aa6ce3963746)

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
   : Kita menggunakan virtual environment untuk membuat lingkungan Python yang terisolasi dari instalasi Python yang ada. Hal ini berguna untuk menghindari konflik antara paket yang berbeda atau versi Python. Django adalah framework web yang membutuhkan paket tertentu untuk berfungsi. Jika kita tidak menggunakan virtual environment, kita mungkin mengalami masalah compatibility atau dependencies. Oleh karena itu, disarankan untuk menggunakan virtual environment saat membuat aplikasi web berbasis Django.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
   : MVC, MVT, dan MVVM adalah pola arsitektur yang digunakan untuk memisahkan antara logika bisnis, tampilan, dan data dalam sebuah aplikasi. Perbedaan dari ketiganya adalah sebagai berikut:
      a. MVC (Model-View-Controller) menggunakan Controller sebagai penghubung antara Model (data) dan View (tampilan). Controller bertanggung jawab untuk mengatur alur aplikasi dan mengirimkan data dari Model ke View.
      b. MVT (Model-View-Template) menggunakan Template sebagai penghubung antara Model (data) dan View (tampilan). Template adalah file HTML yang berisi tag khusus untuk menampilkan data dari Model. MVT biasanya digunakan dalam framework web seperti Django.
      c. MVVM (Model-View-ViewModel) menggunakan ViewModel sebagai penghubung antara Model (data) dan View (tampilan). ViewModel adalah objek yang menyimpan data dari Model dan menyediakan fungsi untuk mengubah atau memperbaiki data tersebut. ViewModel juga dapat berkomunikasi dengan View melalui mekanisme seperti binding atau observables.
