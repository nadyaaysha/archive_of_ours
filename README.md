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
