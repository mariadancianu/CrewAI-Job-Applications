#!/usr/bin/env python
"""
This is the main file that runs the weather forecasting system.
Make sure to have the necessary environment variables set up for the API keys and other configurations.
"""

import warnings

from .crew import JobApplicationsCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the job application crew.
    """

    inputs = {
        "title": "Data Scientist",  
        "location": "Milan, Lombardy, Italy",
        "path_to_cover_letter": "results/sample_cover_letter.md",
        "path_to_job_opportuntities": "results/job_opportunities.md",
        "path_to_submitted_applications": "results/submitted_applications.csv",
        "path_to_filtered_jobs": "results/filtered_jobs.md",
        "path_to_curriculum_vitae": "results/CV_MariaDancianu_updated.pdf",
        #"posted": "1 week ago"
        #"remote": "hybrid or remote"
    }

    # Create and run the crew
    try:
        output = JobApplicationsCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()