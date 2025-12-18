from app.jira.client_jira import get_issue, add_comment, update_summary
from app.ai.client_openai import correct_jir_description

if __name__ == "__main__":
    issue_key = "DEV-2"
    issue = get_issue(issue_key)
    uncorrected = issue["fields"]["summary"]
    print("Unkorrigiert: " + uncorrected)
    corrected_summary= correct_jir_description(uncorrected)

    print("Korrigiert: " + corrected_summary)

    comment_corrected = "Corrected summary, please check!"
    add_comment(issue_key, comment_corrected)

    update_summary(issue_key, corrected_summary)
