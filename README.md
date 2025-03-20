# JobApplications Crew

This project explores basic agentic AI workflows using [CrewAI](https://crewai.com as a hands-on learning experiment. It leverages CrewAI to automate job searching by scraping job opportunities from LinkedIn, generating personalized cover letters, and submitting applications.


## 🛠️ Tech Stack

- Python (3.12+ recommended)
- CrewAI
- OpenAI API
- [AccuWeather API](https://developer.accuweather.com/) (or any weather API of choice)


## Details

Key Components:

    src/job_applications/main.py:
    -> Main script file.


    src/job_applications/crew.py:
    -> Main crew file where agents and tasks come together, and the main logic is executed.


    src/job_applications/config/agents.yaml:
    -> Configuration file for defining agents.


    src/job_applications/config/tasks.yaml:
    -> Configuration file for defining tasks.

Upon running the main.py script, the following results are saved:

    src/job_applications/results/job_opportunities.md:
    -> A structured summary of 20 job opportunities in line with the job title, including the job title, the location, the responsibilities, the salary if available, etc. 


## 🔄 Status

Project is: In Progress


#

📝 Author: Maria Dancianu

📅 Last Updated: March 2025
