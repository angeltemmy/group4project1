group4project1
Project plan
Objective
The objective of this project is to create a data pipeline solution that is capable of looking up accurate real-time and historical data about earthquake events globally. This data includes information such as event magnitude, location (latitude/longitude), depth, time of occurrence, and other seismic event attributes. The goal of this project is to build a robust ETL (Extract, Transform, Load) pipeline to facilitate seamless integration, processing, and analysis of this earthquake data for research, monitoring, and risk assessment.
Earthquake API (https://earthquake.usgs.gov/fdsnws/event/1)
Consumers
Users who would find our datasets useful include:
Seismologists and Geologists:
Use Case: Analyze seismic activity patterns, study tectonic plate movements, and develop models to predict earthquake behavior.
Disaster Management Agencies:
Use Case: Monitor real-time earthquake events to coordinate emergency responses and disaster relief efforts.
Urban Planners and Engineers:
Use Case: Evaluate seismic risk when planning infrastructure projects, construction standards, and building codes.
Insurance Companies and Risk Assessors:
Use Case: Assess earthquake risk in specific regions to model potential losses and calculate insurance premiums.
Government and Regulatory Bodies:
Use Case: Monitor seismic activity for regulatory compliance and safety standards.
Academic and Research Institutions:
Use Case: Conduct research on seismic phenomena, geophysics, and earth sciences.
Utility Companies:
Use Case: Assess risk to critical infrastructure such as power plants, water facilities, and pipelines.
Journalists and Media Organizations:
Use Case: Report on recent earthquake events, trends, and risk analysis.  
Value: Access to real-time and historical data enables accurate reporting and public education.
• Access: Typically through database or BI dashboards
Questions
Our data addresses questions like
• How many earthquakes occur each day, week, month, and year?
• Which regions or countries experience the highest frequency of earthquakes?
• What are the distribution patterns of earthquake magnitudes over time?
• Which tectonic plate boundaries experience the most seismic activity?  
-What countries or regions have seen a significant increase in earthquake occurrences over time?  
-Which regions have the highest potential risk based on historical earthquake data?  
-How frequently do large magnitude (7.0+) earthquakes occur in high-population areas?  
-What are the economic or infrastructural impacts of earthquakes in high-risk zones?
These questions and use cases guide the ETL pipeline development, ensuring it delivers the insights and analytics needed by each user group.
Source datasets
Primary Dataset: USGS Earthquake Catalog API (https://earthquake.usgs.gov/fdsnws/event/1)
Description: This dataset provides real-time and historical data on global earthquake events.
Solution architecture
alt text
Python :
Extracting data from both live and static source.  
Load data to postgres database.  
Setting automatical refreshing.
PostgreSQL DBMS:
Storing live data
AWS RDS:
Hosting and managing postgres database.
Others:
Docker: containerizzing our pipeline.  
ECR: hosting our docker container.  
ECS: running the docker container.  
S3: stroing the .env file.
Installation Instructions
1. Install PostgreSQL and Python
Download PostgreSQL and pgAdmin by going to https://www.postgresql.org/download/ and selecting the installer for your Operating System. Download the latest version of PostgreSQL.
2. Clone Codes
Clone the github repository or manually download it.
3. Create .env file to store authentication information
Create an .env file in the main directory with the following format:
DB information
LOGGING_SERVER_NAME =  
LOGGING_DATABASE_NAME =  
LOGGING_USERNAME =  
LOGGING_PASSWORD =  
LOGGING_PORT =
Run pipeline
Once the previous steps are done, run the pipeline with python.
AWS Screenshots  
We use Docker to contain the pipeline, then load it into AWS ECR, and run on ECS.
AWS ECR
alt text
AWS ECS  
Screenshot of task running:
alt text
AWS RDS screenshot
alt text
Breakdown of tasks
alt text
