# OpenCode Project Instructions

## Operating Boundary

Treat the current working directory as the project boundary. Do not assume parent or sibling directories are part of the active project unless the operator explicitly says so.

Use `external_directory` access only when the operator approves it for a specific reason.

## File Modification Rules

For existing files, do not overwrite or regenerate the whole file.

Before changing an existing file:

1. Read the current file.
2. Describe the intended change briefly.
3. Use the smallest practical edit or patch.

Use write only for new files, and only after confirming the target file does not already exist.

If an exact edit fails, stop and explain why. Do not rewrite the full file as a workaround.

## Structured Data

For JSON, YAML, Terraform state, logs, and schemas, do not approximate.

Validate and inspect structured data with deterministic tools such as `jq`, `yq`, `node`, or Terraform commands where appropriate. If the file is large, inspect structure and relevant slices instead of loading the whole file into context.

Never claim inability to parse structured data before trying available tools.

## Restricted Commands

Do not run these commands unless the operator explicitly changes this rule:

- `aws`
- `kubectl`
- `helm`
- `git push`
- `git commit`
- `git tag`
- `terraform apply`
- `terraform destroy`

The operator runs deployment, cloud mutation, cluster mutation, and Git publishing commands manually.
