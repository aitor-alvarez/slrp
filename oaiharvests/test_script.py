from oaiharvests.models import Repository, Community, Collection
from oaiharvests.utils import batch_harvest_articles, OAIUtils
from sickle import Sickle

oai = OAIUtils()

base_url = 'http://scholarspace.manoa.hawaii.edu/dspace-oai/request'
sickle = Sickle(base_url)
community = Community.objects.get()
cols = oai.list_oai_collections(community)

october = Collection.objects.get(identifier='col_10125_58896')
feb = Collection.objects.get(identifier='col_10125_58892')


# records = oai.harvest_oai_collection_records_sickle(feb)
records = sickle.ListRecords(metadataPrefix='dim', set=feb.identifier)
