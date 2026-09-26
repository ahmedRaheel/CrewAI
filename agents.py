from llm import llm
from crewai import Agent

reseacher = Agent(
     role="AI reseacher",
        goal=(
            "Research Jev AI "
            "and provide accurate information."
        ),
        backstory=(
                "You are an AI researcher "
                "specialized in Jev AI."
            ),
        llm = llm, 
        verbose=True
        
)

coder = Agent(
    role="Python Developer",
    goal=(
        "Create clear and correct "
        "Python code based on research."
    ),
    backstory=(
        "You are an experienced Python "
        "developer who writes clean and "
        "practical code."
    ),
    llm=llm,
    verbose=True
)

reviewer = Agent(
    role="Code Reviewer",
    goal=(
        "Review generated code "
        "and identify problems."
    ),
    backstory=(
        "You are a senior Python reviewer "
        "focused on correctness and quality."
    ),
    llm=llm,
    verbose=True
)

