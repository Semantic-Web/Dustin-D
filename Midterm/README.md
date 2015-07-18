## Abstract

The purpose of this paper is to describe the project-selection process, the objectives for the chosen project, and notes on the execution of the project. The selection process is detailed due to the sheer level of effort that was expended on it.

## Project Selection

### 1. Melissa Serrano

The first project(s) that were considered were the collaborations with Melissa Serrano ("Sentimental Analysis of Twitter Data", "Detecting Stance in Tweets"). Assuming that I'd have difficulty getting her information elsewhere, I started talking with her over LinkedIn, and this grew into several emails/calls to identify what her goals, needs, and schedule were. Though she and I made plans to be on the same team (in the SemEval competition) together, she indicated that she wasn't even going to plan on doing any real work until the beginning of the Fall semester. Therefore, both of these potential ideas weren't going to be useful as projects for this class.

### 2. FuXi

The second project that was considered was "Python FuXi to build RDF data sets". This project had been oftered as a result of a previous conversation that I had had in the class. I had previously spent some time downloading the library and doing a cursory search for information on how to use it. I resumed where I had left and continued evaluating the library modules and searching for documentation/examples. My objectives for this initial investigation were the following:

1. Identify some examples of how to invoke FuXi as a library from other Python code.
2. Identify how to load an OWL document.
3. Identify how to populate data.
4. Identify how to query the data once loaded.

After two-days spent trying to gauge the minimum level of effort required accomplish these goals, I was patently unsuccessful. There are only two documents seemingly written on FuXi (linked to from FuXi), and I had to go to the [Internet Archive](http://www.archive.org) to retrieve one of them, because it was no longer available. The topic of one of the documents, using FuXi's APIs, was only concerned with FuXi's support for InfixOwl, and alternative language. So, I read it btu ultimate couldn't use it.

It turns out that FuXi is often used as a tool and there's almost no information on how to use it as a library. It's largely used with N3 documents (a simpler RDF dialect), and, though it seems that FuXi could use OWL (and even Turtle and Manchester OWL), to do so would appear to go against-the-grain of almost any examples you can find. Finally, even SemanticWeb (a QA site) had almost no FuXi coverage.

I had no choice but to make the following conclusions:

1. I was going to spend almost all of my time trying to figure-out FuXi's APIs via brute-force effort.
2. I am very new to OWL/RDF.
3. Even as a very experienced Python engineer, my time would not be well-spent trying to figure out FuXi because I will first have to master OWL then will have to master SparQL in order to accomplish anything, and I will likely not have enough time to do so. Therefore, I will not be fluent with the schema, not be fluent with the structure of the data, not be familiar-enough with the query syntax, and will therefore be insufficient in my ability to debug false inferences.

This project would only make sense for someone who was already an expert in Semantic Web logic.

### 3. WordNet

Given the remaining options that were either already claimed or not likely to produce fruit (like having to pitch a Raspberry Pi architecture idea to another team, plan it, and then execute it within the next three weeks), I elected one of the two projects that involved fixing broken files: "WordNet in Protege". I will be doing this project alone.

## Overview of Project

The purpose of this project is to debug why the [WordNet.owl](http://www.adampease.org/OP/WordNet.owl) file can not be opened in [Protege](http://protege.stanford.edu).

## Preliminary Investigation

In electing this project, I did some immediate investigation to, first, confirm that there is a problem loading the document, and, second, to determine if there is an obviuos, linear method to achieving success. 

The purpose of the project is to debug why the document doesn't load. The following are the immediate steps that I took:

1. Attempted to load the document into Protege. I was given a memory error.
2. Updated the `run.command` file to allocate more memory. Instead of the initial maximum of 500M, I changed it to 2048M. I could then successfully open the WordNet file.

Technically, I had achieved the goal of the project. However, at the risk of being done too quickly, I went on to try one more thing: See if I could open the file from Python using an RDF library.

1. Installed [Redland/librdf](http://librdf.org) library.
2. Wrote iteration script based on an [example](https://github.com/dajobe/redland-bindings/blob/master/python/example.py) provided by the library. Since this is a planning document and not a technical exposition, I will not include the example here though I will include it in the final project submission.
3. Attempted iteration. Ran into many, many issues related to invalid characters in IDs and duplicate IDs. These were errors raised by the Redland library.

As a result of this, I wondered if it was pracical to consider writing a distillation routine to remove inappropriate content from the document. I wrote a simple XML-iteration script to determine if Python considered the file to be valid XML, in order to determine if I could move forward. There were no problems doing so, so I'm switching gears and declaring the objective of this project to be to distill the WordNet document, since Protege could still choke on issues like those at some point.

The output artifact of this project will be a single tool that will take an OWL file as input and render a file that will detect and remove the bad content experienced in the WordNet document.

## Process

Write one tool to perform the following steps:

1. Write an XML iterator.
2. Determine if the `ID` attribute of each `Thing` instance has invalid characters and fix them.
3. Determine if the `ID` attribute of each `Thing` instance is unique or is already associated with another `Thing` instance. In the case of the latter, remove it.
4. Update all `resource` references to `ID` attributes that were distilled in step (2) to their new names.
5. Write the updated tree out to a new file.

While writing the tool, the Redland library above can be used to determine if we are effectively eliminating the errors with the WordNet file.

## Results

The end result was a tool that did the above. The final document can be given to Redland without it complaining about syntax errors. I was also able to load the distilled WordNet document into Protege without any new problems being introduced. As the purpose of this document is to introduce the project prior to having finished it, I will share the results (because it would seem asinine to wait) but leave the sharing and explanation of the physical project files to the appropriate time.

Interestingly, the predominant problem was the occurrence of single-quotes in the IDs used as accents on certain characters. However, single quotes appeared in other strings besides the ID values, and Redland didn't appear to have a problem with this. This leads me to believe that RDF/OWL explicitly disqualifies that character from being used in IDs. However, Protege still allows it. Therefore, Protege must have either no validation or limited validation of the XML being loaded.

The other problems that were encountered were duplicate IDs and the backslash character being used in IDs. I also encountered some of the IDs that had invalid characters also occuring without those characters. This seems to imply that the WordNet document was built so as to optimize searches by including the same IDs both with and without special characters so that this establishing such an index would not necessarily have to be a concern of every project that implemented the WordNet database.

Finally, Protege doesn't seem to validate the resource-names that refer to the IDs within that same document. There was a point at which I had distilled all of the IDs but had not yet updated resources that referred to them from the same document, and Protege still loaded the document without appearing to complain.
