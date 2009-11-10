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

from google.appengine.ext import db

class NickOfTimeEntry(db.Model):
  title = db.StringProperty(required=True)
  customer = db.StringProperty()
  task = db.StringProperty(required=True)
  taskdescription = db.StringProperty()
  starttime = db.StringProperty()
  endtime = db.StringProperty()
  hoursspent = db.StringProperty()
  ispublic = db.BooleanProperty(default=False)
  
class NickOfTimeUser(db.Model):
  username = db.StringProperty(required=True)
  password = db.StringProperty()
  isgoogleuser = db.BooleanProperty(default=False)
  googleuser = db.UserProperty()
  
