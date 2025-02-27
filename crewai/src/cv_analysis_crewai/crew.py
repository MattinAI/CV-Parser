from crewai import Agent, Crew, Process, Task, Flow
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileWriterTool

@CrewBase
class CvAnalysisCrewai():
	"""CvAnalysisCrewai crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent 
	def resume_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['resume_agent'],
			# tools=[FileWriterTool(output_file=self.output_file)],
			allow_delegation=False
			#verbose=True
		)

	@agent 
	def skills_categorizer_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['skills_categorizer_agent'],
			#tools=[FileWriterTool(output_file=self.output_file)],
			allow_delegation=False
			#verbose=True
		)

	@task
	def generate_cv_resume(self) -> Task:
		return Task(
			config=self.tasks_config['generate_cv_resume'],
			#verbose=True
		)

	@task
	def categorize_skills(self) -> Task:
		return Task(
			config=self.tasks_config['categorize_skills'],
			#verbose=True
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CvAnalysisCrewai crew"""
		return Crew(
			agents=[
				self.resume_agent(), 
				self.skills_categorizer_agent()
				], 
			tasks=[
				self.generate_cv_resume(), 
				self.categorize_skills()
				], 
			process=Process.sequential,
			verbose=True,
		)
