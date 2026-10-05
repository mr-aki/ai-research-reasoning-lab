from arlab.agents import EchoAgent
from arlab.core import AgentContext
from arlab.reasoning import MajorityConsensus, run_independent_agents


def test_consensus_reports_agreement() -> None:
    results = run_independent_agents([EchoAgent(), EchoAgent()], AgentContext("same"))
    consensus = MajorityConsensus().combine(results)
    assert consensus.selected_output == "same"
    assert consensus.agreement == 1.0
