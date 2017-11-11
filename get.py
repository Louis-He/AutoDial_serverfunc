import web
import time

urls = (
    '/index/(.*)', 'index',
    '/search/(.*)', 'search'
)

class index:
    def GET(self, name):
        try:
            global i
            print web.input()
            i = web.input()
            ID = i.ID
            lon = i.lon
            lat = i.lat
            print ID, lon, lat

            f = open('/root/web/posrecord.txt', 'a+')
            f.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']\t' + str(ID) + '\t' + str(lon) + '\t' + str(lat) + '\tPOSITION SAVED\n')
            f.close()
            return "SUCCEED"
        except:
            return "FAIL"


class search:
    def GET(self, name):
        global i
        global id
        global PW
        print web.input()
        i = web.input()
        ID = i.ID
        pw = i.pw
        print ID, pw
        print id, PW

        if ID == id and pw == PW:
            return "IN SEARCH MODE"
        else:
            return "Error: Acceess Denied"



if __name__ == "__main__":
    global i
    global id

    i = 0
    f = open('/root/web/posrecord.txt', 'w+')
    f.close()
    f = open('/root/web/posrecord2.txt', 'w+')
    f.close()

    try:
        global PW
        f = open('/root/web/ID.txt', 'r')
        lines = f.readlines()
        f.close()

        count = 0
        for i in lines:
            j = i.split('\n')[0]
            k = j.split(',')
            for x in k:
                print x
                if count == 0:
                    id = x
                if count == 1:
                    PW = x
                count += 1

        print id, PW
    except:
        print
        'ERR: file DO NOT EXIST.'

    app = web.application(urls, globals())
    app.run()
