

import datetime, json

transaction, HttpResponse,DateTimeJSONEncoder=None

class Notification:
    pass

class NotificationContent:
    pass


def save_notification(request):
    response = {'success': False}
    if request.method == 'POST':
        post = request.POST.copy()
        post['date_comment'] = datetime.datetime.now()
        post['user_id'] = '1'
        post['report_id'] = '1'
        post['public'] = True

        report_ids = request.POST.getlist('report_ids[]')

        if request.user.is_authenticated():
            if request.user is not None:
                if request.user.is_active and request.user.has_perm( 'Can change notification' ):
                    response['user'] ='yes'
                    db = None
                    notif_content = NotificationContent( post )
                    notif_content.save()
                    notifs = {}
                    goodToGo = True
                    for i in range(0, len(report_ids)):
                        report_id = report_ids[i]
                        db.execute("Some SQL statement for id {}".format(report_id) )
                        row = db.fetchall()
                        if (db.rowcount > 0): notifs[i] = Notification(row)
                        else: goodToGo = False

                    if goodToGo:
                        with transaction.atomic():
                            for i in notifs:
                                notifs[i].save()

                        response['success'] = True
                        response['ids'] = ', '.join(report_ids)
                        return HttpResponse(json.dumps(response, cls=DateTimeJSONEncoder),
                                    content_type='application/json')
                    else:
                        response['err'] = 'Invalid observation ID'
                        return HttpResponse(json.dumps(response, cls=DateTimeJSONEncoder),
                                content_type='application/json')

        response['err'] = 'Unauthorized'
        return HttpResponse(json.dumps(response, cls=DateTimeJSONEncoder),
                content_type='application/json')
