from google.appengine.ext import ndb

class MovieEntry(ndb.Model):
    title = ndb.StringProperty()
    category = ndb.StringProperty(repeated=True)
    length = ndb.IntegerProperty()
    rating = ndb.IntegerProperty()
    show_type = ndb.StringProperty()
    last_touch_date_time = ndb.DateTimeProperty( auto_now=True )