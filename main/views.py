from django.shortcuts import render

def show_main(request):
    context = {
        'nama_aplikasi' : 'Kapuas Sportswear',
        'nama': 'Faiz Kusumadinata',
        'kelas': 'PBP A'
    }

    return render(request, "main.html", context)
