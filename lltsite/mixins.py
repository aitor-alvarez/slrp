# mixins.py
from collections import namedtuple
import json

from oaiharvests.models import MetadataElement, Record

""" A namedtuple to construct unique points to plot """
Plot = namedtuple('Plot',['lat', 'lng'])

class MapDataMixin(object):
    """
    Populates additional lists for google map display and browsing.
    Requires a queryset of Record objects. 
    """

    def get_context_data(self, **kwargs):
        context = super(MapDataMixin, self).get_context_data(**kwargs)
        mapped_plots = set()
        mapped_languages = set()
        mapped_records = []

        for record in self.queryset:
            record_dict = record.as_dict() 
            mapped_data = json.loads(record.get_metadata_item('coverage')[0].element_data)
            if mapped_data:
                mapped_plots.add(self.make_map_plot(mapped_data))
                mapped_languages |= set(json.loads(record.get_metadata_item('language')[0].element_data))
                mapped_records.append(record_dict)

        mapped_plots = self.make_json_map_plots(mapped_plots)

        context['mapped_records'] = sorted(mapped_records)
        context['mapped_languages'] = sorted(mapped_languages)
        context['mapped_plots']= unicode(mapped_plots)

        return context

        
    def make_map_plot(self, json_position):
        """
        Create a two-item array from a json representaiton of metaelement coverage data e.g. [u'7.4278', u'134.5495']
        """
        try:
            return Plot(json_position[0], json_position[1])
        except:
            return None

    def make_json_map_plots(self, plots):
        """
        Create a dictionary for each Plot then encode as json string.
        """
        try:
            plots = [ plot._asdict() for plot in list(plots) ]
            return json.dumps( plots ) # jsonify for google maps js client (DOM).
        except:
            return []


class RecordSearchMixin(object):

    def get_queryset(self):
        queryset = super(RecordSearchMixin, self).get_queryset()
        queryset = []
        key = self.request.GET.get('key')
        filteropt = self.request.GET.get('filteropts')

        if key:
            q = MetadataElement.objects.filter(element_type=filteropt).filter(element_data__icontains=key)
            for i in q:
                queryset.append(i.record)
            return queryset
        
        return None