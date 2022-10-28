import docker

client = docker.from_env()
containerList = client.containers.list(all=True)


# finds and kills existing 'gentle' instance if running and deletes container
def removeOldContainer(containerName):
    for container in containerList:
        if container.attrs['Name'] == "/" + containerName:
            if container.attrs['State']['Running'] is True:
                container.kill()
            if container.attrs['State']['Status'] == "exited":
                container.remove()


# launch container and bind default listening port to host
def launchContainer(containerName, containerImage):
    gentleContainer = client.containers.run(
        image=containerImage,
        name=containerName,
        ports={'8765/tcp': 8765},
        detach=True
    )
    return gentleContainer


if __name__ == '__main__':
    containerName = "gentle"
    containerImage = "lowerquality/gentle"
    removeOldContainer(containerName)
    launchContainer(containerName, containerImage)
