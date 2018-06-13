from requests import Request, Session


url = 'https://www.booking.com/searchresults.html'  # your url

params = { 
    'checkin_monthday': 19,
    'checkin_year': 2018,
    'checkout_month': 4,
    'checkout_monthday': 20,
    'checkout_year': 2018,
    'class_interval': 1,
    'dest_id': -1022488,
    'dest_type': 'city',
    'dtdisc': 0,
    'from_sf': 1,
    'group_adults': 2,
    'group_children':   0,
    'inac': 0,
    'index_postcard': 0,
    'label': 'gen1',
    'label_click': 'undef',
    'no_rooms': 1,
    'offset': 0,
    'postcard': 0,
    'raw_dest_type': 'city',
    'room1': 'A,A',
    'sb_price_type': 'total',
    'sb_travel_purpose': 'business',
    'src': 'index',
    'src_elem': 'sb',
    'ss': 'Pokhara',
    'ss_all': 0,
    'ssb': 'empty',
    'sshis': 0,
    'ssne': 'Pokhara',
    'ssne_untouched': 'Pokhara',
}

req = Request('GET', url, params=params)
prepped = req.prepare()
print(prepped.url)  # you send this URL ...

s = Session()
resp = s.send(prepped)
print(resp.url)  # ... but you are redirected to this URL (same as your r.url)