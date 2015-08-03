#!/usr/bin/env python2.7

import logging
import re
import xml.etree.ElementTree

_RDF_NS_URI = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
_OWL_NS_URI = 'http://www.w3.org/2002/07/owl#'

def _get_fq_name(name, ns_uri):
    return '{' + ns_uri + '}' + name

_ID_ATTR_NAME = _get_fq_name('ID', _RDF_NS_URI)
_RESOURCE_ATTR_NAME = _get_fq_name('resource', _RDF_NS_URI)
_THING_TAG_NAME = _get_fq_name('Thing', _OWL_NS_URI)
_INVALID_ID_CHARS_RX = r"[\/']+"

def _configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    logger.addHandler(sh)

_LOGGER = logging.getLogger(__name__)


class WordNetFixer(object):
    def __init__(self, wordnet_owl_filepath):
        self.__wordnet_owl_filepath = wordnet_owl_filepath

        self.__tree = xml.etree.ElementTree.parse(self.__wordnet_owl_filepath)
        self.__root = self.__tree.getroot()
        
        self.__invalid_id_chars_re = re.compile(_INVALID_ID_CHARS_RX)

    def __enumerate_things(self):
        for child in self.__root.findall(_THING_TAG_NAME):
            yield child

    def filter(self):
        """Remove duplicates. Distill IDs having invalid characters. Return a 
        mapping with the distilled IDs.
        """

        ids = set()
        distilled_map = {}
        i = 0

        # We either weren't able to find all of the children or weren't able to 
        # properly delete some of them when we used getchildren(). findall() 
        # fixed this.
        for child in self.__enumerate_things():
            if i % 100000 == 0 and i > 0:
                _LOGGER.info('(%d)', i)

            if _ID_ATTR_NAME not in child.attrib:
                _LOGGER.info("IGNORING: %s", child.attrib)

                i += 1
                continue

            id_ = child.attrib[_ID_ATTR_NAME]

            if self.__invalid_id_chars_re.search(id_):
                _LOGGER.info("2 Distilling name: [%s]", id_)
                distilled_id_ = re.sub(_INVALID_ID_CHARS_RX, '', id_)
                distilled_map[id_] = distilled_id_

                id_ = distilled_id_

            # We need to make sure to use the distilled ID for membership 
            # checks because it looks like the original and the distilled 
            # version might both be registered.
            if id_ in ids:
                _LOGGER.info("1 Dropping duplicate ID: [%s]", id_)
                self.__root.remove(child)

                i += 1
                continue

            ids.add(id_)
            child.attrib[_ID_ATTR_NAME] = id_

            i += 1

        _LOGGER.info("(%d) things traversed. (%d) IDs distilled.", 
                     i, len(distilled_map))

        return distilled_map

    def update_resources(self, distilled_map):
        """Update references to the IDs that were distilled."""

        i = 0
        fixed = 0
        for child in self.__root.findall('.//*[@' + _RESOURCE_ATTR_NAME + ']'):
            resource_name = child.attrib[_RESOURCE_ATTR_NAME]
            if resource_name[0] != '#':
                continue

            resource_name = resource_name[1:]
            
            try:
                distilled = distilled_map[resource_name]
            except KeyError:
                pass
            else:
                child.attrib[_RESOURCE_ATTR_NAME] = distilled
                _LOGGER.info("3 Updating [%s] => [%s]", 
                             resource_name, distilled)

                fixed += 1

            i += 1

        _LOGGER.info("Fixed (%d)/(%d).", fixed, i)

    def write(self, filepath):
        print("Writing.")

        with open(filepath, 'w') as f:
            self.__tree.write(f)

def _distill_main():
    filepath = 'WordNet.owl'
    wnf = WordNetFixer(filepath)
    distilled_map = wnf.filter()
    wnf.update_resources(distilled_map)

    wnf.write('distilled.owl')

def _distill_secondary():
    filepath = 'distilled.owl'
    wnf = WordNetFixer(filepath)
    distilled_map = wnf.filter()

if __name__ == '__main__':
    _configure_logging()

    _distill_main()
#    _distill_secondary()
