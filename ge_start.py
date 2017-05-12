#!/usr/bin/env python
#_*_coding:utf-8_*_
import sys,time,os,commands 
try:
  CONTAINER_name=sys.argv[1]
except:
  CONTAINER_name=False
  print 'try ./start.py we_1'
  exit(0)

def stop(CONTAINER_name):
  stop_CONTAINER = 'docker stop {CONTAINER_name}&& docker rm {CONTAINER_name}'.format(CONTAINER_name=CONTAINER_name)
  os.system(stop_CONTAINER)

web_names = {
  'we_1':'web_10051_ping1',
  'we_2':'web_10030_cash',
  'we_3':'web_10036_seesource',
  'we_4':'web_10053_read',
  'we_5':'web_10055_baidu19_hardable',
  'we_6':'web_20012_insert0202',
}

def main():
  docker_ps = commands.getoutput("docker ps |awk '{print $NF}'")
  if not CONTAINER_name in docker_ps:
    try:
      image_name = web_names[CONTAINER_name]
    except:
      print '{CONTAINER_name} is not in docker'
      exit(0)
  CONTAINER_num = int(CONTAINER_name[3:])
  web_port = 2080+CONTAINER_num*1
  ssh_port = 2020+CONTAINER_num*1

  stop_CONTAINER = 'docker stop {CONTAINER_name}&& docker rm {CONTAINER_name}'.format(CONTAINER_name=CONTAINER_name)
  start_CONTAINER = 'docker run --name={CONTAINER_name} -p {web_port}:80 -p {ssh_port}:22 -itd {image_name} /bin/bash'.format(
  CONTAINER_name=CONTAINER_name
  ,web_port=web_port
  ,ssh_port=ssh_port
  ,image_name=web_names[CONTAINER_name]
  )
  commands.getoutput(stop_CONTAINER)
  commands.getoutput(start_CONTAINER)
  time.sleep(10)
  print 'exec that when service not start:\n"docker exec -it {CONTAINER_name} /bin/bash apache2 start" or "docker exec -it {CONTAINER_name} /bin/bash httpd start"'.format(CONTAINER_name=CONTAINER_name)

if __name__=='__main__':
  if CONTAINER_name=='all':
    for i in range(1,7):
      CONTAINER_name = 'we_'+str(i)
      print CONTAINER_name
      main()
  else:
    main()
	
	
	
	
