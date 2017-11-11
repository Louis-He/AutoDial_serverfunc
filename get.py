import web
import time

urls = (
    '/index/(.*)', 'index',
    '/sos/search/(.*)', 'search',
    '/regular/search/(.*)', 'regularsearch'
)


class index:
    def GET(self, name):
        try:
            print web.input()
            i = web.input()
            ID = i.ID
            lon = i.lon
            lat = i.lat
            status = i.status
            print ID, lon, lat, status

            f = open('/root/web/posrecord.txt', 'a+')
            f.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']\t' + str(ID) + '\t' + str(lon) + '\t' + str(lat) + '\t' + str(status) + '\tPOSITION SAVED\n')
            f.close()

            if status == 'emergency':
                f = open('/root/web/emergencyrecord.txt', 'a+')
                f.write(
                    '[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']\t' + str(ID) + '\t' + str(
                        lon) + '\t' + str(lat) + '\t' + str(status) + '\n')
                f.close()

            try:
                f = open('/root/web/track/' + ID + '.txt', 'a+')
                f.close()
            except:
                f = open('/root/web/track/' + ID + '.txt', 'w+')
                f.write('User,Longitude,Latitude,time,status')
                f.close()

            if status == 'regular':
                status = 1
            elif status == 'emergency':
                status = 911
            else:
                status = 0
            f = open('/root/web/track/' + ID + '.txt', 'a+')
            f.write(
                ID + ',' + str(lon) + ',' + str(lat) + ',' + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + ',' + status)
            f.close()

            return "SUCCEED"
        except:
            return "FAIL"

class search:

    def getIDlist(self):
        global id2
        global acc
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
                        id2 = x
                    else:
                        acc = x
                    count += 1
        except:
            print 'ERR: file DO NOT EXIST.'

    def GET(self, name):
        global id2
        global acc
        self.getIDlist();

        print web.input()
        i = web.input()
        ID = i.ID
        pw = i.pw
        print ID, pw
        print 'id2' + id2
        print 'acc' + acc
        if ID == id2 and pw == acc:
            lista = []
            final = []
            result = 'time(UTC)\tuser\tlon\tlat\n'
            try:
                f = open('/root/web/emergencyrecord.txt', 'r')
                lines = f.readlines()
                f.close()

                for i in lines:
                    lista.append(i)

                if len(lista)>10:
                    for i in range (1,11):
                        final.append(lista[len(lista)-i])
                else:
                    for i in range (1,len(lista)+1):
                        final.append(lista[len(lista)-i])

                for i in range (0,len(final)):
                    result += final[i] + '\n'
            except:
                print 'ERR: file DO NOT EXIST.'
            return "EMERGENCY LISTS\n" + result
        else:
            return "Error: Acceess Denied"

class regularsearch:

    def getIDlist(self):
        global id2
        global acc
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
                        id2 = x
                    else:
                        acc = x
                    count += 1
        except:
            print 'ERR: file DO NOT EXIST.'

    def GET(self, name):
        global id2
        global acc
        self.getIDlist();

        print web.input()
        i = web.input()
        ID = i.ID
        pw = i.pw
        print ID, pw
        print 'id2' + id2
        print 'acc' + acc
        if ID == id2 and pw == acc:
            lista = []
            final = []
            result = 'time(UTC)\tuser\tlon\tlat\n'
            try:
                f = open('/root/web/posrecord.txt', 'r')
                lines = f.readlines()
                f.close()

                for i in lines:
                    lista.append(i)

                if len(lista)>10:
                    for i in range (1,11):
                        final.append(lista[len(lista)-i])
                else:
                    for i in range (1,len(lista)+1):
                        final.append(lista[len(lista)-i])

                for i in range (0,len(final)):
                    result += final[i] + '\n'
            except:
                print 'ERR: file DO NOT EXIST.'
            return "REGULAR LISTS\n" + result
        else:
            return "Error: Acceess Denied"


if __name__ == "__main__":

    id2 = ''
    acc = ''

    i = 0
    f = open('/root/web/posrecord.txt', 'w+')
    f.close()
    f = open('/root/web/emergencyrecord.txt', 'w+')
    f.close()

    app = web.application(urls, globals())
    app.run()
