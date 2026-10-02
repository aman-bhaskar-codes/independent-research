# Reliable Autonomous Learning (RAL) Constitution

*Provisional Note: Derived from context, pending review of original source document (RAL_Constitution.pdf).*

## North-Star Question
How can we establish trustworthy evidence that an autonomous system genuinely improves its capabilities from experience, without succumbing to memorization, capability regression, or evaluator gaming?

## Principles of Genuine Improvement

### 1. Meaningful Generalization
Adaptation is only considered improvement if it transfers to held-out, unseen tasks. Memorization of training examples or development sets constitutes behavioral change, not capability improvement.

### 2. Retention and Regression Monitoring
Learning new skills must not come at the unacceptable cost of unlearning critical prior capabilities. We must explicitly measure retention and characterize the tradeoffs in catastrophic forgetting or performance regression.

### 3. Evaluator Reliability and Gaming
As agents adapt to maximize a reward or metric, they are prone to finding flaws in the automated evaluator itself (reward hacking/gaming). We must design robust evaluators and separate the optimization signal from the true performance metric.

### 4. Observability and Failure Diagnosis
When an adaptation mechanism fails, we must be able to diagnose *why*. Mechanisms must expose sufficient internal state, reasoning traces, and history to permit rigorous failure analysis.

### 5. Memory and Continual Adaptation
Long-term reliability requires managing memory effectively—knowing what to retain, what to abstract, and what to discard.

## Open Questions and Scope Limitations
- [Needs Verification] Are current LLM-based agent frameworks fundamentally limited in their capacity for continuous, unbounded learning?
- [Scope Limitation] This programme initially focuses on discrete task-based improvement rather than continuous embodied learning.
