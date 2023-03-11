## Python' da veri tipleri
# 1)Sayısal Veri Tipi: tamsayıları temsil eden int, ondalık sayıları temsl eden float, karmaşık sayıları temsil eden complex olarak ayırabiliriz.
# 2)String: Metinsel ifadeleri temsil eden ifadelere str, string denmektedir.
# 3)List: Birden çok öğeyi depolamak maksadıyla kullanılmaktadır.
# 4)Tuple: Listeler gibi birden fazla öge depolanabilir fakat tuple veri tipinde listeye kıyasla veriler değiştirilememektedir.
# 5)Sözlükler: dict: anahtar-değer çifti şeklinde öge depolamak maksadıyla kullanılmaktadır.
# 6)Kümeler set: öge koleksiyonunu depolamak için kullanılır.
# 7)Boolean: Şartlı ifadedir. True yada false olarak çıktı verir.

#Kodlama.io sitesine girdiğimizde karşımıza kurs isimleri çıkmaktadır. "(2023) Yazılım Geliştirici Yetiştirme Kampı - Python & Selenium" gibi kurs isimleri string ifadelerle yazılmıştır.

#Kodlama.io sitesinde şart blokları örnekleri

# Şartlı Bloklar
# Siteye giriş yapma kısmı örnek olarak gösterilebilir.

email = "ornek@hotmail.com"
password = "12345678"

if email == "ornek@hotmail.com":
    print("Email adresiniz dogru >>>")
if password == "12345678":
    print("Şifreniz Dogru >>>")
    print("Başarıyla giriş yaptınız")
else:
    print("E-mail adresiniz veya şifreniz hatalı")
