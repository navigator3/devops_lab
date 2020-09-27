import requests


def connect(state, l, p):
    options = {'state': state, 'per_page': 100}
    ltext = 'https://api.github.com/repos/alenaPy/devops_lab/pulls?state=all&per_page=100'
    response = requests.get('%s' % ltext, auth=('%s' % l, '%s' % p))
    status = options['state']
    return(process(response.json(), status))


def process(dic, status):
    my_list = []
    j = 0
    if status == 'open':
        for i in dic:
            line = {}
            if i['state'] == 'open' and len(i['labels']) == 0:
                j += 1
                line['j'] = str(j)
                line['num'] = i['number']
                line['title'] = i['title']
                line['link'] = i['url']
                line['state'] = i['state']
                my_list.append(line)
    elif status == 'closed':
        for i in dic:
            line = {}
            if i['state'] == 'closed':
                j += 1
                line['j'] = str(j)
                line['num'] = i['number']
                line['title'] = i['title']
                line['link'] = i['url']
                line['state'] = i['state']
                my_list.append(line)
    elif status == 'needs work':
        for i in dic:
            line = {}
            if i['state'] == 'open'\
                    and len(i['labels']) == 1\
                    and i['labels'][0]['name'] == 'needs work':
                j += 1
                line['j'] = str(j)
                line['num'] = i['number']
                line['title'] = i['title']
                line['link'] = i['url']
                line['state'] = i['labels'][0]['name']
                my_list.append(line)
    elif status == 'accepted':
        for i in dic:
            line = {}
            if i['state'] == 'open'\
                    and len(i['labels']) == 1\
                    and i['labels'][0]['name'] == 'accepted':
                j += 1
                line['j'] = str(j)
                line['num'] = i['number']
                line['title'] = i['title']
                line['link'] = i['url']
                line['state'] = i['labels'][0]['name']
                my_list.append(line)
    elif status is None:
        for i in dic:
            line = {}
            j += 1
            line['j'] = str(j)
            line['num'] = i['number']
            line['title'] = i['title']
            line['link'] = i['url']
            try:
                line['state'] = i['labels'][0]['name']
            except BaseException:
                line['state'] = i['state']
            my_list.append(line)
    return(my_list)


def get_pulls(state, l, p):
    return (connect(state, l, p))


if __name__ == "__main__":
    get_pulls("state")
