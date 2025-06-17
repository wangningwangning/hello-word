# hello-word
this is a test demo

## Automated Dependency Management

This repository includes automated dependency management through Dependabot and GitHub Actions:

### 🤖 Auto-merge for Dependabot PRs

Dependabot pull requests are automatically merged when:
- All status checks pass (CI workflow)
- The PR is mergeable (no conflicts)
- The PR author is `dependabot[bot]`

### 🔧 How it works

1. **Dependabot** creates pull requests for dependency updates
2. **CI workflow** runs automated tests and checks
3. **Auto-merge workflow** evaluates the PR and merges it if all conditions are met
4. The PR is merged using the "squash and merge" strategy

### 📋 Current Checks

The CI workflow currently includes:
- Basic repository structure validation
- README.md existence check
- Project type detection (Node.js, Python, Ruby)

### 🛠️ Customization

To customize the auto-merge behavior:

1. **Add more tests**: Modify `.github/workflows/ci.yml` to include your specific test suite
2. **Change merge strategy**: Edit the `gh pr merge` command in `.github/workflows/auto-merge-dependabot.yml`
3. **Adjust conditions**: Modify the check conditions in the auto-merge workflow

### 🔒 Security

The auto-merge workflow only processes PRs from `dependabot[bot]` and requires all status checks to pass before merging.
