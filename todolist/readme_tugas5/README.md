# 1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Pada inline style, properti CSS ada pada bagian body dengan elemennya. Pada Internal style. Penulisan tipe ini ada di dalam tag HTML dengan atribut style. Pada internal CSS, rule set berada di berkas HTML dan di dalam section head (CSS disematkan pada berkas HTML). Pada external CSS, berkas CSS terpisah dari berkas HTML di mana berkas tersebut hanya memuat style property dengan bantuan tag attributes. Berkas CSS memiliki ekstensi .css dan harus dihubungkan dengan dokumen HTML-nya dengan menggunakan link tag. Style dengan tipe ini hanya bisa di-set sekali dan akan diaplikasikan pada halaman web.

Perbedaan:
Inline CSS: kode CSS ditulis pada atribut (atribut style) elemen HTML
Internal CSS: kode CSS ditulis di dalam tag <style>, kode HTML ditulis pada bagian header pada berkas HTML
External CSS: kode CSS ditulis terpisah dengan kode pada berkas HTMLnya. 

Kekurangan:
Inline CSS: kurang efisien karena setiap tag HTML harus memiliki style masing-masing, jika hanya menggunakan inline style akan lebih sulit untuk mengatur web karena tipe ini hanya untuk mengubah satu elemen HTML saja.
Internal CSS: tidak efisien jika ingin menggunakan CSS yang sama pada beberapa file yang berbeda, menyebabkan performa web lebih lambat
External CSS: tampilan halaman akan terlihat berantakan jika berkas CSS gagal dipanggil oleh berkas HTML.

Kelebihan:
Inline CSS: dapat memperbaiki kode dengan cepat, proses untuk melakukan load pada web lebih cepat, proses untuk request HTTP lebih kecil
Internal CSS:  jika terdapat perubahan maka hanya akan berlaku pada satu halaman saja, tidak perlu mengunggah berkas HTML dan CSS secara terpisah karena sudah jadi satu, Class dan ID dapat digunakan internal stylesheet
External CSS: ukuran berkas HTML akan menjadi lebih kecil dan struktur kode pada berkas HTML terlihat lebih rapi, ketika terjadi loading pada web akan lebih cepat, berkas CSS dapat digunakan sekaligus untuk beberapa halaman web

source: https://www.niagahoster.co.id/blog/perbedaan-internal-external-dan-inline-css/ 

# 2. Jelaskan tag HTML5 yang kamu ketahui.
<nav>: merupakan tag untuk membuat link navigasi
<header>: tag untuk membuat suatu header dokumen atau bagian
<article>: tag untuk membuat suatu artikel
<footer>: tag untuk membuat suatu footer dokumen atau bagian
<section>: tag untuk membuat bagian pada dokumen
<aside>: tag untuk membuat konten selain dari konten halaman

# 3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
Element Selector: memilih elemen HTML tanpa diawali “#” atau “.”, di antara tipe element selector lain memiliki prioritas yang paling rendah.
Class Selector: memilih elemen HTML dengan diawali “.”, di antara tipe element selector lain memiliki prioritas yang paling tinggi kedua.
ID Selector: memilih elemen HTML dengan diawali “.”, di antara tipe element selector lain memiliki prioritas yang paling tinggi.

# 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pada halaman login, register, dan create-task, saya menggunakan navigasi yang akan menampilkan kata perintah untuk halaman tersebut, ada juga yang saya tambahkan tombol untuk menuju ke halaman sebelumnya. 
Lalu, saya membuat container dengan ukuran row dan column yang sesuai, dan membuat card. Pada card tersebut ada card header dan juga card body. Pada card body, saya membuat form-group, text untuk pada tampilan input user, dan button yang diperlukan. 
Untuk tampilan halaman todolist,  saya membuat looping untuk setiap data pada todolist yang akan ditampilkan pada card. Untuk menampilkan atribut-atribut pada card saya menggunakan list-group. 
Untuk mengatur font kalimat, saya menggunakan font-monospace pada class dan untuk mengatur warna background, diatur pada style.
