import web
import time

urls = (
    '/(.*)', 'index'
)

class index:
    def GET(self, name):
        print web.input()
        i = web.input()
        ID = i.ID
        lon = float(i.lon)
        lat = float(i.lat)
        print ID, lon, lat

        f = open('/root/web/posrecord.txt', 'a+')
        f.write('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ']\t' + str(ID) + '\t' + str(lon) + '\t' + str(lat) + '\tPOSITION SAVED\n')
        f.close()
        return "SUCCEED"


if __name__ == "__main__":
    f = open('/root/web/posrecord.txt', 'w+')
    f.close()
    app = web.application(urls, globals())
    app.run()
