import list


contests = list.upcoming_list()


class Contest:
    def __init__(self, event, start, duration, href, name):
        self.event = event
        self.start = start
        self.duration = duration
        self.href = href
        self.name = name

    def display(self):
        print(self.event + ' ' + self.href)


def nice_data():
    important_data = []
    for x in contests:
        # print(x)
        C1 = [x['start'], x['event'], x['duration'],
              x['href'], x['resource']['name']]
        # C1 = Contest(x['event'], x['start'], x['duration'], x['href'])
        important_data.append(C1)
    data_new = []

    for y in sorted(important_data):
        C1 = Contest(y[1], y[0], y[2], y[3], y[4])
        data_new.append(C1)

    return data_new


# nice_data()
