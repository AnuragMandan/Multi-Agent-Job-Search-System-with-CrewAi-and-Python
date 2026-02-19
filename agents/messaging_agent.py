from crewai import Agent, Task
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.config import GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.4,
    google_api_key=GEMINI_API_KEY
)

def get_messaging_agent():
    return Agent(
        role="Outreach Messaging Specialist",
        goal="Create professional and compelling outreach messages for job applications",
        backstory="You're an expert in professional communication and networking, specializing in crafting personalized messages that get responses from hiring managers and recruiters.",
        llm=llm,
        verbose=True
    )

def create_messaging_task(agent, job_summary, agency_name, user_bio):
    return Task(
        description=f"""
        Create a personalized outreach message for a job application at {agency_name}.
        
        --- Job Summary ---
        {job_summary}
        
        --- User Bio ---
        {user_bio}
        
        Your message should:
        1. Be professional and concise
        2. Show genuine interest in the role and agency
        3. Highlight relevant qualifications
        4. Include a clear call to action
        5. Be suitable for email or LinkedIn messaging
        """,
        expected_output="A professional outreach message that can be sent via email or LinkedIn to express interest in the position.",
        agent=agent,
        output_file='data/messaging_output.txt'
    )