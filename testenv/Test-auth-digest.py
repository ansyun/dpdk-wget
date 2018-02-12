#!/usr/bin/env python3
from sys import exit
from test.http_test import HTTPTest
from misc.wget_file import WgetFile

"""
    This test ensures Wget's Digest Authorization Negotiation.
"""
TEST_NAME = "Digest Authorization"
############# File Definitions ###############################################
File1 = "Need a cookie?"
File2 = "Want cookies with milk!"

File1_rules = {
    "Authentication"    : {
        "Type"          : "Digest",
        "User"          : "Pacman",
        "Pass"          : "Omnomnom",
        "Parm"          : {
            "qop"       : "auth"
        }
    }
}

File2_rules = {
    "Authentication"    : {
        "Type"          : "Digest",
        "User"          : "Pacman",
        "Pass"          : "Omnomnom",
        "Parm"          : {
            "qop"       : None
        }
    }
}
A_File = WgetFile ("File1", File1, rules=File1_rules)
B_File = WgetFile ("File2", File2, rules=File2_rules)

WGET_OPTIONS = "--user=Pacman --password=Omnomnom"
WGET_URLS = [["File1", "File2"]]

Files = [[A_File, B_File]]

ExpectedReturnCode = 0
ExpectedDownloadedFiles = [A_File, B_File]

################ Pre and Post Test Hooks #####################################
pre_test = {
    "ServerFiles"       : Files
}
test_options = {
    "WgetCommands"      : WGET_OPTIONS,
    "Urls"              : WGET_URLS
}
post_test = {
    "ExpectedFiles"     : ExpectedDownloadedFiles,
    "ExpectedRetcode"   : ExpectedReturnCode
}

err = HTTPTest (
                name=TEST_NAME,
                pre_hook=pre_test,
                test_params=test_options,
                post_hook=post_test
).begin ()

exit (err)
