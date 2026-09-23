# Meridian team constraints

Fictional course policy, not a statement of GitHub product enforcement.

Use only supplied synthetic code and data. Keep secrets, customer tickets and production identifiers outside model context. A repository maintainer owns the shared workflow, a team lead owns the pilot and a human reviewer owns each code approval. The organisation's security contact resolves proposed changes to permitted data or tool access.

The pilot covers small Python maintenance changes with existing acceptance criteria. No production credentials, cloud deployment, new dependency or automated merge is in scope. Stop a request with missing requirements, disputed scope or unexpected external access and ask the appropriate human owner.

Instructions guide model behaviour. They do not implement branch protection, sandbox boundaries or required CI checks. The course uses an isolated workspace. Production rollout requires independently configured controls appropriate to the organisation.

The workflow author must preserve actual test failures, label missing evidence, and avoid recording a model's expected result as an observed result. The reviewer checks the diff and executes tests. The human author remains responsible for the proposed change.
