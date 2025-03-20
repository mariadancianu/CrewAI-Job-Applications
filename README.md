# Job Applications with Agentic AI

![JobApplications Crew](images/img.png)

This project explores basic agentic AI workflows using [CrewAI](https://crewai.com) as a hands-on learning experiment. It leverages CrewAI to automate job searching by scraping job opportunities from LinkedIn, generating personalized cover letters, and submitting applications. Additionally, it incorporates human-in-the-loop Agents to confirm with the user which jobs to apply to and whether the generated cover letter is suitable before submission. 

For demonstration purposes, I included only a small portion of the cover letter in this project instead of the full version.

## 🛠️ Tech Stack

- Python (3.12+ recommended)
- CrewAI
- OpenAI API


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
