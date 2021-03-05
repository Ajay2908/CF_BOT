import date_time



def get_url(res_id):
    url_startup = "https://clist.by/api/v1/json/contest/?username=" + \
        USER_NAME+"&api_key="+API_KEY
    url_startup += "&limit=10"
    url_startup += "&resource__id="+str(res_id)
    url_startup += "&start__gt="+str(date_time.get_time())
    url_startup += "&duration__lt=21600"
    url_startup += "&order_by=start"
    return url_startup
