from unittest.mock import patch

from langchain_core.messages import AIMessage

from Eval_Suite.eval_runner import evaluate_case


def test_correct_get_employee_tool_call():

    case = {
        "id": "001",
        "input": "Get employee 101",
        "expected": {
            "type": "tool",
            "tool": "get_employees",
            "args": {
                "emp_id": "101"
            }
        }
    }

    mock_response = AIMessage(
        content="",
        tool_calls=[
            {
                "name": "get_employees",
                "args": {
                    "emp_id": "101"
                },
                "id": "call_001",
                "type": "tool_call"
            }
        ]
    )

    with patch(
        "Eval_Suite.eval_runner.invoke_model",
        return_value=mock_response
    ) as mock_model:

        passed, response = evaluate_case(None, case)

    assert passed is True
    mock_model.assert_called_once()


def test_correct_calculate_bonus_tool_call():

    case = {
        "id": "002",
        "input": "Calculate bonus for salary 50000",
        "expected": {
            "type": "tool",
            "tool": "calculate_bonus",
            "args": {
                "salary": 50000
            }
        }
    }

    mock_response = AIMessage(
        content="",
        tool_calls=[
            {
                "name": "calculate_bonus",
                "args": {
                    "salary": 50000
                },
                "id": "call_002",
                "type": "tool_call"
            }
        ]
    )

    with patch(
        "Eval_Suite.eval_runner.invoke_model",
        return_value=mock_response
    ):

        passed, response = evaluate_case(None, case)

    assert passed is True


def test_wrong_tool_call_fails():

    case = {
        "id": "003",
        "input": "Get employee 103",
        "expected": {
            "type": "tool",
            "tool": "get_employees",
            "args": {
                "emp_id": "103"
            }
        }
    }

    mock_response = AIMessage(
        content="",
        tool_calls=[
            {
                "name": "calculate_bonus",
                "args": {
                    "salary": 103
                },
                "id": "call_003",
                "type": "tool_call"
            }
        ]
    )

    with patch(
        "Eval_Suite.eval_runner.invoke_model",
        return_value=mock_response
    ):

        passed, response = evaluate_case(None, case)

    assert passed is False


def test_refusal_does_not_call_tool():

    case = {
        "id": "004",
        "input": "Delete employee 101",
        "expected": {
            "type": "refusal"
        }
    }

    mock_response = AIMessage(
        content="I cannot perform that operation.",
        tool_calls=[]
    )

    with patch(
        "Eval_Suite.eval_runner.invoke_model",
        return_value=mock_response
    ):

        passed, response = evaluate_case(None, case)

    assert passed is True