import docker
import argparse
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def restart_container(service_name):
    """
    Check the status of a Docker container and restart it if it's running.
    
    Args:
        service_name (str): The name of the container to check and potentially restart.
    """
    try:
        # Initialize Docker client
        client = docker.from_env()
        logger.info(f"Checking status of container: {service_name}")

        # Retrieve all containers (both running and stopped)
        containers = client.containers.list(all=True)
        if not containers:
            logger.warning("No containers found on this Docker host")
            return

        # Find the specific container by its name
        target_container = next((container for container in containers if container.name == service_name), None)

        if target_container:
            # Refresh the container's status
            target_container.reload()
            
            # Check the container's status
            if target_container.status == "running":
                logger.info(f"Container {service_name} is currently running. Attempting restart...")
                try:
                    target_container.restart()
                    logger.info(f"Container {service_name} restarted successfully")
                except docker.errors.APIError as e:
                    logger.error(f"Failed to restart container {service_name}: {str(e)}")
            else:
                logger.warning(f"Container {service_name} is in {target_container.status} state. No action taken.")
        else:
            logger.error(f"Container {service_name} not found")

    except docker.errors.DockerException as e:
        logger.error(f"Docker error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check and restart a Docker container if it's running. This script must be run on the host machine.")
    parser.add_argument("service_name", help="Name of the container to check and potentially restart")
    args = parser.parse_args()

    try:
        restart_container(args.service_name)
    except KeyboardInterrupt:
        logger.info("Script interrupted by user")
        sys.exit(1)
