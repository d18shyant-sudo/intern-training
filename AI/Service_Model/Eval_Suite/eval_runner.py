import json

from langchain_core.messages import HumanMessage

from LangChain_Usage.agent import chain
from pathlib import Path
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type
)
from openai import RateLimitError, APIConnectionError, APITimeoutError
import httpx


@retry(
    stop=stop_after_attempt(4),
    wait=wait_exponential(
        multiplier=1,
        min=1,
        max=10
    ),
    retry=retry_if_exception_type(
        (
            httpx.TimeoutException,
            httpx.ConnectError,
            httpx.ReadError,
            RateLimitError,
            APIConnectionError, 
            APITimeoutError
        )
    ),
    reraise=True
)
def invoke_model(chain, messages):

    return chain.invoke({
        "messages": messages
    })

BASE_DIR = Path(__file__).resolve().parent
GOLDEN_SET_PATH = BASE_DIR/"test_set.json"


def load_golden_set():
    with open(GOLDEN_SET_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def evaluate_case(chain, case):
    """
    Run one golden-set case against the real model
    and return whether it passed
    """

    response = invoke_model(chain=chain,messages=[
            HumanMessage(content=case["input"])
        ])

    expected = case["expected"]

    # --------------------------------
    # Expected refusal
    # --------------------------------

    if expected["type"] == "refusal":

        # A refusal case should not call a tool
        return len(response.tool_calls) == 0, response


    # --------------------------------
    # Expected tool call
    # --------------------------------

    if expected["type"] == "tool":

        # Model didn't call any tool
        if not response.tool_calls:
            return False, response

        actual = response.tool_calls[0]

        actual_tool = actual["name"]
        actual_args = actual["args"]

        expected_tool = expected["tool"]
        expected_args = expected["args"]

        # Check tool name
        if actual_tool != expected_tool:
            return False, response

        # Check arguments
        if actual_args != expected_args:
            return False, response

        return True, response


    return False, response


def run_eval():

    golden_set = load_golden_set()

    # --------------------------------
    # Create the REAL LangChain chain
    # --------------------------------

    passed = 0
    failed = 0

    print("\nRunning evaluation...\n")

    for case in golden_set:

        try:
            passed_case, response = evaluate_case(
                chain,
                case
            )

        except Exception as error:

            passed_case = False
            response = None

            print(
                f"ERROR | {case['id']} | {error}"
            )

        if passed_case:

            passed += 1

            print(
                f"PASS  | {case['id']} | {case['input']}"
            )

        else:

            failed += 1

            print(
                f"FAIL  | {case['id']} | {case['input']}"
            )

            print(
                f"       Expected: {case['expected']}"
            )

            if response is not None:
                print(
                    f"       Actual:   {response.tool_calls}"
                )

    total = len(golden_set)

    pass_rate = (passed / total) * 100

    print("\n" + "=" * 50)

    print(f"Total     : {total}")
    print(f"Passed    : {passed}")
    print(f"Failed    : {failed}")
    print(f"Pass rate : {pass_rate:.2f}%")

    print("=" * 50)

    return pass_rate


if __name__ == "__main__":
    run_eval()