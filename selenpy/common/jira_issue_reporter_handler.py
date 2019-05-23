import os
import datetime
from jira import JIRA


class JiraIssueReporterHandler(object):

    def __init__(self, jiraURL, username, api_token, projectKey):
        self.options = {'server': jiraURL}
        # self.server = jiraURL
        self.auth = (username, api_token)
        self.projectKey = projectKey
        # self.customField_Test_Method = customField_TestMethod

    def get_jira_client(self):
        return JIRA(self.options, basic_auth=self.auth)


    def create_new_bug(self, summary, description):
        jira = self.get_jira_client()
        new_bug = None
        try:
            # Create new issue with issue type is Bug
            new_bug = jira.create_issue(project=self.projectKey, summary=summary,
                                        description=description, issuetype={'name': 'Bug'})

        except Exception as ex:
            print(ex)
        finally:
            if new_bug:
                return new_bug.key
        return None

    def add_bug_comment(self, bug_id, comment):
        jira = self.get_jira_client()
        try:
            bug = jira.issue(bug_id)
            # comment = "This issue is still {color:red}*FAILING*{color}"

            # Add comment
            jira.add_comment(bug, comment)

        except Exception as ex:
            print(ex)

    def get_issue_status(self, issue_id):
        jira = self.get_jira_client()
        try:
            issue = jira.issue(issue_id)
            status = issue.fields.status.name
            return status

        except Exception as ex:
            print(ex)

    def mark_issue_status(self, issue_id, status):
        jira = self.get_jira_client()
        try:
            issue = jira.issue(issue_id)
            transitions = jira.transitions(issue)
            for transition in transitions:
                if transition['name'] == status:
                    jira.transition_issue(issue, transition['id'])
                    break

        except Exception as ex:
            print(ex)

    def get_today(self):
        return datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")



