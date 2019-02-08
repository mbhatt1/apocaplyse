# import docker


# '''
# 1. This api should be able to create n-nugget containers for apocaplyse
# 2. This api should be able to put evidence in a volume, and attach the said volume to containers
# 3. This api should be able to keep track of the containers it created
# 3.1 The keeping track could be done at a higher level as well
# '''

# def get_client():
#     return docker.from_env()


# def get_events(client):
#     events = client.events()
#     return events


# def build_image(client, filepath='', imagetag=''):
#     client.images.build(path=filepath, tag=imagetag)
#     return

# def create_container(client, imagetag='', containername=''):
#     client.containers.run("ubuntu:latest", "/bin/bash", detach=True, stdin_open=True, stdout=True, tty=True)
#     return
    

# def create_n_containers(client, number=1, imagename='', containergroupname=''):
#     a = []
#     for i in range(0,number):
#         containername = containergroupname+str(i)
#         a.append(create_container(client, imagetag=imagename, containername=containername))
#     return a


