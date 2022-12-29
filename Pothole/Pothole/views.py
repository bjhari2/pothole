from django.db import connection
from django.shortcuts import render


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    desc = cursor.description

    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def ins(request):
    params = (request.POST.get('address'), request.POST.get('remarks'))
    stmt = "INSERT into pothole (address, remarks) VALUES (%s, %s)"
    cursor = connection.cursor()
    cursor.execute(stmt, params)
    return render(request, 'index.html', {'info': "Inserted Successfully"})


def index(request):
    stmt = "SELECT p_id, address, remarks, time FROM pothole"
    cursor = connection.cursor()
    cursor.execute(stmt)
    r = dictfetchall(cursor)
    return render(request, 'index.html', {'data': r})
