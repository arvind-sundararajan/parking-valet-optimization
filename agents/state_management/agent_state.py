```json
{
    "agents/state_management/agent_state.py": {
        "content": "
import logging
from typing import Dict, List
from allennlp.common.util import JsonDict
from causalnex.structure import StructureModel
from botpress import BotpressAgent

class AgentState:
    def __init__(self, agent_id: str, state_graph: StructureModel):
        """
        Initialize the agent state.

        Args:
        - agent_id (str): The ID of the agent.
        - state_graph (StructureModel): The state graph of the agent.
        """
        self.agent_id = agent_id
        self.state_graph = state_graph
        self.non_stationary_drift_index: Dict[str, float] = {}
        self.stochastic_regime_switch: List[JsonDict] = []

    def update_non_stationary_drift_index(self, drift_index: Dict[str, float]) -> None:
        """
        Update the non-stationary drift index.

        Args:
        - drift_index (Dict[str, float]): The new drift index.

        Raises:
        - Exception: If the update fails.
        """
        try:
            self.non_stationary_drift_index = drift_index
            logging.info('Updated non-stationary drift index')
        except Exception as e:
            logging.error(f'Failed to update non-stationary drift index: {e}')

    def update_stochastic_regime_switch(self, regime_switch: List[JsonDict]) -> None:
        """
        Update the stochastic regime switch.

        Args:
        - regime_switch (List[JsonDict]): The new regime switch.

        Raises:
        - Exception: If the update fails.
        """
        try:
            self.stochastic_regime_switch = regime_switch
            logging.info('Updated stochastic regime switch')
        except Exception as e:
            logging.error(f'Failed to update stochastic regime switch: {e}')

    def get_state(self) -> Dict[str, object]:
        """
        Get the current state of the agent.

        Returns:
        - Dict[str, object]: The current state of the agent.
        """
        return {
            'agent_id': self.agent_id,
            'state_graph': self.state_graph,
            'non_stationary_drift_index': self.non_stationary_drift_index,
            'stochastic_regime_switch': self.stochastic_regime_switch
        }

if __name__ == '__main__':
    # Create a Botpress agent
    agent = BotpressAgent('rocket_science')

    # Create a state graph
    state_graph = StructureModel()

    # Create an agent state
    agent_state = AgentState('rocket_science', state_graph)

    # Update the non-stationary drift index
    agent_state.update_non_stationary_drift_index({'drift': 0.5})

    # Update the stochastic regime switch
    agent_state.update_stochastic_regime_switch([{'regime': 'stable'}])

    # Get the current state of the agent
    state = agent_state.get_state()

    # Print the current state of the agent
    print(state)
",
        "commit_message": "feat: implement specialized agent_state logic"
    }
}
```