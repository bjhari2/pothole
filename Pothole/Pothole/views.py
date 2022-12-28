from django.db import connection
from django.shortcuts import render


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    desc = cursor.description

    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def index(request):
    stmt = "SELECT p_id, address, remarks, time FROM pothole"
    cursor = connection.cursor()
    cursor.execute(stmt)
    r = dictfetchall(cursor)
    return render(request, 'index.html', {'data': r})
