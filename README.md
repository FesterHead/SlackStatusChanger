# SlackStatusChanger
- Use Python to update slack emoji and status.
- Each run a random emoji and text is selected.

# Emoji's
- See emoji.properties
- One emoji per line
- Include bounding colons
- Example `:astonished:`

# Status texts
- See text.properties
- One status per line
- Example `i like ice cream`

# Slack tokens
- Copy `slack-tokens.properties-default` as `slack-tokens.properties`
- Get your Slack token(s) and add them to the file
- Supports multiple workspaces, one workspace token per line
- Format is `[workspace]=[token]`


# Example crontab
`0 * * * *  cd <project-directory> && ~/.venv/<python-profile>/bin/python3 change-status.py >> log.txt 2>&1`

# log.txt format
```
[run-date] [workspace] | [emoji] | [status]

[2024-01-27 23:47:05.722016] kunitzer | :waning_crescent_moon: | behind us you will only see our dust
```