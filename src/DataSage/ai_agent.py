from llama_index.experimental.query_engine import PandasQueryEngine


class BaseAgent:
    """This is the base class for all agents."""

    def __init__(
        self, llm=None, task_description: str = None, name: str = None, role: str = None
    ):
        self.llm = llm
        self.task_description = task_description
        self.name = name
        self.role = role

    def define(self):
        """
        Define the agent's task and role.
        """
        if self.name is None:
            self.name = "AI Agent"
        if self.role is None:
            self.role = "Assistant"
        return f"{self.name} is a {self.role} that {self.task_description}."


class AnalystAgent(BaseAgent):
    """This is the analyst agent class."""

    def __init__(self, llm=None, task_description: str = None, name: str = None):
        super().__init__(llm=llm, task_description=task_description, name=name)
        self.task_description = (
            task_description or "analyzes data and provides insights"
        )

    def analyze_dataframes(self, df, query: str):
        """Analyze the dataframe based on the user's query."""
        query_engine = PandasQueryEngine(
            df=df, llm=self.llm, verbose=True, synthesize_response=True
        )
        response = query_engine.query(query)
        return response
