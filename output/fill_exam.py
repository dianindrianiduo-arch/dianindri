"""Fill the exam template docx with KKA exam questions."""
import docx
from docx.oxml.ns import qn
from copy import deepcopy

SRC = '/tmp/template.docx'
OUT = '/tmp/template_extracted/output.docx'

doc = docx.Document(SRC)
body = doc.element.body


# =====================================================================
# CONTENT
# =====================================================================

NAMA_GURU = "Roseno Afandi & David Ezra Kurniawan"
MAPEL = "Koding dan Kecerdasan Artifisial (KKA)"
KELAS = "X (Sepuluh)"
TAHUN = "2025/2026"

# Pilihan Ganda
PG = [
    {
        "no": 1,
        "elemen": "Algoritma dan Pemrograman",
        "cp": "Peserta didik memahami konsep dasar koding sebagai instruksi yang diberikan kepada komputer.",
        "tp": "Peserta didik dapat menjelaskan pengertian dan tujuan utama dari koding.",
        "indikator_kompetensi": "Memahami konsep dasar koding/pemrograman.",
        "indikator_soal": "Disajikan narasi tentang koding, peserta didik dapat menentukan pernyataan yang paling tepat menggambarkan tujuan utama koding.",
        "tingkat": "Rendah",
        "kunci": "B",
        "soal": (
            "Koding adalah proses memberikan instruksi kepada komputer menggunakan bahasa tertentu agar komputer dapat menjalankan tugas. Berikut ini yang paling tepat menggambarkan tujuan utama koding adalah ...\n"
            "A. Membuat komputer menjadi lebih cepat secara fisik\n"
            "B. Menulis perintah agar komputer dapat melakukan tugas sesuai yang diinginkan\n"
            "C. Menginstal sistem operasi pada komputer\n"
            "D. Menghubungkan komputer ke jaringan internet\n"
            "E. Memperbaiki kerusakan perangkat keras komputer"
        ),
    },
    {
        "no": 2,
        "elemen": "Algoritma dan Pemrograman",
        "cp": "Peserta didik memahami algoritma sebagai dasar penyelesaian masalah secara terstruktur.",
        "tp": "Peserta didik dapat menjelaskan pengertian algoritma.",
        "indikator_kompetensi": "Memahami konsep algoritma.",
        "indikator_soal": "Disajikan deskripsi penyusunan langkah-langkah penyelesaian masalah, peserta didik dapat menentukan istilah yang tepat.",
        "tingkat": "Rendah",
        "kunci": "C",
        "soal": (
            "Sebelum menulis kode program, seorang programmer pemula biasanya menyusun langkah-langkah logis untuk menyelesaikan suatu masalah. Urutan langkah-langkah logis yang sistematis untuk menyelesaikan masalah disebut ...\n"
            "A. Sintaks\n"
            "B. Variabel\n"
            "C. Algoritma\n"
            "D. Kompilator\n"
            "E. Debugger"
        ),
    },
    {
        "no": 3,
        "elemen": "Algoritma dan Pemrograman",
        "cp": "Peserta didik memahami cara representasi algoritma secara visual.",
        "tp": "Peserta didik dapat menjelaskan pengertian flowchart sebagai representasi visual algoritma.",
        "indikator_kompetensi": "Mengidentifikasi flowchart.",
        "indikator_soal": "Disajikan deskripsi tentang penggambaran algoritma menggunakan simbol-simbol, peserta didik dapat menentukan istilahnya.",
        "tingkat": "Rendah",
        "kunci": "B",
        "soal": (
            "Salah satu cara menggambarkan algoritma secara visual menggunakan simbol-simbol tertentu seperti persegi panjang, belah ketupat, dan jajar genjang. Representasi visual ini dikenal dengan istilah ...\n"
            "A. Pseudocode\n"
            "B. Flowchart\n"
            "C. Struktur data\n"
            "D. Source code\n"
            "E. Mind map"
        ),
    },
    {
        "no": 4,
        "elemen": "Algoritma dan Pemrograman",
        "cp": "Peserta didik memahami penggunaan variabel dalam pemrograman.",
        "tp": "Peserta didik dapat menjelaskan pengertian variabel.",
        "indikator_kompetensi": "Memahami konsep variabel dalam pemrograman.",
        "indikator_soal": "Disajikan deskripsi tentang tempat penyimpanan data dalam program, peserta didik dapat menentukan istilah yang tepat.",
        "tingkat": "Rendah",
        "kunci": "C",
        "soal": (
            "Dalam pemrograman, tempat penyimpanan sementara untuk menampung data atau nilai yang dapat berubah selama program berjalan disebut ...\n"
            "A. Konstanta\n"
            "B. Fungsi\n"
            "C. Variabel\n"
            "D. Operator\n"
            "E. Komentar"
        ),
    },
    {
        "no": 5,
        "elemen": "Algoritma dan Pemrograman",
        "cp": "Peserta didik mengidentifikasi tipe data dalam pemrograman.",
        "tp": "Peserta didik dapat menentukan tipe data dari sebuah variabel.",
        "indikator_kompetensi": "Mengidentifikasi tipe data.",
        "indikator_soal": "Disajikan potongan kode sederhana, peserta didik dapat menentukan tipe data dari variabel tertentu.",
        "tingkat": "Sedang",
        "kunci": "D",
        "soal": (
            "Perhatikan potongan kode berikut:\n"
            "    nama = \"Andi\"\n"
            "    umur = 16\n"
            "Tipe data dari variabel \"umur\" pada kode tersebut adalah ...\n"
            "A. String\n"
            "B. Boolean\n"
            "C. Float\n"
            "D. Integer\n"
            "E. Character"
        ),
    },
    {
        "no": 6,
        "elemen": "Algoritma dan Pemrograman",
        "cp": "Peserta didik memahami struktur kontrol perulangan dalam pemrograman.",
        "tp": "Peserta didik dapat menjelaskan struktur perulangan (looping).",
        "indikator_kompetensi": "Memahami struktur perulangan.",
        "indikator_soal": "Disajikan deskripsi fungsi struktur kontrol, peserta didik dapat menentukan istilah yang tepat.",
        "tingkat": "Sedang",
        "kunci": "B",
        "soal": (
            "Dalam pemrograman, terdapat struktur yang digunakan untuk mengulang eksekusi sekumpulan perintah sampai kondisi tertentu terpenuhi. Struktur ini dikenal dengan istilah ...\n"
            "A. Percabangan\n"
            "B. Perulangan (looping)\n"
            "C. Fungsi\n"
            "D. Array\n"
            "E. Komentar"
        ),
    },
    {
        "no": 7,
        "elemen": "Algoritma dan Pemrograman",
        "cp": "Peserta didik memahami struktur percabangan dalam pemrograman.",
        "tp": "Peserta didik dapat menjelaskan fungsi pernyataan if-else.",
        "indikator_kompetensi": "Memahami struktur percabangan.",
        "indikator_soal": "Disajikan pernyataan tentang if-else, peserta didik dapat menentukan fungsinya.",
        "tingkat": "Sedang",
        "kunci": "C",
        "soal": (
            "Pernyataan if-else dalam bahasa pemrograman digunakan untuk ...\n"
            "A. Mengulang program\n"
            "B. Menyimpan data\n"
            "C. Membuat keputusan berdasarkan kondisi tertentu\n"
            "D. Menjalankan program berulang kali\n"
            "E. Membuat tampilan grafis"
        ),
    },
    {
        "no": 8,
        "elemen": "Algoritma dan Pemrograman",
        "cp": "Peserta didik memahami proses perbaikan kesalahan dalam program.",
        "tp": "Peserta didik dapat menjelaskan pengertian debugging.",
        "indikator_kompetensi": "Memahami konsep debugging.",
        "indikator_soal": "Disajikan deskripsi proses memperbaiki kesalahan kode, peserta didik dapat menentukan istilahnya.",
        "tingkat": "Sedang",
        "kunci": "B",
        "soal": (
            "Proses mencari, menemukan, dan memperbaiki kesalahan (error/bug) pada kode program disebut ...\n"
            "A. Coding\n"
            "B. Debugging\n"
            "C. Encoding\n"
            "D. Compiling\n"
            "E. Running"
        ),
    },
    {
        "no": 9,
        "elemen": "Algoritma dan Pemrograman",
        "cp": "Peserta didik memahami pentingnya dokumentasi dalam pemrograman.",
        "tp": "Peserta didik dapat menjelaskan pengertian komentar pada kode program.",
        "indikator_kompetensi": "Memahami fungsi komentar pada kode.",
        "indikator_soal": "Disajikan deskripsi tentang catatan pada kode yang tidak dijalankan komputer, peserta didik dapat menentukan istilahnya.",
        "tingkat": "Sedang",
        "kunci": "C",
        "soal": (
            "Salah satu kebiasaan baik dalam menulis kode adalah memberi catatan singkat yang menjelaskan fungsi baris kode tertentu. Catatan ini tidak ikut dijalankan oleh komputer dan disebut ...\n"
            "A. Output\n"
            "B. Input\n"
            "C. Komentar (comment)\n"
            "D. Variabel\n"
            "E. Sintaks"
        ),
    },
    {
        "no": 10,
        "elemen": "Algoritma dan Pemrograman",
        "cp": "Peserta didik mengenal bahasa pemrograman yang sesuai untuk pemula.",
        "tp": "Peserta didik dapat menyebutkan bahasa pemrograman yang cocok untuk pemula.",
        "indikator_kompetensi": "Mengenal bahasa pemrograman untuk pemula.",
        "indikator_soal": "Disajikan deskripsi karakteristik bahasa pemrograman, peserta didik dapat menentukan bahasa pemrograman yang sesuai untuk pemula.",
        "tingkat": "Sedang",
        "kunci": "C",
        "soal": (
            "Bahasa pemrograman yang sering direkomendasikan untuk pemula karena sintaksnya sederhana dan mudah dibaca seperti bahasa Inggris adalah ...\n"
            "A. Assembly\n"
            "B. C++\n"
            "C. Python\n"
            "D. Cobol\n"
            "E. Fortran"
        ),
    },
    {
        "no": 11,
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Peserta didik memahami fungsi tools AI berbasis teks.",
        "tp": "Peserta didik dapat menjelaskan fungsi utama ChatGPT.",
        "indikator_kompetensi": "Memahami fungsi ChatGPT.",
        "indikator_soal": "Disajikan deskripsi singkat tentang ChatGPT, peserta didik dapat menentukan fungsi utamanya.",
        "tingkat": "Sedang",
        "kunci": "C",
        "soal": (
            "ChatGPT merupakan salah satu produk kecerdasan artifisial yang dikembangkan oleh OpenAI. Fungsi utama ChatGPT adalah ...\n"
            "A. Mengedit foto dan video\n"
            "B. Membuat presentasi otomatis dari teks\n"
            "C. Menjawab pertanyaan dan menghasilkan teks berdasarkan instruksi pengguna\n"
            "D. Membuat gambar dari deskripsi teks\n"
            "E. Merangkum video YouTube"
        ),
    },
    {
        "no": 12,
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Peserta didik memahami konsep prompt dalam penggunaan AI berbasis teks.",
        "tp": "Peserta didik dapat menjelaskan pengertian prompt.",
        "indikator_kompetensi": "Memahami konsep prompt pada ChatGPT.",
        "indikator_soal": "Disajikan narasi tentang interaksi dengan ChatGPT, peserta didik dapat menentukan istilah untuk instruksi yang diberikan.",
        "tingkat": "Sedang",
        "kunci": "B",
        "soal": (
            "Saat menggunakan ChatGPT, kualitas jawaban yang dihasilkan sangat bergantung pada instruksi atau pertanyaan yang diberikan oleh pengguna. Instruksi yang diberikan kepada AI ini biasa disebut ...\n"
            "A. Output\n"
            "B. Prompt\n"
            "C. Token\n"
            "D. Script\n"
            "E. Algoritma"
        ),
    },
    {
        "no": 13,
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Peserta didik mengenal tools AI generatif untuk gambar dan video.",
        "tp": "Peserta didik dapat menjelaskan fungsi utama Dreamina.",
        "indikator_kompetensi": "Mengenal fungsi Dreamina.",
        "indikator_soal": "Disajikan deskripsi tentang Dreamina, peserta didik dapat menentukan fungsi utamanya.",
        "tingkat": "Sedang",
        "kunci": "A",
        "soal": (
            "Dreamina adalah salah satu platform kecerdasan artifisial dari ByteDance yang banyak digunakan oleh kreator konten. Fungsi utama Dreamina adalah ...\n"
            "A. Membuat gambar dan video dari deskripsi teks (text-to-image dan text-to-video)\n"
            "B. Menerjemahkan bahasa asing secara real-time\n"
            "C. Mengetik dokumen otomatis\n"
            "D. Membuat website tanpa coding\n"
            "E. Mengelola jadwal pelajaran"
        ),
    },
    {
        "no": 14,
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Peserta didik dapat memilih tools AI yang tepat sesuai kebutuhan.",
        "tp": "Peserta didik dapat memilih tools AI untuk pembuatan ilustrasi visual.",
        "indikator_kompetensi": "Menerapkan pemilihan tools AI generatif visual.",
        "indikator_soal": "Disajikan kasus kebutuhan ilustrasi visual, peserta didik dapat menentukan tools AI yang tepat.",
        "tingkat": "Sedang",
        "kunci": "D",
        "soal": (
            "Seorang siswa ingin membuat ilustrasi visual untuk tugas seninya hanya dengan mengetikkan deskripsi seperti \"anak sekolah belajar di bawah pohon saat senja\". Tools AI yang paling tepat digunakan untuk keperluan ini adalah ...\n"
            "A. NotebookLM\n"
            "B. Gamma.app\n"
            "C. Microsoft Excel\n"
            "D. Dreamina\n"
            "E. WhatsApp"
        ),
    },
    {
        "no": 15,
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Peserta didik mengenal tools AI generatif gambar yang unggul dalam tulisan.",
        "tp": "Peserta didik dapat menjelaskan keunggulan Ideogram.",
        "indikator_kompetensi": "Memahami keunggulan Ideogram.",
        "indikator_soal": "Disajikan deskripsi Ideogram, peserta didik dapat menentukan keunggulan utamanya dibandingkan AI image generator lain.",
        "tingkat": "Sedang",
        "kunci": "B",
        "soal": (
            "Ideogram adalah salah satu tools AI generatif untuk membuat gambar. Keunggulan utama Ideogram dibandingkan beberapa AI image generator lain adalah ...\n"
            "A. Dapat membuat video panjang berdurasi 1 jam\n"
            "B. Mampu menghasilkan gambar dengan teks (tulisan) di dalam gambar dengan rapi\n"
            "C. Khusus digunakan untuk membuat game 3D\n"
            "D. Hanya bisa digunakan di komputer mahal\n"
            "E. Tidak memerlukan koneksi internet"
        ),
    },
    {
        "no": 16,
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Peserta didik dapat memilih tools AI yang tepat sesuai kebutuhan.",
        "tp": "Peserta didik dapat memilih tools AI untuk membuat poster dengan teks.",
        "indikator_kompetensi": "Menerapkan pemilihan tools AI untuk pembuatan poster.",
        "indikator_soal": "Disajikan kasus pembuatan poster dengan teks menonjol, peserta didik dapat menentukan tools AI yang paling tepat.",
        "tingkat": "Sulit",
        "kunci": "C",
        "soal": (
            "Perhatikan kebutuhan berikut: \"Membuat poster dengan tulisan 'Selamat Hari Pendidikan Nasional' yang menonjol di tengah gambar.\" Tools AI yang paling tepat digunakan untuk tugas tersebut adalah ...\n"
            "A. Gamma.app\n"
            "B. NotebookLM\n"
            "C. Ideogram\n"
            "D. ChatGPT versi teks\n"
            "E. Google Calendar"
        ),
    },
    {
        "no": 17,
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Peserta didik mengenal tools AI untuk produktivitas presentasi.",
        "tp": "Peserta didik dapat menjelaskan fungsi utama Gamma.app.",
        "indikator_kompetensi": "Memahami fungsi Gamma.app.",
        "indikator_soal": "Disajikan deskripsi Gamma.app, peserta didik dapat menentukan fungsi utamanya.",
        "tingkat": "Sedang",
        "kunci": "A",
        "soal": (
            "Gamma.app adalah platform berbasis AI yang sangat membantu siswa dan guru. Fungsi utama Gamma.app adalah ...\n"
            "A. Membuat presentasi, dokumen, dan halaman web secara otomatis berbasis AI\n"
            "B. Membuat lagu dengan instrumen virtual\n"
            "C. Mengedit gambar wajah menjadi karikatur\n"
            "D. Merekam suara untuk podcast\n"
            "E. Memperbaiki sinyal Wi-Fi"
        ),
    },
    {
        "no": 18,
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Peserta didik dapat memilih tools AI yang tepat sesuai kebutuhan.",
        "tp": "Peserta didik dapat memilih tools AI untuk membuat slide presentasi otomatis.",
        "indikator_kompetensi": "Menerapkan pemilihan tools AI untuk presentasi.",
        "indikator_soal": "Disajikan kasus pembuatan slide presentasi otomatis dari poin singkat, peserta didik dapat menentukan tools AI yang tepat.",
        "tingkat": "Sedang",
        "kunci": "B",
        "soal": (
            "Seorang guru ingin membuat slide presentasi tentang \"Pengenalan Koding\" hanya dengan menuliskan beberapa poin singkat, kemudian AI akan menyusun desain dan isinya secara otomatis. Tools yang paling tepat digunakan adalah ...\n"
            "A. Notepad\n"
            "B. Gamma.app\n"
            "C. Dreamina\n"
            "D. NotebookLM\n"
            "E. Kalkulator"
        ),
    },
    {
        "no": 19,
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Peserta didik mengenal tools AI untuk asisten riset/belajar.",
        "tp": "Peserta didik dapat menjelaskan fungsi utama NotebookLM.",
        "indikator_kompetensi": "Memahami fungsi NotebookLM.",
        "indikator_soal": "Disajikan deskripsi NotebookLM, peserta didik dapat menentukan fungsi utamanya.",
        "tingkat": "Sedang",
        "kunci": "C",
        "soal": (
            "NotebookLM adalah produk kecerdasan artifisial yang dikembangkan oleh Google. Fungsi utama NotebookLM adalah ...\n"
            "A. Membuat gambar dari teks\n"
            "B. Membuat video animasi 3D\n"
            "C. Menganalisis, merangkum, dan menjawab pertanyaan berdasarkan sumber/dokumen yang diunggah pengguna\n"
            "D. Membuat aplikasi mobile\n"
            "E. Menggantikan sistem operasi komputer"
        ),
    },
    {
        "no": 20,
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Peserta didik memahami keunggulan tools AI berbasis sumber.",
        "tp": "Peserta didik dapat menjelaskan keunggulan NotebookLM dibandingkan chatbot AI umum.",
        "indikator_kompetensi": "Memahami keunggulan NotebookLM.",
        "indikator_soal": "Disajikan pertanyaan tentang keunggulan NotebookLM, peserta didik dapat menentukan jawaban yang tepat.",
        "tingkat": "Sulit",
        "kunci": "B",
        "soal": (
            "Keunggulan NotebookLM dibandingkan chatbot AI umum adalah jawaban yang diberikan ...\n"
            "A. Selalu lebih cepat dari semua AI lain\n"
            "B. Didasarkan pada sumber/dokumen yang diunggah pengguna sehingga lebih relevan dan terpercaya\n"
            "C. Bisa membuat lukisan digital\n"
            "D. Hanya berbahasa Inggris\n"
            "E. Dapat menjalankan game"
        ),
    },
]

# Essay
ESSAY = [
    {
        "no": 1,
        "elemen": "Algoritma dan Pemrograman",
        "cp": "Peserta didik memahami pengertian koding dan manfaatnya.",
        "tp": "Peserta didik dapat menjelaskan pengertian koding dan menyebutkan manfaatnya bagi pelajar.",
        "indikator_kompetensi": "Memahami pengertian dan manfaat koding.",
        "indikator_soal": "Disajikan narasi tentang pentingnya koding di era digital, peserta didik dapat menjelaskan pengertian koding dan menyebutkan minimal tiga manfaatnya bagi siswa SMK kelas X.",
        "tingkat": "Sedang",
        "soal": (
            "Di era digital seperti sekarang, hampir seluruh aspek kehidupan manusia telah terhubung dengan teknologi. Aplikasi di smartphone, website pemerintah, mesin ATM, hingga sistem absensi sekolah semua bekerja karena adanya kode program yang dirancang oleh manusia. Inilah yang membuat kemampuan koding menjadi salah satu keterampilan penting di abad ke-21, termasuk bagi pelajar SMK.\n"
            "Berdasarkan narasi di atas, jelaskan pengertian koding dan sebutkan minimal tiga manfaat mempelajari koding bagi siswa SMK kelas X!"
        ),
        "jawaban": (
            "Koding adalah proses menuliskan serangkaian instruksi atau perintah menggunakan bahasa pemrograman tertentu agar komputer dapat menjalankan tugas sesuai keinginan pengguna.\n"
            "Manfaat mempelajari koding bagi siswa SMK kelas X (minimal 3):\n"
            "1) Melatih cara berpikir logis, sistematis, dan terstruktur dalam memecahkan masalah.\n"
            "2) Meningkatkan kemampuan problem solving (pemecahan masalah) sehari-hari.\n"
            "3) Membuka peluang karier di bidang teknologi seperti programmer, web developer, mobile developer, atau data analyst.\n"
            "4) Menumbuhkan kreativitas dalam menghasilkan karya digital (aplikasi, game, website).\n"
            "5) Menjadi modal penting untuk berkolaborasi dengan teknologi AI di masa depan."
        ),
    },
    {
        "no": 2,
        "elemen": "Algoritma dan Pemrograman",
        "cp": "Peserta didik memahami algoritma dan dapat menyusunnya untuk masalah sederhana.",
        "tp": "Peserta didik dapat menjelaskan pengertian algoritma dan menyusun algoritma sederhana.",
        "indikator_kompetensi": "Menyusun algoritma sederhana.",
        "indikator_soal": "Disajikan narasi tentang perencanaan program, peserta didik dapat menjelaskan pengertian algoritma dan menuliskan algoritma menentukan bilangan ganjil/genap.",
        "tingkat": "Sedang",
        "soal": (
            "Sebelum membuat sebuah program, seorang programmer biasanya merencanakan langkah-langkahnya terlebih dahulu. Misalnya untuk membuat program \"menentukan apakah suatu bilangan ganjil atau genap\", programmer akan menulis urutan langkahnya dari awal hingga akhir. Tahapan inilah yang menjadi fondasi setiap program komputer.\n"
            "Jelaskan pengertian algoritma, lalu tuliskan algoritma sederhana untuk menentukan suatu bilangan ganjil atau genap!"
        ),
        "jawaban": (
            "Algoritma adalah urutan langkah-langkah logis dan sistematis yang disusun untuk menyelesaikan suatu masalah atau mencapai tujuan tertentu.\n"
            "Algoritma menentukan bilangan ganjil atau genap:\n"
            "1) Mulai\n"
            "2) Masukkan sebuah bilangan (misal n)\n"
            "3) Bagi n dengan 2, ambil sisa baginya (n mod 2)\n"
            "4) Jika sisa bagi = 0, maka bilangan tersebut GENAP\n"
            "5) Jika sisa bagi ≠ 0, maka bilangan tersebut GANJIL\n"
            "6) Tampilkan hasil\n"
            "7) Selesai"
        ),
    },
    {
        "no": 3,
        "elemen": "Algoritma dan Pemrograman",
        "cp": "Peserta didik memahami konsep variabel dan tipe data.",
        "tp": "Peserta didik dapat menjelaskan pengertian variabel, tipe data, beserta contohnya.",
        "indikator_kompetensi": "Menjelaskan konsep variabel dan tipe data.",
        "indikator_soal": "Disajikan narasi tentang kebutuhan penyimpanan data dalam program, peserta didik dapat menjelaskan variabel & tipe data beserta dua contoh tipe data.",
        "tingkat": "Sedang",
        "soal": (
            "Saat membuat program, kita sering membutuhkan tempat untuk menyimpan nilai sementara, misalnya nama siswa, nilai ujian, atau jumlah barang. Setiap data tersebut memiliki jenis yang berbeda-beda sehingga harus diberi \"wadah\" yang tepat.\n"
            "Jelaskan apa yang dimaksud dengan variabel dan tipe data, lalu berikan masing-masing dua contoh tipe data beserta contoh nilainya!"
        ),
        "jawaban": (
            "Variabel adalah tempat penyimpanan sementara di memori komputer yang digunakan untuk menyimpan nilai/data yang dapat berubah selama program berjalan.\n"
            "Tipe data adalah jenis data yang dapat disimpan oleh sebuah variabel.\n"
            "Contoh tipe data (minimal 2):\n"
            "1) Integer (bilangan bulat) – contoh: umur = 16\n"
            "2) String (teks) – contoh: nama = \"Andi\"\n"
            "3) Float (bilangan desimal) – contoh: nilai = 87.5\n"
            "4) Boolean (benar/salah) – contoh: lulus = True"
        ),
    },
    {
        "no": 4,
        "elemen": "Algoritma dan Pemrograman",
        "cp": "Peserta didik memahami struktur percabangan dan perulangan.",
        "tp": "Peserta didik dapat menjelaskan perbedaan percabangan dan perulangan beserta contohnya.",
        "indikator_kompetensi": "Membedakan percabangan dan perulangan.",
        "indikator_soal": "Disajikan narasi tentang struktur kontrol program, peserta didik dapat menjelaskan perbedaan percabangan dan perulangan beserta contoh kehidupan sehari-hari.",
        "tingkat": "Sedang",
        "soal": (
            "Dalam pemrograman, kita mengenal dua struktur yang sangat sering digunakan, yaitu percabangan (selection) dan perulangan (looping). Keduanya membuat program menjadi lebih cerdas karena dapat mengambil keputusan dan melakukan tugas secara otomatis berulang kali.\n"
            "Jelaskan perbedaan antara percabangan dan perulangan, lalu berikan contoh penggunaannya dalam kehidupan sehari-hari!"
        ),
        "jawaban": (
            "Percabangan (selection) adalah struktur kontrol yang digunakan untuk mengambil keputusan berdasarkan kondisi tertentu. Jika kondisi terpenuhi, program menjalankan satu blok perintah; jika tidak, program menjalankan blok perintah lain.\n"
            "Perulangan (looping) adalah struktur kontrol yang digunakan untuk menjalankan sekumpulan perintah secara berulang selama kondisi tertentu masih terpenuhi.\n"
            "Contoh percabangan: program penentuan kelulusan siswa – jika nilai ≥ 75 maka \"LULUS\", jika tidak maka \"TIDAK LULUS\".\n"
            "Contoh perulangan: program menampilkan angka 1–10, atau mesin ATM yang terus menampilkan menu sampai pengguna memilih \"keluar\"."
        ),
    },
    {
        "no": 5,
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Peserta didik memahami konsep prompt dan dapat menyusun prompt yang baik.",
        "tp": "Peserta didik dapat menjelaskan prompt dan menyusun contoh prompt yang baik.",
        "indikator_kompetensi": "Menyusun prompt yang baik pada ChatGPT.",
        "indikator_soal": "Disajikan narasi tentang penggunaan ChatGPT, peserta didik dapat menjelaskan pengertian prompt, pentingnya prompt yang baik, dan menyusun contoh prompt belajar matematika.",
        "tingkat": "Sedang",
        "soal": (
            "ChatGPT adalah salah satu chatbot AI yang sangat populer dan banyak digunakan oleh pelajar untuk membantu belajar, mencari referensi, atau memahami materi yang sulit. Akan tetapi, kualitas jawaban yang diberikan oleh ChatGPT sangat bergantung pada bagaimana pengguna memberikan instruksi atau pertanyaan.\n"
            "Jelaskan apa yang dimaksud dengan prompt pada ChatGPT, mengapa prompt yang baik itu penting, dan berikan satu contoh prompt yang baik untuk membantu belajar matematika!"
        ),
        "jawaban": (
            "Prompt adalah instruksi, pertanyaan, atau perintah yang diketikkan pengguna kepada AI (ChatGPT) untuk menghasilkan respon/jawaban.\n"
            "Pentingnya prompt yang baik: semakin jelas, spesifik, dan terstruktur prompt yang diberikan, semakin relevan dan akurat jawaban yang dihasilkan AI. Prompt yang kabur akan menghasilkan jawaban yang melenceng dari kebutuhan pengguna.\n"
            "Contoh prompt yang baik untuk belajar matematika:\n"
            "\"Tolong jelaskan langkah demi langkah cara menyelesaikan soal Sistem Persamaan Linear Dua Variabel (SPLDV) untuk siswa SMK kelas X dengan bahasa sederhana, lalu berikan satu contoh soal beserta penyelesaiannya secara rinci.\""
        ),
    },
    {
        "no": 6,
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Peserta didik memahami cara kerja dan manfaat tools AI generatif visual (Dreamina).",
        "tp": "Peserta didik dapat menjelaskan cara kerja Dreamina dan manfaatnya bagi pelajar.",
        "indikator_kompetensi": "Memahami cara kerja dan manfaat Dreamina.",
        "indikator_soal": "Disajikan narasi tentang Dreamina, peserta didik dapat menjelaskan cara kerja secara umum dan menyebutkan minimal tiga manfaat penggunaannya bagi pelajar.",
        "tingkat": "Sedang",
        "soal": (
            "Dreamina adalah platform AI dari ByteDance yang memungkinkan pengguna membuat gambar maupun video pendek hanya dengan mendeskripsikan keinginannya dalam bentuk teks. Dengan teknologi ini, siapa saja, termasuk pelajar, bisa menjadi kreator konten visual tanpa harus mahir menggambar atau mengedit video.\n"
            "Jelaskan bagaimana cara kerja Dreamina secara umum dan sebutkan minimal tiga manfaat penggunaan Dreamina bagi pelajar!"
        ),
        "jawaban": (
            "Cara kerja Dreamina secara umum: pengguna memasukkan deskripsi teks (prompt) yang menggambarkan gambar atau video yang diinginkan. AI di balik Dreamina memproses teks tersebut menggunakan model generatif yang telah dilatih dengan jutaan data gambar dan video, kemudian menghasilkan gambar/video sesuai deskripsi pengguna. Pengguna dapat menambahkan gaya, sudut pandang, warna, atau detail lainnya untuk menyempurnakan hasil.\n"
            "Manfaat penggunaan Dreamina bagi pelajar (minimal 3):\n"
            "1) Membantu pembuatan tugas visual seperti ilustrasi, poster, atau infografis.\n"
            "2) Merangsang kreativitas dan imajinasi siswa.\n"
            "3) Menghemat waktu pembuatan konten dibandingkan menggambar manual.\n"
            "4) Mengenalkan siswa pada teknologi AI generatif yang relevan untuk dunia industri kreatif."
        ),
    },
    {
        "no": 7,
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Peserta didik memahami keunggulan dan pemanfaatan Ideogram.",
        "tp": "Peserta didik dapat menjelaskan keunggulan Ideogram dan memberikan contoh tugas yang cocok dibuat.",
        "indikator_kompetensi": "Memahami keunggulan dan pemanfaatan Ideogram.",
        "indikator_soal": "Disajikan narasi tentang Ideogram, peserta didik dapat menjelaskan keunggulan utamanya dan memberikan minimal dua contoh tugas/karya yang cocok dibuat.",
        "tingkat": "Sedang",
        "soal": (
            "Ideogram menjadi salah satu tools AI image generator yang banyak diminati karena memiliki keunggulan khas dibandingkan tools serupa, yaitu kemampuannya menampilkan teks/tulisan di dalam gambar dengan rapi. Hal ini menjadikan Ideogram sangat berguna untuk membuat poster, logo, dan konten visual yang mengandung kata-kata.\n"
            "Jelaskan keunggulan utama Ideogram dibandingkan beberapa AI image generator lainnya, dan berikan minimal dua contoh tugas/karya yang cocok dibuat menggunakan Ideogram!"
        ),
        "jawaban": (
            "Keunggulan utama Ideogram adalah kemampuannya menghasilkan gambar yang memuat tulisan/teks dengan rapi dan akurat – sesuatu yang sering menjadi kelemahan AI image generator lain (tulisan biasanya rusak, salah eja, atau buram). Ideogram juga menyediakan berbagai pilihan style visual serta komposisi gambar yang baik.\n"
            "Contoh tugas/karya yang cocok dibuat dengan Ideogram (minimal 2):\n"
            "1) Poster kegiatan sekolah dengan judul kegiatan yang menonjol.\n"
            "2) Logo organisasi atau ekstrakurikuler yang memuat nama organisasi.\n"
            "3) Sampul (cover) tugas atau laporan dengan judul mata pelajaran.\n"
            "4) Banner ucapan hari besar (misalnya \"Selamat Hari Pendidikan Nasional\")."
        ),
    },
    {
        "no": 8,
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Peserta didik memahami cara kerja dan manfaat Gamma.app.",
        "tp": "Peserta didik dapat menjelaskan cara kerja Gamma.app dan manfaatnya bagi siswa dan guru.",
        "indikator_kompetensi": "Memahami cara kerja dan manfaat Gamma.app.",
        "indikator_soal": "Disajikan narasi tentang Gamma.app, peserta didik dapat menjelaskan cara kerjanya dan menyebutkan minimal tiga manfaatnya bagi siswa dan guru.",
        "tingkat": "Sulit",
        "soal": (
            "Membuat presentasi yang menarik biasanya membutuhkan waktu yang lama, terutama untuk mendesain tata letak slide dan mencari ilustrasi. Gamma.app hadir sebagai solusi berbasis AI yang dapat membuat presentasi, dokumen, hingga halaman web secara otomatis hanya dari beberapa poin atau topik singkat.\n"
            "Jelaskan bagaimana cara kerja Gamma.app dan sebutkan minimal tiga manfaatnya bagi siswa dan guru!"
        ),
        "jawaban": (
            "Cara kerja Gamma.app: pengguna memasukkan topik atau poin-poin utama yang ingin dibahas. Gamma.app dengan dukungan AI akan secara otomatis menyusun struktur slide/dokumen, memilih tata letak (layout), menambahkan ikon/ilustrasi yang relevan, serta menyusun teks isi untuk setiap slide. Pengguna kemudian dapat mengedit, menambah, atau mengganti elemen sesuai kebutuhan.\n"
            "Manfaat bagi siswa dan guru (minimal 3):\n"
            "1) Menghemat waktu pembuatan presentasi karena sebagian besar bagian dibuat otomatis.\n"
            "2) Menghasilkan desain yang rapi dan profesional tanpa harus ahli desain.\n"
            "3) Membantu siswa fokus pada isi/konten daripada urusan teknis desain.\n"
            "4) Memudahkan guru menyiapkan bahan ajar dengan cepat.\n"
            "5) Hasil dapat dibagikan dalam berbagai format (slide, PDF, atau halaman web)."
        ),
    },
    {
        "no": 9,
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Peserta didik memahami cara kerja dan manfaat NotebookLM.",
        "tp": "Peserta didik dapat menjelaskan cara kerja NotebookLM dan manfaatnya bagi siswa.",
        "indikator_kompetensi": "Memahami cara kerja dan manfaat NotebookLM.",
        "indikator_soal": "Disajikan narasi tentang NotebookLM, peserta didik dapat menjelaskan cara kerjanya dan menyebutkan minimal tiga manfaatnya bagi siswa.",
        "tingkat": "Sulit",
        "soal": (
            "NotebookLM adalah salah satu produk AI dari Google yang dirancang khusus untuk membantu pengguna memahami, merangkum, dan menggali informasi dari sumber-sumber yang mereka unggah sendiri, seperti file PDF, dokumen, atau catatan. Berbeda dengan chatbot AI pada umumnya, jawaban yang diberikan NotebookLM selalu mengacu pada sumber yang telah diunggah.\n"
            "Jelaskan bagaimana cara kerja NotebookLM dan sebutkan minimal tiga manfaatnya untuk mendukung belajar siswa!"
        ),
        "jawaban": (
            "Cara kerja NotebookLM: pengguna mengunggah satu atau beberapa sumber referensi (PDF, dokumen Google Docs, teks, link, atau catatan). NotebookLM kemudian membaca dan menganalisis isi seluruh sumber tersebut. Pengguna dapat mengajukan pertanyaan, meminta ringkasan, outline, atau kuis, dan NotebookLM akan menjawab berdasarkan isi sumber yang diunggah (source-grounded) lengkap dengan rujukan ke bagian sumber tertentu.\n"
            "Manfaat untuk mendukung belajar siswa (minimal 3):\n"
            "1) Memudahkan memahami materi pelajaran yang panjang karena bisa diringkas otomatis.\n"
            "2) Jawaban lebih terpercaya karena bersumber dari materi yang diunggah, bukan karangan AI.\n"
            "3) Membantu membuat ringkasan/catatan/peta materi untuk persiapan ujian.\n"
            "4) Dapat digunakan untuk membuat kuis latihan dari materi yang sudah dipelajari.\n"
            "5) Menghemat waktu belajar dengan menemukan jawaban langsung dari halaman sumber."
        ),
    },
    {
        "no": 10,
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Peserta didik dapat membandingkan berbagai tools AI dan memilih yang tepat.",
        "tp": "Peserta didik dapat membandingkan fungsi utama ChatGPT, Dreamina, Ideogram, Gamma.app, dan NotebookLM.",
        "indikator_kompetensi": "Membandingkan fungsi tools AI populer.",
        "indikator_soal": "Disajikan narasi tentang berbagai tools AI, peserta didik dapat membuat daftar fungsi utama dari ChatGPT, Dreamina, Ideogram, Gamma.app, dan NotebookLM.",
        "tingkat": "Sulit",
        "soal": (
            "Saat ini ada banyak sekali tools berbasis kecerdasan artifisial yang dapat digunakan pelajar, di antaranya ChatGPT, Dreamina, Ideogram, Gamma.app, dan NotebookLM. Masing-masing tools memiliki fungsi utama yang berbeda. Memahami perbedaan ini penting agar pelajar dapat memilih tools yang tepat sesuai dengan kebutuhan tugasnya.\n"
            "Buatlah daftar yang menjelaskan fungsi utama dari masing-masing tools berikut: ChatGPT, Dreamina, Ideogram, Gamma.app, dan NotebookLM!"
        ),
        "jawaban": (
            "1) ChatGPT: chatbot AI berbasis teks (OpenAI) yang berfungsi menjawab pertanyaan, menjelaskan materi, membantu menulis teks/essay/kode, dan berdiskusi melalui prompt.\n"
            "2) Dreamina: AI generatif dari ByteDance untuk membuat gambar dan video pendek dari deskripsi teks (text-to-image & text-to-video).\n"
            "3) Ideogram: AI image generator yang unggul dalam membuat gambar dengan tulisan/teks rapi di dalamnya – cocok untuk poster, logo, dan banner.\n"
            "4) Gamma.app: platform AI berbasis web untuk membuat presentasi, dokumen, dan halaman web secara otomatis dari topik/poin yang dimasukkan pengguna.\n"
            "5) NotebookLM: AI dari Google sebagai asisten riset/belajar pribadi yang memberi ringkasan, jawaban, dan penjelasan berdasarkan sumber/dokumen yang diunggah pengguna (source-grounded)."
        ),
    },
]

# =====================================================================
# HELPERS
# =====================================================================

W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

def set_cell_text(cell, lines, bold=False, size=None):
    """Replace cell content with given lines (list of strings or one string)."""
    if isinstance(lines, str):
        lines = lines.split('\n')
    # Clear existing paragraphs
    tc = cell._tc
    # Remove all existing w:p children of tc
    for p in tc.findall(qn('w:p')):
        tc.remove(p)
    # Add new paragraphs
    for line in lines:
        p = cell.add_paragraph()
        # set tight spacing
        pPr = p._p.get_or_add_pPr()
        spacing = pPr.find(qn('w:spacing'))
        from docx.oxml import OxmlElement
        if spacing is None:
            spacing = OxmlElement('w:spacing')
            pPr.append(spacing)
        spacing.set(qn('w:after'), '0')
        spacing.set(qn('w:line'), '240')
        spacing.set(qn('w:lineRule'), 'auto')
        run = p.add_run(line if line else '')
        run.font.name = 'Calibri'
        if size:
            run.font.size = docx.shared.Pt(size)
        if bold:
            run.bold = True


def set_question_cell(cell, no, soal_text, kunci=None):
    """For the big question area (col 3 in row 3-13). Adds 'No. Soal: N' then soal."""
    tc = cell._tc
    for p in tc.findall(qn('w:p')):
        tc.remove(p)
    from docx.oxml import OxmlElement
    # Soal lines
    for line in soal_text.split('\n'):
        p = cell.add_paragraph()
        pPr = p._p.get_or_add_pPr()
        spacing = pPr.find(qn('w:spacing'))
        if spacing is None:
            spacing = OxmlElement('w:spacing')
            pPr.append(spacing)
        spacing.set(qn('w:after'), '0')
        spacing.set(qn('w:line'), '276')
        spacing.set(qn('w:lineRule'), 'auto')
        run = p.add_run(line if line else '')
        run.font.name = 'Calibri'
        run.font.size = docx.shared.Pt(11)


# =====================================================================
# 1. Fill header paragraphs (Nama Guru, Mata Pelajaran, Kelas at body 14-16)
# =====================================================================

def fill_header_para(paragraph, prefix, value):
    """Replace 'X:.....' style content with 'X : value'."""
    # Clear runs
    p_el = paragraph._p
    for r in p_el.findall(qn('w:r')):
        p_el.remove(r)
    from docx.oxml import OxmlElement
    r = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:ascii'), 'Calibri')
    rFonts.set(qn('w:hAnsi'), 'Calibri')
    rPr.append(rFonts)
    sz = OxmlElement('w:sz')
    sz.set(qn('w:val'), '24')
    rPr.append(sz)
    r.append(rPr)
    t = OxmlElement('w:t')
    t.text = f"{prefix} : {value}"
    t.set(qn('xml:space'), 'preserve')
    r.append(t)
    p_el.append(r)


# Find and fill cover page paragraphs
for p in doc.paragraphs:
    txt = p.text.strip()
    if txt.startswith("Nama  Guru") or txt.startswith("Nama Guru"):
        fill_header_para(p, "Nama Guru", NAMA_GURU)
    elif txt.startswith("Mata Pelajaran"):
        fill_header_para(p, "Mata Pelajaran", f"{MAPEL} / Kelas {KELAS}")
    elif txt.startswith("Kelas"):
        fill_header_para(p, "Kelas", KELAS)


# =====================================================================
# 2. Fill Table 0 (intro header table) with school info
# =====================================================================
# Table 0 has 1 row 1 col with multiline content. Let's fill it.
t0 = doc.tables[0]
cell0 = t0.rows[0].cells[0]
intro_lines = [
    f"Nama Sekolah\t    : SMK 1 PANCASILA",
    f"Nama Penulis Soal\t: {NAMA_GURU}",
    f"Mata Pelajaran/Kelas\t: {MAPEL} / Kelas {KELAS}",
    f"Satuan Unit Kerja\t: SMK 1 PANCASILA AMBULU",
    f"Kurikulum\t\t: Kurikulum Merdeka",
    f"Jumlah Soal\t\t: 30 butir (20 PG + 10 Esay)",
]
set_cell_text(cell0, intro_lines, size=11)


# =====================================================================
# 3. Fill Kisi-kisi table (Table 1) – grid 12 rows x 9 cols
#    Row 0 = header (PG section), Rows 1-4 = 4 entries (PG)
#    Row 5 = header (Essay section), Rows 6-10 = 5 entries (Essay)
#    Row 11 = JUMLAH SOAL
# =====================================================================

t1 = doc.tables[1]

# PG kisi-kisi (4 entries)
pg_kisi = [
    {
        "no": "1",
        "elemen": "Algoritma dan Pemrograman",
        "cp": "Memahami konsep dasar koding, algoritma, dan flowchart.",
        "tp": "Menjelaskan pengertian koding, algoritma, dan representasi visual algoritma.",
        "jml": "4",
        "no_soal": "1 - 4",
        "bentuk": "PG",
        "tingkat": "Rendah",
    },
    {
        "no": "2",
        "elemen": "Algoritma dan Pemrograman",
        "cp": "Memahami variabel, tipe data, dan struktur kontrol program.",
        "tp": "Mengidentifikasi variabel, tipe data, perulangan, percabangan, debugging, komentar, dan bahasa pemrograman untuk pemula.",
        "jml": "6",
        "no_soal": "5 - 10",
        "bentuk": "PG",
        "tingkat": "Sedang",
    },
    {
        "no": "3",
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Memahami fungsi tools AI berbasis teks dan AI generatif visual.",
        "tp": "Menjelaskan fungsi ChatGPT, prompt, Dreamina, dan Ideogram.",
        "jml": "5",
        "no_soal": "11 - 15",
        "bentuk": "PG",
        "tingkat": "Sedang",
    },
    {
        "no": "4",
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Memahami fungsi tools AI untuk produktivitas dan riset.",
        "tp": "Menjelaskan fungsi Gamma.app dan NotebookLM serta memilih tools AI yang tepat.",
        "jml": "5",
        "no_soal": "16 - 20",
        "bentuk": "PG",
        "tingkat": "Sedang/Sulit",
    },
]

# Essay kisi-kisi (5 entries)
essay_kisi = [
    {
        "no": "1",
        "elemen": "Algoritma dan Pemrograman",
        "cp": "Memahami pengertian dan manfaat koding.",
        "tp": "Menjelaskan pengertian koding dan manfaatnya bagi pelajar SMK.",
        "jml": "1",
        "no_soal": "1",
        "bentuk": "Esay",
        "tingkat": "Sedang",
    },
    {
        "no": "2",
        "elemen": "Algoritma dan Pemrograman",
        "cp": "Memahami algoritma, variabel, tipe data, percabangan, dan perulangan.",
        "tp": "Menjelaskan dan menyusun algoritma, menjelaskan variabel & tipe data, serta membedakan percabangan dan perulangan.",
        "jml": "3",
        "no_soal": "2 - 4",
        "bentuk": "Esay",
        "tingkat": "Sedang",
    },
    {
        "no": "3",
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Memahami konsep prompt pada ChatGPT.",
        "tp": "Menjelaskan prompt dan menyusun contoh prompt yang baik.",
        "jml": "1",
        "no_soal": "5",
        "bentuk": "Esay",
        "tingkat": "Sedang",
    },
    {
        "no": "4",
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Memahami cara kerja dan manfaat AI generatif visual (Dreamina, Ideogram).",
        "tp": "Menjelaskan cara kerja Dreamina, manfaatnya, serta keunggulan dan pemanfaatan Ideogram.",
        "jml": "2",
        "no_soal": "6 - 7",
        "bentuk": "Esay",
        "tingkat": "Sedang",
    },
    {
        "no": "5",
        "elemen": "Kecerdasan Artifisial (AI)",
        "cp": "Memahami tools AI produktivitas, riset, dan membandingkan berbagai tools AI.",
        "tp": "Menjelaskan Gamma.app, NotebookLM, dan membandingkan fungsi 5 tools AI.",
        "jml": "3",
        "no_soal": "8 - 10",
        "bentuk": "Esay",
        "tingkat": "Sulit",
    },
]


def fill_kisi_row(row, entry):
    """Fill columns 0..8 with the entry data. Columns 3 & 4 are merged so write to col3 only."""
    cells = row.cells
    # Note: in the kisi-kisi the columns are merged differently
    # Col mapping: 0=No, 1=Elemen, 2=CP, 3=TP (merged with 4), 5=Jml, 6=No Soal, 7=Bentuk, 8=Tingkat
    set_cell_text(cells[0], entry["no"], size=10)
    set_cell_text(cells[1], entry["elemen"], size=10)
    set_cell_text(cells[2], entry["cp"], size=10)
    set_cell_text(cells[3], entry["tp"], size=10)
    set_cell_text(cells[5], entry["jml"], size=10)
    set_cell_text(cells[6], entry["no_soal"], size=10)
    set_cell_text(cells[7], entry["bentuk"], size=10)
    set_cell_text(cells[8], entry["tingkat"], size=10)


# PG kisi-kisi rows 1-4
for i, entry in enumerate(pg_kisi):
    fill_kisi_row(t1.rows[1 + i], entry)

# Essay kisi-kisi rows 6-10
for i, entry in enumerate(essay_kisi):
    fill_kisi_row(t1.rows[6 + i], entry)

# JUMLAH SOAL row 11 - total: PG=20, Essay=10, total=30
# Col 5 (Jml) shows total
set_cell_text(t1.rows[11].cells[5], "30", size=10, bold=True)
set_cell_text(t1.rows[11].cells[6], "PG: 1-20\nEsay: 1-10", size=10, bold=True)


# =====================================================================
# 4. Duplicate PG kartu soal to reach 20 (we have 13, need 7 more)
#    PG tables at body[37,39,...,61]. Last PG table = body[61], followed by para body[62].
#    Duplicate (table + paragraph) 7 times and insert after body[62].
# =====================================================================

# Re-read body since python-docx tables are kept in sync
elements = list(body)
last_pg_tbl = elements[61]
last_pg_para = elements[62]

# Insert 7 duplicates after body[62]
insert_after = last_pg_para
for _ in range(7):
    new_tbl = deepcopy(last_pg_tbl)
    new_para = deepcopy(last_pg_para)
    insert_after.addnext(new_tbl)
    new_tbl.addnext(new_para)
    insert_after = new_para


# =====================================================================
# 5. Now the document has more tables. Fill PG kartu soal cards 1..20.
#    Refresh document.tables - python-docx auto-refreshes
# =====================================================================

# Re-read tables
all_tables = doc.tables
# After insertion:
# Table 0 = intro header, Table 1 = kisi-kisi
# Tables 2..21 = 20 PG cards
# Tables 22..(22+21-1)=42 = 21 essay cards
# We will keep only first 10 essays (tables 22..31), delete tables 32..42

print(f"Total tables after PG duplication: {len(all_tables)}")
# Expected: 2 + 20 + 21 = 43

assert len(all_tables) == 43, f"Expected 43 tables, got {len(all_tables)}"


def fill_kartu_soal(table, item, is_essay=False):
    """Fill a kartu soal table with the given item."""
    # Col 0: rows 1-13 carries the labels and values
    # Let's set:
    #   rows 1-2: Elemen Kompetensi
    #   rows 3-4: (filled value of elemen, since template uses row 0=label?)
    # Actually based on inspection:
    #   row 1 col 0: 'Elemen Kompetensi' (label)
    #   row 2 col 0: 'Jangan sampai lupa. Di isi' (value placeholder for elemen)
    #   row 3 col 0: same value placeholder
    #   row 4 col 0: 'Capaian Pembelajaran:' (label)
    #   row 5 col 0: 'Capaian Pembelajaran:' (label, merged)
    #   row 6 col 0: 'Jangan lupa di isi' (value for CP)
    #   row 7 col 0: 'Jangan lupa di isi' (value for CP, merged)
    #   row 8 col 0: 'Jangan lupa di isi' (value for CP, merged)
    #   row 9 col 0: 'Indikator Pencapaian Kompetensi:'
    #   row 10 col 0: 'Jangan Lupa di isi' (value)
    #   row 11 col 0: 'Indikator Soal / Indikator Asessmen:'
    #   row 12 col 0: 'Jangan lupa di isi' (value)
    #   row 13 col 0: 'Bapak ibu sesiiakan\nTingkat Kesukaran:...'

    # Due to merged cells, when we set cell at (r, c), it may affect multiple rows
    # We'll set the *value* cells (the second cell of each label).

    rows = table.rows
    # Elemen Kompetensi value: row 2/3 col 0 - they refer to the SAME tc (merged)
    set_cell_text(rows[2].cells[0], item["elemen"], size=10)
    # Capaian Pembelajaran value: rows 6,7,8 col 0 (merged)
    set_cell_text(rows[6].cells[0], item["cp"], size=10)
    # Indikator Pencapaian Kompetensi value: row 10 col 0
    set_cell_text(rows[10].cells[0], item["indikator_kompetensi"], size=10)
    # Indikator Soal value: row 12 col 0
    set_cell_text(rows[12].cells[0], item["indikator_soal"], size=10)
    # Tingkat Kesukaran: row 13 col 0
    set_cell_text(rows[13].cells[0], [
        "Tingkat Kesukaran:",
        f"☑ {item['tingkat']}",
    ], size=10)

    # No. Soal value: row 5 col 2
    set_cell_text(rows[5].cells[2], str(item["no"]), size=12, bold=True)
    # NILAI value: row 8 col 2 - leave blank
    # KUNCI JAWABAN value: rows 11/12/13 col 2 (merged)
    if not is_essay:
        # Single letter
        set_cell_text(rows[11].cells[2], [
            "KUNCI JAWABAN",
            "",
            item["kunci"],
        ], size=12, bold=True)
    else:
        # Essay - put short rubric note
        set_cell_text(rows[11].cells[2], [
            "PEDOMAN JAWABAN",
            "(lihat kunci jawaban di bawah)",
        ], size=10, bold=True)

    # Question content: col 3, rows 3-13 (one merged tc that spans many rows)
    # Set the question content in row 3 col 3
    soal_lines = item["soal"].split('\n')
    if is_essay:
        # Append jawaban
        content = list(soal_lines)
        content.append("")
        content.append("Kunci Jawaban / Pedoman Penskoran:")
        content.extend(item["jawaban"].split('\n'))
    else:
        content = soal_lines
    set_question_cell(rows[3].cells[3], item["no"], '\n'.join(content), kunci=item.get("kunci"))


# Fill PG cards (tables 2..21)
for i, item in enumerate(PG):
    table = doc.tables[2 + i]
    fill_kartu_soal(table, item, is_essay=False)
print("Filled 20 PG kartu soal")


# =====================================================================
# 6. Delete excess essay tables (we have 21, keep 10, delete 11)
# =====================================================================

# Re-read body
elements = list(body)
# Find all tbl elements
tbl_indexes = [i for i, e in enumerate(elements) if e.tag.split('}')[-1] == 'tbl']
print(f"Total tables in body: {len(tbl_indexes)}")
# tbl_indexes[0] = intro, [1] = kisi-kisi, [2..21] = 20 PG, [22..42] = 21 essay
# We want to keep indices 22..31 (first 10 essay), delete 32..42 (last 11 essay)

# Delete tables 32..42 and their *following* paragraph
to_delete_tbl_idx = tbl_indexes[32:]  # 11 tables to delete
print(f"Will delete {len(to_delete_tbl_idx)} essay tables")

# Collect xml elements to remove
to_remove = []
for ti in to_delete_tbl_idx:
    tbl = elements[ti]
    to_remove.append(tbl)
    # Following paragraph
    if ti + 1 < len(elements):
        next_el = elements[ti + 1]
        if next_el.tag.split('}')[-1] == 'p':
            to_remove.append(next_el)

# Don't remove the final sectPr / paragraph that contains sectPr
# Check the last paragraph - if it contains sectPr, don't remove
final_keep = []
for el in to_remove:
    has_sect = el.find('.//' + qn('w:sectPr')) is not None
    if has_sect:
        continue
    final_keep.append(el)

for el in final_keep:
    el.getparent().remove(el)


# =====================================================================
# 7. Fill the remaining 10 essay tables
# =====================================================================

# Re-read tables
all_tables = doc.tables
print(f"Total tables after essay deletion: {len(all_tables)}")
# Expected: 2 + 20 + 10 = 32

assert len(all_tables) == 32, f"Expected 32 tables, got {len(all_tables)}"

# Essay cards are tables 22..31
for i, item in enumerate(ESSAY):
    table = doc.tables[22 + i]
    fill_kartu_soal(table, item, is_essay=True)
print("Filled 10 essay kartu soal")


# =====================================================================
# 8. Update KARTU SOAL header for essay cards (they currently say "KARTU SOAL ESAY/URAIAN" - we keep that)
#    Also for cover page, replace placeholder paragraphs with actual data on cover
# =====================================================================

# Save
import os
os.makedirs('/tmp/out', exist_ok=True)
output_path = '/tmp/out/KARTU_SOAL_KKA_Kelas_X_Genap_2025_2026.docx'
doc.save(output_path)
print(f"\nSaved to: {output_path}")
EOF
