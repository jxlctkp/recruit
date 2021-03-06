#!/usr/bin/python
# encoding:utf-8

"""
@author:
contact:
@file: 2017/8/28-ansible-module-learning-ping.py
@time: 2017/8/28 
"""

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(required=False, default=None),
        ),
        supports_check_mode=True
    )
    result = dict(ping='pong')
    if module.params['data']:
        if module.params['data'] == 'crash':
            raise Exception("boom")
        result['ping'] = module.params['data']
    module.exit_json(**result)

if __name__=='__main__':
    main()