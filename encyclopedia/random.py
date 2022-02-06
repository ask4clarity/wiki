import random
from . import util

def random_entry(request):
	entries = util.list_entries()
	return {
		'random': random.choice(entries)
	}