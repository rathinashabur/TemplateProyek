# 1. Apa kegunaan {% csrf_token %} pada elemen <form>? 
#    Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
{% csrf_token %} adalah perintah yang digunakan untuk men-generate token secara random setiap kali halaman form muncul. 
Token ini berguna untuk terjadinya Cross Site Request Forgery (CSRF), yaitu suatu serangan yang dapat terjadi pada aplikasi web kita. 
Jika tidak ada potongan kode {% csrf_token %}  pada elemen <form>, maka peretas dapat melakukan serangan pada web kita dengan mengirim form yang bukan dari server / server asli yang seharusnya, 
melainkan form dari peretas tersebut yang dapat membuat pengguna menjalankan hal-hal yang sebenarnya tidak mereka inginkan.

# 2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Ya, bisa. Berikut adalah tahapannya.
1. <form> dapat dibuat secara manual dengan membuat sebuah class dengan parameter (forms.ModelForm) atau (forms.Form) pada file forms.py dan akan didefinisikan fields atau atribut apa saja yang dibutuhkan untuk form tersebut.
2. Lalu, untuk meng-handle form, kita akan membuat rangkaian kode pada views.py yang akan mengecek validitas form dan memproses data pada form dengan membuat fungsi yang menerima parameter request
dan akan mereturn render dengan parameter(request, "nama_file.html", context). Pada views.py ini, data-data akan di-render.
3. Kita akan membuat sebuah html template untuk tampilan dari form yang telah kita buat.

# 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
1. User akan membuat request dengan memasukkan alamat “http://host/path” lalu server akan menerima request tersebut dan akan menentukan views.py yang sesuai untuk meng-handle request tersebut.
2. Lalu, akan di-generate suatu form halaman HTML dan akan ditampilkan ke user.
3. User akan melakukan insert pada form halaman HTML dan akan di-generate HTTP request, method, dan arguments berdasarkan form tersebut. Lalu, server akan menerima request tersebut dan menentukan views.py yang sesuai untuk meng-handle request tersebut.
4. Lalu, hasil insert form tersebut akan diolah dan hasilnya akan di-generate pada halaman HTML yang nantinya akan ditampilkan ke user.

# 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Saya membuat aplikasi mywatchlist dengan perintah python3 manage.py startapp todolist, mendaftarkan aplikasi todolist pada proyek Django dengan menambahkan ‘todolist’ pada variabel INSTALLED_APPS pada settings.py di folder project_django. 
Lalu saya melakukan migrasi untuk menghubungkan perubahan pada aplikasi todolist ke dalam database dengan perintah python3 manage.py makemigrations dan python3 manage.py migrate.
2. Pada models.py di folder todolist, melakukan import models, membuat class Task yang isinya mendefinisikan atribut-atribut sesuai ketentuan pada soal yang akan digunakan untuk menampilkan data todolist. 
Lalu, saya membuat fungsi show_todolist yang menerima parameter request, mengembalikan return render(request, “todolist.html”, context). Selanjutnya, saya melakukan routing dengan menambahkan path show_todolist pada urls.py pada folder todolist 
dan mendaftarkan aplikasi todolist dengan menambahkan path todolist dan include pada urls.py di folder project_django.
3. Lalu, untuk mengimplementasikan form registrasi, login, dan logout, pada views.py saya meng-import hal-hal yang dibutuhkan dan membuat fungsi register, login_user, dan logout_user yang berisi kode-kode untuk mengolah request user 
dengan proses yang sesuai yang akan mengembalikan hasil dari proses tersebut dan akan ditampilkan kepada user. Saya juga membuat file register.html dan login.html yang berisikan kode untuk tampilan-tampilan pada halaman register dan login. 
Selanjutnya, pada urls.py saya mengimport fungsi register, login_user, dan logout_user serta menambahkan path url untuk halaman register, login, dan logout pada urlpatterns. 
Saya juga menambahkan kode untuk merestriksi akses halaman todolist di atas fungsi show_todolist dan juga kode-kode untuk menampilkan data last login. Pada fungsi-fungsi yang telah dibuat, tidak lupa saya mengecek validitas form.
4. Saya membuat file todolist.html pada folder templates yang berisi kode-kode untuk tampilan utama aplikasi yang menampilkan username pengguna, tombol Tambah Task Baru, tombol logout, 
dan tabel yang berisi tanggal pembuatan, judul, dan deskripsi task dengan melakukan iterasi pada setiap atribut.
5. Untuk membuat halaman form untuk pembuatan task yang meminta user untuk memasukkan judul dan deskripsi task, saya membuat file forms.py yang berisi class Create_Task yang menerima parameter forms.ModelForm 
dan mendefinisikan atribut apa saja yang akan ditampilkan. Lalu data-data dari form akan di-render di mana kodenya dituliskan pada fungsi create_task pada view.py, tidak lupa dicek juga validitas formnya. 
Saya juga membuat file task.html yang akan menampilkan tampilan untuk penambahan task.
6. Lalu, untuk melakukan routing, saya menambahkan path untuk halaman, register, login, logout, dan create-task pada urlpatterns pada urls.py
