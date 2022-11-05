import docker

client = docker.from_env()
containerList = client.containers.list(all=True)


# finds and kills existing 'gentle' instance if running and deletes container
def remove_old_container(container_name):
    for container in containerList:
        if container.attrs['Name'] == "/" + container_name:
            if container.attrs['State']['Running'] is True:
                container.kill()
            container.remove()


# launch container and bind default listening port to host
def launch_container(container_name, container_image):
    gentle_container = client.containers.run(
        image=container_image,
        name=container_name,
        ports={'8765/tcp': 8765},
        detach=True
    )
    return gentle_container


if __name__ == '__main__':
    container_name = "gentle"
    container_image = "lowerquality/gentle"
    remove_old_container(container_name)
    launch_container(container_name, container_image)
