# group4project1
# project1
# Project plan

## Objective

The objective of this project is to create a data pipeline solution that is capable of looking up accurate location data and assessing security threats originating from risky IP addresses using the IPStack API https://ipstack.com/  to extract geolocation data from IP addresses, transform it to integrate with existing datasets (e.g., standardizing location formats or enriching data with additional geographical attributes), and load it into a target system such as a database. This process enables precise geolocation analysis, enhances data quality, and supports location-based decision-making.



## Consumers

Users who would find our datasets useful include:

### 1. **Marketing Teams** 
   - **Usage**: They can use geolocation data to personalize marketing campaigns based on the user's location.
   

### 2. **E-commerce Platforms**
   - **Usage**: To optimize customer experiences by offering location-specific products, services, and delivery estimates.
  

### 3. **Cybersecurity Teams**
   - **Usage**: To detect suspicious activity based on anomalous geolocations and strengthen network security.
 

### 4. **Business Intelligence (BI) Teams**
   - **Usage**: For analyzing regional sales, traffic trends, and market performance across different geographical areas.

- **Access**: Typically through database or BI dashboards 




Example:



## Questions

What questions are you trying to answer with your data? How will your data support your users?

Example:

> - How many orders are there for each customer?
> - What countries and regions have the most orders?
> - What customers have their orders delayed?
> - How many delayed orders are there for each country and region?
> - How many orders do we have for each day?
> - How many delayed orders do we have for each day?

## Source datasets

What datasets are you sourcing from? How frequently are the source datasets updating?

Example:

| Source name | Source type | Source documentation |
| - | - | - |
| Customers database | PostgreSQL database | - |
| Orders API | REST API | - |

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