import os
import sys
import yaml

def ping_domain(domain_name):
  response = os.system("ping -c 1 " + domain_name)
  #and then check the response...
  if response == 0:
    print hostname, 'is up!'
  else:
    print hostname, 'is down!'

def main():
  myhome = os.path.expanduser('~')
  zorgdir = ".zorg.d"
  filename = os.path.join(myhome + os.sep + zorgdir, 'list.domains.yaml')
  to_find = sys.argv[1]
  with open(filename, 'r') as stream:
    content = yaml.safe_load(stream)
    domains = content["DOMAINS"]
    for i in domains:
        if to_find in i:
            print "Server:"
            print i[to_find]["serverType"]
            #.get('ip')
            #.get("ip")
        #    print domains[count][to_find]
        else:
          print "Lalalala"
        #if search_arg in i:
        #    print i
    #if  in domains:
    #  print domains.get(search_arg)


if __name__ == "__main__":
    main()
