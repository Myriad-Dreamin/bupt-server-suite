
from urllib import request, parse
import collections

Response = collections.namedtuple('Response', 'status_code reason text')

def responseF(f):
    return Response(f.status, f.reason, f.read().decode('utf-8'))


def login(session, user, password, host_ip='10.3.8.211'):
    with session.urlopen(session.Request('http://'+ host_ip +'/login'), data=parse.urlencode([
        ('user', user),
        ('pass', password),
    ]).encode('utf-8')) as f:
        response = responseF(f)
    return response
    
def dial(session, host_ip='10.3.8.211'):
    with session.urlopen(session.Request('http://'+ host_ip +'/dial')) as f:
        response = responseF(f)
    return response

def require_session():
    return request

def main():
    import sys
    args = sys.argv[1:]
    if len(args) > 3 or len(args) <= 1:
        print("help: python3 login.py username password [host_ip]")
        exit(0)
    
    host_ip = '10.3.8.211'
    if len(args) == 3:
        host_ip = args[2]

    session = require_session()

    response = login(session, *args)
    if response.status_code != 200:
        print("QAQ connect failed！status code:", response.status_code)
        exit(1)
    
    print("status is ok, validate network yourself orz")

    # print(response.__dict__)
    # response = dial(session, host_ip)

    # print(response.__dict__)
    # if response.status_code != 200:
    #     print("QAQ connect failed！status code:", response.status_code)
    #     exit(1)

if __name__ == '__main__':
    main()