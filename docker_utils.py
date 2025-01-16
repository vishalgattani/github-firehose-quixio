import subprocess
import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s (%(filename)s:%(lineno)d)")


def initialize_quix():
    process = subprocess.run("quix init",shell=True, check=True)
    if process.returncode != 0:
        raise Exception("Quix initialization failed")
    logging.info("Quix initialized")

def initialize_quix_pipeline():
    process = subprocess.run("quix pipeline up",shell=True, check=True)
    if process.returncode != 0:
        raise Exception("Quix pipeline initialization failed")
    logging.info("Quix pipeline initialized")

def get_containers():
    process = subprocess.run("docker ps",shell=True, check=True, capture_output=True)
    containers = process.stdout.decode("utf-8").split("\n")[1:]
    logging.debug(f"Containers: {(containers)}")
    return containers

def stop_quix_pipeline(configuration_file:str = "compose.local.yaml"):
    containers = get_containers()
    assert len(containers) > 0, "No containers found"
    process = subprocess.run(f"docker compose -f {configuration_file} down",shell=True, check=True)
    if process.returncode != 0:
        raise Exception("Quix pipeline stop failed")
    logging.debug(f"{process.stdout}")
    logging.info("Quix pipeline stopped")

def main():
    initialize_quix()
    initialize_quix_pipeline()
    get_containers()
    stop_quix_pipeline()

if __name__ == "__main__":
    main()