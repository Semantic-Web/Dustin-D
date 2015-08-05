# WordNet in Protege

Dustin Oprea

## Abstract

Determine why Professor Shankar couldn't open the [WordNet OWL-compatible RDF file](http://www.adampease.org/OP/WordNet.owl) using [Protege](http://protege.stanford.edu).

If this ends-up being stupidly trivial, we'll write a tool to fix issues in the WordNet file and output well-formed data.


## Background

This particular track was chosen because several other project options (sentiment analysis, stance in tweets, and getting FuXi to work) turned out to either be invalid (the first two) or impossible (FuXi) in the limited amount of remaining time that we had to work on the projects. I lost several days investigating these other projects, and I needed to pick something and spend a couple of days looking at it in order to write a synopsis for the midterm. Once other choices that were either already chosen by other students were eliminated and those with impossible scheduling were eliminated, there were no other more complicated/interesting options still available.

Reportedly, there is a problem with the WordNet RDF file that prevents it from being opened by Professor Shankar. Before electing this project, I verified that I could open it from Python as a standard XML file so that I knew I'd have the minimum amount of functionality to be able to traverse and transform the file as necessary.


## Methods

1. Verified the problem by downloading the OWL file and the current version of Protege, and trying to load the former into the latter. Yes.

2. Identified that the command used to start Protege wasn't configuring Java for enough memory. After changing this from 500M to 2048M, the file loaded fine.

3. Not wanting to be done and still having to write a paper, I went on to generally validate how well-formed the OWL/RDF file was.

4. I attempted to parse it as an XML file using the standard Python library. I could.

5. I attempted to read it as an RDF file from Python, using [librdf](http://librdf.org). It seemed like I would be able to after I fixed some non-structural information in the file (duplicate IDs, invalid characters in the IDs, etc.).

6. Wrote script to traverse XML, determine which "thing" records have IDs with invalid characters, and translate those IDs to acceptable values. We would simply tell *rdflib* to load it and use the error-messages as our guide in determining which characters it considered to be invalid.

7. The script also identifies and removes duplicate "thing" records. References to the old IDs are updated to the new IDs.

8. Validated that the distilled version of the file can successfully be read by 1) *librdf*, and 2) *Protege*.


## Results

We identified that the original problem was, in fact, trivial and related to how Professor Shankar was starting his Protege environment. We then proceeded to write a script that can distill a couple of existing/ubiquitous problems (see Methods#6). While Protege seems to not validate RDF files, other applications might. This tool could be used to preprocess the public version of the file into something that is more correct.

### Tools

The following tools are available among the [project files](https://github.com/Semantic-Web/Dustin-O).

These tools expect the WordNet file to be located in the same directory and called "WordNet.owl". For convenience, Unix-based systems (or any other system that supports the "wget" command) can call the [get_wordnet.sh](get_wordnet.sh) script to download it. Otherwise, you'll have to find the link in the references and download it directly.

To install the dependencies:

```
$ sudo pip install -r requirements.txt
```


#### Distillation tool

Download: [distill.py](distill.py)

Output:

```
$ ./distill.py
2015-08-03 00:32:38,704 - __main__ - INFO - (100000)
2015-08-03 00:32:38,773 - __main__ - INFO - 1 Dropping duplicate ID: [testes]
2015-08-03 00:32:38,787 - __main__ - INFO - 1 Dropping duplicate ID: [quizzes]
2015-08-03 00:32:38,801 - __main__ - INFO - 1 Dropping duplicate ID: [gasses]
2015-08-03 00:32:38,816 - __main__ - INFO - 1 Dropping duplicate ID: [WN30Word-S]
2015-08-03 00:32:38,828 - __main__ - INFO - 1 Dropping duplicate ID: [WN30Word-S]
2015-08-03 00:32:38,840 - __main__ - INFO - 1 Dropping duplicate ID: [WN30Word-S]
2015-08-03 00:32:38,857 - __main__ - INFO - 1 Dropping duplicate ID: [WN30Word-S]
2015-08-03 00:32:38,872 - __main__ - INFO - 1 Dropping duplicate ID: [WN30Word-S]
2015-08-03 00:32:38,887 - __main__ - INFO - 1 Dropping duplicate ID: [WN30Word-S]
2015-08-03 00:32:38,904 - __main__ - INFO - 1 Dropping duplicate ID: [WN30Word-S]
...
```

The output file will be written to *distilled.owl*.


#### RDF loader/tester

Download: [rdf_load.py](rdf_load.py)

Output:

```
$ ./rdf_load.py 
Loaded: (100000)
Loaded: (200000)
Loaded: (300000)
Loaded: (400000)
Loaded: (500000)
Loaded: (600000)
...
```


## Conclusions

More thought should be put into the potential projects that are given to the students of this class. This project officially took five-minutes to do. This could not be discussed with Professor Shankar as he only responded to messages every week or two.


## References

- [WordNet](http://www.adampease.org/OP/WordNet.owl)
- [Protege](http://protege.stanford.edu)
- [Redland/librdf](http://librdf.org)
- [librdf example](https://github.com/dajobe/redland-bindings/blob/master/python/example.py)
