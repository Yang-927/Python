import requests
import re
headers = {
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 Safari/537.36",
	"cookie": "Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1601981789; t=7Ge6kKhMJht4lMYh; wt=7Ge6kKhMJht4lMYh; __g=-; _bl_uid=wOk9sfv4xaCuesl84u9L144bXaCz; lastCity=100010000; __c=1601981789; __l=l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Frecommend&r=https%3A%2F%2Fopen.weixin.qq.com%2F&g=&friend_source=0&friend_source=0; __a=76072720.1593235118.1597844326.1601981789.16.4.10.10; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1601984305; __zp_stoken__=a086bPEo3US1wTzEdSkEsbW5PbSJzK1dTcGVGfEgRfSJLUgVZaVEed0RDOARIWzg8D11uUXZDFy9EVSIkOUQjPxJdUWJTAkN0elIIRw41DBRbHx4cE2lyIHxBIztZLkFcCQxkQm08F1tnXGBHIQ%3D%3D"
}
def main():
	base_url = "https://www.zhipin.com/job_detail/?city=101010100&position=100201"
	res = requests.get(base_url, headers=headers)
	html = res.text
	infos = re.findall(r"""
		# 职位
		<li>.+?<span.+?job-name.+?<a.+?>(.+?)</a>
		.+?<span.+?job-area">(.+?)</span>
		.+?<div.+?job-limit clearfix.+?red">(.+?)</span>
		
	""", html, re.VERBOSE | re.DOTALL)
	print(infos)
	for info in infos:
		print(info)

if __name__ == '__main__':
	main()