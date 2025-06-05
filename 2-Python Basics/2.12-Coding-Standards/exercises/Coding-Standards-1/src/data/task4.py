connection, dictfetchall, HttpResponse, json, DateTimeJSONEncoder = None

def intersects(request):
    selection = request.POST.getlist('selection[]')
    nodes = []
    for i in range(0, len(selection)):
        nodes.append( selection[i] )
    nodes.append( selection[0] )
    poly = 'Polygon(( ' + (', '.join(nodes)) + ' ))'

    db = connection.cursor()
    db.execute(f"SELECT * FROM objects WHERE ST_Intersects(geom, {poly})")
    rows = dictfetchall(db)
    response={}
    response['success'] = True
    response['rows'] = rows
    response['num_rows'] = db.rowcount

    return HttpResponse(json.dumps(response, cls=DateTimeJSONEncoder),
        content_type='application/json')
