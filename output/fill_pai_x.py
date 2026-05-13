"""Fill the exam template docx with PAI Kelas X exam questions."""
import docx
from docx.oxml.ns import qn
from copy import deepcopy

SRC = '/root/.claude/uploads/b3a0fb48-92a3-493e-8b53-f0a69f1f7e44/ea778bad-KARTU_SOAL_UasGENAP_2526okeaslikosongan.docx'

doc = docx.Document(SRC)
body = doc.element.body


# =====================================================================
# CONFIG
# =====================================================================
NAMA_GURU = "NUR LAILY FAUZIYAH, S.Pd.I."
MAPEL = "Pendidikan Agama Islam (PAI)"
KELAS = "X (Sepuluh)"
TAHUN = "2025/2026"


# =====================================================================
# QUESTIONS - PG
# =====================================================================
PG = [
    # ===== BAB 1: LARANGAN PERGAULAN BEBAS DAN ZINA (5 soal) =====
    {
        "no": 1, "bab": "Larangan Pergaulan Bebas dan Perbuatan Zina",
        "elemen": "Akhlak – Larangan Pergaulan Bebas dan Zina",
        "cp": "Peserta didik memahami pengertian pergaulan bebas dan bahayanya.",
        "tp": "Peserta didik dapat menjelaskan pengertian pergaulan bebas.",
        "indikator_kompetensi": "Memahami pengertian pergaulan bebas.",
        "indikator_soal": "Disajikan narasi tentang fenomena remaja, peserta didik dapat menentukan pengertian pergaulan bebas yang tepat.",
        "tingkat": "Rendah", "kunci": "B",
        "soal": (
            "Pergaulan bebas menjadi salah satu masalah serius di kalangan remaja saat ini. Islam dengan tegas melarang segala bentuk pergaulan yang melampaui batas-batas syariat. Pengertian pergaulan bebas yang paling tepat adalah ...\n"
            "A. Pergaulan antara teman sebaya di sekolah dalam belajar bersama\n"
            "B. Pergaulan tanpa batas antara laki-laki dan perempuan yang melanggar norma agama dan susila\n"
            "C. Pergaulan dalam keluarga inti yang harmonis\n"
            "D. Pergaulan dalam organisasi yang bermanfaat\n"
            "E. Pergaulan dengan tetangga yang akrab"
        ),
    },
    {
        "no": 2, "bab": "Larangan Pergaulan Bebas dan Perbuatan Zina",
        "elemen": "Akhlak – Larangan Pergaulan Bebas dan Zina",
        "cp": "Peserta didik memahami QS Al-Isra ayat 32 tentang larangan zina.",
        "tp": "Peserta didik dapat menjelaskan kandungan QS Al-Isra ayat 32.",
        "indikator_kompetensi": "Memahami kandungan QS Al-Isra ayat 32.",
        "indikator_soal": "Disajikan kandungan QS Al-Isra ayat 32, peserta didik dapat menentukan makna ayat tersebut.",
        "tingkat": "Sedang", "kunci": "C",
        "soal": (
            "Allah Swt. berfirman dalam QS Al-Isra ayat 32: \"Wa la taqrabuz-zina, innahu kana fahisyatan wa sa'a sabila.\" Kandungan ayat tersebut adalah ...\n"
            "A. Perintah untuk segera menikah\n"
            "B. Larangan berbuat baik kepada orang tua\n"
            "C. Larangan mendekati zina karena zina merupakan perbuatan keji dan jalan yang buruk\n"
            "D. Perintah untuk berpuasa\n"
            "E. Larangan memakan harta riba"
        ),
    },
    {
        "no": 3, "bab": "Larangan Pergaulan Bebas dan Perbuatan Zina",
        "elemen": "Fikih – Larangan Pergaulan Bebas dan Zina",
        "cp": "Peserta didik memahami macam-macam zina.",
        "tp": "Peserta didik dapat membedakan zina muhshan dan ghairu muhshan.",
        "indikator_kompetensi": "Membedakan macam-macam zina.",
        "indikator_soal": "Disajikan definisi macam zina, peserta didik dapat menentukan jenis zina muhshan.",
        "tingkat": "Sedang", "kunci": "B",
        "soal": (
            "Para ulama fikih membagi zina menjadi dua, yaitu zina muhshan dan zina ghairu muhshan. Zina muhshan adalah perbuatan zina yang dilakukan oleh ...\n"
            "A. Orang yang belum pernah menikah\n"
            "B. Orang yang sudah pernah menikah secara sah\n"
            "C. Orang yang masih anak-anak\n"
            "D. Orang yang sedang sakit\n"
            "E. Orang yang sedang berpuasa"
        ),
    },
    {
        "no": 4, "bab": "Larangan Pergaulan Bebas dan Perbuatan Zina",
        "elemen": "Fikih – Larangan Pergaulan Bebas dan Zina",
        "cp": "Peserta didik memahami hukuman bagi pelaku zina.",
        "tp": "Peserta didik dapat menjelaskan hukuman bagi pelaku zina ghairu muhshan.",
        "indikator_kompetensi": "Mengidentifikasi hukuman bagi pelaku zina.",
        "indikator_soal": "Disajikan QS An-Nur ayat 2, peserta didik dapat menentukan hukuman bagi pelaku zina ghairu muhshan.",
        "tingkat": "Sedang", "kunci": "D",
        "soal": (
            "Berdasarkan QS An-Nur ayat 2, hukuman bagi pelaku zina ghairu muhshan (belum pernah menikah) yang terbukti secara syar'i adalah ...\n"
            "A. Hukuman mati\n"
            "B. Hukuman penjara seumur hidup\n"
            "C. Hukuman denda saja\n"
            "D. Dijilid (didera) seratus kali\n"
            "E. Hukuman rajam"
        ),
    },
    {
        "no": 5, "bab": "Larangan Pergaulan Bebas dan Perbuatan Zina",
        "elemen": "Akhlak – Larangan Pergaulan Bebas dan Zina",
        "cp": "Peserta didik dapat menerapkan cara menghindari pergaulan bebas.",
        "tp": "Peserta didik dapat menentukan cara menghindari pergaulan bebas.",
        "indikator_kompetensi": "Menerapkan cara menghindari pergaulan bebas.",
        "indikator_soal": "Disajikan beberapa pilihan perilaku, peserta didik dapat menentukan cara yang tepat untuk menghindari pergaulan bebas.",
        "tingkat": "Sedang", "kunci": "A",
        "soal": (
            "Sebagai pelajar muslim, kita harus menjauhi pergaulan bebas dengan cara yang sesuai syariat. Berikut ini cara yang TEPAT untuk menghindari pergaulan bebas adalah ...\n"
            "A. Menjaga pandangan, memilih teman yang saleh-salehah, memperbanyak ibadah, dan mengikuti kegiatan positif\n"
            "B. Mengikuti tren pergaulan modern tanpa memilah\n"
            "C. Bergaul bebas asalkan tidak berlebihan\n"
            "D. Menjauhi semua teman tanpa kecuali\n"
            "E. Membatasi diri dari kegiatan sekolah"
        ),
    },
    # ===== BAB 2: MAHABBAH, KHAUF, RAJA', TAWAKAL (5 soal) =====
    {
        "no": 6, "bab": "Mahabbah, Khauf, Raja', dan Tawakal kepada Allah Swt.",
        "elemen": "Akidah/Akhlak – Mahabbah kepada Allah Swt.",
        "cp": "Peserta didik memahami pengertian mahabbah kepada Allah Swt.",
        "tp": "Peserta didik dapat menjelaskan pengertian mahabbah.",
        "indikator_kompetensi": "Memahami pengertian mahabbah.",
        "indikator_soal": "Disajikan deskripsi tentang cinta seorang hamba, peserta didik dapat menentukan pengertian mahabbah.",
        "tingkat": "Rendah", "kunci": "C",
        "soal": (
            "Salah satu sikap terpuji seorang hamba kepada Allah Swt. adalah mahabbah. Pengertian mahabbah yang paling tepat adalah ...\n"
            "A. Rasa benci terhadap maksiat\n"
            "B. Sikap acuh terhadap dunia\n"
            "C. Cinta yang mendalam kepada Allah Swt. yang mendorong seseorang untuk taat dan mendekat kepada-Nya\n"
            "D. Rasa takut kepada makhluk\n"
            "E. Sikap pasrah tanpa usaha"
        ),
    },
    {
        "no": 7, "bab": "Mahabbah, Khauf, Raja', dan Tawakal kepada Allah Swt.",
        "elemen": "Akidah/Akhlak – Khauf kepada Allah Swt.",
        "cp": "Peserta didik memahami pengertian khauf.",
        "tp": "Peserta didik dapat menjelaskan pengertian khauf.",
        "indikator_kompetensi": "Memahami pengertian khauf.",
        "indikator_soal": "Disajikan beberapa pernyataan, peserta didik dapat menentukan pengertian khauf yang tepat.",
        "tingkat": "Sedang", "kunci": "B",
        "soal": (
            "Khauf merupakan salah satu maqam (kedudukan) dalam akhlak tasawuf. Pengertian khauf adalah ...\n"
            "A. Rasa cinta yang berlebihan kepada makhluk\n"
            "B. Rasa takut kepada Allah Swt. atas siksa-Nya akibat dosa dan maksiat, sehingga mendorong untuk taat\n"
            "C. Rasa harap yang tinggi kepada Allah Swt.\n"
            "D. Rasa pasrah yang tanpa ikhtiar\n"
            "E. Rasa percaya diri yang berlebihan"
        ),
    },
    {
        "no": 8, "bab": "Mahabbah, Khauf, Raja', dan Tawakal kepada Allah Swt.",
        "elemen": "Akidah/Akhlak – Raja' kepada Allah Swt.",
        "cp": "Peserta didik memahami pengertian raja'.",
        "tp": "Peserta didik dapat menjelaskan pengertian raja'.",
        "indikator_kompetensi": "Memahami pengertian raja'.",
        "indikator_soal": "Disajikan beberapa pengertian, peserta didik dapat menentukan pengertian raja' yang paling tepat.",
        "tingkat": "Sedang", "kunci": "A",
        "soal": (
            "Raja' merupakan akhlak terpuji yang saling melengkapi dengan khauf. Pengertian raja' adalah ...\n"
            "A. Sikap mengharap rahmat, ampunan, dan ridha Allah Swt. disertai usaha sungguh-sungguh\n"
            "B. Rasa putus asa dari rahmat Allah\n"
            "C. Sikap pasrah tanpa usaha\n"
            "D. Mengharap dipuji oleh manusia\n"
            "E. Berharap kepada selain Allah"
        ),
    },
    {
        "no": 9, "bab": "Mahabbah, Khauf, Raja', dan Tawakal kepada Allah Swt.",
        "elemen": "Akidah/Akhlak – Tawakal kepada Allah Swt.",
        "cp": "Peserta didik memahami pengertian tawakal.",
        "tp": "Peserta didik dapat menjelaskan pengertian tawakal.",
        "indikator_kompetensi": "Memahami pengertian tawakal.",
        "indikator_soal": "Disajikan deskripsi tentang ikhtiar dan doa, peserta didik dapat menentukan pengertian tawakal yang benar.",
        "tingkat": "Sedang", "kunci": "C",
        "soal": (
            "Setelah berusaha (ikhtiar) maksimal, seorang muslim diperintahkan untuk menyerahkan hasilnya kepada Allah Swt. Sikap tersebut disebut tawakal. Pengertian tawakal yang tepat adalah ...\n"
            "A. Berserah diri tanpa berusaha sama sekali\n"
            "B. Hanya berdoa tanpa beramal\n"
            "C. Berserah diri kepada Allah Swt. setelah berusaha dan berdoa secara maksimal\n"
            "D. Putus asa karena hasil belum tercapai\n"
            "E. Bergantung sepenuhnya kepada manusia"
        ),
    },
    {
        "no": 10, "bab": "Mahabbah, Khauf, Raja', dan Tawakal kepada Allah Swt.",
        "elemen": "Akidah/Akhlak – Penerapan Tawakal",
        "cp": "Peserta didik dapat menerapkan sikap tawakal dalam kehidupan.",
        "tp": "Peserta didik dapat memilih contoh tawakal yang benar.",
        "indikator_kompetensi": "Menerapkan sikap tawakal.",
        "indikator_soal": "Disajikan beberapa ilustrasi sikap siswa menjelang ujian, peserta didik dapat menentukan contoh tawakal yang tepat.",
        "tingkat": "Sulit", "kunci": "D",
        "soal": (
            "Menjelang ujian sekolah, terdapat beberapa sikap siswa berikut. Sikap yang mencerminkan tawakal kepada Allah Swt. yang benar adalah ...\n"
            "A. Tidak belajar karena yakin akan lulus\n"
            "B. Mencontek karena pasrah pada nasib\n"
            "C. Hanya berdoa tanpa belajar sama sekali\n"
            "D. Belajar dengan sungguh-sungguh, berdoa, lalu menyerahkan hasilnya kepada Allah Swt.\n"
            "E. Putus asa sebelum ujian dimulai"
        ),
    },
    # ===== BAB 3: MENGHINDARI MARAH, KONTROL DIRI, BERANI MEMBELA KEBENARAN (5 soal) =====
    {
        "no": 11, "bab": "Menghindari Marah, Kontrol Diri, dan Berani Membela Kebenaran",
        "elemen": "Akhlak – Menghindari Marah (Gadab)",
        "cp": "Peserta didik memahami pengertian gadab/marah.",
        "tp": "Peserta didik dapat menjelaskan pengertian gadab.",
        "indikator_kompetensi": "Memahami pengertian gadab.",
        "indikator_soal": "Disajikan deskripsi tentang emosi marah, peserta didik dapat menentukan pengertian gadab.",
        "tingkat": "Rendah", "kunci": "B",
        "soal": (
            "Salah satu akhlak tercela yang harus dihindari seorang muslim adalah gadab. Pengertian gadab adalah ...\n"
            "A. Sikap sabar dalam menghadapi cobaan\n"
            "B. Sifat marah atau emosi yang berlebihan akibat tidak terkontrolnya hawa nafsu\n"
            "C. Sikap berani membela kebenaran\n"
            "D. Sifat mengontrol diri dari hawa nafsu\n"
            "E. Sikap tawakal kepada Allah"
        ),
    },
    {
        "no": 12, "bab": "Menghindari Marah, Kontrol Diri, dan Berani Membela Kebenaran",
        "elemen": "Akhlak – Menghindari Marah (Gadab)",
        "cp": "Peserta didik dapat menerapkan cara menghindari marah sesuai sunah.",
        "tp": "Peserta didik dapat menentukan cara menghindari marah sesuai sunah Rasulullah saw.",
        "indikator_kompetensi": "Menerapkan cara menghindari marah.",
        "indikator_soal": "Disajikan ilustrasi seseorang yang sedang marah, peserta didik dapat menentukan tindakan yang sesuai sunah Nabi saw.",
        "tingkat": "Sedang", "kunci": "C",
        "soal": (
            "Rasulullah saw. memberikan tuntunan ketika seseorang sedang marah. Salah satu tuntunan tersebut adalah ...\n"
            "A. Memukul orang yang membuat marah\n"
            "B. Berteriak sekeras-kerasnya\n"
            "C. Membaca ta'awudz, diam, mengubah posisi (duduk jika berdiri), dan berwudu\n"
            "D. Membalas dengan kemarahan lebih besar\n"
            "E. Menyebarkan kemarahan di media sosial"
        ),
    },
    {
        "no": 13, "bab": "Menghindari Marah, Kontrol Diri, dan Berani Membela Kebenaran",
        "elemen": "Akhlak – Kontrol Diri (Mujahadah an-Nafs)",
        "cp": "Peserta didik memahami pengertian kontrol diri.",
        "tp": "Peserta didik dapat menjelaskan pengertian mujahadah an-nafs.",
        "indikator_kompetensi": "Memahami pengertian kontrol diri (mujahadah an-nafs).",
        "indikator_soal": "Disajikan istilah Arab dan deskripsi, peserta didik dapat menentukan pengertian mujahadah an-nafs.",
        "tingkat": "Sedang", "kunci": "B",
        "soal": (
            "Kontrol diri dalam istilah Islam dikenal dengan mujahadah an-nafs. Pengertian mujahadah an-nafs adalah ...\n"
            "A. Memanjakan hawa nafsu agar bahagia\n"
            "B. Sungguh-sungguh berjuang melawan hawa nafsu untuk meninggalkan maksiat dan melaksanakan ketaatan\n"
            "C. Membiarkan hawa nafsu mengendalikan diri\n"
            "D. Menyalahkan orang lain atas perbuatan dosa\n"
            "E. Lari dari tanggung jawab"
        ),
    },
    {
        "no": 14, "bab": "Menghindari Marah, Kontrol Diri, dan Berani Membela Kebenaran",
        "elemen": "Akhlak – Berani Membela Kebenaran (Syaja'ah)",
        "cp": "Peserta didik memahami pengertian syaja'ah.",
        "tp": "Peserta didik dapat menjelaskan pengertian syaja'ah.",
        "indikator_kompetensi": "Memahami pengertian syaja'ah.",
        "indikator_soal": "Disajikan istilah syaja'ah, peserta didik dapat menentukan pengertian yang tepat dalam konteks Islam.",
        "tingkat": "Sedang", "kunci": "C",
        "soal": (
            "Seorang muslim harus memiliki sikap berani membela kebenaran yang dalam istilah Islam disebut syaja'ah. Pengertian syaja'ah yang paling tepat adalah ...\n"
            "A. Berani melakukan apa saja tanpa perhitungan\n"
            "B. Berani melawan setiap orang yang tidak sependapat\n"
            "C. Berani membela dan menegakkan kebenaran berdasarkan pertimbangan akal yang sehat dan iman, bukan karena hawa nafsu\n"
            "D. Berani berbuat dosa secara terbuka\n"
            "E. Sikap nekat tanpa ilmu"
        ),
    },
    {
        "no": 15, "bab": "Menghindari Marah, Kontrol Diri, dan Berani Membela Kebenaran",
        "elemen": "Akhlak – Penerapan Syaja'ah",
        "cp": "Peserta didik dapat menerapkan sikap syaja'ah dalam kehidupan.",
        "tp": "Peserta didik dapat menentukan contoh syaja'ah yang benar.",
        "indikator_kompetensi": "Menerapkan sikap syaja'ah.",
        "indikator_soal": "Disajikan ilustrasi sikap seorang siswa, peserta didik dapat menentukan contoh syaja'ah yang sesuai ajaran Islam.",
        "tingkat": "Sulit", "kunci": "B",
        "soal": (
            "Perhatikan pernyataan berikut: \"Adi melihat temannya menyontek saat ujian. Adi kemudian mengingatkan temannya dengan baik dan melaporkan kepada guru agar kebenaran tegak.\" Sikap Adi mencerminkan ...\n"
            "A. Sikap pengecut\n"
            "B. Syaja'ah (berani membela kebenaran)\n"
            "C. Gadab (marah)\n"
            "D. Tajassus (mencari-cari kesalahan)\n"
            "E. Namimah (adu domba)"
        ),
    },
    # ===== BAB 4: AL KULLIYAT AL KHAMSAH (5 soal) =====
    {
        "no": 16, "bab": "Al-Kulliyat Al-Khamsah (Lima Prinsip Dasar Hukum Islam)",
        "elemen": "Fikih – Al-Kulliyat Al-Khamsah",
        "cp": "Peserta didik memahami pengertian Al-Kulliyat Al-Khamsah.",
        "tp": "Peserta didik dapat menjelaskan pengertian Al-Kulliyat Al-Khamsah.",
        "indikator_kompetensi": "Memahami pengertian Al-Kulliyat Al-Khamsah.",
        "indikator_soal": "Disajikan istilah Al-Kulliyat Al-Khamsah, peserta didik dapat menentukan pengertiannya.",
        "tingkat": "Rendah", "kunci": "C",
        "soal": (
            "Para ulama merumuskan tujuan-tujuan syariat Islam yang dikenal dengan istilah Al-Kulliyat Al-Khamsah. Pengertian Al-Kulliyat Al-Khamsah adalah ...\n"
            "A. Lima kewajiban shalat\n"
            "B. Lima rukun Islam\n"
            "C. Lima prinsip dasar/tujuan pokok hukum Islam yang harus dijaga (maqashid syari'ah)\n"
            "D. Lima rukun iman\n"
            "E. Lima kewajiban haji"
        ),
    },
    {
        "no": 17, "bab": "Al-Kulliyat Al-Khamsah (Lima Prinsip Dasar Hukum Islam)",
        "elemen": "Fikih – Hifzh ad-Din",
        "cp": "Peserta didik memahami prinsip hifzh ad-din.",
        "tp": "Peserta didik dapat menjelaskan makna hifzh ad-din.",
        "indikator_kompetensi": "Memahami prinsip hifzh ad-din (menjaga agama).",
        "indikator_soal": "Disajikan istilah hifzh ad-din, peserta didik dapat menentukan maknanya.",
        "tingkat": "Sedang", "kunci": "A",
        "soal": (
            "Salah satu dari Al-Kulliyat Al-Khamsah adalah hifzh ad-din. Hifzh ad-din berarti ...\n"
            "A. Menjaga agama – melaksanakan ibadah, mempelajari Islam, dan melindungi akidah dari ajaran sesat\n"
            "B. Menjaga jiwa dari pembunuhan\n"
            "C. Menjaga akal dari mabuk\n"
            "D. Menjaga keturunan dari zina\n"
            "E. Menjaga harta dari pencurian"
        ),
    },
    {
        "no": 18, "bab": "Al-Kulliyat Al-Khamsah (Lima Prinsip Dasar Hukum Islam)",
        "elemen": "Fikih – Hifzh an-Nafs",
        "cp": "Peserta didik memahami prinsip hifzh an-nafs.",
        "tp": "Peserta didik dapat menentukan contoh penerapan hifzh an-nafs.",
        "indikator_kompetensi": "Menerapkan prinsip hifzh an-nafs (menjaga jiwa).",
        "indikator_soal": "Disajikan beberapa pilihan perilaku, peserta didik dapat menentukan contoh penerapan hifzh an-nafs.",
        "tingkat": "Sedang", "kunci": "B",
        "soal": (
            "Hifzh an-nafs (menjaga jiwa) merupakan salah satu prinsip Al-Kulliyat Al-Khamsah. Berikut ini contoh penerapan hifzh an-nafs adalah ...\n"
            "A. Mempelajari Al-Qur'an dan Hadis\n"
            "B. Mengonsumsi makanan halal dan sehat, menjauhi narkoba, serta tidak menyakiti orang lain\n"
            "C. Bekerja keras mencari harta yang halal\n"
            "D. Menikah secara sah untuk menjaga keturunan\n"
            "E. Belajar sungguh-sungguh agar tidak bodoh"
        ),
    },
    {
        "no": 19, "bab": "Al-Kulliyat Al-Khamsah (Lima Prinsip Dasar Hukum Islam)",
        "elemen": "Fikih – Hifzh al-'Aql",
        "cp": "Peserta didik memahami prinsip hifzh al-'aql.",
        "tp": "Peserta didik dapat menentukan contoh penerapan hifzh al-'aql.",
        "indikator_kompetensi": "Menerapkan prinsip hifzh al-'aql (menjaga akal).",
        "indikator_soal": "Disajikan beberapa pilihan perilaku, peserta didik dapat menentukan penerapan hifzh al-'aql.",
        "tingkat": "Sedang", "kunci": "D",
        "soal": (
            "Akal merupakan anugerah Allah Swt. yang sangat berharga sehingga wajib dijaga (hifzh al-'aql). Berikut ini perilaku yang merupakan penerapan hifzh al-'aql adalah ...\n"
            "A. Melaksanakan ibadah salat lima waktu\n"
            "B. Mendonorkan darah kepada yang membutuhkan\n"
            "C. Bekerja keras mencari nafkah\n"
            "D. Menuntut ilmu, tidak mengonsumsi minuman keras dan narkoba\n"
            "E. Menjaga aurat dan pergaulan"
        ),
    },
    {
        "no": 20, "bab": "Al-Kulliyat Al-Khamsah (Lima Prinsip Dasar Hukum Islam)",
        "elemen": "Fikih – Al-Kulliyat Al-Khamsah",
        "cp": "Peserta didik memahami kelima prinsip Al-Kulliyat Al-Khamsah.",
        "tp": "Peserta didik dapat menyebutkan urutan lima prinsip Al-Kulliyat Al-Khamsah.",
        "indikator_kompetensi": "Mengidentifikasi 5 prinsip Al-Kulliyat Al-Khamsah.",
        "indikator_soal": "Disajikan beberapa pilihan urutan, peserta didik dapat menentukan urutan kelima prinsip Al-Kulliyat Al-Khamsah yang benar.",
        "tingkat": "Sulit", "kunci": "A",
        "soal": (
            "Al-Kulliyat Al-Khamsah terdiri dari lima prinsip dasar yang wajib dijaga. Urutan kelima prinsip tersebut yang benar adalah ...\n"
            "A. Hifzh ad-din, hifzh an-nafs, hifzh al-'aql, hifzh an-nasl, hifzh al-mal\n"
            "B. Hifzh al-mal, hifzh an-nafs, hifzh ad-din, hifzh al-'aql, hifzh an-nasl\n"
            "C. Hifzh an-nasl, hifzh al-'aql, hifzh ad-din, hifzh al-mal, hifzh an-nafs\n"
            "D. Hifzh al-'aql, hifzh ad-din, hifzh al-mal, hifzh an-nasl, hifzh an-nafs\n"
            "E. Hifzh an-nafs, hifzh al-mal, hifzh al-'aql, hifzh ad-din, hifzh an-nasl"
        ),
    },
]


# =====================================================================
# QUESTIONS - ESSAY
# =====================================================================
ESSAY = [
    # ===== BAB 1: LARANGAN PERGAULAN BEBAS DAN ZINA (3 soal) =====
    {
        "no": 1, "bab": "Larangan Pergaulan Bebas dan Perbuatan Zina",
        "elemen": "Akhlak – Larangan Pergaulan Bebas",
        "cp": "Peserta didik memahami bahaya pergaulan bebas dan cara menghindarinya.",
        "tp": "Peserta didik dapat menjelaskan pergaulan bebas, dampaknya, dan cara menghindarinya.",
        "indikator_kompetensi": "Menjelaskan pergaulan bebas secara komprehensif.",
        "indikator_soal": "Disajikan narasi tentang pergaulan remaja, peserta didik dapat menjelaskan pengertian, 3 dampak negatif, dan 4 cara menghindari pergaulan bebas.",
        "tingkat": "Sedang",
        "soal": (
            "Pergaulan bebas menjadi salah satu masalah serius di kalangan remaja masa kini. Kemudahan akses teknologi, lemahnya benteng iman, serta lingkungan yang permisif menyebabkan banyak remaja terjerumus dalam pergaulan yang melampaui batas syariat. Islam telah memberikan rambu-rambu yang jelas untuk menjaga generasi muda dari kerusakan tersebut.\n"
            "Jelaskan pengertian pergaulan bebas, sebutkan minimal 3 dampak negatifnya, dan tuliskan minimal 4 cara menghindarinya bagi pelajar muslim!"
        ),
        "jawaban": (
            "Pengertian pergaulan bebas: pergaulan tanpa batas antara laki-laki dan perempuan yang melanggar norma agama, kesusilaan, dan adat, yang dapat mengarah kepada perbuatan zina.\n"
            "\n"
            "Dampak negatif (minimal 3):\n"
            "1) Terjerumus pada perbuatan zina yang merupakan dosa besar.\n"
            "2) Hancurnya masa depan, prestasi belajar menurun, putus sekolah.\n"
            "3) Tertular penyakit menular seksual (PMS) dan HIV/AIDS.\n"
            "4) Hamil di luar nikah, aborsi, dan kelahiran anak tanpa kejelasan nasab.\n"
            "5) Rusaknya reputasi keluarga dan diri sendiri di tengah masyarakat.\n"
            "6) Jauh dari rahmat Allah Swt. dan dimurkai-Nya.\n"
            "\n"
            "Cara menghindari pergaulan bebas (minimal 4):\n"
            "1) Memperkuat iman dengan rutin beribadah (salat, puasa, mengaji).\n"
            "2) Menjaga pandangan (ghadhul bashar) dan menutup aurat.\n"
            "3) Memilih teman yang saleh-salehah dan menghindari teman yang menjerumuskan.\n"
            "4) Mengisi waktu luang dengan kegiatan positif (organisasi, olahraga, belajar).\n"
            "5) Tidak berkhalwat (berdua-duaan) dengan lawan jenis yang bukan mahram.\n"
            "6) Menggunakan media sosial dengan bijak, menjauhi konten yang merangsang syahwat."
        ),
    },
    {
        "no": 2, "bab": "Larangan Pergaulan Bebas dan Perbuatan Zina",
        "elemen": "Fikih – Larangan Zina",
        "cp": "Peserta didik memahami zina, macam-macamnya, dan hukumannya.",
        "tp": "Peserta didik dapat menjelaskan zina, macam-macamnya, dan hukuman bagi pelakunya.",
        "indikator_kompetensi": "Menjelaskan zina dan hukumannya.",
        "indikator_soal": "Disajikan narasi tentang larangan zina, peserta didik dapat menjelaskan pengertian, macam-macam, dan hukuman bagi pelaku zina.",
        "tingkat": "Sedang",
        "soal": (
            "Zina merupakan salah satu dosa besar yang dilarang dalam Islam. Allah Swt. tidak hanya melarang melakukan zina, tetapi juga melarang mendekatinya. Hal ini menunjukkan betapa beratnya dosa zina dan dahsyatnya kerusakan yang ditimbulkan baik bagi pelaku maupun masyarakat.\n"
            "Jelaskan pengertian zina, sebutkan macam-macam zina beserta penjelasannya, dan tuliskan hukuman bagi masing-masing pelaku zina menurut syariat Islam!"
        ),
        "jawaban": (
            "Pengertian zina: hubungan seksual antara laki-laki dan perempuan yang bukan suami istri yang sah menurut syariat Islam.\n"
            "\n"
            "Macam-macam zina:\n"
            "1) Zina Muhshan: zina yang dilakukan oleh orang yang sudah/pernah menikah secara sah.\n"
            "2) Zina Ghairu Muhshan: zina yang dilakukan oleh orang yang belum pernah menikah (lajang/perawan/perjaka).\n"
            "\n"
            "Hukuman menurut syariat Islam:\n"
            "1) Zina muhshan: hukumannya rajam (dilempari batu sampai mati) berdasarkan sunnah Nabi saw.\n"
            "2) Zina ghairu muhshan: hukumannya didera/dijilid 100 kali dan diasingkan (taghrib) selama satu tahun (berdasarkan QS An-Nur: 2 dan sunah).\n"
            "\n"
            "Syarat penegakan hukum had zina sangat ketat: harus ada 4 saksi laki-laki adil yang menyaksikan langsung, atau pengakuan pelaku sendiri. Hukuman ini ditegakkan di negara yang menerapkan syariat oleh pemerintah/hakim, bukan oleh perseorangan."
        ),
    },
    {
        "no": 3, "bab": "Larangan Pergaulan Bebas dan Perbuatan Zina",
        "elemen": "Al-Qur'an – QS Al-Isra ayat 32",
        "cp": "Peserta didik memahami kandungan QS Al-Isra ayat 32.",
        "tp": "Peserta didik dapat menjelaskan kandungan QS Al-Isra ayat 32 dan penerapannya.",
        "indikator_kompetensi": "Menjelaskan kandungan QS Al-Isra ayat 32.",
        "indikator_soal": "Disajikan QS Al-Isra ayat 32, peserta didik dapat menuliskan terjemahan dan menjelaskan kandungannya serta penerapannya.",
        "tingkat": "Sulit",
        "soal": (
            "Allah Swt. berfirman dalam QS Al-Isra ayat 32: \"Wa la taqrabuz-zina, innahu kana fahisyatan wa sa'a sabila.\" Ayat ini menjadi salah satu landasan utama dalam Islam mengenai pencegahan zina sejak dari pintu-pintunya.\n"
            "Tuliskan terjemahan QS Al-Isra ayat 32, jelaskan kandungannya, dan sebutkan minimal 3 contoh perbuatan yang termasuk \"mendekati zina\" yang harus dihindari!"
        ),
        "jawaban": (
            "Terjemahan QS Al-Isra ayat 32: \"Dan janganlah kamu mendekati zina; sesungguhnya zina itu adalah suatu perbuatan yang keji dan suatu jalan yang buruk.\"\n"
            "\n"
            "Kandungan ayat:\n"
            "1) Larangan keras tidak hanya melakukan zina, tetapi juga mendekati segala hal yang bisa mengarah kepada zina (sadd adz-dzari'ah).\n"
            "2) Zina dikategorikan sebagai fahisyah (perbuatan keji/sangat buruk).\n"
            "3) Zina merupakan sa'a sabila (jalan yang buruk) yang menimbulkan banyak kerusakan bagi pelaku, keluarga, dan masyarakat.\n"
            "4) Islam menggunakan prinsip pencegahan (preventif) sebelum kerusakan terjadi.\n"
            "\n"
            "Contoh perbuatan yang termasuk \"mendekati zina\" (minimal 3):\n"
            "1) Berpacaran/berduaan (khalwat) dengan lawan jenis yang bukan mahram.\n"
            "2) Melihat dan menonton tayangan porno (di televisi, internet, atau media sosial).\n"
            "3) Membaca atau membayangkan hal-hal yang menggairahkan syahwat.\n"
            "4) Berbusana yang membuka aurat atau ketat sehingga memamerkan bentuk tubuh.\n"
            "5) Bersentuhan, berpegangan tangan, atau berpelukan dengan lawan jenis yang bukan mahram.\n"
            "6) Saling chat mesra/godaan di media sosial dengan lawan jenis yang bukan mahram."
        ),
    },
    # ===== BAB 2: MAHABBAH, KHAUF, RAJA', TAWAKAL (2 soal) =====
    {
        "no": 4, "bab": "Mahabbah, Khauf, Raja', dan Tawakal kepada Allah Swt.",
        "elemen": "Akidah/Akhlak – Mahabbah, Khauf, dan Raja'",
        "cp": "Peserta didik memahami mahabbah, khauf, dan raja' kepada Allah Swt.",
        "tp": "Peserta didik dapat menjelaskan mahabbah, khauf, dan raja' beserta contohnya.",
        "indikator_kompetensi": "Menjelaskan mahabbah, khauf, dan raja'.",
        "indikator_soal": "Disajikan narasi tentang hubungan hamba dengan Tuhan, peserta didik dapat menjelaskan pengertian dan contoh mahabbah, khauf, dan raja'.",
        "tingkat": "Sedang",
        "soal": (
            "Dalam beribadah kepada Allah Swt., seorang muslim harus menyeimbangkan antara cinta (mahabbah), takut (khauf), dan harap (raja'). Ketiganya ibarat sayap burung yang menerbangkan seorang hamba menuju ridha Allah Swt. Jika hanya cinta tanpa takut, akan lalai; jika hanya takut tanpa harap, akan putus asa; dan jika hanya harap tanpa amal, akan menjadi angan-angan kosong.\n"
            "Jelaskan pengertian mahabbah, khauf, dan raja' kepada Allah Swt., serta berikan masing-masing satu contoh penerapannya dalam kehidupan seorang pelajar!"
        ),
        "jawaban": (
            "1) MAHABBAH\n"
            "   Pengertian: cinta yang mendalam dari seorang hamba kepada Allah Swt. yang mendorongnya untuk taat, ridha terhadap ketentuan-Nya, dan senantiasa berusaha mendekatkan diri kepada-Nya.\n"
            "   Contoh: rajin salat lima waktu tepat waktu karena rindu bertemu Allah Swt., membaca Al-Qur'an dengan tadabur karena cinta firman-Nya.\n"
            "\n"
            "2) KHAUF\n"
            "   Pengertian: rasa takut kepada Allah Swt. atas siksa-Nya akibat dosa dan maksiat yang mendorong seseorang untuk menjauhi larangan-Nya.\n"
            "   Contoh: takut menyontek saat ujian karena ingat Allah Swt. selalu mengawasi dan Maha Mengetahui; takut meninggalkan salat karena khawatir azab-Nya.\n"
            "\n"
            "3) RAJA'\n"
            "   Pengertian: sikap mengharap rahmat, ampunan, dan ridha Allah Swt. yang disertai usaha sungguh-sungguh dan amal saleh.\n"
            "   Contoh: belajar dengan giat dan berdoa karena mengharap Allah memudahkan ujian; bertobat dari kesalahan dengan harapan diampuni dosa-dosanya."
        ),
    },
    {
        "no": 5, "bab": "Mahabbah, Khauf, Raja', dan Tawakal kepada Allah Swt.",
        "elemen": "Akidah/Akhlak – Tawakal",
        "cp": "Peserta didik memahami tawakal kepada Allah Swt.",
        "tp": "Peserta didik dapat menjelaskan tawakal yang benar dan penerapannya.",
        "indikator_kompetensi": "Menjelaskan tawakal yang benar.",
        "indikator_soal": "Disajikan narasi tentang tawakal, peserta didik dapat menjelaskan pengertian, tahapan, dan 3 contoh penerapan tawakal.",
        "tingkat": "Sedang",
        "soal": (
            "Tawakal merupakan akhlak mulia yang menunjukkan keyakinan penuh seorang hamba kepada kekuasaan Allah Swt. Sebagian orang keliru memahami tawakal sebagai pasrah tanpa usaha, padahal tawakal yang benar dalam Islam adalah berserah diri kepada Allah Swt. setelah berusaha (ikhtiar) dan berdoa secara maksimal.\n"
            "Jelaskan pengertian tawakal yang benar, tahapan-tahapan dalam bertawakal, dan berikan minimal 3 contoh penerapan tawakal dalam kehidupan seorang pelajar!"
        ),
        "jawaban": (
            "Pengertian tawakal: sikap berserah diri sepenuhnya kepada Allah Swt. SETELAH melakukan ikhtiar/usaha dan berdoa secara maksimal, dengan keyakinan bahwa hanya Allah-lah yang menentukan hasil akhir.\n"
            "\n"
            "Tahapan dalam bertawakal:\n"
            "1) Ikhtiar (usaha): melakukan usaha yang halal dan maksimal sesuai kemampuan.\n"
            "2) Doa: memohon kepada Allah Swt. agar usaha dimudahkan dan diberi hasil terbaik.\n"
            "3) Tawakal: menyerahkan hasil akhir kepada Allah Swt.\n"
            "4) Ridha: menerima dengan ikhlas hasil yang diberikan Allah, baik sesuai harapan maupun tidak.\n"
            "\n"
            "Contoh penerapan tawakal bagi pelajar (minimal 3):\n"
            "1) Belajar sungguh-sungguh menjelang ujian, berdoa sebelum mengerjakan, lalu mengerjakan soal dengan tenang dan menyerahkan hasilnya kepada Allah Swt.\n"
            "2) Berusaha menjadi peserta didik terbaik dengan disiplin, sekaligus berdoa dan ridha atas peringkat yang diperoleh.\n"
            "3) Berikhtiar mencari sekolah/kampus impian dengan persiapan matang, lalu berserah diri pada keputusan Allah Swt.\n"
            "4) Ketika menghadapi penyakit, berobat ke dokter, minum obat sesuai resep, sambil berdoa dan yakin kesembuhan datang dari Allah Swt."
        ),
    },
    # ===== BAB 3: GADAB, KONTROL DIRI, SYAJA'AH (2 soal) =====
    {
        "no": 6, "bab": "Menghindari Marah, Kontrol Diri, dan Berani Membela Kebenaran",
        "elemen": "Akhlak – Menghindari Gadab",
        "cp": "Peserta didik memahami bahaya gadab dan cara menghindarinya.",
        "tp": "Peserta didik dapat menjelaskan gadab, dampaknya, dan cara menghindarinya.",
        "indikator_kompetensi": "Menjelaskan gadab dan cara menghindarinya.",
        "indikator_soal": "Disajikan narasi tentang gadab, peserta didik dapat menjelaskan pengertian, 3 dampak negatif, dan 4 cara menghindari marah sesuai sunah.",
        "tingkat": "Sedang",
        "soal": (
            "Marah (gadab) adalah salah satu emosi alami manusia. Namun ketika tidak dikendalikan, marah dapat berubah menjadi sumber malapetaka. Rasulullah saw. bersabda: \"Orang yang kuat bukanlah orang yang menang dalam pertarungan, melainkan orang yang mampu menguasai dirinya ketika marah.\" (HR Bukhari & Muslim)\n"
            "Jelaskan pengertian gadab, sebutkan minimal 3 dampak negatifnya, dan tuliskan minimal 4 cara menghindari/meredam marah sesuai sunah Rasulullah saw.!"
        ),
        "jawaban": (
            "Pengertian gadab: sifat marah atau emosi yang berlebihan akibat tidak terkendalinya hawa nafsu yang mendorong seseorang melakukan perkataan/perbuatan tercela.\n"
            "\n"
            "Dampak negatif gadab (minimal 3):\n"
            "1) Merusak hubungan sosial dengan keluarga, teman, dan masyarakat.\n"
            "2) Mendorong perbuatan dosa: mencaci, memukul, bahkan membunuh.\n"
            "3) Merusak kesehatan fisik (darah tinggi, jantung) dan mental.\n"
            "4) Menghilangkan keberkahan dan dijauhi orang lain.\n"
            "5) Mendatangkan murka Allah Swt. dan menjauhkan dari rahmat-Nya.\n"
            "\n"
            "Cara menghindari/meredam marah sesuai sunah (minimal 4):\n"
            "1) Membaca ta'awudz: \"A'udzu billahi minasy-syaithanir rajim\" untuk mengusir bisikan setan.\n"
            "2) Diam dan menahan lisan agar tidak mengeluarkan kata-kata buruk.\n"
            "3) Mengubah posisi: jika berdiri, duduklah; jika duduk, berbaringlah.\n"
            "4) Berwudu dengan air agar emosi mereda.\n"
            "5) Ingat keutamaan menahan marah dan pahala dari Allah Swt.\n"
            "6) Memberi maaf dan berdoa untuk orang yang membuat marah.\n"
            "7) Memperbanyak ibadah, zikir, dan istigfar."
        ),
    },
    {
        "no": 7, "bab": "Menghindari Marah, Kontrol Diri, dan Berani Membela Kebenaran",
        "elemen": "Akhlak – Mujahadah an-Nafs dan Syaja'ah",
        "cp": "Peserta didik memahami mujahadah an-nafs dan syaja'ah.",
        "tp": "Peserta didik dapat menjelaskan mujahadah an-nafs dan syaja'ah beserta contohnya.",
        "indikator_kompetensi": "Menjelaskan mujahadah an-nafs dan syaja'ah.",
        "indikator_soal": "Disajikan narasi tentang akhlak terpuji, peserta didik dapat menjelaskan mujahadah an-nafs dan syaja'ah beserta masing-masing 2 contohnya.",
        "tingkat": "Sulit",
        "soal": (
            "Dua akhlak terpuji yang harus dimiliki seorang muslim adalah mujahadah an-nafs (kontrol diri) dan syaja'ah (berani membela kebenaran). Kontrol diri menahan seseorang dari maksiat dan perbuatan tercela, sedangkan syaja'ah mendorongnya untuk berani tampil membela yang benar meskipun pahit.\n"
            "Jelaskan pengertian mujahadah an-nafs dan syaja'ah, serta berikan masing-masing 2 contoh penerapannya dalam kehidupan pelajar muslim!"
        ),
        "jawaban": (
            "1) MUJAHADAH AN-NAFS (KONTROL DIRI)\n"
            "   Pengertian: sungguh-sungguh berjuang melawan hawa nafsu untuk meninggalkan maksiat/perbuatan tercela dan melaksanakan ketaatan kepada Allah Swt.\n"
            "   Contoh:\n"
            "   a) Menahan diri untuk tidak menyontek saat ujian meskipun ada kesempatan.\n"
            "   b) Menahan diri dari membuka konten/situs yang dilarang agama meskipun penasaran.\n"
            "   c) Mampu mengendalikan emosi ketika diejek teman tanpa membalas dengan kekerasan.\n"
            "\n"
            "2) SYAJA'AH (BERANI MEMBELA KEBENARAN)\n"
            "   Pengertian: berani menegakkan dan membela kebenaran berdasarkan pertimbangan akal sehat dan iman, bukan karena dorongan hawa nafsu, meskipun harus menanggung risiko.\n"
            "   Contoh:\n"
            "   a) Berani menegur teman yang menyontek atau berbuat curang.\n"
            "   b) Berani menyampaikan pendapat yang benar di depan guru/teman meskipun berbeda dengan yang lain.\n"
            "   c) Berani melaporkan kasus bullying atau pelecehan kepada pihak yang berwenang.\n"
            "   d) Berani menolak ajakan teman untuk bolos atau ikut tawuran."
        ),
    },
    # ===== BAB 4: AL-KULLIYAT AL-KHAMSAH (3 soal) =====
    {
        "no": 8, "bab": "Al-Kulliyat Al-Khamsah (Lima Prinsip Dasar Hukum Islam)",
        "elemen": "Fikih – Al-Kulliyat Al-Khamsah",
        "cp": "Peserta didik memahami pengertian dan urgensi Al-Kulliyat Al-Khamsah.",
        "tp": "Peserta didik dapat menjelaskan pengertian Al-Kulliyat Al-Khamsah dan urgensinya.",
        "indikator_kompetensi": "Menjelaskan Al-Kulliyat Al-Khamsah.",
        "indikator_soal": "Disajikan narasi tentang maqashid syariah, peserta didik dapat menjelaskan pengertian, tujuan, dan menyebutkan lima prinsip Al-Kulliyat Al-Khamsah.",
        "tingkat": "Sedang",
        "soal": (
            "Para ulama merumuskan bahwa setiap hukum dalam Islam memiliki tujuan/maksud yang ingin dicapai (maqashid syari'ah). Lima tujuan pokok yang paling utama disebut Al-Kulliyat Al-Khamsah, yang menjadi pilar utama syariat Islam dalam menjaga kemaslahatan manusia di dunia dan akhirat.\n"
            "Jelaskan pengertian Al-Kulliyat Al-Khamsah, tujuannya bagi kehidupan manusia, dan sebutkan kelima prinsipnya secara urut!"
        ),
        "jawaban": (
            "Pengertian Al-Kulliyat Al-Khamsah: lima prinsip dasar atau tujuan pokok hukum Islam yang harus dijaga oleh setiap muslim demi terwujudnya kemaslahatan manusia di dunia dan akhirat. Disebut juga maqashid syari'ah al-khamsah.\n"
            "\n"
            "Tujuan/urgensi Al-Kulliyat Al-Khamsah:\n"
            "1) Menjaga kemaslahatan (al-mashlahah) hidup manusia di dunia dan akhirat.\n"
            "2) Menjadi pedoman dalam memahami dan menerapkan hukum Islam.\n"
            "3) Menolak kerusakan (al-mafsadah) di tengah masyarakat.\n"
            "4) Mewujudkan kehidupan yang seimbang antara hak Allah, hak diri sendiri, dan hak sesama manusia.\n"
            "\n"
            "Lima prinsip Al-Kulliyat Al-Khamsah secara urut:\n"
            "1) Hifzh ad-Din – menjaga agama.\n"
            "2) Hifzh an-Nafs – menjaga jiwa.\n"
            "3) Hifzh al-'Aql – menjaga akal.\n"
            "4) Hifzh an-Nasl – menjaga keturunan/kehormatan.\n"
            "5) Hifzh al-Mal – menjaga harta."
        ),
    },
    {
        "no": 9, "bab": "Al-Kulliyat Al-Khamsah (Lima Prinsip Dasar Hukum Islam)",
        "elemen": "Fikih – Penjelasan 5 Prinsip Al-Kulliyat Al-Khamsah",
        "cp": "Peserta didik memahami setiap prinsip Al-Kulliyat Al-Khamsah.",
        "tp": "Peserta didik dapat menjelaskan kelima prinsip Al-Kulliyat Al-Khamsah secara rinci.",
        "indikator_kompetensi": "Menjelaskan lima prinsip Al-Kulliyat Al-Khamsah.",
        "indikator_soal": "Disajikan narasi tentang 5 prinsip Al-Kulliyat Al-Khamsah, peserta didik dapat menjelaskan masing-masing prinsip beserta contoh penerapannya.",
        "tingkat": "Sulit",
        "soal": (
            "Kelima prinsip Al-Kulliyat Al-Khamsah – hifzh ad-din, hifzh an-nafs, hifzh al-'aql, hifzh an-nasl, dan hifzh al-mal – saling berkaitan dan saling mendukung. Jika salah satu rusak, akan berdampak terhadap yang lain.\n"
            "Jelaskan kelima prinsip Al-Kulliyat Al-Khamsah dan berikan masing-masing satu contoh penerapannya dalam kehidupan sehari-hari!"
        ),
        "jawaban": (
            "1) HIFZH AD-DIN (Menjaga Agama)\n"
            "   Penjelasan: kewajiban setiap muslim menjaga keberlangsungan agamanya dengan melaksanakan ibadah, mempelajari Islam, dan melindungi akidah dari penyimpangan.\n"
            "   Contoh: rajin salat lima waktu, mempelajari Al-Qur'an dan hadis, menjauhi syirik dan ajaran sesat.\n"
            "\n"
            "2) HIFZH AN-NAFS (Menjaga Jiwa)\n"
            "   Penjelasan: kewajiban menjaga keselamatan dan kemuliaan jiwa manusia, baik diri sendiri maupun orang lain.\n"
            "   Contoh: mengonsumsi makanan halal & sehat, tidak menyakiti orang lain, menjauhi narkoba dan tawuran.\n"
            "\n"
            "3) HIFZH AL-'AQL (Menjaga Akal)\n"
            "   Penjelasan: kewajiban menjaga akal sebagai anugerah Allah Swt. agar tetap berfungsi dengan baik untuk memikirkan kebenaran.\n"
            "   Contoh: rajin menuntut ilmu, tidak mengonsumsi minuman keras/narkoba, menjauhi konten yang merusak akal.\n"
            "\n"
            "4) HIFZH AN-NASL (Menjaga Keturunan/Kehormatan)\n"
            "   Penjelasan: kewajiban menjaga keturunan yang sah dan kemurnian nasab melalui pernikahan yang sah serta menjauhi zina.\n"
            "   Contoh: menikah secara sah menurut syariat, menjauhi pergaulan bebas dan zina, menutup aurat.\n"
            "\n"
            "5) HIFZH AL-MAL (Menjaga Harta)\n"
            "   Penjelasan: kewajiban memperoleh, menyimpan, dan menggunakan harta dengan cara yang halal dan menjauhi cara haram.\n"
            "   Contoh: bekerja mencari nafkah halal, menjauhi riba/judi/mencuri/korupsi, menunaikan zakat, hidup hemat dan tidak boros."
        ),
    },
    {
        "no": 10, "bab": "Al-Kulliyat Al-Khamsah (Lima Prinsip Dasar Hukum Islam)",
        "elemen": "Fikih – Penerapan Al-Kulliyat Al-Khamsah",
        "cp": "Peserta didik dapat menerapkan Al-Kulliyat Al-Khamsah dalam kehidupan modern.",
        "tp": "Peserta didik dapat menerapkan Al-Kulliyat Al-Khamsah dalam kehidupan pelajar modern.",
        "indikator_kompetensi": "Menerapkan Al-Kulliyat Al-Khamsah di era modern.",
        "indikator_soal": "Disajikan narasi tantangan zaman modern, peserta didik dapat memberikan contoh penerapan masing-masing prinsip Al-Kulliyat Al-Khamsah dalam kehidupan pelajar.",
        "tingkat": "Sulit",
        "soal": (
            "Di era globalisasi dan digital, pelajar muslim menghadapi berbagai tantangan yang dapat mengancam kelima prinsip Al-Kulliyat Al-Khamsah – mulai dari penyimpangan akidah, kekerasan, narkoba, pergaulan bebas, hingga konsumsi yang berlebihan dan riba. Untuk itu, kelima prinsip ini menjadi pegangan penting agar tetap selamat dunia akhirat.\n"
            "Berikan masing-masing 2 contoh penerapan kelima prinsip Al-Kulliyat Al-Khamsah (hifzh ad-din, hifzh an-nafs, hifzh al-'aql, hifzh an-nasl, dan hifzh al-mal) bagi pelajar muslim di era modern!"
        ),
        "jawaban": (
            "1) HIFZH AD-DIN (Menjaga Agama):\n"
            "   a) Konsisten melaksanakan salat lima waktu meski sedang sibuk gawai/sosmed.\n"
            "   b) Memperdalam ilmu agama melalui kajian online dari ustaz terpercaya dan menjauhi konten dakwah yang menyimpang.\n"
            "\n"
            "2) HIFZH AN-NAFS (Menjaga Jiwa):\n"
            "   a) Tidak mengikuti tawuran/perundungan, baik di dunia nyata maupun cyber bullying.\n"
            "   b) Menjaga kesehatan dengan makanan halal-sehat, olahraga, istirahat cukup, dan tidak begadang tanpa kebutuhan.\n"
            "\n"
            "3) HIFZH AL-'AQL (Menjaga Akal):\n"
            "   a) Memanfaatkan internet untuk belajar dan menuntut ilmu, bukan untuk hal yang merusak.\n"
            "   b) Menjauhi minuman keras, narkoba, dan zat psikoaktif lainnya.\n"
            "\n"
            "4) HIFZH AN-NASL (Menjaga Keturunan/Kehormatan):\n"
            "   a) Tidak berpacaran/berkhalwat, menutup aurat baik di dunia nyata maupun di sosmed.\n"
            "   b) Menjauhi konten pornografi dan menjaga pergaulan dengan lawan jenis.\n"
            "\n"
            "5) HIFZH AL-MAL (Menjaga Harta):\n"
            "   a) Hidup hemat, menjauhi gaya hidup boros/flexing dan menabung untuk masa depan.\n"
            "   b) Mencari rezeki yang halal (tidak mencuri, judi online, atau riba) dan menyisihkan uang untuk sedekah."
        ),
    },
]


# =====================================================================
# KISI-KISI
# =====================================================================
pg_kisi = [
    {"no": "1", "elemen": "Akhlak/Fikih – Larangan Pergaulan Bebas dan Zina",
     "cp": "Memahami larangan pergaulan bebas dan zina serta cara menghindarinya.",
     "tp": "Menjelaskan pergaulan bebas, QS Al-Isra:32, macam-macam dan hukuman zina, serta cara menghindari pergaulan bebas.",
     "indikator_soal": "Peserta didik dapat menentukan pengertian pergaulan bebas, kandungan QS Al-Isra:32, macam zina, hukuman zina ghairu muhshan, dan cara menghindari pergaulan bebas.",
     "jml": "5", "no_soal": "1 - 5", "bentuk": "PG", "tingkat": "Rendah/Sedang"},
    {"no": "2", "elemen": "Akidah/Akhlak – Mahabbah, Khauf, Raja', Tawakal",
     "cp": "Memahami mahabbah, khauf, raja', dan tawakal kepada Allah Swt.",
     "tp": "Menjelaskan mahabbah, khauf, raja', tawakal, dan penerapan tawakal.",
     "indikator_soal": "Peserta didik dapat menentukan pengertian mahabbah, khauf, raja', tawakal, dan contoh penerapan tawakal yang benar.",
     "jml": "5", "no_soal": "6 - 10", "bentuk": "PG", "tingkat": "Sedang"},
    {"no": "3", "elemen": "Akhlak – Gadab, Mujahadah an-Nafs, dan Syaja'ah",
     "cp": "Memahami gadab, mujahadah an-nafs, dan syaja'ah.",
     "tp": "Menjelaskan gadab, cara menghindarinya, mujahadah an-nafs, syaja'ah, dan penerapan syaja'ah.",
     "indikator_soal": "Peserta didik dapat menentukan pengertian gadab, cara menghindari marah sesuai sunah, pengertian mujahadah an-nafs, syaja'ah, dan contoh penerapannya.",
     "jml": "5", "no_soal": "11 - 15", "bentuk": "PG", "tingkat": "Sedang/Sulit"},
    {"no": "4", "elemen": "Fikih – Al-Kulliyat Al-Khamsah",
     "cp": "Memahami Al-Kulliyat Al-Khamsah sebagai prinsip dasar hukum Islam.",
     "tp": "Menjelaskan Al-Kulliyat Al-Khamsah dan kelima prinsipnya (hifzh ad-din, an-nafs, al-'aql, an-nasl, al-mal).",
     "indikator_soal": "Peserta didik dapat menentukan pengertian Al-Kulliyat Al-Khamsah, makna hifzh ad-din, hifzh an-nafs, hifzh al-'aql, dan urutan kelima prinsipnya.",
     "jml": "5", "no_soal": "16 - 20", "bentuk": "PG", "tingkat": "Sedang/Sulit"},
]

essay_kisi = [
    {"no": "1", "elemen": "Akhlak/Fikih/Al-Qur'an – Pergaulan Bebas dan Zina",
     "cp": "Memahami secara komprehensif larangan pergaulan bebas dan zina.",
     "tp": "Menjelaskan pergaulan bebas dan dampaknya, zina dan hukumannya, serta kandungan QS Al-Isra:32.",
     "indikator_soal": "Peserta didik dapat menjelaskan pengertian, dampak, cara menghindari pergaulan bebas, macam dan hukuman zina, serta kandungan QS Al-Isra:32 beserta contoh penerapannya.",
     "jml": "3", "no_soal": "1 - 3", "bentuk": "Esay", "tingkat": "Sedang/Sulit"},
    {"no": "2", "elemen": "Akidah/Akhlak – Mahabbah, Khauf, Raja', Tawakal",
     "cp": "Memahami mahabbah, khauf, raja', dan tawakal beserta penerapannya.",
     "tp": "Menjelaskan mahabbah, khauf, raja', tawakal yang benar, dan contoh penerapan dalam kehidupan pelajar.",
     "indikator_soal": "Peserta didik dapat menjelaskan pengertian mahabbah, khauf, raja', tawakal yang benar, tahapannya, dan contoh penerapan dalam kehidupan pelajar.",
     "jml": "2", "no_soal": "4 - 5", "bentuk": "Esay", "tingkat": "Sedang"},
    {"no": "3", "elemen": "Akhlak – Gadab, Mujahadah an-Nafs, Syaja'ah",
     "cp": "Memahami gadab, mujahadah an-nafs, dan syaja'ah.",
     "tp": "Menjelaskan gadab dan cara menghindarinya, mujahadah an-nafs, dan syaja'ah beserta contohnya.",
     "indikator_soal": "Peserta didik dapat menjelaskan pengertian gadab, dampak negatif, cara menghindari, serta mujahadah an-nafs dan syaja'ah beserta contoh penerapannya.",
     "jml": "2", "no_soal": "6 - 7", "bentuk": "Esay", "tingkat": "Sedang/Sulit"},
    {"no": "4", "elemen": "Fikih – Al-Kulliyat Al-Khamsah",
     "cp": "Memahami dan menerapkan Al-Kulliyat Al-Khamsah.",
     "tp": "Menjelaskan pengertian, kelima prinsip Al-Kulliyat Al-Khamsah, dan penerapannya di era modern.",
     "indikator_soal": "Peserta didik dapat menjelaskan pengertian Al-Kulliyat Al-Khamsah, kelima prinsipnya, contoh masing-masing, serta penerapannya bagi pelajar di era modern.",
     "jml": "3", "no_soal": "8 - 10", "bentuk": "Esay", "tingkat": "Sedang/Sulit"},
    # filler row 5 left empty (template has 5 essay slots)
    {"no": "", "elemen": "", "cp": "", "tp": "", "indikator_soal": "", "jml": "", "no_soal": "", "bentuk": "", "tingkat": ""},
]


# =====================================================================
# HELPERS
# =====================================================================
def set_cell_text(cell, lines, bold=False, size=None):
    if isinstance(lines, str):
        lines = lines.split('\n')
    tc = cell._tc
    for p in tc.findall(qn('w:p')):
        tc.remove(p)
    for line in lines:
        p = cell.add_paragraph()
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


def set_question_cell(cell, soal_text):
    tc = cell._tc
    for p in tc.findall(qn('w:p')):
        tc.remove(p)
    from docx.oxml import OxmlElement
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


def fill_header_para(paragraph, prefix, value):
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


def unmerge_header_cells_3_4(table, header_row_idx, label3, label4):
    """Unmerge cells 3 and 4 in the given header row, then set labels."""
    row = table.rows[header_row_idx]
    tr = row._tr
    tcs = tr.findall(qn('w:tc'))
    tc3 = tcs[3]
    # Remove gridSpan
    tcPr = tc3.find(qn('w:tcPr'))
    if tcPr is not None:
        gridSpan = tcPr.find(qn('w:gridSpan'))
        if gridSpan is not None:
            tcPr.remove(gridSpan)
    # Duplicate tc3
    new_tc = deepcopy(tc3)
    tc3.addnext(new_tc)
    # Now set text in tc3 -> label3, new_tc -> label4
    # Use the cell objects (after structure changed, we need fresh reference)
    # Just operate on _tc directly via set_cell_text by wrapping
    from docx.table import _Cell
    cell3 = _Cell(tc3, row)
    cell4 = _Cell(new_tc, row)
    set_cell_text(cell3, label3, bold=True, size=10)
    set_cell_text(cell4, label4, bold=True, size=10)


# =====================================================================
# 1. Cover page
# =====================================================================
for p in doc.paragraphs:
    txt = p.text.strip()
    if txt.startswith("Nama  Guru") or txt.startswith("Nama Guru"):
        fill_header_para(p, "Nama Guru", NAMA_GURU)
    elif txt.startswith("Mata Pelajaran"):
        fill_header_para(p, "Mata Pelajaran", f"{MAPEL} / Kelas {KELAS}")
    elif txt.startswith("Kelas"):
        fill_header_para(p, "Kelas", KELAS)


# =====================================================================
# 2. Intro Table (Table 0)
# =====================================================================
t0 = doc.tables[0]
intro_lines = [
    f"Nama Sekolah\t    : SMK 1 PANCASILA",
    f"Nama Penulis Soal\t: {NAMA_GURU}",
    f"Mata Pelajaran/Kelas\t: {MAPEL} / Kelas {KELAS}",
    f"Satuan Unit Kerja\t: SMK 1 PANCASILA AMBULU",
    f"Kurikulum\t\t: Kurikulum Merdeka",
    f"Jumlah Soal\t\t: 30 butir (20 PG + 10 Esay)",
]
set_cell_text(t0.rows[0].cells[0], intro_lines, size=11)


# =====================================================================
# 3. Kisi-kisi (Table 1) – unmerge headers to add Indikator Soal column
# =====================================================================
t1 = doc.tables[1]

# Unmerge header rows 0 and 5 (split column 3 (TP) into TP + Indikator Soal)
unmerge_header_cells_3_4(t1, 0, "Tujuan Pembelajaran", "Indikator Soal")
unmerge_header_cells_3_4(t1, 5, "Tujuan Pembelajaran", "Indikator Soal")

def fill_kisi_row(row, entry):
    cells = row.cells
    set_cell_text(cells[0], entry["no"], size=10)
    set_cell_text(cells[1], entry["elemen"], size=10)
    set_cell_text(cells[2], entry["cp"], size=10)
    set_cell_text(cells[3], entry["tp"], size=10)
    set_cell_text(cells[4], entry["indikator_soal"], size=10)
    set_cell_text(cells[5], entry["jml"], size=10)
    set_cell_text(cells[6], entry["no_soal"], size=10)
    set_cell_text(cells[7], entry["bentuk"], size=10)
    set_cell_text(cells[8], entry["tingkat"], size=10)

for i, entry in enumerate(pg_kisi):
    fill_kisi_row(t1.rows[1 + i], entry)
for i, entry in enumerate(essay_kisi):
    fill_kisi_row(t1.rows[6 + i], entry)
set_cell_text(t1.rows[11].cells[5], "30", size=10, bold=True)
set_cell_text(t1.rows[11].cells[6], "PG: 1-20\nEsay: 1-10", size=10, bold=True)


# =====================================================================
# 4. Duplicate PG kartu soal (13 -> 20)
# =====================================================================
elements = list(body)
last_pg_tbl = elements[61]
last_pg_para = elements[62]
insert_after = last_pg_para
for _ in range(7):
    new_tbl = deepcopy(last_pg_tbl)
    new_para = deepcopy(last_pg_para)
    insert_after.addnext(new_tbl)
    new_tbl.addnext(new_para)
    insert_after = new_para


# =====================================================================
# 5. Fill kartu soal
# =====================================================================
def fill_kartu_soal(table, item, is_essay=False):
    rows = table.rows
    set_cell_text(rows[2].cells[0], item["elemen"], size=10)
    set_cell_text(rows[6].cells[0], item["cp"], size=10)
    set_cell_text(rows[10].cells[0], item["indikator_kompetensi"], size=10)
    set_cell_text(rows[12].cells[0], item["indikator_soal"], size=10)
    set_cell_text(rows[13].cells[0], ["Tingkat Kesukaran:", f"☑ {item['tingkat']}"], size=10)
    set_cell_text(rows[5].cells[2], str(item["no"]), size=12, bold=True)
    if not is_essay:
        set_cell_text(rows[11].cells[2], ["KUNCI JAWABAN", "", item["kunci"]], size=12, bold=True)
    else:
        set_cell_text(rows[11].cells[2], ["PEDOMAN JAWABAN", "(lihat kunci di bawah)"], size=10, bold=True)

    soal_lines = item["soal"].split('\n')
    if is_essay:
        content = list(soal_lines)
        content.append("")
        content.append("Kunci Jawaban / Pedoman Penskoran:")
        content.extend(item["jawaban"].split('\n'))
    else:
        content = soal_lines
    set_question_cell(rows[3].cells[3], '\n'.join(content))

for i, item in enumerate(PG):
    fill_kartu_soal(doc.tables[2 + i], item, is_essay=False)


# =====================================================================
# 6. Delete excess essay tables (21 -> 10)
# =====================================================================
elements = list(body)
tbl_indexes = [i for i, e in enumerate(elements) if e.tag.split('}')[-1] == 'tbl']
to_delete_tbl_idx = tbl_indexes[32:]
to_remove = []
for ti in to_delete_tbl_idx:
    tbl = elements[ti]
    to_remove.append(tbl)
    if ti + 1 < len(elements):
        next_el = elements[ti + 1]
        if next_el.tag.split('}')[-1] == 'p':
            to_remove.append(next_el)
for el in to_remove:
    has_sect = el.find('.//' + qn('w:sectPr')) is not None
    if has_sect:
        continue
    el.getparent().remove(el)


# =====================================================================
# 7. Fill essay (tables 22..31)
# =====================================================================
for i, item in enumerate(ESSAY):
    fill_kartu_soal(doc.tables[22 + i], item, is_essay=True)


# =====================================================================
# 8. Save
# =====================================================================
import os
os.makedirs('/home/user/dianindri/output', exist_ok=True)
output_path = '/home/user/dianindri/output/KARTU_SOAL_PAI_Kelas_X_Genap_2025_2026.docx'
doc.save(output_path)
print(f"Saved to: {output_path}")
print(f"Total tables: {len(doc.tables)}")
