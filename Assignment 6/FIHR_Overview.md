### Overview 

Overview of the FHIR API:

    http://fhir.cerner.com/dstu1


### Resource-types

There are a number of FHIR resource-types/nouns that can be queried. For example, the following are the URLs to the SMART for FHIR sandbox for three different nouns for a particular patient:

```
$ curl -s "https://fhir-open-api.smarthealthit.org/Immunization/_search?subject%3APatient=1288992" -H 'Accept: application/json'
$ curl -s "https://fhir-open-api.smarthealthit.org/Encounter/_search?subject%3APatient=1288992" -H 'Accept: application/json'
$ curl -s "https://fhir-open-api.smarthealthit.org/Observation/_search?subject%3APatient=1288992" -H 'Accept: application/json'
```

There doesn't appear to be a way to list the resource-types/nouns that have data for a particular patient. Rather, you just much search them all (this is reasonable).


### Vital signs

Vital-sign measurements are recorded as "Observation" resource-types, and you can filter them by a "LOINC" code. These LOINC codes are passed as the "name" parameter, and are comma-separated. Note that the comma is itself encoded ("%2C"):

```
$ curl -s "https://fhir-open-api.smarthealthit.org/Observation/_search?subject%3APatient=1288992&name=8480-6%2C8462-4%2C8302-2%2C55284-4" -H 'Accept:application/json'
```

The LOINC codes are specified at "http://docs.smarthealthit.org/profiles" under the "LOINC codes for vital signs" heading.


### Profiles

The various different types of recorded data are referred to as "profiles". A profile is a subset of a resource-type/noun. The various other types of profiles form the majority of the content at http://docs.smarthealthit.org/profiles .


### List of patients

You can get a list of patients in the sandbox by querying:

    https://fhir-open-api.smarthealthit.org/Patient

Note that this is essentially a resource-type of "Patient" with no other parameters (as opposed to another resource-type that requires a patient as a parameter).


### Pagination

In a given query, the "link" child may include a "self" child, and, if there is more data, a "next" child. Pagination is automatic, and these links should be used to pull additional data. Do not construct your own URLs for doing this. For more information, see "http://fhir.cerner.com/dstu1".


### Data availability

For convenience, and as an example, patient 1288992 (Daniel Adams) has data for the following resource-types:

- AllergyIntolerance

  https://fhir-open-api.smarthealthit.org/AllergyIntolerance/_search?subject%3APatient=1288992

- Condition

  https://fhir-open-api.smarthealthit.org/Condition/_search?subject%3APatient=1288992

- Encounter

  https://fhir-open-api.smarthealthit.org/Encounter/_search?subject%3APatient=1288992

- MedicationPrescription

  https://fhir-open-api.smarthealthit.org/MedicationPrescription/_search?subject%3APatient=1288992

- Observation

  https://fhir-open-api.smarthealthit.org/Observation/_search?subject%3APatient=1288992

- Patient

  https://fhir-open-api.smarthealthit.org/Patient/1288992


### Notes

By default, the data comes down as XML unless you pass the "Accept" header.
