# https://nashatugaspbp.herokuapp.com/todolist/

# 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Asynchronous programming program-programnya dapat berjalan secara bersamaan dalam satu waktu tanpa harus menunggu program lainnya untuk selesai dieksekusi, maka dari itu user tidak perlu menunggu jika sedang terjadi suatu event dan selalu bisa berinteraksi dengan halaman web ambil menunggu respon dari server. 
Synchronous programming program-programnya berjalan secara sequential sehingga berjalannya suatu program bergantung kepada program lainnya (harus menunggu program lain selesai dieksekusi terlebih dahulu sesuai antrian eksekusi program), maka dari itu user harus selalu menunggu jika sedang terjadi suatu event.

Referensi: https://community.algostudio.net/memahami-synchronous-dan-asynchronous-dalam-pemrograman/

# 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Paradigma event-driven programming adalah suatu paradigma pemrograman di mana event-event yang terjadi menentukan alur dari suatu program. Event ini dapat dapat dipicu oleh penekanan tombol, keyboard, timer, dan lain-lain. 
Pada tugas ini, event-driven programming ini diterapkan ketika user ingin menambahkan task baru. Kita baru akan dapat mengisi form untuk menambahkan task baru setelah kita mengklik tombol untuk menambahkan task baru dan task tersebut baru akan terdaftar ketika kita memencet tombol untuk menyimpan task baru tersebut.

Referensi: http://www.myspsolution.com/news-events/solace-event-driven/

# 3. Jelaskan penerapan asynchronous programming pada AJAX.
Pada ajax, kita dapat melakukan POST dan GET pada suatu halaman html. Asynchronous programming pada AJAX memungkinkan halaman menampilkan data yang baru ditambahkan dengan POST dan mengambil data dengan GET yang ada tanpa harus mereload seluruh halaman. 

# 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Saya membuat fungsi-fungsi yang dibutuhkan terlebih dahulu pada views.py. Fungsi-fungsi tersebut adalah show_todolist_json untuk menampilkan data json dari data-data todolist, lalu ada add_todolist untuk menambahkan task baru pada todolist kita secara asynchronous dengan ajax.

Lalu, saya mendaftarkan path untuk kedua fungsi tersebut pada urls.py. Path yang saya daftarkan adalah sebagai berikut:
path(‘json/’, show_todolist_json, name=’show_todolist_json),
path(‘add/’, add_todolist, name=’add_todolist),

Saya membuat tombol untuk form modal, yaitu tombol untuk dapat menambahkan task baru secara asynchronous. Pada form modal tersebut, user akan menginput judul dan deskripsi task baru. 
Kode untuk modal yang saya buat saya dapatkan dari bootstrap (https://getbootstrap.com/docs/5.2/components/modal/). Lalu saya menambahkan id untuk setiap input data dari user pada modal.

Saya menambahkan script untuk ajax jquery saya dan script untuk get dan post data pada bagian head. Fungsi AJAX get akan mengambil data-data dari /todolist/json dan akan disimpan ke new_data. Lalu, dilakukan iterasi pada setiap data dan dengan metode append, data-data tersebut akan dimasukkan pada card dan akan ditambahkan pada row. 
Lalu, pada fungsi AJAX post, fungsi akan terjadi setelah tombol untuk modal menambahkan task baru diklik. Lalu, data-data tersebut akan dipost ke /todolist/add/. Task baru akan ditampilkan pada halaman todolist secara asynchronous dengan menambahkan card task tersebut pada row. 
Lalu, untuk menghubungkan fungsi get dan post AJAX dengan fungsimodal yang telah dibuat, id-id inputan user pada modal akan dipanggil pada fungsi post dan get AJAX.
