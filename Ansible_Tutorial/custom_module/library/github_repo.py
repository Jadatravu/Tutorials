#!/usr/bin/python
from ansible.module_utils.basic import *
import requests

github_url = "https://api.github.com/user/repos"

def create_github_repo(data):
        name = data['name']
        description = data['description']
        userid = data['userid']
        passwd = data['passwd']
	data = json.dumps({'name':name, 'description':description})
	res = requests.post(github_url, data, auth=(userid, passwd))
	if res.status_code != 201 and res.status_code != 200:
    		return_response = json.loads(res.text)
    		if len(return_response["errors"])> 0:
        		return (-1,return_response["errors"][0]["message"])
	else:
                return (0,"success")

def main():
        fields = {
		"userid": {"required": True, "type": "str"},
		"name": {"required": True, "type": "str" },
	        "description": {"required": True, "type": "str"},
       		"passwd": {"default": True, "type": "str" },
        }
	module = AnsibleModule(argument_spec=fields)
        code,message =create_github_repo(module.params)
        if code == -1:
		module.exit_json(changed=False, meta={"absent":message})
        else:
		module.exit_json(changed=True, meta={"present":message})

if __name__ == '__main__':
    main()
