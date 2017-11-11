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
        global ACCESS
        print web.input()
        i = web.input()
        ID = i.ID
        pw = i.pw
        print ID, pw
        print ACCESS
        if ID == id and pw == ACCESS:
            return "IN SEARCH MODE"
        else:
            return "Error: Acceess Denied"



if __name__ == "__main__":
    global i
    global id
    global ACCESS
    i = 0
    f = open('/root/web/posrecord.txt', 'w+')
    f.close()
    f = open('/root/web/posrecord2.txt', 'w+')
    f.close()

    try:
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
                    ACCESS = x
                    print ACCESS
                count += 1

    except:
        print 'ERR: file DO NOT EXIST.'

    app = web.application(urls, globals())
    app.run()
