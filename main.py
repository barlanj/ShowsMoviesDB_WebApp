#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os

from google.appengine.ext import ndb
import jinja2
import webapp2

from models import MovieEntry


jinja_env = jinja2.Environment(
                   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                   autoescape=True)
#generic key used to group MovieQuotes into an entity group
PARENT_KEY = ndb.Key("Entity", "movieentry_root")


class HomePage(webapp2.RequestHandler):
    def get(self):
        movie_entry_query = MovieEntry.query(ancestor=PARENT_KEY).order(-MovieEntry.last_touch_date_time)
        template = jinja_env.get_template("templates/home.html")
        self.response.write(template.render({"movie_entry_query": movie_entry_query
                                             }))

class InsertEditEntry(webapp2.RequestHandler):
    def post(self):
        k = self.request.get("entity_key")
        if k:
            # if edit
            movie_key = ndb.Key(urlsafe=k)
            movie = movie_key.get()
            movie.title = self.request.get("input-title")
            movie.category = self.request.get_all("input-category")
            movie.length = int(self.request.get("input-length"))
            movie.rating = int(self.request.get("input-rating"))
            movie.show_type = self.request.get("input-type")
            movie.put()
        else:
            #if add
            
            #get the values of the elements whose name="value"
            title = self.request.get("input-title")
            category = self.request.get_all("input-category")
            length = int(self.request.get("input-length"))
            rating = int(self.request.get("input-rating"))
            show_type = self.request.get("input-type")
            
            #create an object
            new_movie_entry = MovieEntry(parent=PARENT_KEY,
                                         title = title,
                                         category = category,
                                         length = length,
                                         rating = rating,
                                         show_type = show_type
                                         )
            #save it to the datastore
            new_movie_entry.put()
            
        #redirect
        self.redirect(self.request.referer)

class DeleteEntry(webapp2.RequestHandler):
    def post(self):
        k = self.request.get("entity_key")
        if k:
            entry_key = ndb.Key(urlsafe=k)
            entry_key.delete()
        self.redirect(self.request.referer)
            
        

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/insertentry', InsertEditEntry),
    ('/deleteentry', DeleteEntry)
], debug=True)
