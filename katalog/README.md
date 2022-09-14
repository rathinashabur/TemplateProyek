# Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
JAWAB: 
![Bagan_Tugas2](/Bagan_Tugas2.jpg)

# Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
JAWAB: 
Jika kita membuat banyak aplikasi pada satu sistem operasi yang sama, virtual environment berguna agar setiap aplikasi tersebut memiliki modul dan ruang atau lingkupnya sendiri serta tidak dapat diakses dari luar. Virtual environment memungkinkan pengguna untuk menggunakan versi yang berbeda untuk proyek aplikasi yang berbeda dalam satu sistem operasi. Adanya virtual environment juga memudahkan kita untuk mengerjakan aplikasi yang misalnya awalnya kita kerjakan pada laptop untuk dapat lanjut kita kerjakan pada PC meskipun versi dari PC tersebut berbeda dari versi yang di laptop.

Kita masih bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi akan terjadi masalah ketika kita melakukan pembaruan versi sedangkan aplikasi web yang kita buat menggunakan versi lama. Aplikasi tersebut menjadi tidak bisa dijalankan dengan versi baru karena terdapat perubahan-perubahan yang diakibatkan oleh pembaruan. Maka dari itu, diperlukan virtual environment agar aplikasi yang kita buat dapat dijalankan dengan versi apapun.

Referensi: https://www.petanikode.com/python-virtualenv/

# Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
JAWAB:
Berikut adalah hal-hal yang saya lakukan untuk mengimplementasikan poin 1 sampai 4:
1. Membuat direktori yang dibutuhkan dan melakukan cloning repository template. Lalu mempersiapkan migrasi skema model dan menerapkan skema model ke database Django lokal.
2. Melakukan load data initial_catalog_data_.json
3. Membuat fungsi pada views.py dari folder “katalog” yang menerima parameter request dan mengembalikan return render(request, “katalog.html”)
4. Melakukan routing terhadap fungsi views pada urls.py dari folder “katalog” dengan meng-import show_katalog dan menambahkan include dan path agar halaman HTML dapat ditampilkan pada browser.
5. Mendaftarkan aplikasi katalog pada urls.py folder “project_django” dengan menambahkan path(‘katalog/’, include(‘katalog.urls’)), pada variabel urlpatterns.
6. Melakukan import CatalogItem dari katalog.models pada berkas views.py agar class tersebut dapat digunakan untuk mengambil data dari database. Lalu, saya memanggil fungsi query ke model database dan menyimpan hasil query ke dalam suatu variabel dengan menambahkan beberapa potongan kode pada fungsi show_katalog views.py folder “template”.
7. Menambahkan context pada kode return sehingga menjadi return render(request, “katalog.html”, context) supaya Django dapat me-render data pada variabel context juga yang telah dibuat pada langkah sebelumnya agar dapat ditampilkan pada halaman HTML.
8. Agar dapat menampilkan data-data yang telah di-render pada halaman HTML, akan dilakukan pemetaan. Saya mengubah Fill me! yang ada di dalam HTML tag <p> dengan nama dan juga NPM saya. Lalu, agar informasi katalog dapat ditampilkan, saya melakukan iterasi pada item_katalog dan memanggil data objek-objek pada item_katalog dengan variabel-variabelnya yang sesuai seperti pada models.py.
9. Untuk melakukan deploy,pada konfigurasi repositori GitHub saya, saya menambahkan variabel repository secret baru dengan pasangan Nama-Value yang telah saya dapatkan dari API Key lalu saya simpan variabel-variabel tersebut dan menjalankan kembali workflow yang gagal.
10. Selanjutnya, saya melakukan add, commit, dan push ke heroku.
