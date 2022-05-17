# Programmatic - Linux - Debian Linux distro and derivatives

- Open your preferred terminal and run the following command:

    ```shell
    sudo apt update && sudo apt -y upgrade
    sudo apt -y install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install -y python3.10
    python -m pip install ${VARS["repo_name"]}
    ```

- You can now use ${VARS["repo_name"]} programmatically!
