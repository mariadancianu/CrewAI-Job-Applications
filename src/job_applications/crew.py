"""
Creates the crew of agents and tasks for the weather forecasting system,
with the provided tools and configurations.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

# Initialize the tool with the website URL, 
# so the agent can only scrap the content of the specified website
#linkedin_scraper = ScrapeWebsiteTool(website_url='https://www.linkedin.com')

@CrewBase
class JobApplicationsCrew:
    """WeatherCrew crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def job_searcher(self) -> Agent:
        """
        Creates the Activities Searcher agent.
        """
        return Agent(
            config=self.agents_config["job_searcher"],
            verbose=True,
            max_iter=3,  # Maximum iterations before the agent must provide its best answer. Default is 20.
            tools=[
                SerperDevTool(),  # search the internet and return the most relevant results.
                ScrapeWebsiteTool(),
            ],
            #tools=linkedin_scraper
            # allow_delegation=False,
        )

    @task
    def get_jobs_task(self) -> Task:
        """
        Creates the activities_suggestion task.
        """
        return Task(
            config=self.tasks_config["get_jobs_task"],
            output_file="/results/job_opportunities.md",
        )

    @crew
    def crew(self) -> Crew:
        """
        Creates the WeatherCrew with the agents and tasks.
        """

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,  # or Process.hierarchical
            verbose=True,
        )