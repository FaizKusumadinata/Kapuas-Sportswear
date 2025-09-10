Nama: Faiz Kusumadinata
Kelas: PBP A
NPM: 2406426196
1. Langkah-langkah implementasi checkpoint: 
   Dalam membuat proyek Django baru, langkah pertama adalah membuat folder baru untuk proyek. Setelah folder dibuat, direktorinya dibuka dengan command prompt atau Windows Powershell. Dalam terminal, aktifkan Virtual Environment dan proyek Django baru dibuat dengan command "django-admin startproject <proyek> .". Dengan command tersebut, maka proyek telah dibuat di dalam folder proyek. Setelah proyek dibuat, maka langkah selanjutnya adalah membuat konfigurasi dari proyek, seperti nama host database, konfigurasi environment, dan lainnya. Dibuat file ".env" yang akan digunakan untuk development lokal dan ".env.prod" yang akan digunakan untuk production deployment. ".env.prod" juga akan yang menjadi file dimana kredensial database disimpan.
   Setelah melakukan konfigurasi lebih lanjut pada file settings, maka dibuat aplikasi "main" pada proyek dengan pertama membuat folder baru bernama "main" di folder proyek. Di dalam folder main, dibuat file HTML dengan nama yang sama. Setelah mebuat file HTML, maka file models.py akan diisi dengan Models untuk aplikasi main. Di dalam file models, dibuat Class dengan nama Products, yang berisi atribut name dengan tipe charfield, price dengan tipe IntegerField, description dengan tipe TextField, thumbnail dengan tipe URLfield, category dengan tipe charField, dan is_featured dengan tipe boolean_field. Langkah selanjutnya adalah mengisi file views.py dengan fungsi show_main yang akan digunakan untuk menampilkan nama aplikasi, nama, dan kelas pada file HTML. Langkah terakhir adalah mengkonfigurasi file urls.py. File urls.py akan digunakan untuk menghubungkan fungsi dari views.py ke aplikasi main. File urls.py diisi dengan command untuk menambahkan rute ke aplikasi main.
   
2. Penjelasan kaitan antara urls.py, views.py, models.py, dan berkas html: 
   views.py berfungsi untuk menyimpan fungsi yang akan digunakan untuk ditampilkan pada file HTML. urls.py berguna menghubungkan antara views.py dengan HTML. File models.py berfungsi menyimpan atribut-atribut aplikasi. Bagan yang menjelaskan hubungannya dapat diakses dengan link berikut: https://towardsdatascience.com/wp-content/uploads/2021/02/1JI0ZJiVs7PDDUZlXAf59gg-768x901.png
   Link tersebut diambil dari https://towardsdatascience.com/a-beginners-guide-to-using-djangos-impressive-data-management-abilities-9e94efe3bd6e/
   
3. Peran settings.py di Django: 
   File settings.py dalam proyek Django berfungsi untuk menyimpan konfigurasi terkait database, host, dan production. Settings dapat menyimpan daftar dari host mana saja yang dapat mengakses aplikasi. Settings juga dapat dimodifikasi dengam mengimpor load_dotenv agar dapat menggunakan environment variables, yakni variabel dari luar program yang menyimpan kredensial database, API keys, dan pengaturan lainnya.
   
4. Cara kerja migrasi pada database Django: 
   Migrasi pada database Django dijalankan setelah menerima command "makemigrations" dan "migrate". Setelah command dijalankan, maka program akan membandingkan kondisi terkini dari model Django dengan database. Jika telah terjadi perubahan pada model Django, maka database akan diupdate. Command "makemigrations" berfungsi menyiapkan segala perubahan pada model Django dan "migrate" berfungsi untuk melakukan perubahan pada database untuk mengikuti kondisi terkini dari model Django.
   
5. Framework Django: 
   Framework Django direkomendasikan bagi pemula untuk mempelajari pengembangan perangkat lunak karena memiliki sejumlah keuntungan. Django merupakan framework open source yang fleksibel dalam penggunaannya, memiliki keamanan yang bagus, memiliki performa yang cepat, dan kaya akan fitur. 
