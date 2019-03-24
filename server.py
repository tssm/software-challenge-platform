import threed
import json
import web

# Database

db = {}

# API:

urls = ("/scans", "scans",
        "/scans/(\d+)", "scan",
        "/scans/(\d+)/boundingbox", "boundingbox")

class boundingbox:
    def GET(self, id):
        try:
            scan = db[id]
            bbox = threed.boundingbox(scan)
            center = threed.center(scan)
            body = json.dumps({ 'boundingbox': bbox, 'center': center })
            web.ok(self, headers = { 'Content-Type': 'application/json'})
            return body
        except KeyError:
            web.notfound(self)

class scan:
    def GET(self, id):
        try:
            scan = db[id]
            body = json.dumps({ 'id': int(id), 'points': scan })
            web.ok(self, headers = { 'Content-Type': 'application/json'})
            return body
        except KeyError:
            web.notfound(self)

    def PUT(self, id):
        if id == 0:
            web.badrequest(self, message="Indexes start at 1")
            return

        updating = id in db
        db[id] = json.loads(web.data())['points']
        body = json.dumps({ 'id': int(id), 'points': db[id] })
        if updating:
            web.ok(self, headers = { 'Content-Type': 'application/json'})
        else:
            web.created(self, headers =
                { 'Location': 'http://0.0.0.0:8080/scans/' + str(id)
                , 'Content-Type': 'application/json'})
        return body

class scans:
    def POST(self):
        lnDb = len(db)
        newindex = str(1 if lnDb == 0 else int(sorted(db.keys())[-1]) + 1)
        db[newindex] = json.loads(web.data())
        body = json.dumps({ 'id': int(newindex), 'points': db[newindex] })
        web.created(self, headers =
            { 'Location': 'http://0.0.0.0:8080/scans/' + str(newindex)
            , 'Content-Type': 'application/json'})
        return body

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
