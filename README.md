# python-pubsub-demo
This demo application written in Python demonstrates how to use the Ethos Integration publish-subscribe messaging pattern. A general overview of this pattern is described [here.](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)

## Ethos Integration Overview

Ethos Integration has the concept of *applications* and *resources*. An application represents a software application like a student information system or ERP system. A resource represents an object or entity that an application cares about. For example, a student information system would have resources like students, courses or grades.

Applications in Ethos Integration are further divided into *authoritative applications* and *subscribing applications*. In the example of a student information system with resources like students, courses and grades, the student information system is considered an *authoritative application*. The student information system is said to be authoritative for the resources student, course and grade. The authoritative application owns those resources.

A *subscribing application* listens for *change notifications* from an *authoritative application*. A change notification represents a change to a resource (create, update, delete) that the authoritative application is responsible for publishing to Ethos Integration.

An application may be both an *authoritative application* and *subscribing application*. An application can own resources and subscribe to other application's resources.

## Example Business Case

Imagine a college campus where there is a parking ticket system and a finance system. Campus security issues parking tickets and records them in the parking ticket system. The finance system collects the parking tickets so that the students can be billed.

The *authoritative application* is the parking ticket system which owns the *resource* parking-tickets.  The *subscribing application* is the finance system which listens for *change notifications* to the parking-tickets *resource*.

![](/images/usecase2.png)

## Configuring Ethos Integration

In order to run the demo code Ethos Integration must be configured properly. The configuration steps are not hard but can be confusing to new users of Ethos Integration. These steps must be completed for the demo to work. Acquiring access to the Ethos Integration administrative website is beyond the scope of this document. Please contact your Ellucian representative about getting access to Ethos Integration.

Configuration steps:

* Login to Ethos Integration
    * Select *Applications* from the sidebar menu

    ![](/images/menu.png)
* Create Parking Ticket System application
    * Click *Add Application* from the Manage Applications screen

    ![](/images/add.png)
    * On the Application Setup Wizard click *Add an Application Manually*

    ![](/images/manual.png)
    * Name the application *Parking Ticket System* and click *Add*

* Add parking-tickets resource to owned resources
    * On the Manage Applications screen, hover over the Parking Ticket System card and click the pencil edit icon.

    ![](/images/app_pts_edit.png)

    * In the Owned Resources widget click the gear icon.

    ![](/images/resources_gear.png)

    * On the Owned Resources screen enter a Base URI by clicking the pencil edit icon. This field is required but will not be used in the demo.  Enter a valid url like *http://www.google.com* and click Save.

    ![](/images/baseuri.png)

    * Stay on the Owned Resources screen and click *Add Resources*. On the options dialog select *Add A Custom Resource* and click Next. Enter *parking-tickets* for resource name and leave other fields blank.  Click Add.

    ![](/images/create_resource.png)

    * When complete, the Owned Resources screen should look like:

    ![](/images/owned_resources.png)    

* Get the API Key for the Parking Ticket System
    * On the Manage Applications screen click the pencil edit icon again for the Parking Ticket System application. On the application screen for the Parking Ticket System, click *Manage API Keys*.

    ![](/images/manage_apikeys.png)

    * On the API Keys screen an API Key will have been auto-created. The API Key is a UUID in the format of xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. Copy this value and save it, the API Key will need to be placed in the code.

    ![](/images/apikey.png)

* Create Finance System application
    * Click *Add Application* from the Manage Applications screen

    ![](/images/add.png)
    * On the Application Setup Wizard click *Add an Application Manually*

    ![](/images/manual.png)
    * Name the application *Finance System* and click *Add*

* Subscribe to parking-tickets
    * On the Manage Applications screen, hover over the Finance System card and click the pencil edit icon

    ![](/images/app_fs_edit.png)

    * In the Subscriptions widget click the gear icon.

    ![](/images/subscriptions_gear.png)

    * On the Subscriptions screen click *Add Subscriptions*.

    ![](/images/add_subscriptions.png)

    * On the Add Subscriptions modal window find *parking-tickets* in the list and click checkbox. Click Add.  *Note - there may be other resources listed here.*

    ![](/images/add_subscriptions_modal.png)

    * When complete, the Subscriptions screen should look like:

    ![](/images/subscriptions.png)

* Get the API Key for the Finance System
    * On the Manage Applications screen click the pencil edit icon again for the Finance System application. On the application screen for the Finance System, click *Manage API Keys*.

    ![](/images/manage_apikeys.png)

    * On the API Keys screen an API Key will have been auto-created. The API Key is a UUID in the format of xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. Copy this value and save it, the API Key will need to be placed in the code.

    ![](/images/apikey_fs.png)

## Installing

The demo is written in python 3. The only library dependency is the Requests library, documentation can be found [here.](http://docs.python-requests.org/en/master/) To install the dependency:

```
pip install requests
```

Note - The demo will work in python 2.7 however some minor syntax changes will need to be made.  For example, the *print("some string")* function in needs to be re-written as *print 'some string'*.

## Running the demo

The demo code simulates two separate systems using Ethos Integration. **Each "system" must have a valid Ethos Integration API key.** These API keys were created in the **Configuring Ethos Integration** section of this document.

In the file *parking_ticket_system.py* file replace the value for the API_KEY variable with the API key that was created in the previous steps for the Parking Ticket System. In the file *finance_system.py* file replace the value for the API_KEY variable with the API key that was created in the previous steps for the Finance System.

To start the parking ticket system, open a new console and type:
```
python parking_ticket_system.py
```
In a new, separate console type:
```
python finance_system.py
```
The python programs will start using Ethos Integration to communicate with each other. If there are error messages on the screen related to "Invalid API Key", verify the correct API keys were copied to the appropriate python file.

## Notes about the code

The parking_ticket_system.py file will generate random parking tickets and publish them to Ethos Integration as change notifications. The code will run in an infinite loop publishing change notifications waiting randomly up to 20 seconds. The finance_system.py will check for change notifications every 60 seconds and print them to the screen. When both files are running the output will look something like:

![](/images/pts_console.png)

![](/images/fs_console.png)

The ethos.py file is a simple python class that encapsulates all the Ethos Integration specific code. There are methods to get a JWT, send a change notification and receive change notifications.

The Ethos Integration APIs are secured with [JSON Web Tokens (JWT)](https://en.wikipedia.org/wiki/JSON_Web_Token). In order to obtain a JWT the code sends an API Key. This can be seen in the *get_jwt()* method. JWT's in Ethos Integration expire after 5 minutes. When an API call is made with an expired JWT the API call will fail with an HTTP code 401.  The *send_change_notification()* and *get_change_notifications()* methods will respond to a 401 by attempting to obtain a new JWT.
