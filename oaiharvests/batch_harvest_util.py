from oaiharvests.models import Repository, Community
from oaiharvests.utils import batch_harvest_issues

base_url = 'http://scholarspace.manoa.hawaii.edu/dspace-oai/request'
community_id = 'com_10125_27123' # Language Learning and Technology community collection

try:
	repo = Repository.objects.all()[0]  # retrieve the repository registered with site.
except:
	print 'Repository needs to be added to db first.'

try:
	community = Community.objects.get(identifier=community_id)
	batch_harvest_issues(community)
except:
	print 'A Language Learning and Technology community collection (com_10125_27123) needs to be added to db first.'


