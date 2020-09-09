from oaiharvests.utils import *
from oaiharvests.models import *

from sickle import Sickle

community = Community.objects.all()[0]
batch_harvest_issues(community)

collection = Collection.objects.all()[7]
record = collection.record_set.all()[5]
record.hdr_identifier
try:
    sickle = Sickle(collection.community.repository.base_url)        
    sickle.class_mapping['GetRecord'] = LltRecordBitstream
    record = sickle.GetRecord(metadataPrefix='ore', identifier=record.identifier)
    print type(record)
    # print record.metadata['bitstream'][0].replace('+', '%20')

except Exception as e:
    print e, 'Unable to construct bitstream url.'



# 
