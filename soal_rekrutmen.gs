// ============================================================
// SCRIPT GOOGLE APPS SCRIPT - REKRUTMEN SMK 1 PANCASILA
// Topik: Coding, AI Tools & Konten Kreator
// Total: 50 Soal | Nilai per soal: 2 | Total: 100
//
// URUTAN MENJALANKAN:
//   LANGKAH 1 → Jalankan: buatSoalRekrutmen()
//   LANGKAH 2 → Jalankan: setupLengkap()
//   (onFormSubmit akan berjalan OTOMATIS setiap ada peserta submit)
//
// CARA PASTE:
//   1. Buka Google Form → ikon ⋮ → Script editor
//   2. Hapus semua kode lama → Paste script ini → Save
//   3. Jalankan buatSoalRekrutmen() → izinkan akses
//   4. Jalankan setupLengkap() → izinkan akses
// ============================================================


// ════════════════════════════════════════════════════════════
// LANGKAH 1 — Buat Form + Biodata + Soal
// ════════════════════════════════════════════════════════════
function buatSoalRekrutmen() {

  var form = FormApp.getActiveForm();

  // Hapus semua item lama agar tidak dobel
  var existingItems = form.getItems();
  for (var i = existingItems.length - 1; i >= 0; i--) {
    form.deleteItem(existingItems[i]);
  }

  form.setTitle("Tes Rekrutmen Karyawan - SMK 1 Pancasila Ambulu");
  form.setDescription(
    "Bidang: Coding, AI Tools & Konten Kreator\n" +
    "Jumlah Soal: 50 | Nilai per soal: 2 | Total Nilai: 100\n" +
    "Waktu: 60 menit\n\n" +
    "Petunjuk: Pilih satu jawaban yang paling tepat.\n" +
    "Isi biodata dengan lengkap dan benar sebelum mengerjakan soal."
  );

  form.setIsQuiz(true);
  form.setShowLinkToRespondAgain(false);

  // ── BIODATA PESERTA ───────────────────────────────────────
  form.addSectionHeaderItem()
    .setTitle("DATA PESERTA")
    .setHelpText("Isi biodata kamu dengan lengkap dan benar.");

  form.addTextItem()
    .setTitle("Nama Lengkap")
    .setRequired(true);

  form.addTextItem()
    .setTitle("Nomor WhatsApp")
    .setHelpText("Contoh: 08123456789")
    .setRequired(true);

  form.addListItem()
    .setTitle("Pendidikan Terakhir")
    .setRequired(true)
    .setChoiceValues([
      "SMA / SMK / Sederajat",
      "D1",
      "D2",
      "D3",
      "S1 (Sarjana)",
      "S2 (Magister)",
      "S3 (Doktor)"
    ]);

  form.addTextItem()
    .setTitle("Pengalaman Mengajar")
    .setHelpText("Contoh: 2 tahun di SMP Negeri 1  |  Belum ada pengalaman")
    .setRequired(true);

  // ── HELPER FUNGSI ─────────────────────────────────────────
  var huruf = ["A", "B", "C", "D", "E"];

  function tambahSoal(data) {
    var item = form.addMultipleChoiceItem();
    item.setTitle(data[0]);
    item.setRequired(true);
    item.setPoints(2);
    var choices = [];
    for (var j = 0; j < data[1].length; j++) {
      choices.push(item.createChoice(huruf[j] + ". " + data[1][j], j === data[2]));
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

  for (var i = 0; i < soalCoding.length; i++) tambahSoal(soalCoding[i]);

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

  for (var i = 0; i < soalAI.length; i++) tambahSoal(soalAI[i]);

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

  for (var i = 0; i < soalKonten.length; i++) tambahSoal(soalKonten[i]);

  Logger.log("✅ Form selesai dibuat! 50 soal + biodata berhasil ditambahkan.");
  Logger.log("➡️  Sekarang jalankan: setupLengkap()");
}


// ════════════════════════════════════════════════════════════
// LANGKAH 2 — Buat Spreadsheet + 2 Sheet + Trigger Otomatis
// ════════════════════════════════════════════════════════════
function setupLengkap() {

  var form = FormApp.getActiveForm();

  // Buat spreadsheet baru
  var ss = SpreadsheetApp.create("Rekrutmen SMK 1 Pancasila Ambulu");

  // Hubungkan form ke spreadsheet
  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());

  // Tunggu Google membuat sheet "Form Responses 1"
  Utilities.sleep(3000);

  // ── Sheet 1: BIODATA PESERTA ──────────────────────────────
  var sheet1 = ss.insertSheet("BIODATA PESERTA", 0);

  var headers1 = ["No", "Waktu Submit", "Nama", "Nomor WA", "Pendidikan Terakhir", "Pengalaman Mengajar", "Nilai", "Keterangan"];
  sheet1.appendRow(headers1);

  // Style header Sheet 1
  var headerRange1 = sheet1.getRange(1, 1, 1, headers1.length);
  headerRange1.setBackground("#1a73e8")
              .setFontColor("#ffffff")
              .setFontWeight("bold")
              .setHorizontalAlignment("center");

  // Lebar kolom Sheet 1
  sheet1.setColumnWidth(1, 40);   // No
  sheet1.setColumnWidth(2, 150);  // Waktu
  sheet1.setColumnWidth(3, 180);  // Nama
  sheet1.setColumnWidth(4, 140);  // Nomor WA
  sheet1.setColumnWidth(5, 160);  // Pendidikan
  sheet1.setColumnWidth(6, 200);  // Pengalaman
  sheet1.setColumnWidth(7, 70);   // Nilai
  sheet1.setColumnWidth(8, 100);  // Keterangan
  sheet1.setFrozenRows(1);

  // ── Sheet 2: HASIL JAWABAN ────────────────────────────────
  var sheet2 = ss.insertSheet("HASIL JAWABAN", 1);

  var headers2 = ["No", "Waktu Submit", "Nama"];
  for (var i = 1; i <= 50; i++) {
    headers2.push("Soal " + i);
  }
  headers2.push("Nilai");
  sheet2.appendRow(headers2);

  // Style header Sheet 2
  var headerRange2 = sheet2.getRange(1, 1, 1, headers2.length);
  headerRange2.setBackground("#0f9d58")
              .setFontColor("#ffffff")
              .setFontWeight("bold")
              .setHorizontalAlignment("center");

  sheet2.setColumnWidth(1, 40);
  sheet2.setColumnWidth(2, 150);
  sheet2.setColumnWidth(3, 180);
  sheet2.setFrozenRows(1);
  sheet2.setFrozenColumns(3);

  // ── Hapus trigger lama lalu buat trigger baru ─────────────
  var triggers = ScriptApp.getProjectTriggers();
  for (var t = 0; t < triggers.length; t++) {
    ScriptApp.deleteTrigger(triggers[t]);
  }

  ScriptApp.newTrigger("onFormSubmit")
    .forForm(form)
    .onFormSubmit()
    .create();

  Logger.log("✅ Setup selesai!");
  Logger.log("📊 Spreadsheet: " + ss.getUrl());
  Logger.log("Form siap digunakan. Trigger otomatis sudah aktif.");
}


// ════════════════════════════════════════════════════════════
// OTOMATIS — Berjalan setiap ada peserta yang submit form
// (Jangan dijalankan manual)
// ════════════════════════════════════════════════════════════
function onFormSubmit(e) {

  var form    = FormApp.getActiveForm();
  var ss      = SpreadsheetApp.openById(form.getDestinationId());
  var sheet1  = ss.getSheetByName("BIODATA PESERTA");
  var sheet2  = ss.getSheetByName("HASIL JAWABAN");

  if (!sheet1 || !sheet2) {
    Logger.log("❌ Sheet tidak ditemukan. Jalankan setupLengkap() terlebih dahulu.");
    return;
  }

  var response      = e.response;
  var itemResponses = response.getItemResponses();
  var timestamp     = response.getTimestamp();
  var nilai         = response.getScore() || 0;

  // Pisahkan biodata dan jawaban soal
  var nama       = "";
  var nomorWA    = "";
  var pendidikan = "";
  var pengalaman = "";
  var answers    = [];

  for (var i = 0; i < itemResponses.length; i++) {
    var ir    = itemResponses[i];
    var title = ir.getItem().getTitle();
    var jawab = ir.getResponse();

    if      (title === "Nama Lengkap")          nama       = jawab;
    else if (title === "Nomor WhatsApp")         nomorWA    = jawab;
    else if (title === "Pendidikan Terakhir")    pendidikan = jawab;
    else if (title === "Pengalaman Mengajar")    pengalaman = jawab;
    else                                         answers.push(jawab);
  }

  // ── Tulis ke Sheet 1 (BIODATA PESERTA) ───────────────────
  var no1          = sheet1.getLastRow(); // baris header = 1, jadi no = lastRow
  var keterangan   = nilai > 75 ? "LOLOS" : "GUGUR";
  var barisBaru1   = sheet1.getLastRow() + 1;

  sheet1.appendRow([no1, timestamp, nama, nomorWA, pendidikan, pengalaman, nilai, keterangan]);

  // Warna kolom Nilai
  sheet1.getRange(barisBaru1, 7)
        .setFontWeight("bold")
        .setHorizontalAlignment("center");

  // Warna kolom Keterangan: LOLOS = hijau, GUGUR = merah
  var ketCell = sheet1.getRange(barisBaru1, 8);
  ketCell.setFontWeight("bold").setHorizontalAlignment("center");

  if (nilai > 75) {
    ketCell.setBackground("#34a853").setFontColor("#ffffff"); // Hijau
  } else {
    ketCell.setBackground("#ea4335").setFontColor("#ffffff"); // Merah
  }

  // ── Tulis ke Sheet 2 (HASIL JAWABAN) ─────────────────────
  var no2   = sheet2.getLastRow();
  var row2  = [no2, timestamp, nama].concat(answers).concat([nilai]);
  sheet2.appendRow(row2);

  // Warna nilai di Sheet 2
  var nilaiCol2 = sheet2.getLastRow();
  sheet2.getRange(nilaiCol2, row2.length)
        .setFontWeight("bold")
        .setHorizontalAlignment("center");
}
