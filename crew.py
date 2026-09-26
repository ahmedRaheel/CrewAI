from crewai import Crew, Process

from agents import (
    reseacher,
    coder,
    reviewer
)

from tasks import (
    research_task,
    coding_task,
    review_task
)

crew = Crew(
    agents=[
        reseacher,
        coder,
        reviewer
    ],
    tasks=[
        research_task,
        coding_task,
        review_task
    ],
    process=Process.sequential,
    verbose=True
)


