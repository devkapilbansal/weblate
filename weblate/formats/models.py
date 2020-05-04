#
# Copyright © 2012 - 2020 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#


from appconf import AppConf
from django.utils.functional import cached_property

from weblate.trans.util import delete_configuration_error
from weblate.utils.classloader import ClassLoader


class FileFormatLoader(ClassLoader):
    def __init__(self):
        super().__init__("WEBLATE_FORMATS", False)
        self.errors = {}

    @cached_property
    def autoload(self):
        result = []
        for fileformat in self.data.values():
            for autoload in fileformat.autoload:
                result.append((autoload, fileformat))
        return result

    def load_data(self):
        result = super().load_data()

        for fileformat in list(result.values()):
            error_name = "File format: {0}".format(fileformat.format_id)
            delete_configuration_error(error_name)
            try:
                fileformat.get_class()
            except (AttributeError, ImportError) as error:
                result.pop(fileformat.format_id)
                if fileformat.format_id != "rc":
                    self.errors[fileformat.format_id] = str(error)

        return result


FILE_FORMATS = FileFormatLoader()


class FormatsConf(AppConf):
    FORMATS = (
        "weblate.formats.ttkit.PoFormat",
        "weblate.formats.ttkit.PoMonoFormat",
        "weblate.formats.ttkit.TSFormat",
        "weblate.formats.ttkit.XliffFormat",
        "weblate.formats.ttkit.PoXliffFormat",
        "weblate.formats.ttkit.StringsFormat",
        "weblate.formats.ttkit.StringsUtf8Format",
        "weblate.formats.ttkit.PropertiesUtf8Format",
        "weblate.formats.ttkit.PropertiesUtf16Format",
        "weblate.formats.ttkit.PropertiesFormat",
        "weblate.formats.ttkit.JoomlaFormat",
        "weblate.formats.ttkit.PhpFormat",
        "weblate.formats.ttkit.LaravelPhpFormat",
        "weblate.formats.ttkit.RESXFormat",
        "weblate.formats.ttkit.AndroidFormat",
        "weblate.formats.ttkit.JSONFormat",
        "weblate.formats.ttkit.JSONNestedFormat",
        "weblate.formats.ttkit.WebExtensionJSONFormat",
        "weblate.formats.ttkit.I18NextFormat",
        "weblate.formats.ttkit.CSVFormat",
        "weblate.formats.ttkit.CSVSimpleFormat",
        "weblate.formats.ttkit.CSVSimpleFormatISO",
        "weblate.formats.ttkit.YAMLFormat",
        "weblate.formats.ttkit.RubyYAMLFormat",
        "weblate.formats.ttkit.SubRipFormat",
        "weblate.formats.ttkit.MicroDVDFormat",
        "weblate.formats.ttkit.AdvSubStationAlphaFormat",
        "weblate.formats.ttkit.SubStationAlphaFormat",
        "weblate.formats.ttkit.DTDFormat",
        "weblate.formats.ttkit.WindowsRCFormat",
        "weblate.formats.ttkit.FlatXMLFormat",
        "weblate.formats.external.XlsxFormat",
        "weblate.formats.txt.AppStoreFormat",
    )

    class Meta:
        prefix = "WEBLATE"
