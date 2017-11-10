import web

urls = (
    '/(.*)', 'index'
)

class index:
    def GET(self, name):
        print web.input()
        i = web.input()
        ID = i.ID
        ts = i.ts
        lon = float(i.lon)
        lat = float(i.lat)
        print ID, ts, lon, lat
        return "GET hello world"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
