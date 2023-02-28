months_turkish_english = {
    "January" : "Ocak",
    "February" : "Şubat",
    "March" : "Mart",
    "April" : "Nisan",
    "May" : "Mayıs",
    "June" : "Haziran",
    "July" : "Temmuz",
    "August" : "Ağustos",
    "September" : "Eylül",
    "October" : "Ekim",
    "November" : "Kasım",
    "December" : "Aralık",
}

print(months_turkish_english["March"])
print(months_turkish_english.get("mmm", "Not a valid value"))
print(months_turkish_english.get("November", "Not a valid value"))