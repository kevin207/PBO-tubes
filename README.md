# PBO-tubes

Tubes PBO - Kelompok "manajer" - Bank Management System

Anggota:
- Ihza Fajrur Achmad Hasani
- Kevin Tanuwijaya
- Resya Lianti
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

DESKRIPSI APLIKASI:

Aplikasi yang dikembangkan ini adalah aplikasi yang befungsi sebagai sistem manajemen bank, dimana dalam pengembanganya digunakan bahasa pemrograman python dan mengandung unsur pemrograman berorientasi objek. Pada aplikasi ini user dapat melakukan login, logout, daftar akun, cek transaksi, dan melakukan transaksi.  

Ada 2 tipe user yang dapat mengakses aplikasi ini yaitu admin dan customer. Admin maupun customer keduanya harus melakukan login terlebih dahulu agar dapat mengakses fitur pada aplikasi. User admin dapat melakukan penghapusan akun customer dan menampilkan data customer serta balance yang dimiliki, sedangkan user customer dapat melakukan daftar customer (apabila bukan customer), daftar akun (checking account, saving account, dan loan account), akses akun, mengecek transaksi dan melakukan transaksi. Jumlah akun yang dapat dimiliki oleh customer dapat lebih dari satu.

Transaksi yang dapat dilakukan antara lain:
- Melakukan Penarikan (Withdraw)
- Melakukan Penabungan (Deposit)
- Melakukan Peminjaman (Make Loan)
- Melakukan Pelunasan (Pay Off)

Pada loan dan saving account akan ada bunga sebesar 10% dari balance yang ada pada akun tersebut untuk setiap bulan-nya. Pada akun loan balance adalah besar peminjaman yang dilakukan sedangkan pada akun saving dan checking, balance adalah jumlah tabungan yang dimiliki. Pada akun checking value balance dapat negatif karena pada akun checking dapat dilakukan overdraft (penarikan melebihi balance yang dimiliki akun) yang memiliki credit limit sebesar Rp. 10.000.000. Saat melakukan peminjaman(loan) ada batas waktu pelunasan yaitu selama 1 bulan untuk setiap peminjaman, apabila selama waktu yang ditentukan peminjaman tidak juga dilunasi maka akan dikenakan denda sebesar 20% dari pinjaman yang diambil.
