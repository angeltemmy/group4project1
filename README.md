# group4project1

# Project plan

## Objective

The objective of this project is to create a data pipeline solution that is capable of looking up accurate real-time and historical data about earthquake events globally. This data includes information such as event magnitude, location (latitude/longitude), depth, time of occurrence, and other seismic event attributes. The goal of this project is to build a robust ETL (Extract, Transform, Load) pipeline to facilitate seamless integration, processing, and analysis of this earthquake data for research, monitoring, and risk assessment.

 Earthquake API (https://earthquake.usgs.gov/fdsnws/event/1)


## Consumers

Users who would find our datasets useful include:

# Seismologists and Geologists:
Use Case: Analyze seismic activity patterns, study tectonic plate movements, and develop models to predict earthquake behavior.

# Disaster Management Agencies:
Use Case: Monitor real-time earthquake events to coordinate emergency responses and disaster relief efforts.

# Urban Planners and Engineers:
Use Case: Evaluate seismic risk when planning infrastructure projects, construction standards, and building codes.

# Insurance Companies and Risk Assessors:
Use Case: Assess earthquake risk in specific regions to model potential losses and calculate insurance premiums.

# Government and Regulatory Bodies:
Use Case: Monitor seismic activity for regulatory compliance and safety standards.

# Academic and Research Institutions:

Use Case: Conduct research on seismic phenomena, geophysics, and earth sciences.

# Utility Companies:
Use Case: Assess risk to critical infrastructure such as power plants, water facilities, and pipelines.

# Journalists and Media Organizations:
Use Case: Report on recent earthquake events, trends, and risk analysis.
Value: Access to real-time and historical data enables accurate reporting and public education.
- **Access**: Typically through database or BI dashboards 


## Questions

Our data addresses questions like

- How many earthquakes occur each day, week, month, and year?
- Which regions or countries experience the highest frequency of earthquakes?
- What are the distribution patterns of earthquake magnitudes over time?
- Which tectonic plate boundaries experience the most seismic activity?
-What countries or regions have seen a significant increase in earthquake occurrences    over time?
-Which regions have the highest potential risk based on historical earthquake data?
-How frequently do large magnitude (7.0+) earthquakes occur in high-population areas?
-What are the economic or infrastructural impacts of earthquakes in high-risk zones?

 These questions and use cases guide the ETL pipeline development, ensuring it delivers the insights and analytics needed by each user group.

## Source datasets

Primary Dataset: USGS Earthquake Catalog API (https://earthquake.usgs.gov/fdsnws/event/1)

Description: This dataset provides real-time and historical data on global earthquake events.

## Solution architecture

How are we going to get data flowing from source to serving? What components and services will we combine to implement the solution? How do we automate the entire running of the solution?

- What data extraction patterns are you going to be using?
- What data loading patterns are you going to be using?
- What data transformation patterns are you going to be performing?

We recommend using a diagramming tool like [draw.io](https://draw.io/) to create your architecture diagram.

Here is a sample solution architecture diagram:

![images/sample-solution-architecture-diagram.png](images/sample-solution-architecture-diagram.png)

## Breakdown of tasks

How is your project broken down? Who is doing what?

We recommend using a free Task board such as [Trello](https://trello.com/). This makes it easy to assign and track tasks to each individual.

Example:

![images/kanban-task-board.png](images/kanban-task-board.png)
