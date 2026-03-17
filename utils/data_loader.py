```json
{
    "utils/data_loader.py": {
        "content": "
import logging
from typing import Dict, List
import allennlp
from causalnex import StructureModel
from allennlp.modules import LangGraph

def load_non_stationary_drift_index(data: List[Dict]) -> List[float]:
    """
    Load non-stationary drift index from data.

    Args:
    data (List[Dict]): List of dictionaries containing data.

    Returns:
    List[float]: List of non-stationary drift indices.
    """
    try:
        logging.info('Loading non-stationary drift index')
        non_stationary_drift_index = []
        for item in data:
            # Calculate non-stationary drift index using allennlp
            index = allennlp.calculate_drift_index(item)
            non_stationary_drift_index.append(index)
        return non_stationary_drift_index
    except Exception as e:
        logging.error(f'Error loading non-stationary drift index: {e}')
        return []

def load_stochastic_regime_switch(data: List[Dict]) -> List[bool]:
    """
    Load stochastic regime switch from data.

    Args:
    data (List[Dict]): List of dictionaries containing data.

    Returns:
    List[bool]: List of stochastic regime switches.
    """
    try:
        logging.info('Loading stochastic regime switch')
        stochastic_regime_switch = []
        for item in data:
            # Calculate stochastic regime switch using causalnex
            switch = causalnex.calculate_regime_switch(item)
            stochastic_regime_switch.append(switch)
        return stochastic_regime_switch
    except Exception as e:
        logging.error(f'Error loading stochastic regime switch: {e}')
        return []

def load_lang_graph(data: List[Dict]) -> LangGraph:
    """
    Load language graph from data.

    Args:
    data (List[Dict]): List of dictionaries containing data.

    Returns:
    LangGraph: Language graph.
    """
    try:
        logging.info('Loading language graph')
        # Create language graph using allennlp
        lang_graph = LangGraph()
        for item in data:
            lang_graph.add_node(item)
        return lang_graph
    except Exception as e:
        logging.error(f'Error loading language graph: {e}')
        return None

def load_structure_model(data: List[Dict]) -> StructureModel:
    """
    Load structure model from data.

    Args:
    data (List[Dict]): List of dictionaries containing data.

    Returns:
    StructureModel: Structure model.
    """
    try:
        logging.info('Loading structure model')
        # Create structure model using causalnex
        structure_model = StructureModel()
        for item in data:
            structure_model.add_node(item)
        return structure_model
    except Exception as e:
        logging.error(f'Error loading structure model: {e}')
        return None

if __name__ == '__main__':
    # Simulate 'Rocket Science' problem
    data = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 20},
        {'id': 3, 'value': 30}
    ]
    non_stationary_drift_index = load_non_stationary_drift_index(data)
    stochastic_regime_switch = load_stochastic_regime_switch(data)
    lang_graph = load_lang_graph(data)
    structure_model = load_structure_model(data)
    print('Non-stationary drift index:', non_stationary_drift_index)
    print('Stochastic regime switch:', stochastic_regime_switch)
    print('Language graph:', lang_graph)
    print('Structure model:', structure_model)
",
        "commit_message": "feat: implement specialized data_loader logic"
    }
}
```