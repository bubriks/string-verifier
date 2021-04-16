# File content checker

This action will validate that the provided string are following regex expression and matching on groups.

## Usage

The verification is done using regex and in case of match the group tuple is returned.

### Example Usage

```yaml
name: My Workflow
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2

    - name: Check content
      uses: bubriks/string-verifier@0.0.3
      with:
        expression: ^contributions/(.+)/(.+)/
        strings: contributions/1/2/test contributions/1/2/
```

#### Result from example

```
groups::1 2
result::contributions/1/2/
```

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `expression`  | Regex string for string verification    |
| `strings` | List of strings to verify    |

### Outputs

| Output                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `groups`  | The matching groups (based on regex)    |
| `result`  | Result of the matching    |
