// ============================================================
// SCRIPT GOOGLE APPS SCRIPT - SOAL REKRUTMEN SMK 1 PANCASILA
// Topik: Coding, AI Tools & Konten Kreator
// Total: 50 Soal | Nilai per soal: 2 | Total: 100
//
// CARA PAKAI:
//   1. Buka Google Form kamu
//   2. Klik ikon titik tiga (⋮) pojok kanan atas → "Script editor"
//   3. Hapus semua kode yang ada
//   4. Paste SELURUH script ini
//   5. Klik Save (Ctrl+S), lalu klik ▶ Run
//   6. Pilih fungsi: buatSoalRekrutmen
//   7. Klik "Review permissions" → izinkan akses
// ============================================================

function buatSoalRekrutmen() {

  var form = FormApp.getActiveForm();

  form.setTitle("Tes Rekrutmen Karyawan - SMK 1 Pancasila Ambulu");
  form.setDescription(
    "Bidang: Coding, AI Tools & Konten Kreator\n" +
    "Jumlah Soal: 50 | Nilai per soal: 2 | Total Nilai: 100\n" +
    "Waktu: 60 menit\n\n" +
    "Petunjuk: Pilih satu jawaban yang paling tepat."
  );

  // Format: ["Pertanyaan", ["A","B","C","D","E"], indeks_jawaban_benar]
  // Indeks jawaban: 0=A, 1=B, 2=C, 3=D, 4=E

  // ── AKTIFKAN QUIZ MODE ─────────────────────────────────────
  form.setIsQuiz(true);

  var huruf = ["A", "B", "C", "D", "E"];

  // Helper untuk menambahkan satu soal ke form
  function tambahSoal(item_data) {
    var pertanyaan = item_data[0];
    var pilihan    = item_data[1];
    var jawabanIdx = item_data[2];

    var item = form.addMultipleChoiceItem();
    item.setTitle(pertanyaan);
    item.setRequired(true);
    item.setPoints(2);

    var choices = [];
    for (var j = 0; j < pilihan.length; j++) {
      choices.push(item.createChoice(huruf[j] + ". " + pilihan[j], j === jawabanIdx));
    }
    item.setChoices(choices);
  }

  // ══════════════════════════════════════════════════════════
  // BAGIAN 1: CODING (Soal 1–20)
  // ══════════════════════════════════════════════════════════
  form.addSectionHeaderItem()
    .setTitle("BAGIAN 1: CODING")
    .setHelpText("Soal nomor 1 sampai 20");

  var soalCoding = [
    ["1. Bahasa pemrograman yang paling umum untuk membuat website di sisi frontend adalah...",
      ["Python", "Java", "JavaScript", "C++", "PHP"], 2],

    ["2. Tag HTML yang digunakan untuk membuat hyperlink adalah...",
      ["<link>", "<a>", "<href>", "<url>", "<nav>"], 1],

    ["3. Properti CSS yang digunakan untuk mengubah warna teks adalah...",
      ["font-color", "text-color", "color", "foreground", "style"], 2],

    ["4. Kepanjangan dari IDE dalam dunia pemrograman adalah...",
      ["Integrated Design Environment", "Integrated Development Environment", "Internal Development Engine", "Internet Development Engine", "Integrated Data Editor"], 1],

    ["5. Perintah Python yang benar untuk mencetak teks adalah...",
      ["echo()", "print()", "console.log()", "printf()", "puts()"], 1],

    ["6. Dalam pemrograman, fungsi if-else digunakan untuk...",
      ["Mengulang blok kode", "Mendefinisikan fungsi baru", "Membuat percabangan logika", "Mengimpor library", "Membuat array"], 2],

    ["7. Manakah yang merupakan contoh tipe data boolean?",
      ["'True' (string)", "123 (integer)", "True", "3.14 (float)", "[1,2,3] (list)"], 2],

    ["8. Fungsi tag div dalam HTML adalah...",
      ["Membuat tabel", "Membuat tautan", "Membuat gambar", "Sebagai container/wadah elemen", "Membuat formulir"], 3],

    ["9. Struktur data yang menggunakan prinsip LIFO (Last In First Out) disebut...",
      ["Queue", "Array", "Stack", "Linked List", "Tree"], 2],

    ["10. Yang dimaksud dengan responsive design dalam web development adalah...",
      ["Website yang berjalan offline", "Website yang tampilannya menyesuaikan ukuran layar", "Website dengan banyak animasi", "Website dengan banyak halaman", "Website terhubung ke database"], 1],

    ["11. Dalam JavaScript, cara mendeklarasikan variabel yang nilainya tidak bisa diubah adalah...",
      ["var", "let", "const", "static", "final"], 2],

    ["12. Git adalah alat yang digunakan untuk...",
      ["Mendesain website", "Version control atau manajemen versi kode", "Membuat database", "Mengoptimasi gambar", "Membuat animasi"], 1],

    ["13. Kepanjangan dari SQL adalah...",
      ["Simple Query Language", "Structured Query Language", "System Query Language", "Standard Query Language", "Sequential Query Language"], 1],

    ["14. Manakah yang termasuk framework CSS populer?",
      ["Django", "Laravel", "React", "Bootstrap", "Node.js"], 3],

    ["15. Loop yang digunakan saat jumlah iterasi belum diketahui pasti disebut...",
      ["for loop", "do-while loop", "while loop", "foreach loop", "repeat loop"], 2],

    ["16. API adalah singkatan dari...",
      ["Application Programming Interface", "Automated Program Integration", "Application Process Integration", "Automated Programming Interface", "Application Protocol Interface"], 0],

    ["17. Ekstensi file untuk bahasa Python adalah...",
      [".js", ".java", ".py", ".php", ".rb"], 2],

    ["18. Konsep OOP yang memungkinkan class mewarisi sifat class lain disebut...",
      ["Encapsulation", "Polymorphism", "Abstraction", "Inheritance", "Interface"], 3],

    ["19. Fungsi utama dari framework dalam pengembangan aplikasi adalah...",
      ["Menggantikan bahasa pemrograman", "Mempercepat dan menyederhanakan proses pengembangan", "Membuat aplikasi lebih lambat", "Menghapus bug secara otomatis", "Membuat desain grafis"], 1],

    ["20. Manakah yang BUKAN contoh bahasa pemrograman backend?",
      ["PHP", "Python", "Node.js", "CSS", "Ruby"], 3]
  ];

  for (var i = 0; i < soalCoding.length; i++) {
    tambahSoal(soalCoding[i]);
  }

  // ══════════════════════════════════════════════════════════
  // BAGIAN 2: AI TOOLS (Soal 21–35)
  // ══════════════════════════════════════════════════════════
  form.addSectionHeaderItem()
    .setTitle("BAGIAN 2: AI TOOLS")
    .setHelpText("Soal nomor 21 sampai 35");

  var soalAI = [
    ["21. ChatGPT dikembangkan oleh perusahaan...",
      ["Google", "Meta", "OpenAI", "Microsoft", "Amazon"], 2],

    ["22. AI generatif adalah jenis AI yang mampu...",
      ["Hanya menganalisis data angka", "Membuat konten baru seperti teks, gambar, atau musik", "Menjalankan robot secara fisik", "Hanya bekerja dengan database", "Menggantikan sistem operasi"], 1],

    ["23. Alat AI paling populer untuk menghasilkan gambar dari teks adalah...",
      ["ChatGPT", "DALL-E atau Midjourney", "Grammarly", "Notion AI", "GitHub Copilot"], 1],

    ["24. Dalam konteks AI, prompt berarti...",
      ["Nama model AI", "Perintah atau instruksi yang diberikan kepada AI", "Hasil output dari AI", "Kode pemrograman AI", "Server AI"], 1],

    ["25. GitHub Copilot adalah alat AI yang berfungsi untuk...",
      ["Membuat desain logo", "Menyunting video otomatis", "Membantu menulis kode program", "Mengelola media sosial", "Membuat presentasi"], 2],

    ["26. Teknik memberikan contoh dalam prompt agar AI menghasilkan output lebih akurat disebut...",
      ["Zero-shot prompting", "Few-shot prompting", "Chain-of-thought prompting", "Negative prompting", "System prompting"], 1],

    ["27. Gemini adalah produk AI yang dikembangkan oleh...",
      ["Apple", "Meta", "OpenAI", "Google", "Samsung"], 3],

    ["28. Kepanjangan dari LLM dalam dunia AI adalah...",
      ["Large Language Model", "Long Learning Machine", "Linear Logic Model", "Large Learning Module", "Layered Language Machine"], 0],

    ["29. Contoh penggunaan AI untuk produktivitas di sekolah adalah...",
      ["Bermain game online", "Menggunakan Notion AI untuk merangkum materi", "Menonton YouTube", "Membagikan meme di WhatsApp", "Mengunduh film"], 1],

    ["30. Alat AI yang membantu memperbaiki tata bahasa dan gaya penulisan adalah...",
      ["Canva AI", "Grammarly", "Runway ML", "ElevenLabs", "Pika Labs"], 1],

    ["31. Risiko utama penggunaan AI secara tidak bijak di dunia kerja adalah...",
      ["AI terlalu murah", "Plagiarisme dan misinformasi dari konten yang tidak diverifikasi", "AI bekerja terlalu cepat", "AI tidak bisa diakses di Indonesia", "AI hanya untuk programmer"], 1],

    ["32. Canva AI menyediakan fitur yang dapat...",
      ["Memprogram robot", "Membuat desain grafis otomatis berdasarkan teks", "Mengelola server website", "Menerjemahkan kode program", "Membuat database sekolah"], 1],

    ["33. Model AI yang menggunakan data pasangan teks-gambar untuk membuat gambar disebut...",
      ["Natural Language Processing", "Diffusion Model", "Decision Tree", "Support Vector Machine", "K-Means Clustering"], 1],

    ["34. ElevenLabs adalah platform AI yang berfokus pada...",
      ["Pengeditan foto", "Pembuatan musik instrumental", "Kloning dan sintesis suara", "Pembuatan video pendek", "Analisis data keuangan"], 2],

    ["35. Saat menggunakan AI untuk keperluan sekolah, yang harus diperhatikan adalah...",
      ["Menyalin semua output AI tanpa verifikasi", "Memverifikasi dan mengedit output AI sebelum digunakan", "Menggunakan AI secara rahasia dari guru", "Tidak perlu memahami output AI", "Biarkan AI mengerjakan semua tugas"], 1]
  ];

  for (var i = 0; i < soalAI.length; i++) {
    tambahSoal(soalAI[i]);
  }

  // ══════════════════════════════════════════════════════════
  // BAGIAN 3: KONTEN KREATOR (Soal 36–50)
  // ══════════════════════════════════════════════════════════
  form.addSectionHeaderItem()
    .setTitle("BAGIAN 3: KONTEN KREATOR")
    .setHelpText("Soal nomor 36 sampai 50");

  var soalKonten = [
    ["36. Yang dimaksud dengan thumbnail dalam konten YouTube adalah...",
      ["Judul video", "Gambar pratinjau yang mewakili sebuah video", "Deskripsi video", "Tag video", "Watermark video"], 1],

    ["37. Rasio aspek ideal untuk konten video TikTok dan Instagram Reels adalah...",
      ["16:9", "4:3", "1:1", "9:16", "2:1"], 3],

    ["38. CTR (Click-Through Rate) dalam pemasaran digital berarti...",
      ["Jumlah total penonton", "Persentase pengguna yang mengklik setelah melihat konten", "Jumlah komentar", "Waktu tonton rata-rata", "Jumlah pembagian konten"], 1],

    ["39. Strategi memposting konten secara konsisten dan terencana disebut...",
      ["Content Spam", "Content Calendar atau Jadwal Konten", "Content Boost", "Content Dumping", "Content Archive"], 1],

    ["40. Alat gratis populer untuk mengedit video di smartphone adalah...",
      ["Adobe Premiere Pro", "Final Cut Pro", "CapCut", "DaVinci Resolve", "Sony Vegas"], 2],

    ["41. Hook dalam konten video berfungsi untuk...",
      ["Menutup video dengan kesan yang baik", "Menarik perhatian penonton di detik-detik pertama", "Menambahkan musik latar", "Membuat transisi antar klip", "Menambahkan teks subtitle"], 1],

    ["42. SEO (Search Engine Optimization) untuk konten kreator berarti...",
      ["Teknik mempercepat unduhan video", "Strategi mengoptimasi konten agar mudah ditemukan di mesin pencari", "Cara membuat thumbnail yang menarik", "Teknik meningkatkan kualitas audio", "Cara berkolaborasi dengan kreator lain"], 1],

    ["43. Manakah yang termasuk KPI penting untuk konten media sosial?",
      ["Warna tema channel", "Engagement rate, reach, dan impressions", "Jumlah aplikasi yang terinstall", "Kecepatan internet kreator", "Merk kamera yang digunakan"], 1],

    ["44. Teknik storytelling AIDA dalam konten kreator merupakan singkatan dari...",
      ["Attention Interest Desire Action", "Audio Image Design Animation", "Audience Idea Draft Analyze", "Attention Idea Design Attract", "Analyze Integrate Develop Achieve"], 0],

    ["45. Strategi menjangkau audiens lebih luas tanpa biaya iklan yang paling tepat adalah...",
      ["Memposting konten sekali sebulan", "Menggunakan hashtag relevan dan berkolaborasi dengan kreator lain", "Menghapus konten lama", "Mengubah nama akun setiap minggu", "Memposting konten sama di semua platform"], 1],

    ["46. Format konten Behind the Scene (BTS) populer karena...",
      ["Lebih murah untuk dibuat", "Menampilkan sisi autentik kreator yang membuat audiens merasa dekat", "Tidak memerlukan editing", "Selalu viral di semua platform", "Dibuat otomatis oleh AI"], 1],

    ["47. Platform paling cocok untuk mendistribusikan konten artikel dan tulisan panjang adalah...",
      ["TikTok", "Instagram Stories", "LinkedIn dan Medium", "YouTube Shorts", "Twitter atau X"], 2],

    ["48. Fungsi utama Call to Action (CTA) dalam sebuah konten adalah...",
      ["Membuat konten lebih panjang", "Mendorong audiens melakukan tindakan tertentu seperti subscribe atau klik", "Menambahkan efek visual", "Mempercepat waktu loading konten", "Membuat konten lebih berwarna"], 1],

    ["49. Konten paling efektif untuk meningkatkan kepercayaan publik pada media sosial sekolah adalah...",
      ["Meme lucu tanpa konteks", "Konten prestasi siswa, kegiatan sekolah, dan testimoni alumni yang otentik", "Iklan berbayar setiap hari", "Repost konten dari sekolah lain", "Konten hiburan yang tidak berkaitan sekolah"], 1],

    ["50. Langkah pertama membuat kalender konten 1 bulan untuk tim media sekolah adalah...",
      ["Langsung membuat video tanpa perencanaan", "Mengidentifikasi tujuan, tema bulanan, dan momen penting sekolah", "Membeli follower agar akun cepat besar", "Menyalin konten sekolah lain", "Menunggu instruksi kepala sekolah setiap hari"], 1]
  ];

  for (var i = 0; i < soalKonten.length; i++) {
    tambahSoal(soalKonten[i]);
  }

  Logger.log("Selesai! 50 soal berhasil ditambahkan.");
  Logger.log("URL Form: " + form.getPublishedUrl());
}
