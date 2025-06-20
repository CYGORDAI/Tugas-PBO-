from user import User

# Menambahkan user baru
u = User("20230040176", "Septian Adiwiguna", "Teknik Informatika")
u.save()

# Menampilkan semua user
users = User.all()
for user in users:
    print(f"{user['nim']} {user['nama']} - {user['prodi']}")
