<3 TUGAS 5 <3

1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

a) Tag Selector, adalah selector yang memilih element berdasarkan nama tag, contoh: p {color: red;} akan memilih semua element <p> dan mengubah warna teksnya menjadi merah.

b) Class Selector, adalah selector yang memilih element berdasarkan nama class yang diberikan, contoh: .red {color: white; background: red; padding: 5px;} akan memilih semua elemen yang memiliki class red dan mengubah warnanya menjadi putih, latar belakangnya menjadi merah, dan menambahkan padding sebesar 5 piksel.

c) ID Selector, adalah selector yang memilih element berdasarkan ID, contoh: # header {background: pink; color: white; height: 200px: padding: 25px;} akan memilih element dengan ID header dan mengubah warna latar belakangnya menjadi pink, warna teks menjadi putih, tinggi dan padding masing-masing sebesar 200 dan 25 piksel.

d) Attribute Selector, adalah selector yang memilih element berdasarkan attribute yang dimilikinya, contoh: {border: 2px black;} akan memberikan border sebesar 2 piksel dengan warna hitam pada semua element.

2. Jelaskan HTML5 Tag yang kamu ketahui.
- <main>: Menampilkan konten utama dari halaman web.

- <nav>: Menampilkan navigasi atau menu halaman web.

- <section>: Menampilkan bagian dari halaman web.

- <article>: Menampilkan konten independen yang dapat berdiri sendiri.

- <aside>: Menampilkan konten yang terkait dengan konten lain di sekitarnya.

- <audio>: Menampilkan audio atau suara.

- <embed>: Menampilkan media yang disematkan, seperti video atau animasi.

- <footer>: Menampilkan footer atau bagian bawah halaman web.

- <header>: Menampilkan header atau bagian atas halaman web.

- <canvas>: Menampilkan gambar atau grafik yang dapat diubah secara dinamis.

- <datalist>: Menampilkan daftar opsi untuk elemen input.

- <details>: Menampilkan informasi tambahan yang dapat ditampilkan atau disembunyikan.

3. Jelaskan perbedaan antara margin dan padding.

: Margin adalah jarak antara element HTML dan tepi kotak yang mengelilinginya. Margin menciptakan ruang kosong di luar element, dan tidak mempengaruhi ukuran elemen itu sendiri. Margin dapat diatur menggunakan properti CSS seperti margin-top, margin-bottom, margin-left, dan margin-right. Margin digunakan untuk mengontrol tata letak elemen pada halaman, seperti mengatur jarak antar elemen yang berdekatan. Padding adalah jarak antara content element HTML dan tepi kotak yang mengelilinginya. Padding menciptakan ruang kosong di dalam element, dan dapat memperbesar ukuran elemen itu sendiri. Padding dapat diatur menggunakan properti CSS seperti padding-top, padding-bottom, padding-left, dan padding-right. Padding digunakan untuk menambah ruang internal suatu elemen.

4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

![image](https://github.com/nadyaaysha/archive_of_ours/assets/124881541/2f0a76ca-bf65-414a-98b8-573a20921098)

: Pilihan antara TailWind dan BootStrap sebetulnya balik lagi ke kebutuhan developer. Jika developer ingin membuat situs web yang responsif dan cepat, maka BootStrap adalah pilihan terbaik karena komponen responsif berbasis mobile yang telah didesain sebelumnya untuk merancang halaman website yang fast-response. Namun, jika developer memiliki ide kreativitas yang tinggi dan ingin memegang kontrol penuh atas gaya dan tata letak dalam web-nya, maka TailWind menjadi pilihan terbaik karena fleksibilitas desainnya yang lebih luas.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

>>> Kustomisasi desain pada template HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut

# Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.

a. Dalam block <style> saya menambahkan attribute body dan .login yang akan saya gunakan untuk kostumisasi halaman login saya. Di dalam kurung kurawal body, display akan saya set menjadi flex, pengaturan content dan aligning akan berada di tengah, tinggi dari keseluruhan content adalah 100vh, margin akan saya set juga menjadi 0 agar seluruh content berada di tengah, serta warna background menjadi ungu untuk login page dan merah muda untuk register page.

b. Di dalam kurung kurawal .login disinilah saya akan menampung isi content utama dari login ke dalam suatu box. Display akan saya set menjadi flex, arah flex akan saya atur berdasarkan kolom, pengaturan content dan aligning akan berada di tengah, padding sebesar 20 piksel, warna box menjadi ungu muda untuk login page dan merah yang lebih muda untuk register page, radius border sebesar 10 piksel, bayangan box menjadi hitam dan besarnya 10 piksel, serta tinggi dan lebar box masing-masing sebesar 350 dan 450 piksel.

# Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan approach lain seperti menggunakan Card.

a. Dalam block <style>, saya atur body, html nya sedemikian rupa sehingga memiliki margin dan padding masing-masing 0.

b.Lalu, dalam kurung kurawal .custom-table, saya atur lebar tabelnya memenuhi layar, yakni 100 persen, serta border-collapsenya menjadi collapse.

c. Dalam .custom-table, saya akan atur headernya sehingga textnya berada di tengah, background colornya kuning, padding 10 piksel, serta border 1 piksel.

d. Untuk isi inventory atau komisi essay maupun fiksi dari user, isi content akan saya align di center dan padding sebesar 10 piksel, serta border sebesar 1 piksel.

# [BONUS] Memberikan warna yang berbeda (teks atau background) pada baris terakhir dari item pada inventory anda menggunakan CSS.

: Untuk menunjukkan recent commision user, saya akan kostumisasi item terakhir yang user komisi agar memiliki warna background yang berbeda, yakni warna kuning muda, teksnya juga saya italics agar berbeda dengan komisi user yang lain.
=========================================================================================================================================================================================
—Tugas 4—

1.] Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
: Django UserCreationForm adalah suatu form yang membuat user baru, tanpa privilege, dari username dan password yang diberikan. Pada Django UserCreationForm terdapat 3 fields: username, password1, dan password2 (yang digunakan sebagai konfirmasi password). Django UserCreationForm dapat diimport dari django.contrib.auth.forms.
    Beberapa kelebihan dari Django UserCreationForm adalah:
- Mudah digunakan, Django UserCreationForm sudah disediakan oleh Django Authentication Framework dan sehingga seorang pelajar pemula seperti saya tidak perlu membuat form sendiri.
- Terjamin aman, Django UserCreationForm terjamin aman karena menggunakan validasi dan enkripsi untuk password user.
- Fleksibel, Django UserCreationForm bisa dimodifikasi sesuai kebutuhan melalui subclass dan merubah atribut Meta class-nya.

	Beberapa kekurangan dari Django UserCreationForm adalah:
- Form ini hanya meminta username dan password saja, user tidak diminta untuk mencantumkan nama panjang ataupun e-mail. Sehingga data yang ditampung cenderung kurang lengkap.
- Form ini tidak mendukung custom user model, sehingga untuk para developers yang mungkin membuat custom user model sendiri, maka hanya bisa mengandalkan user model yang sudah ada saja.
- Form ini menampilkan informasi tambahan mengenai password yang mungkin terkesan ribet dan eksesif.

2.] Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
: Autentikasi adalah proses mengidentifikasi user atau pengguna secara
aman. Autentikasi akan mencoba untuk mengidentifikasi identitas user dan
memutuskan apakah user tersebut sebenarnya adalah orang yang dia wakili.
Sedangkan otorisasi adalah, proses menentukan tingkat akses atau privilege
yang dapat diakses oleh user yang telah di-autentikasi. Di sebagian besar
sistem berbasis host dan client-server, kedua mekanisme ini
diimplementasikan menggunakan sistem perangkat keras atau sistem
perangkat lunak yang sama. Skema otorisasi bergantung pada autentikasi
untuk memastikan identitas user yang masuk ke sistem dan mendapatkan
akses ke sumber daya. Kedua skema ini penting untuk menjaga keamanan
dan privasi data pada aplikasi web.

3.] Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
: Cookies adalah file teks yang berisi data unik tentang aktivitas user saat mengunjungi suatu website. Cookie dibuat oleh web server dan dikirim ke browser user, yang kemudian mengirimkannya kembali ke web server setiap kali user mengakses website tersebut. Cookie digunakan untuk menyimpan informasi login, preferensi user, dan lain-lain. Cookie juga dapat membantu server menyiapkan halaman web yang disesuaikan dengan pengguna. Django menggunakan cookies untuk menyimpan ID sesi di sisi client dan menyimpan data sesi di sisi server. ID sesi hanya terlihat oleh user, sedangkan data sesi tetap tersembunyi di server.

4.] Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada resiko potensial yang harus diwaspadai?
: Cookies sebetulnya tidak dianggap sebagai ancaman untuk privasi dan keamanan website, karena tidak menyimpan data pribadi (kecuali jika user menyimpan nomor kartu kredit dan alamat IP) dan tidak bisa digunakan untuk mengirim virus. Namun, ada pula risiko cookies dapat disusupi oleh pihak yang tidak bertanggung jawab, menyebabkan kebocoran informasi yang sensitif. Cookies juga dapat menurunkan performa perangkat jika terlalu banyak disimpan. Untuk mengurangi risiko tersebut, kita dapat menghapus cookie secara berkala atau membatasi izin cookie pada browser kita.

5.] Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step,

a.) Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
-> Saya mengimpor redirect, UserCreationForm, dan messages agar dapat membuat halaman register untuk aplikasi web saya. Lalu, saya membuat fungsi register yang menerima parameter request dan menghasilkan form registrasi untuk dapat membuat akun user ketika data di-submit dari form. Variabel form akan membuat UserCreationForm baru dengan memasukkan QueryDict berdasarkan masukan dari user, lalu akan dicek validitas isi masukan dari form, jika valid maka data tersebut akan disimpan dari form. Sebuah pesan pop-up akan muncul jika data berhasil disimpan dan user akan di redirect kembali ke halaman utama.

-> Saya membuat berkas register.html dengan nama yang sama dengan fungsi yang telah saya buat sebelumnya, berkas ini berisi template yang akan menampilkan halaman form registrasi untuk user. Lalu, saya melakukan routing agar halaman ini dapat diakses dengan mengimpor fungsi sebelumnya di urls.py dan menambah path url ke urlpatterns.

-> Sebelum saya membuat fungsi dan berkas login, saya perlu mengimpor authenticate dan login agar dapat membuat halaman login dan meng-autentikasi user. Saya membuat fungsi login_user yang menerima parameter request dan akan digunakan untuk melakukan autentikasi user berdasarkan username dan password yang diberikan dari request saat pengguna login. Lalu, saya membuat berkas login.html yang akan menampilkan halaman login di browser pengguna. Terakhir, saya melakukan routing agar halaman dapat diakses dengan mengimpor fungsi yang telah dibuat sebelumnya di urls.py dan menambahkan pathnya ke urlpatterns.

-> Fungsi terakhir yang akan dibuat adalah fungsi logout setelah mengimpor logout di views.py. Fungsi logout_user menerima parameter request yang akan menghapus sesi user yang sedang masuk dan mengarahkan user ke halaman login di website saya. Pada berkas main.html, saya akan menambahkan tombol logout agar user dapat keluar dari akunnya dengan mudah. Jangan lupa saya untuk melakukan routing fungsi logout_user dengan mengimpornya di urls.py dan menambahkan pathnya di urlpatterns.

b.) Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

![InShot_20230925_092545481](https://github.com/nadyaaysha/archive_of_ours/assets/124881541/ddb5f3f4-525d-4995-bf6e-5546503477fb)

c.) Menghubungkan model Item dengan User.
-> Pertama-tama, kita mengimpor User pada models.py dan menambahkan variabel user di dalam class Item yang akan menghubungkan satu Item dengan satu user melalui suatu hubungan, dimana sebuah item pasti diasosiasikan dengan satu user.

-> Pada fungsi create_item, di dalam kondisi “if”, parameter commit yang disetting menjadi false berguna untuk mencegah Django dari menyimpan objek yang telah dibuat dari form langsung ke database. Hal ini kita manfaatkan untuk memodifikasi objek tersebut sebelum disimpan ke database. Field user diisi dengan objek User dari return value request.user yang terotorisasi untuk memberitahu bahwa objek tersebut dimiliki oleh user yang sedang login.

-> Pada fungsi show_main, saya mengganti value dari ‘name’ menjadi request.user.username agar username user yang sedang login saat ini akan ditampilkan di halaman main. Lalu di dalam parameter Item.objects.filter saya menaruh parameter user = request.user agar data yang ditampilkan hanya data yang diasosiasikan dengan user yang sedang login.
Setelah menyimpan seluruh perubahan, saya melakukan migrasi model.

d.) Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

![image](https://github.com/nadyaaysha/archive_of_ours/assets/124881541/d85c9a9d-b7ad-41ea-a137-f2d30ac4e9bf)
![image](https://github.com/nadyaaysha/archive_of_ours/assets/124881541/7d87e0e7-699f-437e-86f6-e209f4582957)

-> Pertama, saya mengimpor hal-hal yang diperlukan seperti datetime, HttpResponseRedirect, dan reverse. Lalu, pada fungsi login_user yang telah saya buat sebelumnya, saya menambahkan cookie last_login yang akan memperlihatkan kapan terakhir kali user melakukan login. User akan login terlebih dahulu, lalu kita akan menerima respons yang berupa cookie last_login. Pada variabel context, kita juga akan menambahkan informasi cookie last_login yang akan ditampilkan di halaman web.

-> Terakhir, pada fungsi logout_user, saya akan menambahkan method response yang akan menghapus cookie last_login ketika user melakukan logout dari halaman web. Tidak lupa pada berkas main.html saya menambahkan detail sesi terakhir login agar user dapat melihat kapan ia terakhir login di web.

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
![Screenshot (45)](https://github.com/nadyaaysha/archive_of_ours/assets/124881541/7dd8068b-1127-45e5-b02f-0730c256cb5c)
![Screenshot (46)](https://github.com/nadyaaysha/archive_of_ours/assets/124881541/12a7fe9f-0ac6-4b3e-bf7a-cdb9edfc8cf2)
![Screenshot (47)](https://github.com/nadyaaysha/archive_of_ours/assets/124881541/2846fb56-367f-45c6-9378-af494eac1630)
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
