# test_veita_informatika


===== Instalation ======

+ instal uwsgi
pip install uwsgi

+ instal urllib

pip install urllib3

====== run program ======


uwsgi --http :9090 --wsgi-file test_kerja.py
 
 atau 

 uwsgi --http :9090 --wsgi-file test_kerja2.py

silahkan akses link dibawah ini di browser kesayangan anda
http://localhost:9090/

 ====== informasi ======

 + test_kerja

 hasil sesuai dengan contoh

 + test_kerja2

 hasil lebih banyak karena dari data ada lebih dari 1 features
