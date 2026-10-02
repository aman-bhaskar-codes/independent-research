# Draft Protocol: Improvement Verification

*Note: These are proposed design choices and have not yet been validated by evidence.*

## 1. Research Question
Does providing execution feedback on development tasks lead to strategy updates that generalize to improved performance on held-out, unseen coding tasks?

### Operational Meaning of Improvement
Improvement is defined as a statistically significant increase in the pass rate on the held-out evaluation set, compared to a frozen baseline, without an unacceptable increase in token cost or execution time.

## 2. Hypothesis
An agent utilizing strategy updates from feedback will outperform a frozen baseline on the held-out set, indicating genuine generalization rather than memorization.

## 3. Baselines and Controls
- **Baseline**: A frozen agent that does not update its strategy across tasks.
- **Control**: An agent that receives randomized or uninformative feedback, to isolate the effect of *valid* feedback.

## 4. Task Splits and Contamination
Tasks will be partitioned into:
- **Development Set (60%)**: Used for the agent to attempt tasks, fail, and synthesize strategy updates.
- **Evaluation Set (40%)**: Strictly held out. The agent will attempt these tasks using the learned strategy *without* further adaptation.

## 5. Metrics and Effect Thresholds
- **Primary Metric**: Pass rate (percentage of tasks with all unit tests passing).
- **Secondary Metrics**: Token usage (cost), time to completion.
- **Practical Effect Threshold**: A minimum absolute improvement of +5% pass rate over the baseline is required to be considered practically significant.

## 6. Planned Uncertainty Analysis
Given the stochasticity of LLMs, all evaluations will be repeated $N=5$ times using different temperature seeds. We will report mean pass rates and 95% confidence intervals.

## 7. Stopping Rules
The evaluation set will only be run *once* per fully defined experiment configuration. Repeated evaluation on the held-out set to tune hyperparameters is strictly forbidden (test set contamination).

## 8. Acceptance and Rejection Criteria
- **Accept**: If the mean pass rate on the Evaluation set is >5% higher than the baseline, with non-overlapping confidence intervals.
- **Reject**: If the difference is <5%, or if performance on a subset of previously passed tasks degrades significantly (regression).

## 9. Failure Analysis
If the hypothesis is rejected, we will sample 20 failed evaluation tasks and manually categorize the failure modes (e.g., syntax error, logic error, hallucinated API).

## 10. Limitations
- The tasks are simple and may not reflect the complexity of real-world software engineering.
- The adaptation mechanism is highly constrained.
