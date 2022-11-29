#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def gmail_check(gmail_address):
    """Check a gmail address."""
    valid_username = r'^[a-z0-9.]{6,30}$'
    valid_domain = 'gmail.com'

    username, domain = re.split(r'@', gmail_address)

    if re.match(valid_username, username) and domain == valid_domain:

        if re.search('^\\.', username) or re.search('\\.$', username) \
           or re.search('\\.{2}', username):
            return False
        else:
            return True

    else:
        return False


# USERNAME PARAMETERS FOR GMAIL
# From https://support.google.com/mail/answer/9211434?hl=en
#
# Character length:
# Choose a username 6–30 characters long. Your username can be any combination
# of letters, numbers or symbols.
#
# Special characters:
# Usernames can contain letters (a-z), numbers (0-9), and periods (.).
# Usernames cannot contain an ampersand (&), equals sign (=), underscore (_),
# apostrophe ('), dash (-), plus sign (+), comma (,), brackets (<,>),
# or more than one period (.) in a row.
# Usernames can begin or end with non-alphanumeric characters
# except periods (.). Other than this rule, periods (dots) don’t matter in
# Gmail addresses.
