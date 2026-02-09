catatan = []

def tambah_catatan():
    """Meminta input mapel, topik, dan durasi (menit), lalu menyimpan ke list catatan."""
    mapel = input("Mapel: ").strip()
    topik = input("Topik: ").strip()

    while True:
        durasi_str = input("Durasi belajar (menit): ").strip()
        try:
            durasi = int(durasi_str)
            if durasi < 0:
                print("Durasi tidak boleh negatif. Coba lagi.")
                continue
            break
        except ValueError:
            print("Masukkan angka bulat untuk durasi (mis. 30). Coba lagi.")

    catatan.append({
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi,
    })
    print("Catatan berhasil ditambahkan.")

def lihat_catatan():
    """Menampilkan semua catatan belajar dengan rapi.
    Menyediakan opsi untuk memfilter berdasarkan mapel.
    Jika kosong atau filter tidak menemukan data, tampilkan pesan."""
    if not catatan:
        print("Belum ada catatan belajar.")
        return

    pilih = input("Ingin memfilter berdasarkan mapel? (y/n): ").strip().lower()
    if pilih == "y":
        nama_mapel = input("Masukkan nama mapel untuk filter: ").strip()
        hasil = [c for c in catatan if c["mapel"].lower() == nama_mapel.lower()]
        if not hasil:
            print(f"Tidak ada catatan untuk mapel '{nama_mapel}'.")
            return
        print(f"\nCatatan untuk mapel '{nama_mapel}':")
        for i, c in enumerate(hasil, start=1):
            print(f"{i}. Mapel: {c['mapel']} | Topik: {c['topik']} | Durasi: {c['durasi']} menit")
    else:
        print("\nDaftar Catatan Belajar:")
        for i, c in enumerate(catatan, start=1):
            print(f"{i}. Mapel: {c['mapel']} | Topik: {c['topik']} | Durasi: {c['durasi']} menit")

def total_waktu():
    """Menghitung dan menampilkan total durasi belajar.
    Menyediakan opsi untuk menghitung total per mapel. Jika tidak difilter,
    tampilkan juga rincian durasi untuk setiap mapel.
    """
    if not catatan:
        print("Belum ada catatan belajar.")
        return

    pilih = input("Ingin memfilter total berdasarkan mapel? (y/n): ").strip().lower()
    if pilih == "y":
        nama_mapel = input("Masukkan nama mapel untuk filter: ").strip()
        hasil = [c for c in catatan if c["mapel"].lower() == nama_mapel.lower()]
        if not hasil:
            print(f"Tidak ada catatan untuk mapel '{nama_mapel}'.")
            return
        total = sum(c["durasi"] for c in hasil)
        konteks = f" untuk mapel '{nama_mapel}'"
        jam = total // 60
        menit = total % 60
        if jam > 0:
            print(f"Total waktu belajar{konteks}: {total} menit ({jam} jam {menit} menit)")
        else:
            print(f"Total waktu belajar{konteks}: {total} menit")

        # Rincian per topik untuk mapel yang difilter
        totals_per_topik = {}
        for c in hasil:
            key = c["topik"]
            totals_per_topik[key] = totals_per_topik.get(key, 0) + c["durasi"]

        print("\nRincian per topik:")
        for t, d in totals_per_topik.items():
            j = d // 60
            mt = d % 60
            if j > 0:
                print(f"- {t}: {d} menit ({j} jam {mt} menit)")
            else:
                print(f"- {t}: {d} menit")
    else:
        totals_per_mapel = {}
        for c in catatan:
            key = c["mapel"]
            totals_per_mapel[key] = totals_per_mapel.get(key, 0) + c["durasi"]

        total = sum(totals_per_mapel.values())
        jam = total // 60
        menit = total % 60
        if jam > 0:
            print(f"Total waktu belajar: {total} menit ({jam} jam {menit} menit)")
        else:
            print(f"Total waktu belajar: {total} menit")

        print("\nRincian per mapel:")
        for m, t in totals_per_mapel.items():
            j = t // 60
            mt = t % 60
            if j > 0:
                print(f"- {m}: {t} menit ({j} jam {mt} menit)")
            else:
                print(f"- {m}: {t} menit")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")