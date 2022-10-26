from enum import Enum, unique
from typing import Any, Optional

import streamlit as st


@unique
class StateVar(Enum):
    FUNCTION = 'function'
    LEFT_BOUNDARY = 'left_boundary'
    RIGHT_BOUNDARY = 'right_boundary'
    PRECISION = 'precision'
    SHOW_TABLE = 'show_table'
    SHOW_PRECISE_SOLUTION = 'show_precise_solution'
    METHOD_NAME = 'method_name'
    MAX_NUMBER_OF_NODES = 'max_number_of_nodes'

    def get(self, *, default: Optional[Any] = None) -> Optional[Any]:
        return st.session_state.get(self.value, default)

    def set(self, value: Any) -> None:
        st.session_state[self.value] = value
