"""
Creates the crew of agents and tasks for the job applications system,
with the provided tools and configurations.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from crewai_tools import FileReadTool


@CrewBase
class JobApplicationsCrew:
    """JobApplications crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def job_searcher(self) -> Agent:
        """
        Creates the Job Searcher agent. 
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
    @agent
    def cover_letter_customizer(self) -> Agent:
        """
        Creates the Activities Searcher agent.
        """
        return Agent(
            config=self.agents_config["cover_letter_customizer"],
            verbose=True,
            max_iter=3,  # Maximum iterations before the agent must provide its best answer. Default is 20.
            tools=[
                FileReadTool(), 
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

    @task
    def customize_cover_letter_task(self) -> Task:
        """
        Creates the activities_suggestion task.
        """
        return Task(
            config=self.tasks_config["customize_cover_letter_task"],
            output_file="/results/customized_cover_letters.md",
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