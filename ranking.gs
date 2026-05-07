// ============================================================
// SCRIPT RANKING - REKRUTMEN SMK 1 PANCASILA
//
// CARA PAKAI:
//   1. Buka Script editor di Google Form
//   2. Paste script ini
//   3. Jalankan: setupRanking()
//   4. Izinkan akses → selesai
//
//   onFormSubmit() berjalan OTOMATIS setiap ada yang submit.
//   Untuk update manual dari data yang sudah masuk,
//   jalankan: updateRanking()
// ============================================================


// ── LANGKAH 1: Jalankan sekali untuk setup ─────────────────
function setupRanking() {

  var form = FormApp.getActiveForm();
  var ss   = SpreadsheetApp.openById(form.getDestinationId());

  // Hapus sheet lama jika ada, lalu buat baru
  var existing = ss.getSheetByName("RANKING");
  if (existing) ss.deleteSheet(existing);

  var sheet = ss.insertSheet("RANKING", 0);

  // Header
  sheet.appendRow(["NAMA", "NILAI", "KETERANGAN"]);

  sheet.getRange(1, 1, 1, 3)
    .setBackground("#1a73e8")
    .setFontColor("#ffffff")
    .setFontWeight("bold")
    .setFontSize(11)
    .setHorizontalAlignment("center");

  sheet.setColumnWidth(1, 220);
  sheet.setColumnWidth(2, 90);
  sheet.setColumnWidth(3, 120);
  sheet.setFrozenRows(1);

  // Setup trigger otomatis
  var triggers = ScriptApp.getProjectTriggers();
  for (var t = 0; t < triggers.length; t++) {
    if (triggers[t].getHandlerFunction() === "onFormSubmit") {
      ScriptApp.deleteTrigger(triggers[t]);
    }
  }
  ScriptApp.newTrigger("onFormSubmit").forForm(form).onFormSubmit().create();

  // Isi data dari respons yang sudah ada
  updateRanking();

  Logger.log("✅ Sheet RANKING siap! Trigger otomatis aktif.");
  Logger.log("📊 Spreadsheet: " + ss.getUrl());
}


// ── Update ranking (bisa dijalankan manual kapan saja) ─────
function updateRanking() {

  var form  = FormApp.getActiveForm();
  var ss    = SpreadsheetApp.openById(form.getDestinationId());
  var sheet = ss.getSheetByName("RANKING");

  if (!sheet) {
    Logger.log("❌ Sheet RANKING tidak ada. Jalankan setupRanking() dulu.");
    return;
  }

  // Hapus data lama, pertahankan header
  var lastRow = sheet.getLastRow();
  if (lastRow > 1) sheet.getRange(2, 1, lastRow - 1, 3).clear();

  // Ambil semua respons form
  var responses = form.getResponses();
  var data = [];

  for (var i = 0; i < responses.length; i++) {
    var resp  = responses[i];
    var nama  = "";
    var nilai = resp.getScore() || 0;

    var itemResps = resp.getItemResponses();
    for (var j = 0; j < itemResps.length; j++) {
      if (itemResps[j].getItem().getTitle() === "Nama Lengkap") {
        nama = itemResps[j].getResponse();
        break;
      }
    }

    if (nama) data.push([nama, nilai]);
  }

  // Urutkan nilai tertinggi ke terendah
  data.sort(function(a, b) { return b[1] - a[1]; });

  // Tulis ke sheet
  for (var k = 0; k < data.length; k++) {
    var baris      = k + 2;
    var namaVal    = data[k][0];
    var nilaiVal   = data[k][1];
    var keterangan = nilaiVal > 75 ? "LOLOS" : "GUGUR";

    sheet.getRange(baris, 1).setValue(namaVal);
    sheet.getRange(baris, 2).setValue(nilaiVal)
      .setHorizontalAlignment("center")
      .setFontWeight("bold");

    var ketCell = sheet.getRange(baris, 3);
    ketCell.setValue(keterangan)
      .setFontWeight("bold")
      .setHorizontalAlignment("center");

    if (nilaiVal > 75) {
      ketCell.setBackground("#34a853").setFontColor("#ffffff"); // Hijau
    } else {
      ketCell.setBackground("#ea4335").setFontColor("#ffffff"); // Merah
    }
  }
}


// ── Otomatis dipanggil setiap ada peserta submit ────────────
function onFormSubmit(e) {
  updateRanking();
}
