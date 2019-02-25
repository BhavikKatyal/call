# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.
import requests
from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'Bhavik_Katyal'

LOGGER = getLogger(__name__)


class NewSkill(MycroftSkill):
    def __init__(self):
        super(NewSkill, self).__init__(name="NewSkill")

    def initialize(self):

        cal_event_intent = IntentBuilder("CalEventIntent"). \
            require("CalEventKeyword").build()
        self.register_intent(cal_event_intent, self.handle_cal_event_intent)



        

    def handle_cal_event_intent(self, message):

        self.speak_dialog("Did I forget to introduce myself? I’m your voice Assistant. Maverick!!”)

    


    def stop(self):
        pass

