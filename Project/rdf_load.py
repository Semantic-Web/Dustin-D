#!/usr/bin/env python2.7

import RDF

storage = \
    RDF.Storage(
        storage_name="hashes",
        name="test",
        options_string="new='yes',hash-type='memory',dir='.'")

if storage is None:
    raise Exception("new RDF.Storage failed")

model = RDF.Model(storage)
if model is None:
    raise Exception("new RDF.model failed")

test_file = 'WordNet.owl'

uri = RDF.Uri(string="file:" + test_file)

parser = RDF.Parser('raptor')
if parser is None:
    raise Exception("Failed to create RDF.Parser raptor")

parsed = parser.parse_as_stream(uri, uri)
for i, s in enumerate(parsed):
    model.add_statement(s)

    if i % 100000 == 0 and i > 0:
        print("Loaded: ({0})".format(i))
