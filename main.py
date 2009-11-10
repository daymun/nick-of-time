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
import wsgiref.handlers
import os

from nickoftimedatamodel import NickOfTimeEntry

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class MainHandler(webapp.RequestHandler):

  def get(self):
    # If we are logged in, then display all available timesheets
    # If we are not logged in, then display all public timesheets (if any)
    templateValues = []
    self.response.out.write(template.render('main.html', templateValues))


class TimeSheetHandler(webapp.RequestHandler):

  def get(self):
    # Return a single Time Entry displayed on screen
    timeKey = self.request.get('timekey')
    if (len(timeKey) > 0):
      time = NiceOfTimeEntry.get_by_key_name(key_names = timeKey)
      templateValues = { 'time': time }
    else:
      templateValues = {}
    
    directory = os.path.join(os.path.dirname(__file__), "html")
    path = os.path.join(directory, "main.html")
    self.response.out.write(template.render("main.html", templateValues))
    
  def post(self):
    # If it is a new Time Entry, add it to the datastore, otherwise add a new version
    # of the existing Time Entry
    timeKey = self.request.get('timekey')
    if (len(timeKey) > 0):
      time = NickOfTimeEntry.get_by_key_name(key_names = timeKey)
      msg = "Time Entry saved successfully."
    else:
      msg = "Time Entry added successfully."
      
    time = NickOfTimeEntry(
      title = self.request.get('title'),
      task = self.request.get('task'),
      taskdescription = self.request.get('taskdescription'),
      ispublic = (self.request.get('ispublic') == 'on'))
    time.put()
    
    directory = os.path.join(os.path.dirname(__file__), "html")
    path = os.path.join(directory, "tssaveresponse.json")
    self.response.out.write(template.render('tssaveresponse.json', {"time": time, "haserror": "false", "message": msg}))
    
def main():
  application = webapp.WSGIApplication([('/', TimeSheetHandler),
                                        ('/ts', TimeSheetHandler)], 
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
