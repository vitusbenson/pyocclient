# -*- coding: utf-8 -*-
# vim: expandtab shiftwidth=4 softtabstop=4
#
import time

# unique id to use for testing
test_id = int(time.time())

Config = {
    # Change this to your ownCloud's URL
    'owncloud_url': 'http://127.0.0.1/',
    # ownCloud login
    'owncloud_login': 'admin',
    # ownCloud password
    'owncloud_password': 'admin',
    # test user whom we want to share a file
    'owncloud_share2user': 'share',
    # test group, uses to add owncloud_share2user to it etc
    'test_group': 'my_test_group',
    # remote root path to use for testing
    'test_root': 'pyoctestroot%s' % test_id,
    # app name to use when testing privatedata API
    'app_name': 'pyocclient_test%s' % test_id,
    #groups to be created
    'groups_to_create': ["grp1","grp2","grp3"],
    #not existing group
    'not_existing_group': 'this_group_should_not_exist',
    # single session mode (only set to False for ownCloud 5)
    'single_session': True
}
