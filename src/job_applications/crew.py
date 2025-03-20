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
        )
    @agent
    def cover_letter_customizer(self) -> Agent:
        """
        Creates the Cover Letter customization agent.
        """
        return Agent(
            config=self.agents_config["cover_letter_customizer"],
            verbose=True,
            max_iter=3,  # Maximum iterations before the agent must provide its best answer. Default is 20.
            tools=[
                FileReadTool(), 
            ],
        )
    @agent
    def filter_job_opportunities(self) -> Agent:
        """
        Creates the Filter job opportunities agent.
        """
        return Agent(
            config=self.agents_config["filter_job_opportunities"],
            verbose=True,
            max_iter=3,  # Maximum iterations before the agent must provide its best answer. Default is 20.
            tools=[
                FileReadTool(), 
            ],
            allow_delegation=True,

        )
    @agent
    def apply_job_opportunities(self) -> Agent:
        """
        Creates the Apply job opportunities agent.
        """
        return Agent(
            config=self.agents_config["apply_job_opportunities"],
            verbose=True,
            max_iter=3,  # Maximum iterations before the agent must provide its best answer. Default is 20.
            tools=[
                FileReadTool(), 
                ScrapeWebsiteTool(), # is this agent useful for scraping websites?
            ],
            allow_delegation=True,
        )

    @task
    def get_jobs_task(self) -> Task:
        """
        Creates the get_jobs task.
        """
        return Task(
            config=self.tasks_config["get_jobs_task"],
            output_file="/results/job_opportunities.md",
        )

    @task
    def customize_cover_letter_task(self) -> Task:
        """
        Creates the customize_cover_letter task.
        """
        return Task(
            config=self.tasks_config["customize_cover_letter_task"],
            output_file="/results/customized_cover_letters.md",
        )
    @task
    def filter_jobs_task(self) -> Task:
        """
        Creates the customize_cover_letter task.
        """
        return Task(
            config=self.tasks_config["filter_jobs_task"],
            output_file="/results/filtered_jobs.md",
            human_input=True
        )
    @task
    def apply_to_jobs_task(self) -> Task:
        """
        Creates the apply_to_jobs_task.
        """
        return Task(
            config=self.tasks_config["apply_to_jobs_task"],
            human_input=True
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