from django.shortcuts import render

kategori_liste=["macera","romantik","bilim kurgu","dram","aksiyon"]
film_liste=[
    {"film_adi":"film 1",
      "aciklama":"film 1 açıklama",
      "resim": "1.jpg" ,
      "anasayfa":True
    },
    {"film_adi":"film 2",
      "aciklama":"film 2 açıklama",
      "resim": "2.jpg" ,
      "anasayfa":True
    },
    {"film_adi":"film 3",
      "aciklama":"film 3 açıklama",
      "resim": "3.jpg" ,
      "anasayfa":False
    },{"film_adi":"film 4",
      "aciklama":"film 4 açıklama",
      "resim": "4.jpg", 
        "anasayfa":False
    }
    
    ]

def home(request):
    data={
        "kategoriler":kategori_liste,
        "filmler":film_liste
    }
    return render(request,"index.html",data)

def movies(request):
    data={
        "kategoriler":kategori_liste,
        "filmler":film_liste
    }
    return render(request,"movies.html",data)