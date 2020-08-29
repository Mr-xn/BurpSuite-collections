# Xkeys - Burp Suite Extension to extract interesting strings (key, secret, token, or etc.) from a webpage.
# Type : Passive Scanner
# By: Verry Darmawan (github.com/vsec7)
# Twitter: https://twitter.com/verry__d

# Code Credits:
# PortSwigger example-scanner-checks: https://github.com/PortSwigger/example-scanner-checks
# Redhunlabs Asset_Discover: https://github.com/redhuntlabs/BurpSuite-Asset_Discover

from burp import IBurpExtender
from burp import IScannerCheck
from burp import IScanIssue
from array import array
import re

class BurpExtender(IBurpExtender, IScannerCheck):

    def	registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._callbacks.setExtensionName("Xkeys")
        self._callbacks.registerScannerCheck(self)
        print("Thank you for installing xkeys")
        print("Passive scanner to extract interesting strings (key, secret, token, or etc.)")
        print("By : Verry Darmawan (github.com/vsec7)")
        print("Twitter : https://twitter.com/verry__d\n")
        return

    def consolidateDuplicateIssues(self, existingIssue, newIssue):
        if (existingIssue.getIssueDetail() == newIssue.getIssueDetail()):
            return -1
        else:
            return 0

    def doPassiveScan(self, baseRequestResponse):
        scan_issues = []
        tmp_issues = []

        self._CustomScans = CustomScans(baseRequestResponse, self._callbacks)

        # Add your keywords for pattern
        keywords = [
            "access_key",
            "access_token",
            "accessKey",
            "accessToken",
            "account_sid",
            "accountsid",
            "admin_pass",
            "admin_user",
            "api_key",
            "api_secret",
            "apikey",
            "app_key",
            "app_secret",
            "app_url",
            "application_id",
            "aws_secret_token",
            "authsecret",
            "aws_access",
            "aws_access_key_id",
            "aws_bucket",
            "aws_config",
            "aws_default_region",
            "aws_key",
            "aws_secret",
            "aws_secret_access_key",
            "aws_secret_key",
            "aws_token",
            "bucket_password",
            "client_secret",
            "cloudinary_api_key",
            "cloudinary_api_secret",
            "cloudinary_name",
            "connectionstring",
            "consumer_secret",
            "database_dialect",
            "database_host",
            "database_logging",
            "database_password",
            "database_schema",
            "database_schema_test",
            "database_url",
            "database_username",
            "db_connection",
            "db_database",
            "db_dialect",
            "db_host",
            "db_password",
            "db_port",
            "db_server",
            "db_username",
            "dbpasswd",
            "dbpassword",
            "dbuser",
            "django_password",
            "elastica_host",
            "elastica_port",
            "elastica_prefix",
            "email_host_password",
            "facebook_app_secret",
            "facebook_secret",
            "fb_app_secret",
            "fb_id",
            "fb_secret",
            "gatsby_wordpress_base_url",
            "gatsby_wordpress_client_id",
            "gatsby_wordpress_client_secret",
            "gatsby_wordpress_password",
            "gatsby_wordpress_protocol",
            "gatsby_wordpress_user",
            "github_id",
            "github_secret",
            "google_id",
            "google_oauth",
            "google_oauth_client_id",
            "google_oauth_client_secret",
            "google_oauth_secret",
            "google_secret",
            "google_server_key",
            "gsecr",
            "heroku_api_key",
            "heroku_key",
            "heroku_oauth",
            "heroku_oauth_secret",
            "heroku_oauth_token",
            "heroku_secret",
            "heroku_secret_token",
            "htaccess_pass",
            "htaccess_user",
            "incident_bot_name",
            "incident_channel_name",
            "jwt_passphrase",
            "jwt_password",
            "jwt_public_key",
            "jwt_secret",
            "jwt_secret_key",
            "jwt_secret_token",
            "jwt_token",
            "jwt_user",
            "keyPassword",
            "mail_driver",
            "mail_encryption",
            "mail_from_address",
            "mail_from_name",
            "mail_host",
            "mail_password",
            "mail_port",
            "mail_username",
            "mailgun_key",
            "mailgun_secret",
            "maps_api_key",
            "mix_pusher_app_cluster",
            "mix_pusher_app_key",
            "mysql_password",
            "oauth_discord_id",
            "oauth_discord_secret",
            "oauth_key",
            "oauth_token",
            "oauth2_secret",
            "password",
            "paypal_identity_token",
            "paypal_sandbox",
            "paypal_secret",
            "paypal_token",
            "playbooks_url",
            "postgres_password",
            "private_key",
            "pusher_app_cluster",
            "pusher_app_id",
            "pusher_app_key",
            "pusher_app_secret",
            "queue_driver",
            "redis_host",
            "redis_password",
            "redis_port",
            "response_auth_jwt_secret",
            "response_data_secret",
            "response_data_url",
            "root_password",
            "sa_password",
            "secret",
            "secret_access_key",
            "secret_bearer",
            "secret_key",
            "secret_token",
            "secretKey",
            "security_credentials",
            "send_keys",
            "sentry_dsn",
            "session_driver",
            "session_lifetime",
            "sf_username",
            "sid twilio",
            "sid_token",
            "sid_twilio",
            "slack_channel",
            "slack_incoming_webhook",
            "slack_key",
            "slack_outgoing_token",
            "slack_secret",
            "slack_signing_secret",
            "slack_token",
            "slack_url",
            "slack_webhook",
            "slack_webhook_url",
            "square_access_token",
            "square_apikey",
            "square_app",
            "square_app_id",
            "square_appid",
            "square_secret",
            "square_token",
            "squareSecret",
            "squareToken",
            "ssh2_auth_password",
            "sshkey",
            "storePassword",
            "strip_key",
            "strip_secret",
            "strip_secret_token",
            "strip_token",
            "stripe_key",
            "stripe_secret",
            "stripe_secret_token",
            "stripe_token",
            "stripSecret",
            "stripToken",
            "stripe_publishable_key",
            "token_twilio",
            "trusted_hosts",
            "twi_auth",
            "twi_sid",
            "twilio_account_id",
            "twilio_account_secret",
            "twilio_account_sid",
            "twilio_accountsid",
            "twilio_api",
            "twilio_api_auth",
            "twilio_api_key",
            "twilio_api_secret",
            "twilio_api_sid",
            "twilio_api_token",
            "twilio_auth",
            "twilio_auth_token",
            "twilio_secret",
            "twilio_secret_token",
            "twilio_sid",
            "twilio_token",
            "twilioapiauth",
            "twilioapisecret",
            "twilioapisid",
            "twilioapitoken",
            "TwilioAuthKey",
            "TwilioAuthSid",
            "twilioauthtoken",
            "TwilioKey",
            "twiliosecret",
            "TwilioSID",
            "twiliotoken",
            "twitter_api_secret",
            "twitter_consumer_key",
            "twitter_consumer_secret",
            "twitter_key",
            "twitter_secret",
            "twitter_token",
            "twitterKey",
            "twitterSecret",
            "wordpress_password",
            "zen_key",
            "zen_tkn",
            "zen_token",
            "zendesk_api_token",
            "zendesk_key",
            "zendesk_token",
            "zendesk_url",
            "zendesk_username",
            "zendesk_password"
        ]

        for key in keywords:
            regex = "(?i)"+key+"['\"]?\s?(=|:)?\s?['\"]?([^\s\"'&]+)"
            issuename = "Xkeys ["+key+"]"
            issuelevel = "Information"
            issuedetail = """[$key$] : <b>$value$</b>
                             <br><br><b>Info:</b> Maybe sensitive data exposure"""

            tmp_issues = self._CustomScans.findRegEx(regex, key, issuename, issuelevel, issuedetail)
            scan_issues = scan_issues + tmp_issues

        if len(scan_issues) > 0:
            return scan_issues
        else:
            return None

class CustomScans:
    def __init__(self, requestResponse, callbacks):
        self._requestResponse = requestResponse
        self._callbacks = callbacks

        self._helpers = self._callbacks.getHelpers()

        self._params = self._helpers.analyzeRequest(requestResponse.getRequest()).getParameters()
        return

    def findRegEx(self, regex, key, issuename, issuelevel, issuedetail):
        scan_issues = []
        offset = array('i', [0, 0])
        response = self._requestResponse.getResponse()
        responseLength = len(response)

        rg = re.compile(regex, re.DOTALL)
        matchs = rg.findall(self._helpers.bytesToString(response))

        for out in matchs:
            url = self._helpers.analyzeRequest(self._requestResponse).getUrl()

            value = out[1]
            offsets = []
            start = self._helpers.indexOf(response, value, True, 0, responseLength)
            offset[0] = start
            offset[1] = start + len(value)
            offsets.append(offset)

            try:
                print "[Xkeys] "+key+" : "+value
                scan_issues.append(ScanIssue(self._requestResponse.getHttpService(),
                self._helpers.analyzeRequest(self._requestResponse).getUrl(),
                [self._callbacks.applyMarkers(self._requestResponse, None, offsets)],
                issuename, issuelevel, issuedetail.replace("$key$", key).replace("$value$", value)))
            except:
                continue                              
        return (scan_issues)

class ScanIssue(IScanIssue):
    def __init__(self, httpservice, url, requestresponsearray, name, severity, detailmsg):
        self._url = url
        self._httpservice = httpservice
        self._requestresponsearray = requestresponsearray
        self._name = name
        self._severity = severity
        self._detailmsg = detailmsg

    def getUrl(self):
        return self._url

    def getHttpMessages(self):
        return self._requestresponsearray

    def getHttpService(self):
        return self._httpservice

    def getRemediationDetail(self):
        return None

    def getIssueDetail(self):
        return self._detailmsg

    def getIssueBackground(self):
        return None

    def getRemediationBackground(self):
        return None

    def getIssueType(self):
        return 0

    def getIssueName(self):
        return self._name

    def getSeverity(self):
        return self._severity

    def getConfidence(self):
        return "Certain"
