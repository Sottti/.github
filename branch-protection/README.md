# Branch protection

The common policy protects the repository's default branch and `develop`,
including a `develop` branch created later. It requires pull requests, resolved
review threads and passing required CI checks against an up-to-date base.
It blocks force pushes and branch deletion and has no bypass actors, including
administrators. Existing stricter repository rules continue to apply.

Required approvals remain zero for solo maintenance. Automated review findings
must still be assessed and addressed. GitHub's conversation-resolution rule
enforces resolved inline review threads; ordinary Conversation comments need
human or agent follow-through and have no native resolved flag.

## Required checks

Required check names are repository-specific and use the GitHub App that emits
them. A workflow's display name is not necessarily its job's check name.

| Repository | Required checks |
| --- | --- |
| Android-App-Template | Build & Validate; Analyze (actions); Analyze (java-kotlin); CodeQL |
| RollerCoasters | Build; JVM Tests |
| Morylia | Validate Gradle wrapper JAR; Resolve and validate Gradle dependencies |
| Agent-Workflows | Python 3.9; Python 3.14 |
| Sotti-Web | verify |
| Morylia-Dashboard-Web | verify: dashboard build, validators and Node tests |
| Morylia-Dashboard-Data | verify: tracked JSON syntax, unique keys and finite constants |
| Android-Interview-Practice | verify: content checks, TypeScript, production build and artifact privacy |
| .github | verify: shared files, template/config YAML and policy JSON |

The Data check validates JSON syntax; it does not replace the canonical data
contract's schema and publication checks. Morylia's local readiness and review
requirements remain additional contributor responsibilities.

## New repositories

GitHub does not inherit branch rules or workflows from the personal `.github`
repository or an Android template. Repository templates copy files and branch
contents. Account-wide branch rulesets are an organization feature.

After initializing a new repository:

1. Add meaningful CI that runs on every pull request, including documentation
   changes, and supports manual dispatch on an exact branch tip. Prefer a stable final job called `verify`; it must fail if any
   required build or test fails, rather than skip or report success.
2. Import [ruleset.json](ruleset.json) under Settings, Rules, Rulesets, or use
   the GitHub CLI from this repository's checkout:

   ```sh
   gh api --method POST repos/OWNER/REPOSITORY/rulesets \
     --input branch-protection/ruleset.json
   ```

3. Set the real repository-specific required check names and their source Apps.
   The example requires `verify` from GitHub Actions. Keep strict up-to-date
   checks, review-thread resolution and an empty bypass list enabled.
4. Read back the active ruleset and effective rules on the default branch and
   `develop`, and confirm a pull request actually emits the required checks.
   Protecting an empty or nonexistent check name does not provide useful CI.
5. Before creating `develop` later, run CI on the exact commit that will become
   its initial tip. For a default-branch commit, dispatch the CI workflow on that
   branch and confirm its successful `verify` check belongs to that exact SHA;
   then create `develop` from that SHA. Check enforcement on branch creation
   deliberately remains enabled (`do_not_enforce_on_create: false`), so an
   unchecked initial commit is rejected. No temporary bypass is needed.

This is an explicit setup step; storing JSON here does not automatically
protect repositories created in the future.

GitHub references: [rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets),
[organization rulesets](https://docs.github.com/en/organizations/managing-organization-settings/creating-rulesets-for-repositories-in-your-organization),
and [repository templates](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).
