#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def gmail_check(gmail_address):
    """Check a gmail address."""
    valid_username = r'^[a-z0-9.]{6,30}$'
    valid_domain = 'gmail.com'

    username, domain = re.split(r'@', gmail_address)

    if re.match(valid_username, username) and domain == valid_domain:
        print('email matched ok')

        if re.search('^\\.', username) or re.search('\\.$', username) \
           or re.search('\\.{2}', username):
            return False
        else:
            return True

    else:
        return False


def main():
    email_address = input("Input email to match or 'end' to end: ")

    while email_address != 'end':
        print('email input: ', email_address)
        valid = gmail_check(email_address)

        if valid:
            print('input is valid')
        else:
            print('no match input is invalid')

        email_address = input("Input email to match or 'end' to end: ")


if __name__ == '__main__':
    main()


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
