from ansible.module_utils.basic import *

#json_arguments = """<<INCLUDE_ANSIBLE_MODULE_JSON_ARGS>>"""
def main():

	module = AnsibleModule(argument_spec=dict(message=dict(type='str', required=True)))
	module.exit_json(changed=False, meta=module.params)


if __name__ == '__main__':
    main()
