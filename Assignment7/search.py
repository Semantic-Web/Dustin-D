import geonames.compat
import geonames.adapters.search

import lxml.etree

sa = geonames.adapters.search.Search('dsoprea')
sa.place_name_like('detroit').country('us').feature_code('STM')
result = sa.execute()

print("Flat:")
print('')

results = result.get_flat_results()
for (id_, name) in results:
    print(u"[{0}]: [{1}]".format(id_, name))

print('')

print("RDF:")
print('')

print(lxml.etree.tostring(result.xml, pretty_print=True))

print('')
