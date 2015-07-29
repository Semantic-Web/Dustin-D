## Introduction

The purpose of this assignment was to query Geonames' RDF service-endpoint. Since only their "Search" API has an RDF endpoint, we'll search for a particular place/entity.

In order to do this project, I wrote a public library and tool to query that service-endpoint. The other students will be able to benefit from this, too.


## Requirements

This project is Python 2.x- and 3.x-compatible. To install the dependencies:

```
$ sudo pip install -r requirements.txt
```


## Project

### Code

```python
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
```


### Running

To execute the code, run:

```
$ python search.py 
Flat:

[http://sws.geonames.org/4990746/]: [Detroit River]

RDF:

<rdf:RDF xmlns:cc="http://creativecommons.org/ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:foaf="http://xmlns.com/foaf/0.1/" xmlns:gn="http://www.geonames.org/ontology#" xmlns:owl="http://www.w3.org/2002/07/owl#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#" xmlns:wgs84_pos="http://www.w3.org/2003/01/geo/wgs84_pos#">
<gn:Feature rdf:about="http://sws.geonames.org/4990746/">
<rdfs:isDefinedBy rdf:resource="http://sws.geonames.org/4990746/about.rdf"/>
<gn:name>Detroit River</gn:name>
<gn:featureClass rdf:resource="http://www.geonames.org/ontology#H"/>
<gn:featureCode rdf:resource="http://www.geonames.org/ontology#H.STM"/>
<gn:countryCode>US</gn:countryCode>
<wgs84_pos:lat>42.04116</wgs84_pos:lat>
<wgs84_pos:long>-83.14965</wgs84_pos:long>
<wgs84_pos:alt>174</wgs84_pos:alt>
<gn:parentCountry rdf:resource="http://sws.geonames.org/6252001/"/>
<gn:nearbyFeatures rdf:resource="http://sws.geonames.org/4990746/nearby.rdf"/>
<gn:locationMap rdf:resource="http://www.geonames.org/4990746/detroit-river.html"/>
<gn:wikipediaArticle rdf:resource="http://en.wikipedia.org/wiki/Detroit_River"/>
<rdfs:seeAlso rdf:resource="http://dbpedia.org/resource/Detroit_River"/>
</gn:Feature>
</rdf:RDF>
```


## Command-Line Tool

You can get the exact same results using the command-line tool that comes with the client.

### Print results as a simple list

```
$ gn_search dsoprea -p place_name_like detroit -p country us -p feature_code STM 
[http://sws.geonames.org/4990746/]: [Detroit River]
```


### Print results as an RDF document

```
$ gn_search dsoprea -p place_name_like detroit -p country us -p feature_code STM -x
<rdf:RDF xmlns:cc="http://creativecommons.org/ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:foaf="http://xmlns.com/foaf/0.1/" xmlns:gn="http://www.geonames.org/ontology#" xmlns:owl="http://www.w3.org/2002/07/owl#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#" xmlns:wgs84_pos="http://www.w3.org/2003/01/geo/wgs84_pos#">
<gn:Feature rdf:about="http://sws.geonames.org/4990746/">
<rdfs:isDefinedBy rdf:resource="http://sws.geonames.org/4990746/about.rdf"/>
<gn:name>Detroit River</gn:name>
<gn:featureClass rdf:resource="http://www.geonames.org/ontology#H"/>
<gn:featureCode rdf:resource="http://www.geonames.org/ontology#H.STM"/>
<gn:countryCode>US</gn:countryCode>
<wgs84_pos:lat>42.04116</wgs84_pos:lat>
<wgs84_pos:long>-83.14965</wgs84_pos:long>
<wgs84_pos:alt>174</wgs84_pos:alt>
<gn:parentCountry rdf:resource="http://sws.geonames.org/6252001/"/>
<gn:nearbyFeatures rdf:resource="http://sws.geonames.org/4990746/nearby.rdf"/>
<gn:locationMap rdf:resource="http://www.geonames.org/4990746/detroit-river.html"/>
<gn:wikipediaArticle rdf:resource="http://en.wikipedia.org/wiki/Detroit_River"/>
<rdfs:seeAlso rdf:resource="http://dbpedia.org/resource/Detroit_River"/>
</gn:Feature>
</rdf:RDF>
```
