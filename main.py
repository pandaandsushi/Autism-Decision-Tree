# A simple program CLI based a representation for the decision tree made

import function as fn
print("Selamat datang di program berbasis pohon keputusan sederhana untuk mendiagnosis autisme pada anak!\n")
print("Silakan masukkan inputan (yes/no) sesuai dengan keadaan anak saat ini\n")
question={
    "r":"Anak stress jika ada perubahan rutinitas/keadaan?",
    "s":"Anak memiliki ketertarikan untuk berinteraksi sosial?",
    "t":"Ada anggota keluarga lain yang autis?",
    "u":"Anak merespon suara, sentuhan, cahaya, dan bau dengan tidak normal?",
    "v":"Anak hanya tertarik pada topik tertentu?",
    "w":"Anak sulit bicara dan susah dimengerti?",
    "x":"Anak tidak mampu kontak mata ketika diajak bicara?",
    "y":"Anak suka berputar-putar, berkedip-kedip, dan melakukan gerakan berulang-ulang lainnya?",
    "z":"Anak pernah/sering melakukan tindakan tidak lazim (agresi, menyakiti diri sendiri)?",
}

answer = {key: fn.getinput(value) for key, value in question.items()}
isR = answer["r"]
isS = answer["s"]
isT = answer["t"]
isU = answer["u"]
isV = answer["v"]
isW = answer["w"]
isX = answer["x"]
isY = answer["y"]
isZ = answer["z"]
print("Berikut adalah hasilnya... ")
case1 = isS==1
case2 = isR==1 and isU==0 and isV==0 and isY==0
case3 = isR==0 and isV==0
case4 = isR==1 and isT==0 and isV==0
if (case1 or case2 or case3 or case4):
    print("Anak BUKANLAH penderita autisme.\n")
else:
    print("Anak BERPOTENSI sebagai penderita autisme!\n")
print("*Harap periksakan pada tenaga kesehatan profesional untuk memastikan hasilnya kembali.\n")