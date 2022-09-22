# 1. Jelaskan perbedaan antara JSON, XML, dan HTML!
HTML: ekstensinya adalah .html, mengirim data melalui form, syntaxnya menggunakan tanda tag, tidak case sensitive, tag pada HTML digunakan untuk menampilkan data, bersifat statis, 
merupakan Hyper Text Markup Language, support array, tidak membutuhkan end tags

JSON: ekstensinya adalah .json, menyimpan elemen dengan efisien tetapi tidak rapi untuk dilihat oleh mesin dan manusia, case sensitive, 
merupakan JavaScript Object Notation berdasarkan bahasa JavaScript, support array, tidak membutuhkan end tags, digunakan untuk mengirim data dengan cara menguraikan datanya dulu lalu dikirim melalui internet

XML: ekstensinya adalah .xml, elemen disimpan secara terstruktur dan mudah dibaca oleh manusia serta mesin tetapi kurang efisien, case sensitive, 
tag pada XML digunakan untuk mendeskripsikan data bukan menampilkan, bersifat dinamis, merupakan extensible Markup Language dan bahasanya diambil dari SGML, tidak support array, membutuhkan end tags, data lebih terstruktur

# https://www.dicoding.com/blog/apa-itu-json/
# https://www.geeksforgeeks.org/html-vs-xml/
# https://www.geeksforgeeks.org/difference-between-json-and-xml/

# 2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan dalam mengembangkan suatu platform karena ada kalanya data-data pada suatu stack perlu dikirimkan ke stack lainnya dan bentuk dari data-data tersebut dapat bermacam-macam.

# 3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Saya membuat aplikasi mywatchlist dengan perintah python3 manage.py startapp mywatchlist, mendaftarkan aplikasi mywatchlist pada proyek Django dengan menambahkan ‘mywatchlist’ 
pada variabel INSTALLED_APPS pada settings.py di folder project_django.
2. Pada models.py di folder mywatchlist, melakukan import models, membuat class WatchlistKu yang isinya mendefinisikan tipe-tipe data yang akan digunakan untuk menampilkan data watchlist.
3. Melakukan migrasi untuk menghubungkan perubahan pada aplikasi mywatchlist ke dalam database dengan perintah python3 manage.py makemigrations dan python3 manage.py migrate.
4. Membuat folder bernama fixtures pada folder mywatchlist dan membuat berkas bernama initial_mywatchlist_data.json dan mengisinya dengan hal-hal yang diperlukan 
untuk menampilkan tampilan yang sesuai pada ketentuan soal dengan syntax json. Lalu data diload ke database Django lokal dengan perintah python3 manage.py loaddata initial_mywatchlist_data.json
5. Membuat fungsi show_mywatchlist yang menerima parameter request, mengembalikan return render(request, “mywatchlist.html”, context). 
6. Membuat folder baru bernama templates pada folder mywatchlist dan membuat berkas bernama mywatchlist.html di dalamnya dan mengisinya dengan 
hal-hal yang dibutuhkan untuk ditampilkan seperti pada soal dengan syntax HTML dan melakukan iterasi pada data_mywatchlist untuk menampilkan data-data yang ada dengan memanggil variabel-variabel sesuai yang sudah didefinisikan sebelumnya.
7. Melakukan routing dengan menambahkan path show_mywatchlist pada urls.py pada folder mywatchlist dan mendaftarkan apliikasi mywatchlist dengan 
menambahkan path mywatchlist dan include pada urls.py di folder project_django.
8. Lalu saya juga membuat fungsi show_xml dan show_json yang menerima parameter request dan berisi variabel yang menyimpan hasil query dari seluruh data pada WatchlistKu, 
yang mengembalikan return HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML/jso dan parameter content_type yang sesuai. Tidak lupa sebelumnya melakukan 
import untuk render, WatchlistKu, HttpResponse, dan juga serializers. Lalu saya melakukan import show_xml dan show_json pada urls.py pada folder mywatchlist serta menambahkan 
path untuk xml dan json pada urlpatterns agar dapat mengakses fungsi yang sebelumnya sudah diimpor.
9. Menjalankan aplikasi mywatchlist dengan perintah python3 manage.py runserver.

# Mengakses tiga URL di poin 6 menggunakan Postman, menangkap screenshot, dan menambahkannya ke dalam README.md
html: ![html](/html.png)
xml: ![xml](/xml.png)
json: ![json](/json.png)