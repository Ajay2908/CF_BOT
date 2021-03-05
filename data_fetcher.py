import resources as R
import url

url_list = []
for ids in R.resourceids.keys():
    current_url = url.get_url(R.resourceids[ids])
    url_list.append(current_url)


def get_list():
    return url_list
