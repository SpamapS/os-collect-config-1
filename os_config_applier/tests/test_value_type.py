# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import testtools

from os_config_applier import config_exception
from os_config_applier import value_types


class ValueTypeTestCase(testtools.TestCase):

    def test_unknown_type(self):
        self.assertRaises(
            ValueError, value_types.ensure_type, "foo", "badtype")

    def test_int(self):
        self.assertEqual("123", value_types.ensure_type("123", "int"))

    def test_default(self):
        self.assertEqual("foobar",
                         value_types.ensure_type("foobar", "default"))

    def test_default_bad(self):
        self.assertRaises(config_exception.ConfigException,
                          value_types.ensure_type, "foo\nbar", "default")