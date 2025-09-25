import json
import pandas as pd

# === 1. Baca file JSON ===
with open("MuhammadKhairulIhsan_V3925031.json", "r", encoding="utf-8") as f:
    data = json.load(f)

dataset = data["Muhammad_Khairul_Ihsan_V3925031"]

# === 2. Ambil 25 data pertama dari setiap sumber ===
media_sosial_df     = pd.DataFrame(dataset["media_sosial"][:25])
pelaporan_warga_df  = pd.DataFrame(dataset["pelaporan_warga"][:25])
cctv_df             = pd.DataFrame(dataset["cctv_kamera_smart_city"][:25])
layanan_navigasi_df = pd.DataFrame(dataset["layanan_navigasi"][:25])

# === 3. Simpan ke Excel dengan sheet terpisah ===
output_file = "Dataset_Demo_4_Sumber.xlsx"
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    media_sosial_df.to_excel(writer, sheet_name="Media Sosial", index=False)
    pelaporan_warga_df.to_excel(writer, sheet_name="Pelaporan Warga", index=False)
    cctv_df.to_excel(writer, sheet_name="CCTV Smart City", index=False)
    layanan_navigasi_df.to_excel(writer, sheet_name="Layanan Navigasi", index=False)

print(f"✅ File berhasil dibuat: {output_file}")
