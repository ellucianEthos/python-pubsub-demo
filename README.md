# python-pubsub-demo
This demo application written in Python shows how to use the Ethos Integration publish-subscribe messaging pattern. A general overview of this pattern is described [here.](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)

## Ethos Integration Overview

Ethos Integration has the concept of *applications* and *resources*. An application represents a software application like a student information system or ERP system. A resource represents an object or entity that an application cares about. For example, a student information system would have resources like students, courses or grades.

Applications in Ethos Integration are further divided into *authoritative applications* and *subscribing applications*. In the example of a student information system with resources like students, courses and grades, the student information system is considered an *authoritative application*. The student information system is said to be authoritative for the resources student, course and grade. The authoritative application owns those resources.

A *subscribing application* listens for *change notifications* from an *authoritative application*. A change notification represents a change to a resource (create, update, delete) that the authoritative application is responsible for publishing to Ethos Integration.

An application may be both an *authoritative application* and *subscribing application*. An application can own resources and subscribe to other application's resources.

## Example Business Case

Imagine a college campus where there is a parking ticket system and a finance system. Campus security issues parking tickets and records them in the parking ticket system. The finance system collects the parking tickets so that the students can be billed.

The *authoritative application* is the parking ticket system which owns the *resource* parking-tickets.  The *subscribing application* is the finance system which listens for *change notifications* to the parking-tickets *resource*.

diagram here

## Configuring Ethos Integration

In order to run this demo code Ethos Integration must be configured properly. The configuration steps are not hard but can be confusing to new users of Ethos Integration. Acquiring access to the Ethos Integration administrative website is beyond the scope of this document.

Configuration steps:

* #### Login to Ethos Integration##
* Create parking ticket system application
* Add parking-tickets resource to owned resources
* grab api key
* Create finance system application
* Subscribe to parking-tickets
* grab api key


## Ethos Integration Technical Overview
Adheres to HTTP REST principles
http -
uses JWT

Sub

Notes about the code
pip install requests library

Important Notes
update the api keys in the code

publish change notifications

applications, resources and authoritative applications
api keys and jwts, jwts good for 5 minutes, don't need to get one every time
