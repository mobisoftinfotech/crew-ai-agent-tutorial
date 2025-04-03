from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from math_agent.tools.custom_tool import math_tool

@CrewBase
class MathAgent():
	"""MathAgent crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def math_expert(self) -> Agent:
		config = self.agents_config['math_expert']
		config['tools'] = [math_tool]
		return Agent(
			config=config,
			verbose=True
		)

	@task
	def math_task(self) -> Task:
		config = self.tasks_config['math_task']
		config['tools'] = [math_tool]
		return Task(
			config=config,
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the MathAgent crew"""

		return Crew(
			agents=self.agents,
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
		)
