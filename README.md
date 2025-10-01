Nama: Faiz Kusumadinata
Kelas: PBP A
NPM: 2406426196

Tugas Individu 2
1. Langkah-langkah implementasi checkpoint: 
   Dalam membuat proyek Django baru, langkah pertama adalah membuat folder baru untuk proyek. Setelah folder dibuat, direktorinya dibuka dengan command prompt atau Windows Powershell. Dalam terminal, aktifkan Virtual Environment dan proyek Django baru dibuat dengan command "django-admin startproject <proyek> .". Dengan command tersebut, maka proyek telah dibuat di dalam folder proyek. Setelah proyek dibuat, maka langkah selanjutnya adalah membuat konfigurasi dari proyek, seperti nama host database, konfigurasi environment, dan lainnya. Dibuat file ".env" yang akan digunakan untuk development lokal dan ".env.prod" yang akan digunakan untuk production deployment. ".env.prod" juga akan yang menjadi file dimana kredensial database disimpan.
   
   Setelah melakukan konfigurasi lebih lanjut pada file settings, maka dibuat aplikasi "main" pada proyek dengan pertama membuat folder baru bernama "main" di folder proyek. Di dalam folder main, dibuat file HTML dengan nama yang sama. Setelah mebuat file HTML, maka file models.py akan diisi dengan Models untuk aplikasi main. Di dalam file models, dibuat Class dengan nama Products, yang berisi atribut name dengan tipe charfield, price dengan tipe IntegerField, description dengan tipe TextField, thumbnail dengan tipe URLfield, category dengan tipe charField, dan is_featured dengan tipe boolean_field. Langkah selanjutnya adalah mengisi file views.py dengan fungsi show_main yang akan digunakan untuk menampilkan nama aplikasi, nama, dan kelas pada file HTML. Langkah terakhir adalah mengkonfigurasi file urls.py. File urls.py akan digunakan untuk menghubungkan fungsi dari views.py ke aplikasi main. File urls.py diisi dengan command untuk menambahkan rute ke aplikasi main.
   
3. Penjelasan kaitan antara urls.py, views.py, models.py, dan berkas html: 
   views.py berfungsi untuk menyimpan fungsi yang akan digunakan untuk ditampilkan pada file HTML. urls.py berguna menghubungkan antara views.py dengan HTML. File models.py berfungsi menyimpan atribut-atribut aplikasi. Bagan yang menjelaskan hubungannya dapat diakses dengan link berikut: https://towardsdatascience.com/wp-content/uploads/2021/02/1JI0ZJiVs7PDDUZlXAf59gg-768x901.png
   Link tersebut diambil dari https://towardsdatascience.com/a-beginners-guide-to-using-djangos-impressive-data-management-abilities-9e94efe3bd6e/
   
4. Peran settings.py di Django: 
   File settings.py dalam proyek Django berfungsi untuk menyimpan konfigurasi terkait database, host, dan production. Settings dapat menyimpan daftar dari host mana saja yang dapat mengakses aplikasi. Settings juga dapat dimodifikasi dengam mengimpor load_dotenv agar dapat menggunakan environment variables, yakni variabel dari luar program yang menyimpan kredensial database, API keys, dan pengaturan lainnya.
   
5. Cara kerja migrasi pada database Django: 
   Migrasi pada database Django dijalankan setelah menerima command "makemigrations" dan "migrate". Setelah command dijalankan, maka program akan membandingkan kondisi terkini dari model Django dengan database. Jika telah terjadi perubahan pada model Django, maka database akan diupdate. Command "makemigrations" berfungsi menyiapkan segala perubahan pada model Django dan "migrate" berfungsi untuk melakukan perubahan pada database untuk mengikuti kondisi terkini dari model Django.
   
6. Framework Django: 
   Framework Django direkomendasikan bagi pemula untuk mempelajari pengembangan perangkat lunak karena memiliki sejumlah keuntungan. Django merupakan framework open source yang fleksibel dalam penggunaannya, memiliki keamanan yang bagus, memiliki performa yang cepat, dan kaya akan fitur.



Tugas Individu 3
1. Mengapa Data Delivery diperlukan?
   Data Delivery diperlukan untuk menyimpan dan membagikan data secara online. Sebagai contoh, ketika sebuah browser memberikan request terhadap file tertentu, maka server akan mengembalikan file tersebut. Adapun Data Delivery tidak hanya mencakup pembagian data web secara online, tetapi juga mendeteksi error, menjaga keutuhan data, dan memastikan penerima data sudah tepat.
2. Lebih baik XML atau JSON? Mengapa JSON lebih populer?
   Kedua XML dan JSON merupakan mark-up language yang digunakan untuk menyimpan data dalam web development. XML memiliki bahasa yang menyerupai HTML dengan menggunakan tag yang dapat dikustomisasi untuk menyesuaikan model dan atribut dari web. XML juga menggunakan struktur data tree. JSON menggunakan Javascript, dimana penulisan model dan atribut lebih mudah dan sederhana dibandingkan XML. Akibat kemudahan dalam menulis inilah JSON menjadi lebih populer daripada XML. Adapun JSON juga dapat mencari data lebih cepat dibandingkan XML.
3. Mengapa memerlukan is_valid() pada form Django?
   Method .isvalid() diperlukan dalam form Django untuk memastikan bahwa data yang diinput oleh pengguna dalam form sudah sesuai dengan tipe data yang diperlukan.
4. Apa fungsi csrf_token pada form Django?
   csrf_token dalam form Django berguna untuk melindungi web. csrf_token merupakan token yang digenerate oleh Django secara otomatis untuk mencegah serangan. Serangan csrf merupakan serangan dimana penyerang menirukan request dari situs dan memanfaatkannya untuk mengambil data yang dimasukkan oleh pengguna. Token csrf berguna untuk menciptakan token unik yang dimiliki hanya oleh situs tersebut.
5. Penjelasan step by step implementasi checkpoint
   Langkah pertama dalam Tugas Individu 3 adalah menciptakan sebuah kerangka yang akan diterapkan oleh views ketika menciptakan halaman-halaman baru selain main pada proyek Django. Pada root folder, dibuat sebuah folder template yang akan menyimpan sebuah file html bernama "base". Base akan berisi struktur penampilan yang akan ditampilkan oleh setiap halaman. Base akan menerapkan Template Tags yang akan me-load dari Django ke HTML. Langkah berikutnya adalah menjadikan base.html sebagai template dengan mengaturnya dalam konfigurasi settings.py. Setelah menjadi template, maka file main.html dan file halaman lainnya yang akan dibuat akan ditambahkan "extends base.html" di awal setiap kodenya.
   Langkah berikutnya adalah membuat file forms.py yang akan menjadi kerangka untuk menyimpan dan mengidentifikasi tipe-tipe data yang akan diterima ketika menciptakan produk. Untuk tugas individu 3 ini, maka dibuat dua file html baru untuk dua halaman baru. Kedua halaman merupakan halaman untuk menambahkan produk baru dan halaman untuk melihat detail dari produk. Dengan kedua halaman sudah dibuat, maka dibuat dua fungsi terkait kedua halaman tersebut dalam views.py. Fungsi pertama create_products akan menggunakan forms.py untuk menyimpan data yang dimasukkan oleh pengguna. Fungsi kedua, yakni show_products akan menampilkan detail produk. Setelah kedua fungsi selesai dibuat, maka akan dihubungkan ke web melalui urls.py.
   Dengan dua halaman untuk menampilkan detail dan menciptakan ptoduk, maka selanjutnya adalah membuat fungsi untuk mengembalikan data menggunakan XML dan JSON. Untuk XML, langkah petama adalah membuat fungsi show_xml(request) yang akan mengambil semua model produk dan mentranslasikan model produk tersebut dengan serializers agar menjadi model XML. Adapun dibuat fungsi untuk mengembalikan data XML sesuai dengan id tertentu. Kedua langkah tersebut juga dilakukan untuk mengembalikan data menggunakan JSON. Dengan keempat fungsi telah dibuat, maka dihubungkaan ke web melalui urls.py.


Tugas Individu 4

Nama Akun 1: faiz_kusumadinata

Password akun 1: omega_centaury

Nama Akun 2: fariz_kusumadinata

Password akun 2: Arwana777 

1. Apa itu Django Authentication Form?
   Django Authentication Form merupakan Form yang disediakan oleh DJango untuk mengolah input data oleh pengguna untuk proses autentikasi. Authentication Form ini mengolah data seperti username dan password beserta validasinya.
3. Apa perbedaan autorisasi dan autentikasi?
   Autorisasi merupakan proses menentukan izin dari seorang pengguna dalam aksesnya. Autorisasi menentukan bagi setiap pengguna tindakan apa saja yang dapat mereka lakukan atau objek apa saja yang dapat mereka akses. Autentikasi merupakan proses menverifikasi seorang pengguna berdasarkan username dan passwordnya. Autentikasi hanya bertindak dalam memberikan akses bagi siapa saja yang memiliki kredensial yang telah diberi akses.
5. Kelemahan dan kelebihan session dan cookies?
   Dalam kelebihannya, coookies membantu meningkatkan pengalaman pengguna pada website. Cookies dapat menggunakan data yang telah diperoleh dari pengguna untuk mempersonalisasikan dan menyesuaikan website dengan pengguna. Adapun kelemahannya, cookies juga rentan terhadap ancaman. Salah satu ancaman yang umum dialami oleh cookies adalah Cross-Site Request Forgery yang dapat membahayakan data pengguna.
7. Apakah pengguna cookie aman secara default?
   Secara default, cookies tidak aman. Akan tetapi terdapat cara-cara untuk meningkatkan keamanan dari cookies pada website.





